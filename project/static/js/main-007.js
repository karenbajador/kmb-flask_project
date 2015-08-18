// custom javascript


$(document).on('change', '.btn-file :file', function() {
  var input = $(this),
      numFiles = input.get(0).files ? input.get(0).files.length : 1,
      label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
  input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {

	$('#fuzzy-fileupload').change(function(){

		console.log("*************")
		$.each( $(this)[0].files, function( index, file ) {
			console.log( "file: " + file.name );
			$("#fuzzy-selectedfiles").append("<br/>")
			$("#fuzzy-selectedfiles").append(file.name)

		});
		console.log("*************")


	})


});