function titleFilter() {

    let filter, table, element, txtValue;

    let titleInput = document.getElementById('TitleInput');
    filter = titleInput.value.toUpperCase();
    table = document.getElementById("books-to-filter");
    element = table.getElementsByTagName('tr');

    for (let i = 1; i < element.length; i++) {
        let td = element[i].getElementsByTagName("td")[0];
        txtValue = td.innerText;
        if (txtValue.toUpperCase().includes(filter)) {
          element[i].style.display = "";
        } else {
          element[i].style.display = "none";
        }
    }
}

function authorFilter() {

    let filter, table, element, txtValue;

    let AuthorInput = document.getElementById('AuthorInput');
    filter = AuthorInput.value.toUpperCase();
    table = document.getElementById("books-to-filter");
    element = table.getElementsByTagName('tr');

    for (let i = 1; i < element.length; i++) {
        let td = element[i].getElementsByTagName("td")[1];
        txtValue = td.innerText;
        if (txtValue.toUpperCase().includes(filter)) {
          element[i].style.display = "";
        } else {
          element[i].style.display = "none";
        }
    }
}

function languageFilter() {

    let filter, table, element, txtValue;

    let LanguageInput = document.getElementById('LanguageInput');
    filter = LanguageInput.value.toUpperCase();
    table = document.getElementById("books-to-filter");
    element = table.getElementsByTagName('tr');

    for (let i = 1; i < element.length; i++) {
        let td = element[i].getElementsByTagName("td")[6];
        txtValue = td.innerText;
        if (txtValue.toUpperCase().includes(filter)) {
          element[i].style.display = "";
        } else {
          element[i].style.display = "none";
        }
    }
}

function dateFilter() {

    let table, element, txtValue;
    let StartDateInput = document.getElementById('StartDateInput');
    let EndDateInput = document.getElementById('EndDateInput');

    table = document.getElementById("books-to-filter");
    element = table.getElementsByTagName('tr');

    for (let i = 1; i < element.length; i++) {
        let td = element[i].getElementsByTagName("td")[2];
        txtValue = td.innerText;
        if (dateCompare(txtValue,StartDateInput.value) && dateCompare(EndDateInput.value,txtValue)) {
          element[i].style.display = "";
        } else {
          element[i].style.display = "none";
        }
    }
}

function dateCompare(d1, d2){
    const date1 = new Date(d1);
    const date2 = new Date(d2);

    if(date1 > date2){
        return true
    } else if(date1 < date2){
        return false
    } else{
        return true
    }
}