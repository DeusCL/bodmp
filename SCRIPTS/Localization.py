import Bladex

tokens = Bladex.GetTokens()
tokens.reverse()

def GetTranslation(data, key):

	for token in tokens:
		new_key = key + token
		if new_key in data.keys():
			return data[new_key]

	return data[key]
