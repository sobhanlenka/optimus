# -*- coding: utf-8 -*-
from optimus import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.filters import filters
import logging

bro = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    #response_selection_method=get_random_response,
    tie_breaking_method='random_response',
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
    database="./db.sqlite3",
    #trainer='chatterbot.trainers.ChatterBotCorpusTrainer' # Uncomment this line to train
   #trainer="chatterbot.trainers.ListTrainer"
    
)
#bro.train("chatterbot.corpus.telugu") # Uncomment this line to train 



print("Type something to begin...")

while True:
    try:
     print('\nAlien:')
     bot_input = bro.get_response(None)
    except (KeyboardInterrupt, EOFError, SystemExit):
     break
