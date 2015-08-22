// (function () {

//   angular.module('fuzzy', ['ngFileUpload'])
//   .controller("fuzzyController", ['$scope', 'Upload', '$timeout',   function ('$scope', Upload, '$timeout') {
//       $scope.uploadFiles = function(files) {
//         angular.forEach(files, function(file){
//           console.log(file);
//         });
//       }

//   }]);




// }());


//inject angular file upload directives and services.
var app = angular.module('fuzzy', ['ngFileUpload']);

app.controller('fuzzyController',  function () {
    this.uploadFiles = function(files) {
        console.log("@@@@@@ "+files);
        this.files = files;
        this.filesNotEmpty = this.files;

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
       
});



   