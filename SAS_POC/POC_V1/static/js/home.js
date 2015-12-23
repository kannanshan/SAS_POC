$( document ).ready(function() {
    console.log("ready");
    $( "#submit" ).bind( "click", getTicketDetails);
});

function getTicketDetails() {
	 var fd = new FormData();
   var ticketID = $('#ticket-id').val();
   console.log(ticketID);
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
