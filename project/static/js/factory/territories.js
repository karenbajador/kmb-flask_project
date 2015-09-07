(function () {

  angular
    .module('app')
    .factory("territoriesFactory", territoriesFactory);

  function territoriesFactory() {
       
    return {
             territories : [
                {"id":"Abu Dhabi", "name":"Abu Dhabi"}, 
                {"id":"Dubai", "name":"Dubai"}, 
                {"id":"Jeddah", "name":"Jeddah"},
                {"id":"Riyadh", "name":"Riyadh"}, 
                {"id":"Eastern Province", "name":"Eastern Province"},
                {"id":"Oman", "name":"Oman"},  
                ]
    }            

  }

}());