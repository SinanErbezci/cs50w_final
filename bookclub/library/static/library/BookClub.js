/**
 * @typedef {Object} InstantSearchOptions
 * @property {URL} searchUrl
 * @property {string} queryParam
 * @property {Function} responseParser
 * @property {Function} templateFunction
 */
class InstantSearch {
    /**
     * Initialises the instant search bar. Retrieves and creates element.
     * 
     * @param {HTMLElement} instantSearch 
     * @param {InstantSearchOptions} options 
     */
    constructor(instantSearch, options) {
        this.options = options;
        this.elements = {
            main: instantSearch,
            input: instantSearch.querySelector("input"),
            resultsContainer: document.createElement("div")
        };

        this.elements.resultsContainer.classList.add("search-bar-results");
        this.elements.main.appendChild(this.elements.resultsContainer);

        this.addListeners();
    }

    addListeners() {
        let delay;

        this.elements.input.addEventListener("input", () => {
            clearTimeout(delay);

            const query = this.elements.input.value;
            
            console.log(query)
            delay = setTimeout(() => {
                if (query.length < 3) {
                    this.populateResults([]);
                    return;
                }

                this.performSearch(query).then(results => {
                    this.populateResults(results);
                });
            },500);
        });

        this.elements.input.addEventListener("focus", () => {
            this.elements.resultsContainer.classList.add("visible");
        });

        this.elements.input.addEventListener("blur", () => {
            this.elements.resultsContainer.classList.remove("visible");
        });
    }

    populateResults(results) {
        // Removing all existing results
        while (this.elements.resultsContainer.firstChild) {
            this.elements.resultsContainer.removeChild(this.elements.resultsContainer.firstChild);
        }
    
        for (const [key,value] of Object.entries(results)) {
            if (Object.entries(value).length > 0) {
                for (const [title,id] of Object.entries(value)) {
                    let resultElement = document.createElement("div");
                    resultElement.className = "search-result";
                    this.elements.resultsContainer.appendChild(resultElement);
                    resultElement.innerHTML = this.createResultElement(key,title,id)
                }
            }

        }

    }

    createResultElement(type,title,id) {
        let linkId;
        if (type === "book") {
            linkId = `./browse/books/${id}`;
        }
        else if (type === "genre") {
            linkId = `./browse/genres/${id}`;
        }
        else {
            linkId = `./browse/authors/${id}`;
        }

        const elementName = `
            <a href="${linkId}" class="search-result-title book-link">${title}</a>
            <span class="search-result-type ">${type}</span>
        `;

        return elementName;
       const anchorElement = document.createElement("a");
       const spanElement = document.createElement("span");

       anchorElement.className = "search-result-title book-link";
       anchorElement.innerHTML = title;
       anchorElement.setAttribute('href', id)
       
       spanElement.classList.add("search-result-type");
       spanElement.innerHTML = type;



    }
    performSearch(query) {
        const url = new URL(this.options.searchUrl.toString());

        url.searchParams.set(this.options.queryParam,query);
        url.searchParams.set("long", "");

        this.setLoading(true);

        return fetch(url, {
            method: "get"
        }).then(response => {
            if (response.status !== 200) {
                throw new Error("Something went wrong with the search app.");
            }

            return response.json();
        }).then(responseData => {
            console.log(responseData);

            return this.options.responseParser(responseData);
        }).catch(error => {
            console.error(error);

            return [];
        }).finally(results => {
            this.setLoading(false);

            return results;
        });
    }

    setLoading(b) {
        this.elements.main.classList.toggle("search-bar-loading", b);
    }
}

export default InstantSearch;

// const descP = document.getElementById('collapse-desc');
// const showButton = document.querySelector('.show-more');
// const starRatings = document.querySelectorAll('.rating-star i');
// const ratingInput = document.querySelector('.rating-star input');
// const submitBtn = document.getElementById('review-submit');
// const feedbackForm = document.querySelector('.form-feedback');
// const reviewForm = document.getElementById('review-form');

// const readReviewBtns = document.querySelectorAll('#read-review');


// document.addEventListener('DOMContentLoaded', () => {
    
//     checkButton();
    
//     window.addEventListener('resize', () => {
//          checkButton();
//     });

//     showButton.addEventListener('click', readMoreLess);

//     // Star Rating
//     starRatings.forEach((item,index) => {
//         item.addEventListener('click', () => {
//             ratingInput.value = index + 1;
//             starRatings.forEach( i => {
//                 i.classList.replace('bi-star-fill', 'bi-star')
//                 i.classList.remove('active')
//             })
//             for( let i = 0; i < starRatings.length; i++) {
//                 if (i <= index) {
//                     starRatings[i].classList.replace('bi-star', 'bi-star-fill');
//                     starRatings[i].classList.add('active')
//                 }
//             }
//         })
//     });

//     // Submit Check
//     if (submitBtn !== null ){
//     submitBtn.addEventListener('click', (event) => {
//         event.preventDefault();
//         feedbackForm.style.display = 'block';

//         let a = document.getElementById('reviewform-text').value;
//         if (ratingInput.value){
//             if (a.length < 50) {
//                 feedbackForm.innerHTML = "Your review should be atleast 50 characters."
//             }
//             else if (a.length > 500) {
//                 feedbackForm.innerHTML = "Your review should not exceed 500 characters."
//             }
//             else {
//                 console.log("good");
//                 reviewForm.submit();
//             }
//         }
//         else {      
//             feedbackForm.innerHTML = "Please give a Star.";
//         }
//     })}

//     // readReviewBtns.forEach( (elem) => {
//     //     elem.addEventListener('click', (item) => {
//     //         item.
//     //     })
//     // })

//     ratingCheck();

// });

// function checkButton() {
//     if (descP.scrollHeight > descP.clientHeight) {
//         showButton.style.display = "block";}
//     else {
//         showButton.style.display = "none";
//         descP.className = "mb-0 collapse";
//         showButton.setAttribute('aria-expanded', "false");
//         showButton.innerHTML = '<i class="bi bi-caret-down-fill"></i> Read more  <i class="bi bi-caret-down-fill">'   
//     }
// }

// function readMoreLess() {
//     if (showButton.getAttribute('aria-expanded') == "true") {
//         showButton.innerHTML = '<i class="bi bi-caret-up-fill"></i> Read less  <i class="bi bi-caret-up-fill">'
//     }
//     else {
//         showButton.innerHTML = '<i class="bi bi-caret-down-fill"></i> Read more  <i class="bi bi-caret-down-fill">'
//     }
// }

// function ratingCheck() {
//     let starsRatings = document.querySelectorAll('.star-inner');
//     starsRatings.forEach( (elem) => {
//         elem.style.width = `${Math.round(Number(elem.dataset.rating)*20)}%`
//     })
// }
