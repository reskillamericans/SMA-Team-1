const edit_button = document.querySelector(".edit_button");
const modal = document.querySelector(".modal_all");
const save = document.querySelector(".save_button");
const close_button = document.querySelector(".modal_close_button");
const body = document.body;

const bio_text_field = document.querySelector("#bio_edit");

const name_edit = document.querySelector("#name_edit");
const job_edit = document.querySelector("#job_edit");
const website_edit = document.querySelector("#website_edit");
const location_edit = document.querySelector("#location_edit");

const username = document.querySelectorAll(".username");
const occupation = document.querySelectorAll(".occupation");
const website = document.querySelector(".website");
const location_text = document.querySelector(".location_text");
const bio_profile = document.querySelector("._user_summary");

const wordcount = document.querySelector(".wordcount");
const text = document.querySelector("._user_summary").innerText;







let count_spaces = function(){
    var numWords = 0;
    for (var i = 0; i < text.length; i++) {
      var currentCharacter = text[i];

 
      if (currentCharacter == " ") {
        numWords += 1;
      }
    }
    return numWords
}




function your_function(event) {
  
}

bio_text_field.addEventListener('keyup', function(e){
  wordCounter(e.target.value);
});







function wordCounter(text) {
  var text = bio_text_field.value;
  var wordCount = 0;
  for (var i = 0; i <= text.length; i++) {
    if (text.charAt(i) == " ") {
      wordCount++;
    }
  }
  wordcount.innerText = wordCount;
  console.log(wordCount)
if(wordCount>50){
    wordcount.classList.add('red_over')
     save.classList.add("disabled_text");
    document.querySelector(".save_button").disabled = true;

}
else{
     wordcount.classList.remove("red_over");
         document.querySelector(".save_button").disabled = false;
           save.classList.remove("disabled_text");
}
if(wordCount > 50){

}


}


edit_button.addEventListener("click", () => {
  modal.classList.remove("modal_hide");
  body.classList.add("limit_scroll");
  fill();
});

close_button.addEventListener("click", () => {
  console.log(bio_text_field.value);
    modal.classList.add("modal_hide");
 
});

const fill = function () {
    numWords=0
  for (i = 0; i < username.length; i++) {
    name_edit.value = username[i].innerText;
  }

  for (i = 0; i < occupation.length; i++) {
    job_edit.value = occupation[i].innerText;
  }

  location_edit.value = location_text.innerText;
  website_edit.value = website.innerText;
  bio_text_field.value = bio_profile.innerText;

  for (var i = 0; i < text.length; i++) {
    var currentCharacter = text[i];


    if (currentCharacter == " ") {
      numWords += 1;
    }
  }
  wordcount.innerText = numWords;
 
};

save.addEventListener("click", () => {
  for (i = 0; i < username.length; i++) {
    username[i].innerText = name_edit.value;
  }

  for (i = 0; i < occupation.length; i++) {
    occupation[i].innerText = job_edit.value;
  }

  location_text.innerText = location_edit.value;
  website.innerText = website_edit.value;

  bio_profile.innerText = bio_text_field.value;

  modal.classList.add("modal_hide");
});
