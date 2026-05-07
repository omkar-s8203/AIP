from nltk.chat.util import Chat, reflections

pairs = [

    [r"hi|hello|hey",
     ["Hello! How can I help you today?"]],

    [r"what is your name ?",
     ["I am a chatbot created using NLTK."]],

    [r"how are you ?",
     ["I'm fine. How can I assist you?"]],

    [r"(.*) product (.*)",
     ["We offer laptops and mobiles."]],

    [r"(.*) location (.*)",
     ["We are located in Pune."]],

    [r"(quit|bye|exit)",
     ["Thank you for chatting!"]]
]

chatbot = Chat(pairs, reflections)

# Sample inputs
questions = [
    "hello",
    "what is your name ?",
    "product",
    "location",
    "bye"
]

for q in questions:
    print("You:", q)
    print("Bot:", chatbot.respond(q))