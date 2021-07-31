function myFunction(changed) {

    let filter, table, element, txtValue;

    let titleInput = document.getElementById('TitleInput');
    let AuthorInput = document.getElementById('AuthorInput');
    let LanguageInput = document.getElementById('LanguageInput');

    switch (changed) {
        case 'Title':
            filter = titleInput.value.toUpperCase();
            break;
        case 'Author':
            filter = AuthorInput.value.toUpperCase();
            break;
        case 'Language':
            filter = LanguageInput.value.toUpperCase();
            break;
        case 'Date':
            let StartDateInput = document.getElementById('StartDateInput');
            let EndDateInput = document.getElementById('EndDateInput');
            break;
    }

    table = document.getElementById("books-to-filter");
    element = table.getElementsByTagName('tr');

    for (let i = 1; i < element.length; i++) {
    let td = element[i].getElementsByTagName("td")[0];
    txtValue = td.innerText;
    if (txtValue.toUpperCase().includes(filter)) {
      element[i].style.display = "flow";
    } else {
      element[i].style.display = "none";
    }
    }
}