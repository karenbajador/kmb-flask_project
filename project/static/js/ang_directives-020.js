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
});



   