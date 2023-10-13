// Get elements
const chatContainer = document.getElementById('chat-container');
const userMessageInput = document.getElementById('user-message');
const sendButton = document.getElementById('send-button');

// Function to display a user message in the chat
function displayUserMessage(message) {
    const userMessage = document.createElement('div');
    userMessage.classList.add('user-message');
    userMessage.innerText = message;
    chatContainer.appendChild(userMessage);
}

// Function to display a chatbot response
function displayChatbotResponse(response) {
    const chatbotMessage = document.createElement('div');
    chatbotMessage.classList.add('chatbot-message');
    chatbotMessage.innerText = response;
    chatContainer.appendChild(chatbotMessage);
}

// Event listener for sending a user message
sendButton.addEventListener('click', () => {
    const userText = userMessageInput.value;
    displayUserMessage(userText);

    // Add code to send the user message to the chatbot and get a response
    const chatbotResponse = 'This is a sample chatbot response.';
    displayChatbotResponse(chatbotResponse);

    userMessageInput.value = '';
});
