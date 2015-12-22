$( document ).ready(function() {
    console.log( "ready!" );
    $( "#submit" ).bind( "click", getSimilarTickets);
});

function getSimilarTickets() {
	var ticketID = $("#ticketID").val()
	console.log(ticketID)
    $.ajax({
    	url: "/getSimilarTickets", 
    	type: "GET",
    	data:  ticketID,
    	success: function(result){
       $(".similarTickets").html(result)
    }});
}