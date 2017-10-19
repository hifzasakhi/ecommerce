$(function(){
	$('button').click(function(){
		var email = $('#txtEmail').val();
		var pass = $('#txtPassword').val();
		$.ajax({
			url: '/signUpUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
