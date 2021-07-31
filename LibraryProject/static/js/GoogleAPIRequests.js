let input = document.getElementById('Input');
let url = "http://127.0.0.1:8000/";
let books =  null;
function PrintResults() {

    document.getElementById("content").innerHTML = "";
    books = sendGET();


}

sendGET = () => {
        return fetch("https://www.googleapis.com/books/v1/volumes?q="+input.value.replace(/\s/g,'+')+":keyes&key=AIzaSyCXjqhDbKoNHDV9o7AQkD5hVhOTKhdl3JI",{
            headers: {
                'Content-Type': 'application/json'
            },
            method: "GET",

        })
        .then((response) => response.json())
        .then((json) => {
            let bookdata = json;
            for (var i = 0; i < bookdata.items.length; i++) {
            var item = bookdata.items[i];
            // in production code, item.text should have the HTML entities escaped.
            document.getElementById("content").innerHTML += "<br>" + item.volumeInfo.title + "<input id="+i+" type='submit'/>" ;
            }
            for (var i = 0; i < bookdata.items.length; i++) {
                // in production code, item.text should have the HTML entities escaped.
                document.getElementById(i.toString()).addEventListener("click", add) ;
                document.getElementById(i.toString()).myParam = {
                    id: i,
                    book: bookdata.items
                }
            }
        })
        .catch((error) => {
            console.error(error);
        });
    };


add = (evt) => {
    let number = evt.currentTarget.myParam.book[evt.currentTarget.myParam.id].volumeInfo;
    let temp = null;
    console.log(number);
    if(number.publishedDate.length < 10){
        temp = number.publishedDate+"-01-01";
    }else{
        temp = number.publishedDate;
    }
    let data = {
        title: number.title,
        author: number.authors[0],
        publication_date: temp,
        isbn: number.industryIdentifiers[0].identifier,
        number_of_pages: number.pageCount,
        cover: number.imageLinks.thumbnail,
        language: number.language
    };

    return fetch(url+"books-add-view",{
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
