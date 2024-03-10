// Handles the form submission for the text input
document.getElementById('textForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const userInput = document.getElementById('textInput').value;


    // Make an AJAX call to the backend to process the user input
    // no idea how to do this so bless chatGPT for the help
    fetch('/generate_flashcards', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: userInput })
    })
    .then(response => response.json())
    .then(data => {
        if (typeof(data.output) === 'string'){
            displayFlashcards(data.output)
        }
        else{
            displayFlashcards("Error: The server did not return a valid response. Backend error go fix it.")
        }

    })
    .catch((error) => {
        console.error('Error:', error);
    });

});


function displayFlashcards(flashcards) {
    const flashcardsOutput = document.getElementById('flashcardsOutput');
    flashcardsOutput.value = flashcards; // Assuming 'flashcards' is a string
}


// Handles the `copy to clipboard` button clicks
document.getElementById('copyButton').addEventListener('click', function() {
    const flashcardsOutput = document.getElementById('flashcardsOutput');
    flashcardsOutput.select();
    navigator.clipboard.writeText(flashcardsOutput.value);
});
