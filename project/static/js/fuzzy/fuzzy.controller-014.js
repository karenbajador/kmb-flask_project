(function () {

  angular
    .module('fuzzy')
    .controller("fuzzyController", fuzzyController);

  fuzzyController.$inject(countryFactory,territoriesFactory)

  function fuzzyController(countryFactory,territoriesFactory) {
    var vm = this;
    vm.btn_fuzzy_disabled= true;
    vm.btn_cancel_disabled = true;
    vm.uploadFiles = uploadFiles;
    vm.uploadAndMatch = uploadAndMatch;
    vm.countries = countryFactory.countries
    vm.territories = territoriesFactory.territories
    


    function uploadFiles (files) {
        console.log("@@@@@@ "+files);
        vm.files = files;
        vm.filesNotEmpty = vm.files;
        vm.btn_fuzzy_disabled= false;
    }

    function uploadAndMatch (fuzzylist) {
        console.log("^^^^^^^^^^^^^@@");
        console.log(fuzzylist);
        console.log("^^^^^^^^^^^^^@@");
    }


  }

}());





   