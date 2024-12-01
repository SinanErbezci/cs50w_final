var descP = document.getElementById('collapse-desc');
var showButton = document.querySelector('.show-more');

document.addEventListener('DOMContentLoaded', () => {
    
    checkButton();
    
    window.addEventListener('resize', () => {
         checkButton();
    });

    showButton.addEventListener('click', readMoreLess);
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