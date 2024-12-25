import InstantSearch from "./BookClub.js";

const searchSection = document.querySelector("#searchBar"); 
const instantSearch = new InstantSearch(searchSection, {
    searchUrl: new URL("http://127.0.0.1:8000/search"),
    queryParam: "q",
    responseParser: (responseData) => {
        return responseData.data;
    },
    templateFunction: (result) => {
        
    }
});

console.log(instantSearch);