input_file = "/Users/franziskahafner/Desktop/paper/testing_AI/input/names_to_ethnicity_equal_gender_age_nat_21else.csv"
output_file_1 = "/Users/franziskahafner/Desktop/paper/testing_AI/input/names_to_ethnicity_equal_gender_age_nat_21else_namsor_1.csv"
output_file_2 = "/Users/franziskahafner/Desktop/paper/testing_AI/input/names_to_ethnicity_equal_gender_age_nat_21else_namsor_2.csv"

with open(input_file, "r") as i:
    with open(output_file_1, "w") as o_1:
        with open(output_file_2, "w") as o_2:
            o_1.write("firstName,lastName\n")
            o_2.write("firstName,lastName\n")
            first_line = True
            line_nr = 0
            for line in i.readlines():
                if line_nr <5000:
                    if first_line == False:
                        line_nr += 1
                        line = line.strip().split(",")
                        names = line[0]
                        last_name = names.split(" ")[-1]
                        first_name = " ".join(names.split(" ")[:-1])
                        o_1.write(first_name+","+last_name+"\n")
                    else:
                        first_line = False
                else:
                    line_nr += 1
                    line = line.strip().split(",")
                    names = line[0]
                    last_name = names.split(" ")[-1]
                    first_name = " ".join(names.split(" ")[:-1])
                    o_2.write(first_name+","+last_name+"\n")
        print(line_nr)
            