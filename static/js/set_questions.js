let optionsCount = 1;
const addOptionsBtn = document.querySelector("#add-options-btn");
const optionsContainer = document.querySelector(".options-container");

// * Event Listeners

addOptionsBtn.addEventListener("click", addOptionToContainer);

// * Event handlers

function addOptionToContainer(e) {
  e.preventDefault();
  if (optionsCount <= 4) {
    let newOptionInput = document.createElement("input");
    newOptionInput.setAttribute("class", "form-control");
    newOptionInput.setAttribute("name", `option_${optionsCount}`);
    newOptionInput.setAttribute("maxlength", 18);
    optionsContainer.appendChild(newOptionInput);
    optionsCount++;
  } else {
    alert("Maximum of 4 options allowed");
  }
}
