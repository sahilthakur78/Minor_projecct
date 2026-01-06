// Home page JavaScript
console.log("Brain Blitz Home - Loaded");

document.addEventListener('DOMContentLoaded', function() {
    const homeScreen = document.querySelector('.home-screen');
    const categoryScreen = document.querySelector('.category-screen');
    const startBtn = document.getElementById('startBtn');
    const startQuizBtn = document.getElementById('startQuizBtn');
    const backBtn = document.getElementById('backBtn');
    const categories = document.querySelectorAll('.category');
    
    let currentCategory = 'javascript';
    
    // Event Listeners
    if (startBtn) {
        startBtn.addEventListener('click', showCategoryScreen);
    }
    
    if (startQuizBtn) {
        startQuizBtn.addEventListener('click', startQuiz);
    }
    
    if (backBtn) {
        backBtn.addEventListener('click', showHomeScreen);
    }
    
    // Category selection
    categories.forEach(category => {
        category.addEventListener('click', function() {
            categories.forEach(cat => cat.classList.remove('selected'));
            this.classList.add('selected');
            currentCategory = this.getAttribute('data-category');
            console.log("Selected category:", currentCategory);
        });
    });
    
    // Functions
    function showCategoryScreen() {
        homeScreen.classList.remove('active');
        categoryScreen.classList.add('active');
        console.log("Showing category screen");
    }
    
    function showHomeScreen() {
        categoryScreen.classList.remove('active');
        homeScreen.classList.add('active');
        console.log("Showing home screen");
    }
    
    function startQuiz() {
        if (!currentCategory) {
            alert('Please select a category!');
            return;
        }
        window.location.href = `/quiz?category=${currentCategory}`;
    }
    
    // Auto-select first category
    if (categories.length > 0) {
        categories[0].classList.add('selected');
        currentCategory = categories[0].getAttribute('data-category');
    }
    
    console.log("✅ Home page ready!");
});