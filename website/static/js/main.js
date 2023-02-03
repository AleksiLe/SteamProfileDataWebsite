function deleteNote(steamdata_id) {
    fetch('/delete-steam_id', {
        method: 'POST',
        body: JSON.stringify({steamdata_id: steamdata_id})
    }).then((_res) => {
        window.location.href = "/";
    });
}
//Select DOM Items
/*
const submitBtn = document.querySelector('.submit-btn');
const data = document.querySelector('.data');

//Set On Click Listener
let showInfo = false;
submitBtn.addEventListener('click', toggleBtn);

function toggleBtn() {
    if(!showInfo) {
        console.log(document.getElementById('steam-id').value)
        data.classList.add('show');


        //Set Info State
        showInfo = true;
    } else {
        data.classList.remove('show');

        //Set Info State
        showInfo = false;
    }
}
*/
