import random

input_file = "/Users/franziskahafner/Desktop/paper/testing_AI/input/persons-with-significant-controll-2020-05-30.csv"
output_file = "/Users/franziskahafner/Desktop/paper/testing_AI/input/names_to_ethnicity_equal_gender_age_nat_21else.csv"

contained_ethnicities = ["british", "indian", "hungarian", "spanish", "german", "zimbabwean", "polish", "bulgarian", "turkish", "pakistani", "italian", "romanian",
 "french", "chinese", "swedish", "nigerian", "greek", "japanese", "dutch", "ukrainian", "danish", "russian"]

#contained_ethnicities = ["british", "indian", "spanish", "american", "german", "polish", "pakistani", "italian", "romanian",  "french"
 #, "chinese", "nigerian", "japanese", "russian"]

name_dict = {}

with open(input_file, "r") as f:
    for line in f.readlines():
        line = line.strip().split(",")
        nationality = line[-1]
        name = line[2]
        try:
            age = int(line[-2])
        except:
            age = 0
        gender = line[-3]
        if nationality not in contained_ethnicities:
            nationality = "else"
        if nationality not in name_dict:
            name_dict[nationality] = {"female":{"1900-1909":[],"1910-1919":[],"1920-1929":[],"1930-1939":[],"1940-1949":[],"1950-1959":[],"1960-1969":[],"1970-1979":[],"1980-1989":[],"1990-1999":[]}, 
                                        "male":{"1900-1909":[],"1910-1919":[],"1920-1929":[],"1930-1939":[],"1940-1949":[],"1950-1959":[],"1960-1969":[],"1970-1979":[],"1980-1989":[],"1990-1999":[]}}
        if gender in name_dict[nationality]:
            if age >=1900 and age <= 1909:
                name_dict[nationality][gender]["1900-1909"]+=[name]
            if age >=1910 and age <= 1919:
                name_dict[nationality][gender]["1910-1919"]+=[name]
            if age >=1920 and age <= 1929:
                name_dict[nationality][gender]["1920-1929"]+=[name]
            if age >=1930 and age <= 1939:
                name_dict[nationality][gender]["1930-1939"]+=[name]
            if age >=1940 and age <= 1949:
                name_dict[nationality][gender]["1940-1949"]+=[name]
            if age >=1950 and age <= 1959:
                name_dict[nationality][gender]["1950-1959"]+=[name]
            if age >=1960 and age <= 1969:
                name_dict[nationality][gender]["1960-1969"]+=[name]
            if age >=1970 and age <= 1979:
                name_dict[nationality][gender]["1970-1979"]+=[name]
            if age >=1980 and age <= 1989:
                name_dict[nationality][gender]["1980-1989"]+=[name]
            if age >=1990 and age <= 1999:
                name_dict[nationality][gender]["1990-1999"]+=[name]

def choose_random_names(data, length):
    random.shuffle(data)
    return data[:length]

with open(output_file, "w") as f:
    f.write("names, year_of_birth, gender, nationality\n")
    for nationality in name_dict:
        for gender in name_dict[nationality]:
            for age in ["1950-1959","1960-1969","1970-1979","1980-1989","1990-1999"]:
                name_list = name_dict[nationality][gender][age]
                name_list = choose_random_names(name_list, 30)
                print(len(name_list))
                for name in name_list:
                    f.write(name + "," + age + "," + gender + "," + nationality + "\n")
                    #print(nationality+ " " + gender + " "+ age+ " "+ str(len(name_dict[nationality][gender][age])))
                
