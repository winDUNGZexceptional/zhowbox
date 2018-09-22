// shortcut for document.ready and $(function() {})
$(() => {


	$('#send_like').click( send_like );


});


function send_like() {


	var csrf = $('meta[name="csrf"]').attr('content');
	var movie_id = $('meta[name="position_y"]').attr('content');
	// position_y is just a random name but it is just movie_id
	console.log(csrf);

	$.ajax({
		type: 'POST',
		data: {'csrfmiddlewaretoken' : csrf,},
		dataType: 'json',
		url: window.location.origin + '/movie/' + movie_id + '/like/',

		beforeSend: () => {
			console.log('sending..');

		},

		success: () => {
			console.log('success');

		},

		error: () => {
			console.log('error');
		}
	});



}