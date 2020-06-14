
function follows(follow_id) {

    var xhr = new XMLHttpRequest();
    xhr.open('POST',  'http://127.0.0.1:8000/follow/' + follow_id + '/');
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
    xhr.send(); 
}