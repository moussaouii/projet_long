from rasa_nlu.model import Interpreter
#import json

def parse_sentence(message):
	interpreter = Interpreter.load("./models/current/nlu")
#message = "voyons quelques restaurants italiens"
	return interpreter.parse(message)
#print(json.dumps(result, indent=2))
