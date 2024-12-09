const descP = document.getElementById('collapse-desc');
const showButton = document.querySelector('.show-more');
const starRatings = document.querySelectorAll('.rating-star i');
const ratingInput = document.querySelector('.rating-star input');
const submitBtn = document.getElementById('review-submit');
const feedbackForm = document.querySelector('.form-feedback');
const reviewForm = document.getElementById('review-form');

const readReviewBtns = document.querySelectorAll('#read-review');


document.addEventListener('DOMContentLoaded', () => {
    
    checkButton();
    
    window.addEventListener('resize', () => {
         checkButton();
    });

    showButton.addEventListener('click', readMoreLess);

    // Star Rating
    starRatings.forEach((item,index) => {
        item.addEventListener('click', () => {
            ratingInput.value = index + 1;
            starRatings.forEach( i => {
                i.classList.replace('bi-star-fill', 'bi-star')
                i.classList.remove('active')
            })
            for( let i = 0; i < starRatings.length; i++) {
                if (i <= index) {
                    starRatings[i].classList.replace('bi-star', 'bi-star-fill');
                    starRatings[i].classList.add('active')
                }
            }
        })
    });

    // Submit Check
    if (submitBtn !== null ){
    submitBtn.addEventListener('click', (event) => {
        event.preventDefault();
        feedbackForm.style.display = 'block';

        let a = document.getElementById('reviewform-text').value;
        if (ratingInput.value){
            if (a.length < 50) {
                feedbackForm.innerHTML = "Your review should be atleast 50 characters."
            }
            else if (a.length > 500) {
                feedbackForm.innerHTML = "Your review should not exceed 500 characters."
            }
            else {
                console.log("good");
                reviewForm.submit();
            }
        }
        else {      
            feedbackForm.innerHTML = "Please give a Star.";
        }
    })}

    // readReviewBtns.forEach( (elem) => {
    //     elem.addEventListener('click', (item) => {
    //         item.
    //     })
    // })

    ratingCheck();

});

function checkButton() {
    if (descP.scrollHeight > descP.clientHeight) {
        showButton.style.display = "block";}
    else {
        showButton.style.display = "none";
        descP.className = "mb-0 collapse";
        showButton.setAttribute('aria-expanded', "false");
        showButton.innerHTML = '<i class="bi bi-caret-down-fill"></i> Read more  <i class="bi bi-caret-down-fill">'   
    }
}

function readMoreLess() {
    if (showButton.getAttribute('aria-expanded') == "true") {
        showButton.innerHTML = '<i class="bi bi-caret-up-fill"></i> Read less  <i class="bi bi-caret-up-fill">'
    }
    else {
        showButton.innerHTML = '<i class="bi bi-caret-down-fill"></i> Read more  <i class="bi bi-caret-down-fill">'
    }
}

function ratingCheck() {
    let starsRatings = document.querySelectorAll('.star-inner');
    starsRatings.forEach( (elem) => {
        elem.style.width = `${Math.round(Number(elem.dataset.rating)*20)}%`
    })
}
