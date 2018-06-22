from chatterbot import ChatBot

bro = ChatBot(
    'bro',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the odia corpus
bro.train("chatterbot.corpus.odia")

# Get a response to an input statement
bro.get_response("Hello, how are you today?")