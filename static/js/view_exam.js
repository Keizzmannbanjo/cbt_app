let tabBtns = document.querySelectorAll(".tab-btn");
tabBtns.forEach((item) => {
  item.addEventListener("click", handleTabChange);
});

function handleTabChange(e) {
  if (e.target.classList.contains("question-btn")) {
    document.querySelector(".candidates_container").style.display = "none";
    document.querySelector(".questions_container").style.display = "block";
    if (!e.target.classList.contains(".active")) {
      document.querySelector(".question-btn").classList.add("active");
      document.querySelector('.candidate-btn').classList.remove('active')
    }
  } else if (e.target.classList.contains("candidate-btn")) {
    document.querySelector(".questions_container").style.display = "none";
    document.querySelector(".candidates_container").style.display = "block";
    if (!e.target.classList.contains(".active")) {
      document.querySelector(".candidate-btn").classList.add("active");
      document.querySelector('.question-btn').classList.remove('active')
    }
  }
}
