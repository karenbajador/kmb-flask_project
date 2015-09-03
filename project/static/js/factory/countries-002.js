(function () {

  angular
    .module('app')
    .factory("countryFactory", countryFactory);

  function countryFactory() {
       
    return {
             countries : [
                    {"country_code":"ae", "country_name":"United Arab Emirates"}, 
                    {"country_code":"sa", "country_name":"Saudi Arabia"}, 
                    {"country_code":"om", "country_name":"Oman"}, 
                ]
    }

    
  }  

}());