$(document).ready(function(){
    // Forming csrf_token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie != '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };


    let data = {}

    $('.mybutton').on('click', function(e){
        data['action'] = 'NeedRandom';
        data['csrfmiddlewaretoken'] = getCookie('csrftoken');
        SendAjax();
    });


    function SendAjax(){
        $.ajax({
            url: 'http://127.0.0.1:8000/confirm/',
            method: 'POST',
            data: data,
            cached: true,
            success: function(data){
                console.log(data);
            },
            error: function(e){
                console.log(e);
            }
        })
    }
})