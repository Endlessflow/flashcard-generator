# Scope and Project Requirements

## Project Overview

The objective of this project is to create a simplified web application leveraging the capabilities of OpenAI's language models to generate flashcards from user-provided text. The application aims to facilitate learning by enabling users to extract key information from texts and convert them into a question-and-answer format suitable for memorization and study.

## Core Functionality

### Flashcard Generation

- **User Input Processing**: Accept textual input from the user to be transformed into flashcards.
- **Text Cleaning**: Implement a preprocessing step to clean and normalize the input text.
- **Text Processing and Flashcard Creation**: Process the cleaned text to extract salient points and generate flashcards in a question-and-answer format.

### Optional Feature

- **Export to Anki-Compatible Format**: If time permits, add functionality to export generated flashcards into a CSV format compatible with Anki, focusing on simplicity with a question and answer format.

## Technology Stack

- **Backend Framework**: Flask will be used for its simplicity and suitability for beginners, offering a gentle learning curve.
- **LLM Integration**: OpenAI API will be directly utilized for leveraging language model capabilities, prioritizing straightforward integration for text processing.
- **Frontend Development**: Basic HTML, CSS, and potentially minimal JavaScript will be employed to handle user interactions and display the generated flashcards.

## User Stories

- **Scenario**: A user, Mark, is studying concurrency and wishes to remember a specific paragraph from a tutorial.
- **Action**: Mark inputs the paragraph into the application and clicks the process button.
- **Outcome**: The application processes the text, and the interface displays generated flashcards in a human-readable format, allowing Mark to review and manually transfer selected flashcards into Anki.

## Project Structure

### Frontend

- The user interface will adopt a two-column layout, with the left column designated for text input and the right column for displaying generated flashcards.

### Backend

- **Controller**: A simple router will direct requests to a facade controller responsible for the "process text" operation, returning flashcard data as a JSON list.
- **Agents**: The backend will feature a series of agents, each tasked with a specific function in the text processing chain—text cleaning, information extraction for rote memorization, and flashcard generation.

## Testing

- **Route Testing**: Initial tests will verify the functionality and robustness of application routes.
- **Flexibility for Additional Tests**: Further testing will be determined based on project progress and will adapt to development needs.



*This document was generated with the help of our good friend chatGPT for improved readability*