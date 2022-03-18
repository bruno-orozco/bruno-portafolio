function updateMenuButton() {
	$('.js-menu-button').find('.menu-icon').toggleClass('is-active');
}

$(document).ready(function() {

	$('.js-menu-button').click(function(e){

		e.preventDefault();
		updateMenuButton();

	});

});

const hambur = document.getElementsByClassName('nav__lines')[0];
const menu = document.getElementsByClassName('nav-ul')[0];



hambur.addEventListener('click', () => {
    if(menu.style.display === "flex"){  
        menu.style.display = "none";
    } else{
        menu.style.display = "flex";
    }
    
})

