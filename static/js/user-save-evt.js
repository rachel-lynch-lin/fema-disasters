"use strict";

function showEventResults(result) {

    $("#saved-events").append(`<li><a href="/events/${result.fema_id}"> ${result.event_name} (${result.fema_id})</a></li>`);
    console.log(result);
}

function saveEvent(evt) {
    evt.preventDefault();
    
    const femaID = $("#event-id").val();
    console.log(`/save/event/${femaID}`);

    
    $.post(`/save/event/${femaID}`, femaID, showEventResults);
}

$("#save-event-form").on('submit', saveEvent);
