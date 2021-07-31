const url = "http://127.0.0.1:8000/";

let titleInput = document.getElementById('TitleInput');
let AuthorInput = document.getElementById('AuthorInput');
let LanguageInput = document.getElementById('LanguageInput');
let StartDateInput = document.getElementById('StartDateInput');
let EndDateInput = document.getElementById('EndDateInput');

let data = {
    title: titleInput.value,
    author: AuthorInput.value,
    language: LanguageInput.value,
    start_date: StartDateInput.value,
    end_date: EndDateInput.value
};
sendPOST = () => {
    document.getElementById("search-result").innerHTML = "";
        return fetch(url+"books-title",{
            headers: {
                'X-CSRFToken': csrftoken,
                'Content-Type': 'application/json'
            },
            method: "POST",
            body: JSON.stringify(data)
        })
        .then((response) => response.json())
        .then((json) => {
            json = JSON.parse(json);
            for (let i = 0; i < json.length; i++) {
            let item = json[i].fields;
            console.log(item);
            document.getElementById("search-result").innerHTML += "<br>" + item.title;
            }
        })
        .catch((error) => {
            console.error(error);
        });
    };