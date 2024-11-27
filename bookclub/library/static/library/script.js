var descP = document.getElementById('collapse-desc');
var showButton = document.querySelector('.show-more');

document.addEventListener('DOMContentLoaded', () => {
    
    checkButton();
    
    // window.addEventListener('resize', () => {
        
    //     let heightDesc = parseInt(computedDesc.getPropertyValue('height')) / parseInt(computedDesc.getPropertyValue('line-height'));
    //     console.log(heightDesc);
    // })
});

function checkButton() {
    let computedDesc = window.getComputedStyle(descP);
    let heightDesc = parseInt(computedDesc.getPropertyValue('height')) / parseInt(computedDesc.getPropertyValue('line-height'));
    console.log(heightDesc);
    if (heightDesc >= 7) {
        console.log("yes");
        showButton.innerHTML = '<i class="bi bi-caret-down-fill"></i> Read more  <i class="bi bi-caret-down-fill"></i>'
        showButton.style.display = "block";}
}