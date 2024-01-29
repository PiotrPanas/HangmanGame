let newValue = 5; // or whatever value you want
incorrectGuesses = newValue;

function guessHearts(incorrectGuesses) {
  var guessesDiv = document.getElementById("guesses");
  guessesDiv.innerHTML = ""; // Clear the guesses div

  for (let i = 1; i <= 5; i++) {
    var img = document.createElement("img");
    img.id = "guess" + i;

    if (i <= incorrectGuesses) {
      img.src = "/static/images/heart-broken.png";
    } else {
      img.src = "/static/images/heart-full.png";
    }

    guessesDiv.appendChild(img);
  }
}

// Call the guessHearts function when the page loads
window.onload = function () {
  guessHearts(incorrectGuesses);
};

// AJAX request to handle guesses
$("#guessButton").click(function () {
  var guess = $("#guessInput").val();
  $.ajax({
    url: "/guess",
    type: "POST",
    data: { guess: guess },
    success: function (response) {
      if (response.correct === false) {
        incorrectGuesses++;
        guessHearts(incorrectGuesses);
      }
    },
  });
});
