const SearchField = document.querySelector("#searchField");

SearchField.addEventListener('keyup', (e) => {
    const searchValue = e.target.value;

    if (searchValue.trim().length>0){
        console.log("searchValue", searchValue);

        fetch("/search-expenses", {
        body: JSON.stringify({ searchText: searchValue }),
        method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);

                if(data.length===0)()
            })
    }
});