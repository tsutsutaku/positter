


function likes(pk, tf) {

    var color = document.getElementById(`like_${pk}`).style.color;

    if (color == "red") {
        const like_num = parseInt(document.getElementById(`like_num_${pk}`).textContent); 
        document.getElementById(`like_num_${pk}`).innerHTML = like_num - 1
        document.getElementById(`like_${pk}`).style.color = 'black';

    } else {
        const like_num = parseInt(document.getElementById(`like_num_${pk}`).textContent); 
        document.getElementById(`like_num_${pk}`).innerHTML = like_num + 1
        document.getElementById(`like_${pk}`).style.color = 'red';
    }
    var xhr = new XMLHttpRequest();
    xhr.open('POST',  'http://127.0.0.1:8000/like/' + pk + '/');
    xhr.setRequestHeader("X-CSRFToken", Cookies.get('csrftoken'));
    xhr.send(); 
}