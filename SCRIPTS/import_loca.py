import csv
import string
import Bladex
import sys
import os
import Reference
import PanelFillerCommon
import re

# The CSV must have the first line containing the language names
# Set the desired language here:
languages = ["Spanish", "English", "French", "Italian", "German", "Russian", "Chinese", "Japanese", "Korean", "Polish", "Portugese"]

LanguageToImport = "undefined"

def get_language_column_index(content, language):
	index = 0
	for part in content[0]:
		if part[0:len(language)] == language:
			return index
		index = index + 1
	print "Error: Language not found in content."


def get_entry_from_key(content, key):
	for entry in content:
		if entry[0] == key:
			return entry

	return None

def generate_achievement():
	content = csv.parse("../../Localization/achievements.csv")

	output_file = open("../../Data/Achievements/" + LanguageToImport + ".json", "w")

	output_file.write("{\n")
	output_file.write("  \"Achievements\": {\n")
	output_file.write("    \"path\": \"../../DATA/achievements/\",\n")
	output_file.write("    \"list\": [\n")

	language_column_index = get_language_column_index(content, LanguageToImport)

	for entry in content:
		if entry[0] != "" and entry[0] != None and entry[0][0:5] == "title":
			titleKey = entry[0]
			entryId = titleKey[5:]
			infoEntry =  get_entry_from_key(content, "info" + entryId)
			if infoEntry != None:
				titleValue = entry[language_column_index]
				infoValue =  infoEntry[language_column_index]
				if titleValue != None and titleValue != "" and infoValue != None and infoValue != "":
					output_file.write("      {\n")
					output_file.write("        \"name\": \"" + titleValue + "\",\n")
					output_file.write("        \"info\": \"" + infoValue + "\",\n")
					output_file.write("        \"texture\": [\n")
					output_file.write("          \"" + entryId + ".png\"\n")
					output_file.write("        ]\n")
					output_file.write("      },\n")

	output_file.seek(output_file.tell() - 2)
	output_file.write("\n    ],\n")
	output_file.write("    \"\": \"\"\n")
	output_file.write("  }\n")
	output_file.write("}\n")
	output_file.close()

def generate_menu():
	content = csv.parse("../../Localization/menu.csv")
	output_file=open("../../Data/Menu/" + LanguageToImport + ".py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)
	output_file.write("global ForeingDict\n")
	output_file.write("ForeingDict = {\n")

	for entry in content:
		value = entry[language_column_index]
		if value != None and value != "":
			output_file.write("    \"" + entry[0] + "\" : \"" + entry[language_column_index] + "\",\n")

	output_file.write("}")
	output_file.close()

def generate_tutor():
	content = csv.parse("../../Localization/tutor.csv")
	Textos = {}
	execfile("../../Data/Text/EnglishUS/tutor.py")
	original_content = Textos
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/tutor.py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)

	# for key in original_content.keys():
		# entry = get_entry_from_key(content, key)
	for entry in content:
		key = entry[0]
		if entry == None:
			print "Warning: Missing key " + key
		else:
			if key != "":
				translation = entry[language_column_index]
				lines = string.split(translation, "\n")
				output_file.write("Textos['" + key + "'] = (\n")

				for line in lines:
					output_file.write("\t\"" + line + "\",\n")

				output_file.write(")\n")

	output_file.close()

def generate_objIds():
	content = csv.parse("../../Localization/objIds.csv")
	Reference.DefaultSelectionData = {}
	execfile("../../Data/ObjIds/EnglishUS.py")
	original_content = Reference.DefaultSelectionData
	output_file=open("../../Data/ObjIds/" + LanguageToImport + ".py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)

	for key in original_content.keys():
		entry = get_entry_from_key(content, key)
		if entry == None:
			print "Warning: Missing key " + key
		else:
			translation = entry[language_column_index]
			lines = string.split(translation, "\n")
			output_file.write("Reference.DefaultSelectionData['" + key + "'] = (" + str(original_content[key][0]) + "," + str(original_content[key][1]) + ",\"" + translation + "\")\n")

	output_file.close()

def generate_m(index):
	index = str(index)
	content = csv.parse("../../Localization/M" + index + ".csv")
	Textos = {}
	execfile("../../Data/Text/EnglishUS/M" + index + ".py")
	original_content = Textos
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/M" + index + ".py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)

	for key in original_content.keys():
		value = original_content[key]
		entry = get_entry_from_key(content, key)
		if entry == None:
			print "Warning: Missing key " + key
		else:
			translation = entry[language_column_index]
			output_file.write("Textos['" + key + "'] = (" + str(value[0]) + ",\n")
			output_file.write("\t" + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + ",\n")
			converted_value = string.replace(entry[language_column_index], "\n", "\\n")
			output_file.write("\t\"\"\"" + converted_value + "\"\"\"\n")
			output_file.write(")\n\n")

	output_file.close()


def generate_all_m():
	for i in range(1, 18):
		generate_m(i)


