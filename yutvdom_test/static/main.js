$(function ($) {
    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }

    $('#ajax_login').submit(function(e){
        e.preventDefault()
        console.log(this)
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            headers:{'X-CSRFToken': getCookie(name:'csrftoken ')},
            dataType: "json",
            success: function (response){
                console.log('ok -', response)
            }
            error: function (response){
                console.log('err-', response)
            }
        })
    })
})