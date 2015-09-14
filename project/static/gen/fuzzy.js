(function(){angular.module('fuzzy').controller("fuzzyController",fuzzyController);fuzzyController.$inject=['countryFactory','territoriesFactory','Upload','$http','$timeout','$q'];function fuzzyController(countryFactory,territoriesFactory,Upload,$http,$timeout,$q){var vm=this;vm.btn_fuzzy_disabled=true;vm.btn_cancel_disabled=true;vm.btn_sendcrm_disabled=true;vm.btn_label="Run Fuzzy!"
vm.uploadFiles=uploadFiles;vm.submit=submit;vm.uploadAndMatch=uploadAndMatch;vm.cancel=cancel;vm.f_alert=f_alert;vm.loadTags=loadTags;vm.selectCountry=selectCountry;vm.countries=countryFactory.countries
vm.territories=territoriesFactory.territories
vm.countryMapping=territoriesFactory.countryMapping
vm.getAllCountries=getAllCountries
vm.tags={};function getAllCountries(callback){callback(vm.countries);};function selectCountry(selected){if(selected!=undefined){fillTerritory(this.$parent.idx,String(selected.originalObject.country_code))}}
function fillTerritory(idx,selectedCountry){vm['selectedCountry_'+idx]=selectedCountry
var bayt_territories=vm.countryMapping[selectedCountry]
if(bayt_territories==undefined){bayt_territories=[{text:'International'}]}
vm.tags[idx]=bayt_territories}
function loadTags(query){var defer=$q.defer();defer.resolve(vm.territories);return defer.promise;}
function uploadFiles(files){vm.files=files;vm.filesNotEmpty=vm.files;vm.btn_fuzzy_disabled=false;vm.btn_sendcrm_disabled=true;for(var i=0;i<vm.files.length;i++){vm['lbl_loading_disabled'+i]=true
vm['lbl_finished_disabled'+i]=true
vm['status'+i]=""}}
function submit(){if(vm.btn_label=="Run Fuzzy!"){uploadAndMatch()}else{cancel()}}
function cancel(){vm.btn_label="Run Fuzzy!"
console.log("JOB IDSSSSSSSSSSSSSSSSSSSSSSSSSSSS"+vm.job_ids)
$http({url:'cancel',method:"POST",sendFieldsAs:'json',data:{'job_ids':vm.job_ids}}).then(function(response){ if(status===200){for(var i=0;i<vm.files.length;i++){vm['lbl_loading_disabled'+i]=true
vm['lbl_finished_disabled'+i]=true
vm['status'+i]=data}
console.log('The current status is : '+data)}},function(response){
});}
function uploadAndMatch(){vm.btn_label="Cancel"
vm.job_ids=[]
vm.btn_sendcrm_disabled=true;for(var i=0;i<vm.files.length;i++){console.log("i : "+i)
vm['lbl_loading_disabled'+i]=false
vm['lbl_finished_disabled'+i]=true
vm['btn_download_disabled'+i]=true
vm.tags[i]
var territory=[]
$.each(vm.tags[i],function(key,value){territory.push(value['text'])});Upload.upload({url:'upload',fields:{'i':i,'country':vm['selectedCountry_'+i],'territory':territory,},file:vm.files[i],sendFieldsAs:'json',method:'POST',}).progress(function(evt){var progressPercentage=parseInt(100.0*evt.loaded/evt.total);console.log('progress: '+progressPercentage+'% '+evt.config.file.name);}).success(function(data,status,headers,config){console.log("Response Job_id: "+data.job_id)
console.log("Response id: "+data.i)
vm.job_ids.push(data.job_id)
getResults(data.job_id,data.i)}).error(function(data,status,headers,config){console.log('error status: '+status);vm.btn_fuzzy_disabled=false;vm.btn_label="Run Fuzzy!"})}}
function getResults(job_id,i){var timeout="";var tracker=function(){ $http.get('result/'+job_id).success(function(data,status,headers,config){if(status===202){vm['status'+i]=data
console.log('The current status is : '+data)}else if(status===200){console.log('The current status is : '+data)
if(data=="SUCCESS"){console.log('It is done. SUPERB!')
vm['status'+i]="FINISHED!"
vm['btn_download_disabled'+i]=false
vm.btn_sendcrm_disabled=false;}else if(data=="REVOKED"){vm['status'+i]="CANCELLED"}else{vm['status'+i]="FAILED!"}
vm.btn_label="Run Fuzzy!"
vm['lbl_loading_disabled'+i]=true
vm['lbl_finished_disabled'+i]=false
return false;}
 
timeout=$timeout(tracker,2000);}).error(function(error){});};tracker();}
function f_alert(text){alert(text)}}}());