$(function ($) {
    $('#ajax_login').submit(function(e){
        e.preventDefault()
        console.log(this)
        $.ajax({
            type: this.method,
            url: this.action,
            data: $(this).serialize(),
            dataType: "json",
            success: function (response){
                console.log(response)
            }
            error: function (response){
                console.log(response)
            }
        })
    })
})