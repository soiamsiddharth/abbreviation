
import json

from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):

	word = word.lower()
	if word in data:
	   	return data[word]


	elif word.title() in data:
	     return data[word.title()]

	elif word.upper() in data:
   		   return data[word.upper()]

	elif len(get_close_matches(word, data.keys())) > 0:
		yn = input ("Do you mean %s? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])
		yn = yn.upper()

		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]

		elif yn == "X":
			return "The word does not exist. Please double check it."

		else:
			return "word not available in library"

	else:
		return "The word does not exist. Please double check it."

user_word = input("Please enter : ")

output = translate(user_word)


if type(output) == list:


	for	item in output:
		print(item)

else:
	print(output)
