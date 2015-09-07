(function () {

  angular
    .module('fuzzy')
    .controller("fuzzyController", fuzzyController);

  fuzzyController.$inject = ['countryFactory','territoriesFactory'];


  function fuzzyController(countryFactory,territoriesFactory) {
    var vm = this;
    vm.btn_fuzzy_disabled= true;
    vm.btn_cancel_disabled = true;
    vm.uploadFiles = uploadFiles;
    vm.uploadAndMatch = uploadAndMatch;
    vm.countries = countryFactory.countries
    vm.territories = territoriesFactory.territories
    vm.getAllCountries = getAllCountries

 
    function getAllCountries (callback) {
        callback(vm.countries);
    };


    function uploadFiles (files) {

        vm.files = files;
        vm.filesNotEmpty = vm.files;
        vm.btn_fuzzy_disabled= false;
    }

    function uploadAndMatch () {

        for (var i = 0; i < vm.files.length; i++) {
            console.log(vm.files[i].name);
            console.log(vm['selectedCountry_'+i].originalObject.country_code);
            console.log(vm['selectedTerritory_'+i]);

            Upload.upload({
                url: 'upload/url',
                fields: {'country': vm['selectedCountry_'+i].originalObject.country_code, 'territory': vm['selectedTerritory_'+i, },
                file: vm.files[i]
            })
            // .progress(function (evt) {
            //     var progressPercentage = parseInt(100.0 * evt.loaded / evt.total);
            //     console.log('progress: ' + progressPercentage + '% ' + evt.config.file.name);
            // }).success(function (data, status, headers, config) {
            //     console.log('file ' + config.file.name + 'uploaded. Response: ' + data);
            // }).error(function (data, status, headers, config) {
            //     console.log('error status: ' + status);
            // })
        
        }

    }


  }

}());

