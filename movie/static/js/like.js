// shortcut for document.ready and $(function() {})
$(() => {


send_like();


});


function send_like() {


	var csrf = $('meta[name="csrf"]').attr('content');
	console.log(csrf)

}