const like = document.querySelector(".like_container");
const post = document.querySelector(".post_container");

const reply = document.querySelector(".reply_container");



const posts = document.querySelector(".posts");
const likes = document.querySelector(".likes");
const replies = document.querySelector(".replies");

const middlenavspre = document.getElementsByClassName("section_nav");
const middlenavs = Array.from(middlenavspre);

const side_iconspre = document.getElementsByClassName("side_icon");
const side_icons = Array.from(side_iconspre);

const hamb = document.querySelector(".hamb_button");
const x_button = document.querySelector(".X_button");
const left_side = document.querySelector(".left_side_bar");
const mobile_profile = document.querySelector(".mobile-profile-pic-sidebar");

const redd_heartspre = document.getElementsByClassName('heart_img')
const redd_hearts = Array.from(redd_heartspre)


hamb.addEventListener("click", () => {
  left_side.classList.add("left_side_bar_mobile_slide");
  mobile_profile.classList.toggle("mobile_visible");
});
x_button.addEventListener("click", () => {
  left_side.classList.toggle("left_side_bar_mobile_slide");

  setTimeout(function () {
    mobile_profile.classList.toggle("mobile_visible");
  }, 600);
});

const left_linkspre = document.getElementsByClassName(
  "side_icon_and_links_item"
);
const left_links = Array.from(left_linkspre);



function blacktext() {
  middlenavs.forEach((middlenav) => {
    middlenav.classList.remove("clicked");
  });
}



function blacktext_leftside() {
  left_links.forEach((left_link) => {
    left_link.classList.remove("blue-links");
  });
}

function blackicon_leftside() {
  side_icons.forEach((side_icon) => {
   side_icon.classList.remove("side_icon_blue");
  });
}





function showNav() {
  if (!posts.classList.contains("clicked")) {
    post.classList.add("hidenav");
  } else {
    post.classList.remove("hidenav");
  }

  if (!likes.classList.contains("clicked")) {
    like.classList.add("hidenav");
  } else {
    like.classList.remove("hidenav");
  }

  if (!replies.classList.contains("clicked")) {
    reply.classList.add("hidenav");
  } else {
    reply.classList.remove("hidenav");
  }
}

for (let i = 0; i < middlenavs.length; i++) {
  middlenavs[i].addEventListener("click", function () {
    blacktext();
    middlenavs[i].classList.add("clicked");
 
    showNav();
  });
}

for (let i = 0; i < left_links.length; i++) {
  left_links[i].addEventListener("click", function () {
    blacktext_leftside();
    blackicon_leftside();
    left_links[i].classList.add("blue-links");
       side_icons[i].classList.toggle("side_icon_blue");
  });
}


function redhearts() {
  red_hearts.forEach((red_heart) => {
    red_hearts.classList.remove("red_heart");
  });
}


for (let i = 0; i < redd_hearts.length; i++) {
  redd_hearts[i].addEventListener("click", function () {
   
    
    redd_hearts[i].classList.toggle("red_heart");
  });
}

