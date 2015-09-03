(function () {

  angular
    .module('app')
    .factory("territoriesFactory", territoriesFactory);

  function territoriesFactory() {
       
    return {
             territories : [
                {"id":"x", "name":"Abu Dhabi"}, 
                {"id":"e", "name":"Dubai"}, 
                {"id":"r", "name":"Jeddah"},
                {"id":"r", "name":"Riyadh"}, 
                {"id":"r", "name":"Eastern Province"},
                {"id":"r", "name":"Oman"},  
                ]
    }            

  }

}());