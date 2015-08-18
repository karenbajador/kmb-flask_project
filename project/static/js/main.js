// custom javascript


$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {
    $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        
        var input = $(this).parents('.input-group').find(':text'),
            log = numFiles > 1 ? numFiles + ' files selected' : label;
        
        if( input.length ) {
            input.val(log);
        } else {
            if( log ) alert(log);
        }
        
    });

	// Storing the file name in the queue
	var fileName = "";

	// On file add assigning the name of that file to the variable to pass to the web service
	$('#fileupload').bind('fileuploadadd', function (e, data) {
	  $.each(data.files, function (index, file) {
	    fileName = file.name;
	    console.log("fileName:"+fileName)
	  });
	});

	// On file upload submit - assigning the file name value to the form data
	$('#fileupload').bind('fileuploadsubmit', function (e, data) {
	  data.formData = {"file" : fileName};
	  console.log("fileName >> :"+fileName)
	});	



});