def generate_map2d():
	content = csv.parse("../../Localization/map2D.csv")
	MapList = {}
	execfile("../../Data/Text/EnglishUS/map2D.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/map2D.py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)

	for entry in content:
		key = entry[0]
		if key != "":
			translation = entry[language_column_index]
			output_file.write(key + " = \"" + translation + "\"\n")

	output_file.write("\n\n")

	output_file.close()

def generate_combos():
	content = csv.parse("../../Localization/combos.csv")
	ComboNames = {
              "Knight_N"   : {},
              "Barbarian_N": {},
              "Amazon_N"   : {},
              "Dwarf_N"    : {},
              "Default"    : {},
            }
	execfile("../../Data/Text/EnglishUS/Combos.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/Combos.py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)
	original_content = ComboNames

	for key in original_content.keys():
		for key2 in original_content[key].keys():
			entry = get_entry_from_key(content, key + " " + key2)
			if entry == None:
				print "Warning: Missing key " + key
			else:
				translation = entry[language_column_index]
				output_file.write("ComboNames['" + key + "']['" + key2 + "']" + " = \"" + translation + "\"\n")

	output_file.close()

def generate_combosPanel():
	content = csv.parse("../../Localization/combosPanel.csv")
	language_column_index = get_language_column_index(content, LanguageToImport)
	lang = LanguageToImport

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelCombosLoca.py", "w")

	output_file.write("import PanelFillerCommon\n\n")

	for entry in content:
		key = entry[0]
		keys = string.split(key, " ")
		if len(keys) > 1:
			character = keys[0]
			attribute = keys[1]

			if attribute == "Title":
				abbreviation = None
				short_character = string.split(character, '_')[0]
				if short_character == "Amazon":
					abbreviation = "Amz"
				if short_character == "Barbarian":
					abbreviation = "Barb"
				if short_character == "Dwarf":
					abbreviation = "Dwf"
				if short_character == "Knight":
					abbreviation = "Kgt"
				
				output_file.write("combos[\"" + lang + "\"][\"" + character + "\"][\"" + attribute + "\"] = PanelFillerCommon.Get" + abbreviation + "Title()\n")
			else:
				output_file.write("combos[\"" + lang + "\"][\"" + character + "\"][\"" + attribute + "\"] = [")
				values = string.split(entry[language_column_index], "\n")

				first = 1
				for value in values:
					if value != "":
						if first == 0:
							output_file.write(", ")

						output_file.write("\"" + value + "\"")
						first = 0

				output_file.write("]\n")

	output_file.close()

def generate_buttons():
	content = csv.parse("../../Localization/buttons.csv")
	language_column_index = get_language_column_index(content, LanguageToImport)
	lang = LanguageToImport

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelButtonsLoca.py", "w")

	entry = get_entry_from_key(content, "Button")
	output_file.write("buttons[\"" + lang + "\"] = [")

	values = string.split(entry[language_column_index], "\n")

	first = 1
	for value in values:
		if value != "":
			if first == 0:
				output_file.write(", ")

			output_file.write("\"" + value + "\"")
			first = 0

	output_file.write("]\n")

	output_file.close()

def generate_abilities():
	content = csv.parse("../../Localization/abilities.csv")
	language_column_index = get_language_column_index(content, LanguageToImport)
	lang = LanguageToImport

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelAbilitiesLoca.py", "w")

	for entry in content:
		key = entry[0]
		keys = string.split(key, " ")
		if len(keys) > 1:
			character = keys[0]
			attribute = keys[1]

			output_file.write("abilities[\"" + lang + "\"][\"" + character + "\"][\"" + attribute + "\"] = [")

			if string.find(entry[language_column_index], ',') != -1:
				values = string.split(entry[language_column_index], ",")
			else:
				values = string.split(entry[language_column_index], "\n")

			first = 1
			for value in values:
				if value != "":
					if first == 0:
						output_file.write(", ")
					converted_value = string.replace(value, "\n", "\\n")
					output_file.write("\"" + converted_value + "\"")
					first = 0

			output_file.write("]\n")

	output_file.close()

def generate_items():
	content = csv.parse("../../Localization/items.csv")
	language_column_index = get_language_column_index(content, LanguageToImport)
	lang = LanguageToImport

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelItemsLoca.py", "w")

	output_file.write("import PanelFillerCommon\n\n")
	for entry in content:
		if entry[0] != "Key":
			key = entry[0]
			output_file.write("items[\"" + lang + "\"][\"" + key + "\"] = [")
			value = entry[language_column_index]
			output_file.write("\"" + value + "\"]\n")

	output_file.close()

def generate_specials():
	content = csv.parse("../../Localization/specials.csv")
	language_column_index = get_language_column_index(content, LanguageToImport)
	lang = LanguageToImport

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelSpecialsLoca.py", "w")

	output_file.write("import PanelFillerCommon\n\n")

	for entry in content:
		key = entry[0]
		keys = string.split(key, " ")
		if len(keys) > 1:
			character = keys[0]
			attribute = keys[1]

			if attribute == "Title":
				abbreviation = None
				short_character = string.split(character, '_')[0]
				if short_character == "Amazon":
					abbreviation = "Amz"
				if short_character == "Barbarian":
					abbreviation = "Barb"
				if short_character == "Dwarf":
					abbreviation = "Dwf"
				if short_character == "Knight":
					abbreviation = "Kgt"
				
				output_file.write("specials[\"" + lang + "\"][\"" + character + "\"][\"" + attribute + "\"] = PanelFillerCommon.GetSpecial" + abbreviation + "Title()\n")
			else:
				output_file.write("specials[\"" + lang + "\"][\"" + character + "\"][\"" + attribute + "\"] = [")
				values = string.split(entry[language_column_index], "\n")

				first = 1
				for value in values:
					if value != "":
						if first == 0:
							output_file.write(", ")

						output_file.write("\"" + value + "\"")
						first = 0

				output_file.write("]\n")

	output_file.close()

def generate_casa():
	content = csv.parse("../../Localization/casa.csv")
	execfile("../../Data/Text/EnglishUS/casa.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/casa.py", "w")
	language_column_index = get_language_column_index(content, LanguageToImport)

	chars = ["Bar", "Kgt", "Amz", "Dwf" ]

	for char in chars:
		for i in range(1, 5):
			key = "TextInfoChar" + char + str(i)
			entry = get_entry_from_key(content, key)
			translation = entry[language_column_index]
			output_file.write(key + " = \"\"\"" + translation + "\"\"\"\n")

	output_file.close()

def generate_maptext():
	content = csv.parse("../../Localization/mapTexts.csv")
	maps = PanelFillerCommon.GetEmptyData()
	maps2 = {
			 "English": {},
			 "French": {},
			 "Italian": {},
			 "German": {},
			 "Spanish": {},
			 "Russian": {},
			 "Chinese": {},
			 "Japanese": {},
			 "Korean": {},
			 "Portugese": {},
			 "Polish": {}
			}
	execfile("../../SCRIPTS/Combos/English/PanelMapTextLoca.py")
	try:
		os.mkdir("../../SCRIPTS/Combos/" + LanguageToImport)
	except:
		pass

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelMapTextLoca.py", "w")

	language_column_index = get_language_column_index(content, LanguageToImport)
	original_content = maps

	for x in range(1, len(content)):
		key = content[x][0]
		if key != "":
			keys = string.split(key)
			entry = get_entry_from_key(content, content[x][0])

			if entry == None:
				print "Warning: Missing key"
				print keys
			else:
				translation = entry[language_column_index]
				translations = string.split(translation, "\n", 1)
				if len(keys) == 2:
					output = "maps['" + LanguageToImport + "']['" + keys[0] + "']['" + keys[1]
				elif len(keys) == 1:
					output = "maps2['" + LanguageToImport + "']['" + keys[0]
				output = output + "']" + " = [\"" + translations[0] + "\",\n"
				lines = string.split(translations[1], '\n')
				i = 0
				for line in lines:
					output = output + '"' + line
					if i != len(lines) - 1:
						output = output + "\\n\"\n"
					else:
						output = output + "\""
					i = i + 1
				output = output + "]\n\n"
				output_file.write(output)

	output_file.close()

def generate_secrets():
	content = csv.parse("../../Localization/secrets.csv")
	secrets = {
			 "English": {},
			 "French": {},
			 "Italian": {},
			 "German": {},
			 "Spanish": {},
			 "Russian": {},
			 "Chinese": {},
			 "Japanese": {},
			 "Korean": {},
			 "Portugese": {},
			 "Polish": {}
			}
	execfile("../../SCRIPTS/Combos/English/PanelSecretsLoca.py")
	try:
		os.mkdir("../../SCRIPTS/Combos/" + LanguageToImport)
	except:
		pass

	output_file=open("../../SCRIPTS/Combos/" + LanguageToImport + "/PanelSecretsLoca.py", "w")

	language_column_index = get_language_column_index(content, LanguageToImport)
	original_content = secrets

	for x in range(1, len(content)):
		key = content[x][0]
		if key != "":
			entry = get_entry_from_key(content, key)
			if entry == None:
				print "Warning: Missing key " + key
			else:
				translation = entry[language_column_index]
				output = "secrets['" + LanguageToImport + "']['" + key + "'] = [\n"
				lines = string.split(translation, '\n')
				i = 0
				for line in lines:
					output = output + '"' + line
					if i != len(lines) - 1:
						output = output + "\\n\"\n"
					else:
						output = output + "\""
					i = i + 1
				output = output + "]\n\n"
				output_file.write(output)

	output_file.close()
			
for language in languages:
	global LanguageToImport
	LanguageToImport = language
	print "Importing " + language
	generate_achievement()
	generate_items()
	generate_objIds()
	generate_menu()
	generate_tutor()
	generate_all_m()
	generate_map2d()
	generate_casa()
	generate_combos()
	generate_combosPanel()
	generate_buttons()
	generate_abilities()
	generate_specials()
	generate_maptext()
	generate_secrets()

print "End of localization import"
sys.exit(0)
