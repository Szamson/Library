const url = "http://127.0.0.1:8000/";
const data = {
    title: "Game of Thrones",
    author: "",
    language: "",
    start_date: "1000-01-01",
    end_date: "2021-07-12"
};
sendPOST = () => {
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
            return json;
        })
        .catch((error) => {
            console.error(error);
        });
    };

console.log(sendPOST());