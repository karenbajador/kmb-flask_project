(function () {

  angular
    .module('app')
    .factory("territoriesFactory", territoriesFactory);

  function territoriesFactory() {
       
    return {
             territories : [
                  { text: 'International'},
                  { text: 'Abu Dhabi' },
                  { text: 'Dubai' },
                  { text: 'Oman' },
                  { text: 'Qatar' },
                  { text: 'Jeddah' },
                  { text: 'Eastern Province'},
                  { text: 'Riyadh' },
                  { text: 'Egypt'},
                  { text: 'Jordan'},
                  { text: 'Bahrain'},
                  { text: 'Lebanon'},
                  { text: 'Karachi'},
                  { text: 'Lahore'},
                  { text: 'Pakistan'},
                  { text: 'Kuwait'},
                  { text: 'Sri Lanka'},
                  { text: 'Iraq'},
                  ],
            countryMapping:   {
                  "AE" : [{ text: 'Abu Dhabi'},{ text: 'Dubai' }],
                  "SA" : [{ text: 'Eastern Province'},{ text: 'Riyadh' },{ text: 'Jeddah' }],
                  "QA" : [{ text: 'Qatar'}],
                  "OM" : [{ text: 'Oman'}],
                  "EG" : [{ text: 'Egypt'}],
                  "BH" : [{ text: 'Bahrain'}],
                  "LB" : [{ text: 'Lebanon'}],
                  "PK" : [{ text: 'Pakistan'},{ text: 'Karachi' },{ text: 'Lahore' }],
                  "KW" : [{ text: 'Kuwait'}],
                  "LK" : [{ text: 'Sri Lanka'}],
                  "IQ" : [{ text: 'Iraq'},{ text: 'International' }],
                  "JO" : [{ text: 'Jordan'}],
              },
    }            

  }

}());