function showLoginStatus(result) {
    alert(result);
}

function submitLogin(evt) {
    evt.preventDefault();

    var formInputs = {
        "username": $("#username").val(),
        "password": $("#password").val(),
    };

    $.post("/login", 
           formInputs,
           showLoginStatus);
}

$("#login-form").on("submit", submitLogin);