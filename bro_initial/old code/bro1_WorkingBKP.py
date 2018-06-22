# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.filters import filters
import logging

bro = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    logic_adapters=[
        "chatterbot.logic.MathematicalEvaluation",
	"chatterbot.logic.BestMatch",
	"chatterbot.logic.LowConfidenceAdapter",
	#"chatterbot.logic.MultiLogicAdapter",
	#"chatterbot.logic.TimeLogicAdapter",
	#"chatterbot.filters.RepetitiveResponseFilter"
	
    ],
    input_adapter="chatterbot.input.TerminalAdapter",
    output_adapter="chatterbot.output.TerminalAdapter",
    output_format="text",
    database="../database.db",
    #trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
   # trainer="chatterbot.trainers.ListTrainer"
)
#bro.train("chatterbot.corpus.french")

bro.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'Non of your business'
])



print("Type something to begin...")

while True:
    try:
     print('\nAlien:')
     bot_input = bro.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
     break
