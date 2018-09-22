// shortcut for document.ready and $(function() {})
$(() => {

	var current_likes;

	$('#send_like').click( send_like );


});


function send_like() {


	var current_likes;
	
	var csrf = $('meta[name="csrf"]').attr('content');
	var movie_id = $('meta[name="position_y"]').attr('content');
	// position_y is just a random name but it is just movie_id

	$.ajax({
		type: 'POST',
		data: {'csrfmiddlewaretoken' : csrf,},
		dataType: 'json',
		url: window.location.origin + '/movie/' + movie_id + '/like/',

		beforeSend: () => {
			console.log('sending..');

		},

		success: (data) => {
			console.log('success!')
			$('#movie_likes').html(data.likes.toString());

		},

		error: () => {
			console.log('error.');
		}
	});

}