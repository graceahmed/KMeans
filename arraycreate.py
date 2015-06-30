line_school = open("myfile.csv", "rb")
for line in line_school:
    array = [i.strip() for i in line.split(',')]
    print array
