# this is for creating a file of names on which to test gender sensitifity and specitifity of a name-ethnicity classification AI. 
# this file will contain names balanced on gender and ethnicity.

import ast
import random
import pickle

nr_of_names_per_nat = 1000
separated_by_gender = True
#contained_ethnicities = ["else", "british", "indian", "hungarian", "spanish", "german", "zimbabwean", "polish", "bulgarian", "turkish", "pakistani", "italian", "romanian",
# "french", "chinese", "swedish", "nigerian", "greek", "japanese", "dutch", "ukrainian", "danish", "russian"]

contained_ethnicities = ["british", "else", "indian", "spanish", "american", "german", "polish", "pakistani", "italian", "romanian",  "french"
 , "chinese", "nigerian", "japanese", "russian"]

gender_name_to_ethnicity_file = "/Users/franziskahafner/Desktop/paper/testing_AI/input/names_to_ethnicity_known_gender_and_age_14else.csv"

def handle_nationality (nationality):
    nationality = nationality.strip()
    british_list = ["british","england","united kingdom","uk","u k","welsh","wales","n. irish","english","scottish", "scotland","gb", "northern ireland", '"british', "scots", "aberdeen", "n.irish", "btitish", 'uk citizen', 'bristish', 'britsh', 'n irish', 'bristish', 'britsh', 'white british', 'northern irish', 'brittish', 'british citizen', 'brittish', 'u.k.', 'btittish','great britain']
    if nationality in british_list:
        nationality = "british"
    if nationality == "ireland" or nationality == "irish resident":
        nationality = "irish"
    american_list = ["united states", "american", "u.s.","usa", "us citizen", "british:american", "united states of america", "u.s.a.", "citizen of usa", "united states citizen", 'american (usa)', 'united states citize', 'america', 'usa citizen', "u s a", "us", "us american", "u.s. citizen", 'amercian']
    if nationality in american_list:
        nationality = "american"
    if nationality == "portugal":
        nationality = "portugese"
    if nationality == "bangladesh":
        nationality = "bangladeshi"
    if nationality == "japan":
        nationality = "japanese"
    if nationality == "new zealand":
        nationality = "new zealander"
    if nationality in ["west german", "germany", "deutsch"]:
        nationality = "german"
    if nationality == "singapore citizen":
        nationality = "singaporian"
    if nationality == "republic of china" or nationality == "china":
        nationality = "chinese"
    if nationality == "united arab emirates" or nationality == "uae":
        nationality = "emirati"
    if nationality == "swede":
        nationality = "swedish"
    if nationality == "italy":
        nationality = "italian"
    if nationality in ['afghanistan','afghanistani','afghani']:
        nationality = "afghan"
    if nationality == 'india':
        nationality = "indian"
    if nationality == 'portuguese':
        nationality ='portugese'
    if nationality == 'philippine':
        nationality ='philipino'
    if nationality == 'ghanaian':
        nationality = 'ghanian'
    if nationality == "israel":
        nationality = "israeli"
    if nationality == "pakistan":
        nationality = "pakistani"
    if nationality == "sweden":
        nationality = "swedish"
    if nationality == "switzerland":
        nationality = "swiss"
    if nationality == "france":
        nationality = "french"
    if nationality == 'slovakian':
        nationality = "slovak"
    if nationality == "netherlands":
        nationality = "dutch"
    if nationality == "russia":
        nationality = "russian"
    if nationality == "bulgaria":
        nationality = "bulgarian"
    if nationality == "canada":
        nationality = "canadian"
    if nationality == "poland":
        nationality = "polish"
    if nationality == "turkey":
        nationality = "turkish"
    if nationality == "nigeria":
        nationality = "nigerian"
    if nationality == "spain":
        nationality = "spanish"
    if nationality == "austria":
        nationality = "austrian"
    if nationality == "belgium":
        nationality = "belgian"
    if nationality == "norway":
        nationality = "norwegan"
    if nationality == "ukraine":
        nationality = "ukrainian"
    if nationality == "uromania":
        nationality = "romanian"
    if nationality == "china":
        nationality = "chinese"
    return nationality

abc_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","-"]

