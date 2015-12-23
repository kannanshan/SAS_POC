$( document ).ready(function() {
    console.log("ready");
    $( "#submit" ).bind( "click", getTicketDetails);
    $( "#fetch" ).bind( "click", getSimilarTickets);
    $( "#fetch" ).hide()
});

function getTicketDetails() {
	 var fd = new FormData();
   var ticketID = $('#ticket-id').val();
   console.log(ticketID);
   $( "#fetch" ).show()
   fd.append('ticket_id',ticketID);
   $.ajax({
                  url: '/get_ticket_details',
                  data: fd,
                  contentType: false,
                  processData: false,
                  type: 'POST',
                  dataType: 'html',
                  success: function(resp){
                    $('.ticket-details').html(resp);

                                       }
              });
}

function getSimilarTickets() {
   var fd = new FormData();
   var ticketID = $('#ticket-id').val();
   console.log(ticketID);
   fd.append('ticket_id',ticketID);
   $.ajax({
                  url: '/get_similar_tickets',
                  data: fd,
                  contentType: false,
                  processData: false,
                  type: 'POST',
                  dataType: 'html',
                  success: function(resp){
                    $('.similar-tickets').html(resp);

                                       }
              });
}
