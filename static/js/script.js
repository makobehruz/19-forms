document.addEventListener('DOMContentLoaded', function() {
    const addQuestionBtn = document.getElementById('add-question');
    const questionsContainer = document.getElementById('questions-container');
    const questionTemplate = document.getElementById('question-template').content;

    let questionCount = 0;

    function addQuestion() {
        questionCount++;
        const newQuestion = document.importNode(questionTemplate, true);
        newQuestion.querySelector('.question-number').textContent = questionCount;

        const removeBtn = newQuestion.querySelector('.remove-question');
        removeBtn.addEventListener('click', function() {
            this.closest('.question-formset').remove();
            updateQuestionNumbers();
        });

        questionsContainer.appendChild(newQuestion);
        updateQuestionNumbers();
    }

    function updateQuestionNumbers() {
        const questions = questionsContainer.querySelectorAll('.question-formset');
        questions.forEach((question, index) => {
            question.querySelector('.question-number').textContent = index + 1;
        });
    }

    addQuestionBtn.addEventListener('click', addQuestion);

    // Add the first question by default
    addQuestion();
});