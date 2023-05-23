
$(document).ready(function() {
		$('body').on('submit','#contact-form', function(event) {
				event.preventDefault(); //prevent the default form submission

				//perform an AJAX request to submit the form data
				$.ajax({
					url:$(this).attr('action'),
					method: $(this).attr('method'),
					data: $(this).serialize(),
					dataType: 'json',
					success: function(response) {
						if (response.success) {
						//refresh the page silently
						window.location.reload(true);  // this performs hard reflesh
						} else {
						// handle form errors
						console.log(response.errors);
						}
						},
						error: function(xhr, textStatus, errorThrown) {
						console.log('Error:', errorThrown);
						}
						});
		});
});
