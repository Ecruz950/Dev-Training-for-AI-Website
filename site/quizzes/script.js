
// Mappings of correct feedback for each question
const q1CorrectFeedback = new Map([
    // Question 1 
    ["Large Language Models", "Correct, LLM explicitly stands for this phrase."]
]);
const q2CorrectFeedback = new Map([
    // Question 2
    ["False", "Correct, they can produce confident but incorrect statements."]
]);
const q3CorrectFeedback = new Map([
    // Question 3
    ["The quality of the training data and amount of training data.", "Correct, both factors limit capabilities."]
]);
const q4CorrectFeedback = new Map([
    // Question 4
    ["True", "Correct, generated code can contain flaws"]
]);
const q5CorrectFeedback = new Map([
    // Question 5
    ["False", "Correct, we only have narrower AI."]
]);
const q6CorrectFeedback = new Map([
    // Question 6
    ["True", "Correct, present AI is specialized for specific tasks."]
]);
const q7CorrectFeedback = new Map([
    // Question 7
    ["False", "Correct, they cannot reliably handle completely novel tasks without errors."]
]);
const q8CorrectFeedback = new Map([
    // Question 8
    ["All of the above.", "Correct, all are examples of bias."]
]);
const q9CorrectFeedback = new Map([
    // Question 9
    ["The software developer using LLMs.", "Correct, it’s up to developers to vet the code."]
]);
const q10CorrectFeedback = new Map([
    // Question 10
    ["Spell Check", "Correct, they suggest text or responses based on learned patterns."]
]);
const q11CorrectFeedback = new Map([
    // Question 11
    ["No", "Correct, they are not designed to reliably replace search engines."]
]);

// Mappings of incorrect feedback for each question
const q1IncorrectFeedback = new Map([
    // Question 1
    ["Long Language Models", "Incorrect, \"LLM\" stands for \"Large Language Models,\" not \"Long.\""],
    ["Long Language Mappings", "Incorrect, this is not a known term."],
    ["None of the above", "Incorrect, there is a correct option given."],
]);
const q2IncorrectFeedback = new Map([
    // Question 2
    ["True", "Incorrect, LLMs may struggle with fact-checking."]
]);
const q3IncorrectFeedback = new Map([
    // Question 3
    ["There are no restrictions.", "Incorrect, data quality and quantity both matter."],
    ["The quality of the training data.", "Incorrect, quality alone is not enough."],
    ["The amount of training data.", "Incorrect, quantity alone is not enough."]
]);
const q4IncorrectFeedback = new Map([
    // Question 4
    ["False", "Incorrect, vulnerabilities are possible."]
]);
const q5IncorrectFeedback = new Map([
    // Question 5
    ["True", "Incorrect, AGI does not yet exist."]
]);
const q6IncorrectFeedback = new Map([
    // Question 6
    ["False", "Incorrect, narrow AI does exist today."]
]);
const q7IncorrectFeedback = new Map([
    // Question 7
    ["True", "Incorrect, they rely heavily on their training data."]
]);
const q8IncorrectFeedback = new Map([
    // Question 8
    ["Only hiring male candidates because those were the successful candidates in the training data.", "Incorrect, this is not the only example of bias."],
    ["Higher false positive matching for faces of racial minorities.", "Incorrect, this is not the only example of bias."],
    ["An image sorting algorithm assuming a banana is a bus.", "Incorrect, this is not the only example of bias."],
]);
const q9IncorrectFeedback = new Map([
    // Question 9
    ["Those who made the AI.", "Incorrect, they can’t verify each use case."],
    ["The AI.", "Incorrect, AI cannot assume legal or ethical responsibility."],
    ["Thomas Edison.", "Incorrect, this is not relevant."]
]);
const q10IncorrectFeedback = new Map([
    // Question 10
    ["Search Engines", "Incorrect, they do not primarily retrieve existing data."],
    ["Operating Systems", "Incorrect, they do not manage hardware or system resources."],
    ["Calculator Applications", "Incorrect, they’re not purely for arithmetic."]
]);
const q11IncorrectFeedback = new Map([
    // Question 11
    ["Yes", "Incorrect, they can be inaccurate or outdated."],
]);
// Counter for the number of correct answers
let correctCount = 0;


