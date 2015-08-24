(function () {

  angular.module('fuzzy', ['ngFileUpload'])
  .controller("fuzzyController", fuzzyController);

  function fuzzyController() {
    this.btn_fuzzy_disabled= true;
    this.btn_cancel_disabled = true;
    
    this.uploadFiles = function(files) {
        console.log("@@@@@@ "+files);
        this.files = files;
        this.filesNotEmpty = this.files;
        this.btn_fuzzy_disabled= false;
    }

    
    this.uploadAndMatch = function(fuzzylist) {
        console.log("^^^^^^^^^^^^^@@");
        console.log(fuzzylist);
        console.log("^^^^^^^^^^^^^@@");
    }

    
    this.countries = [
                {"country_code":"ae", "country_name":"United Arab Emirates"}, 
                {"country_code":"sa", "country_name":"Saudi Arabia"}, 
                {"country_code":"om", "country_name":"Oman"}, 
            ]

    this.territories = [
                {"id":"x", "name":"Abu Dhabi"}, 
                {"id":"e", "name":"Dubai"}, 
                {"id":"r", "name":"Jeddah"},
                {"id":"r", "name":"Riyadh"}, 
                {"id":"r", "name":"Eastern Province"},
                {"id":"r", "name":"Oman"},  
            ]
  }

}());