function addInputField() {
  var container = document.getElementById("additionalInputs");
  var inputField = document.createElement("div");

  inputField.innerHTML = `
    <input type="text" placeholder="Food item" class="added-input" name="fooditem[]">
    <input type="text" placeholder="Quantity" class="added-input" name="quantity[]">
    <button class="delete-button">Delete</button>
  `;

  container.appendChild(inputField);

  // Attach a click event listener to the delete button
  inputField.querySelector(".delete-button").addEventListener("click", function() {
    container.removeChild(inputField);
  });
}