function checkAnswer(name, feedbackResult) {
    // Gets the html element of the selected radio button
    const selectedOption = document.querySelector(`input[name=${name}]:checked`);
    // console.log(selectedOption);
    // Gets the html element to display the response feedback
    const resultElement = document.getElementById(feedbackResult);
    // Gets the text contained next to the users selected radio button
    const label = selectedOption.parentElement.textContent.trim();
    // Gets the html element of the proceed button
    const proceedButton = document.getElementById("proceedBtn");

    // Check what question the user is answering based on the radio button they selected (q1, q2, q3, etc.)
    if (name === "q1") {
        // if the correct answer is selected, display the correct feedback
        if (q1CorrectFeedback.has(label)) {
            // Display the correct feedback
            resultElement.textContent = q1CorrectFeedback.get(label);
            // Disable all radio buttons for the question
            document.querySelectorAll('input[name="q1"]').forEach(radio => radio.disabled = true);
            // Change the class of the result element to "correct" so that it appears to the user
            resultElement.className = "correct";
            // Increment the correct count
            correctCount++;
        // If the incorrect answer is selected, display the incorrect feedback
        } else if (q1IncorrectFeedback.has(label)) {
            // Display the incorrect feedback
            resultElement.textContent = q1IncorrectFeedback.get(label);
            // Change the class of the result element to "incorrect" so that it appears to the user
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q2") {
        // if the correct answer is selected, display the correct feedback
        if (q2CorrectFeedback.has(label)) {
            resultElement.textContent = q2CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q2"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q2IncorrectFeedback.has(label)) {
            resultElement.textContent = q2IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q3") {
        // if the correct answer is selected, display the correct feedback
        if (q3CorrectFeedback.has(label)) {
            resultElement.textContent = q3CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q3"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q3IncorrectFeedback.has(label)) {
            resultElement.textContent = q3IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q4") {
        // if the correct answer is selected, display the correct feedback
        if (q4CorrectFeedback.has(label)) {
            resultElement.textContent = q4CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q4"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q4IncorrectFeedback.has(label)) {
            resultElement.textContent = q4IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q5") {
        // if the correct answer is selected, display the correct feedback
        if (q5CorrectFeedback.has(label)) {
            resultElement.textContent = q5CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q5"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q5IncorrectFeedback.has(label)) {
            resultElement.textContent = q5IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q6") {
        // if the correct answer is selected, display the correct feedback
        if (q6CorrectFeedback.has(label)) {
            resultElement.textContent = q6CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q6"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q6IncorrectFeedback.has(label)) {
            resultElement.textContent = q6IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q7") {
        // if the correct answer is selected, display the correct feedback
        if (q7CorrectFeedback.has(label)) {
            resultElement.textContent = q7CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q7"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q7IncorrectFeedback.has(label)) {
            resultElement.textContent = q7IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q8") {
        // if the correct answer is selected, display the correct feedback
        if (q8CorrectFeedback.has(label)) {
            resultElement.textContent = q8CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q8"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q8IncorrectFeedback.has(label)) {
            resultElement.textContent = q8IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q9") {
        // if the correct answer is selected, display the correct feedback
        if (q9CorrectFeedback.has(label)) {
            resultElement.textContent = q9CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q9"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q9IncorrectFeedback.has(label)) {
            resultElement.textContent = q9IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q10") {
        // if the correct answer is selected, display the correct feedback
        if (q10CorrectFeedback.has(label)) {
            resultElement.textContent = q10CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q10"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q10IncorrectFeedback.has(label)) {
            resultElement.textContent = q10IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    else if (name === "q11") {
        // if the correct answer is selected, display the correct feedback
        if (q11CorrectFeedback.has(label)) {
            resultElement.textContent = q11CorrectFeedback.get(label);
            document.querySelectorAll('input[name="q11"]').forEach(radio => radio.disabled = true);
            resultElement.className = "correct";
            correctCount++;
        } else if (q11IncorrectFeedback.has(label)) {
            resultElement.textContent = q11IncorrectFeedback.get(label);
            resultElement.className = "incorrect";
        }
    }
    // If all questions are correct, enable the submit button for the user to proceed
    if (correctCount === 11) {
        proceedButton.className = "button";
    }
}