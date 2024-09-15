import nltk
from nltk.chat.util import Chat, reflections

# Download the necessary NLTK data
nltk.download('punkt')

patterns = [
    # Greetings
    (r'hi|hello|hey', ['Hello! How can I assist you today?']),
    (r'what is your name?', ['I am a support chatbot. How can I help you?']),
    (r'how are you today?|how are you|how are you doing', ['I am good. How can I assist you today?']),

    # Contact and Support
    (r'how can I contact support?', ['You can reach support at support@example.com.']),
    (r'where can I find customer service?', ['Our customer service can be reached at support@example.com or through our contact page.']),
    (r'what are your hours of operation?', ['Our support team is available from 9 AM to 5 PM, Monday to Friday.']),

    # Products and Services
    (r'(.*) (product|service) (.*)', ['Can you please provide more details about the product or service?']),
    (r'what products do you offer?', ['We offer a variety of products including electronics, clothing, and home goods.']),
    (r'what services are available?', ['We offer services such as product support, returns, and exchanges.']),

    # Issues and Complaints
    (r'(.*) (issue|problem) (.*)', ['I am sorry to hear about the issue. Can you provide more details?']),
    (r'how can I report a problem?', ['You can report a problem by contacting our support team at support@example.com.']),
    (r'why is my order delayed?', ['I apologize for the delay. Please contact support@example.com with your order details, and we will assist you.']),

    # Account and Orders
    (r'how can I track my order?', ['You can track your order using the tracking number provided in your confirmation email.']),
    (r'how do I update my account information?', ['You can update your account information by logging into your account and accessing the settings.']),
    (r'how can I reset my password?', ['To reset your password, go to the login page and click on "Forgot Password". Follow the instructions to reset it.']),

    # Miscellaneous
    (r'what is the return policy?', ['Our return policy allows returns within 30 days of purchase. Please visit our website for more details.']),
    (r'where are you located?', ['Our headquarters are located at 123 Main Street, Hometown, USA.']),
    (r'what payment methods do you accept?', ['We accept various payment methods including credit cards, PayPal, and bank transfers.']),
    
    # General fallback response
    (r'(.*)', ['I am not sure how to respond to that. Can you please elaborate?'])
]


chatbot = Chat(patterns, reflections)

def get_response(user_input):
    return chatbot.respond(user_input)

if __name__ == "__main__":
    # Run the chatbot in a loop
    print("Hello! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        response = get_response(user_input)
        print("Chatbot:", response)
