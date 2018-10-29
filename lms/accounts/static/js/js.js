function changeTable(button){
     var allButtons = document.getElementById("nav-btns");

     for(i = 0; i < allButtons.getElementsByTagName("a").length; i++)
     {
          allButtons.getElementsByTagName("a")[i].classList.remove("active-button");
     }
     button.className += "active-button"


     
     //change table de notas
}