dict_nat_to_names = {}
dict_nat_to_names["else"]=[]
with open ("/Users/franziskahafner/Desktop/paper/testing_AI/input/persons-with-significant-control-snapshot-2020-05-30.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        line = ast.literal_eval(line)
        try:
            name = line["data"]["name"].lower()
            contains_foreign_letters = False
            name = name.replace(".","")
            name = name.replace(",","")
            for letter in name:
                if letter not in abc_list:
                    contains_foreign_letters = True
            
            try:
                year_of_birth = line["data"]["date_of_birth"]["year"]
                name = name + ", " + str(year_of_birth)
                contains_year_of_birth = True
            except:
                contains_year_of_birth = False
            if contains_foreign_letters == False and contains_year_of_birth == True:
                try:
                    nationality = line["data"]["nationality"].lower().strip()
                    if "/" in nationality:
                        nationality = nationality.split("/")[-1].strip()
                    if "," in nationality:
                        nationality = nationality.split(",")[-1].strip()
                    if "&" in nationality:
                        nationality = nationality.split("&")[-1].strip()
                    if "(" in nationality:
                        nationality = nationality.split("(")[0].strip()
                    if "national" in nationality:
                        nationality = nationality.split(" ")
                        if nationality [0] == "national":
                            nationality = nationality [-1]
                        else:
                            nationality = nationality [0]
                    nationality = handle_nationality(nationality)
                    if nationality in contained_ethnicities:
                        if nationality not in dict_nat_to_names:
                            dict_nat_to_names[nationality]=[name]
                        else:
                            dict_nat_to_names[nationality]+=[name]
                    else:
                        dict_nat_to_names["else"]+=[name]
                except:
                    pass
            else:
                pass
        except:
            pass

nat_to_nr_of_names = {}
dict_seperated_gender = {}
for key in dict_nat_to_names:
    dict_nat_to_names[key] = list(set(dict_nat_to_names[key]))
    nat_to_nr_of_names[key] = len(dict_nat_to_names[key])
    dict_seperated_gender[key] = {"female":[],"male":[]}
    for name in dict_nat_to_names[key]:
        if name[:3] == "mr " or name[:3] == "mr." or name[:5] == "lord " or name[:4] == "sir " :
            name = name.split(" ")[1:]
            name = ' '.join(name)
            dict_seperated_gender[key]["male"]+=[name]
        elif name [:3]== "mrs" or  name [:3]== "ms " or name [:5]== "miss " or name [:4]== "mrs. " or name [:4]== "lady" or name [:3]== "ms.":
            name = name.split(" ")[1:]
            name = ' '.join(name)
            dict_seperated_gender[key]["female"]+=[name]

dict_main_ethnicities = {}
dict_amount_female_male = {}
dict_chosen_names = {}
dict_chosen_names["other"] = []

def choose_random_names(data, length):
    random.shuffle(data)
    return data[:length]

if separated_by_gender == True:
    for key in dict_nat_to_names:
        dict_amount_female_male[key]= {"amount_female":len(dict_seperated_gender[key]["female"]),"amount_male":len(dict_seperated_gender[key]["male"])}
        dict_amount_female_male [key]["amount_total"]= dict_amount_female_male [key]["amount_female"] + dict_amount_female_male [key]["amount_male"]
        smaller_gen = min(dict_amount_female_male[key]["amount_female"], dict_amount_female_male[key]["amount_male"])
        if smaller_gen > nr_of_names_per_nat/2:
            female_list = choose_random_names(dict_seperated_gender[key]["female"], int(nr_of_names_per_nat/2))
            male_list = choose_random_names(dict_seperated_gender[key]["male"], int(nr_of_names_per_nat/2))
            #all_names = choose_random_names(female_list+male_list, nr_of_names_per_nat*2)
            dict_chosen_names[key] = {"female":[],"male":[]}
            dict_chosen_names[key]["female"] = female_list
            dict_chosen_names[key]["male"] = male_list

else:
    for key in dict_nat_to_names:
        if len(dict_nat_to_names[key]) >=nr_of_names_per_nat:
            dict_chosen_names[key]=choose_random_names(dict_nat_to_names[key],len(dict_nat_to_names[key]))

with open(gender_name_to_ethnicity_file, "w") as f:
    f.write("names, year_of_birth, gender, nationality\n")
    for nationality in contained_ethnicities:
        for name in dict_chosen_names[nationality]["female"]:
            f.write(name + ", " + "female, "+ nationality + "\n")
        for name in dict_chosen_names[nationality]["male"]:
            f.write(name + ", " + "male, "+ nationality + "\n")