from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot("bro",
storage_adapter="chatterbot.storage.SQLStorageAdapter",
	input_adapter="chatbot.input.TerminalAdapter",
 	output_adapter="chatbot.output.TerminalAdapter"
)

conversation = ([
  #  "Hello",
   # "Hi there!",
    # "How are you doing?",
     # "I'm doing great.",
#    "That is good to hear",
 #   "Thank you.",
  #  "You're welcome."
	"Bhak Be"
])

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)
chatbot.train([
    "Greetings!",
    "Hello",
    "Bhak Bey"
])

response = chatbot.get_response("Bhak Be")
print(response)


while True:
    try:
       
       bot_input = bro.get_response(None)

    except (KeyboardInterrupt, EOFError, SystemExit):
        break
