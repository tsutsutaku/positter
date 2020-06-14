
function follows(follow_id) {

    var follow = document.getElementById('follow_button').innerHTML;

    console.log(follow)
    if (follow === 'フォロー中') {
        const follower_n = document.getElementById('follower').innerHTML
        document.getElementById('follower').innerHTML = parseInt(follower_n)-1;
        document.getElementById('follow_button').innerHTML = 'フォローする'
    } else {
        const follower_n = document.getElementById('follower').innerHTML
        document.getElementById('follower').innerHTML = parseInt(follower_n)+1;
        document.getElementById('follow_button').innerHTML = 'フォロー中'
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST',  'http://127.0.0.1:8000/follow/' + follow_id + '/');
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
    xhr.send(); 

}