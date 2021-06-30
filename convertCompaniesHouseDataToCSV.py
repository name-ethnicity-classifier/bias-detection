import ast

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

with open ("/Users/franziskahafner/Desktop/paper/testing_AI/input/persons-with-significant-control-snapshot-2020-05-30.txt", "r") as f:
    with open("/Users/franziskahafner/Desktop/paper/testing_AI/input/persons-with-significant-controll-2020-05-30.csv", "w") as c:
        c.write("company_number,postal_code,names,gender,year_of_birth,nationality\n")
        for line in f.readlines():
            data_string = ""
            line = line.strip()
            line = ast.literal_eval(line)
            #get company_number:
            try:
                company_number = line["company_number"]
                company_number = company_number.replace(",","")
                data_string += company_number + ","
            except:
                data_string += ","
            #get postal_code:
            try:
                postal_code = line["data"]["address"]["postal_code"]
                postal_code = postal_code.replace(",","")
                data_string += postal_code + ","
            except:
                data_string += ","
            #get names:
            try:
                name = line["data"]["name"].lower()
                name = name.replace(".","")
                name = name.replace(",","")
            except:
                name = ""
            #get gender:
            try:
                gender = ""
                if name[:3] == "mr " or name[:3] == "mr." or name[:5] == "lord " or name[:4] == "sir " :
                    name = name.split(" ")[1:]
                    name = " ".join(name)
                    gender = "male"
                elif name [:3]== "mrs" or  name [:3]== "ms " or name [:5]== "miss " or name [:4]== "mrs. " or name [:4]== "lady" or name [:3]== "ms.":
                    gender = "female"
                    name = name.split(" ")[1:]
                    name = " ".join(name)
            except:
                gender = ""
            data_string += name + "," + gender + ","
            #get year_of_birth:
            try:
                year_of_birth = line["data"]["date_of_birth"]["year"]
                data_string += str(year_of_birth) + ","
            except Exception as e:
                data_string += ","
            #get nationality:
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
                data_string += nationality + "\n"
            except:
                data_string += "\n"
            #print(data_string)
            c.write(data_string)
            