function showEventResults(result) {
   $("#saved-events").append(" The End!");
   console.log(result);
}

function saveEvent(evt) {
    evt.preventDefault();
    
    const femaID = $("#event-id").val();
    console.log(`/save/event/${femaID}`);

    
    $.post(`/save/event/${femaID}`, femaID, showEventResults);
}

$("#save-event-form").on('submit', saveEvent);



// $.get("/save/event/{", function (results) {
//       alert(": " + results);
// });