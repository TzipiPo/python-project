from Family import Family
import numpy as np


# func for run classes
def build_family():
    last_name = input("the last name: ")
    father_name = input("father name: ")
    father_age = input("father age: ")
    mother_name = input("mother name: ")
    mother_age = input("mother age: ")
    children = dict()
    while True:
        try:
            num_of_children = int(input("enter num of children"))
            break
        except:
            print("the number is invalid")
            continue
    for i in range(num_of_children):
        child_name = input("name of child: ")
        child_age = input("age of child: ")
        children[child_name] = child_age
    family = Family(
        {'father': {'name': father_name, 'age': father_age}, 'mother': {'name': mother_name, 'age': mother_age}},
        children, last_name)
    return family


# func for run classes
def print_family_details(family):
    print(f"family: {family.last_name}")
    for k, v in family.parents.items():
        print(k, "--")
        for kk, vv in v.items():
            print(kk, ": ", vv)
    print('children--')
    for k, v in family.get_children().items():
        print(k, ": ", v)


# func for iterators
def sin_x(x):
    if x == 0:
        return 1
    return np.sin(x) / x


# func for iterators
def cos_x(x):
    if x == 0:
        return 1
    return np.cos(x) / x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # classes
    family1 = build_family()
    print_family_details(family1)
    num = int(input("enter num of child: "))
    name, age = family1.get_child(num)
    print(f"child number {num}: {name}, {age}")
    father_name, mother_name = family1.get_parents_names()
    print(f"father: {father_name}, mother: {mother_name}")

    # iterators
    r = np.arange(-100, 100, 0.01)
    sinx = [sin_x(i) for i in r]
    cosx = [cos_x(i) for i in r]

    # files
    names_list = ["Rachel", 'Miri', 'Shimon', "Ohad"]
    file_name = input("enter a file name") + ".txt"
    with open(file_name, "w") as handler:
        for name in names_list:
            handler.write(name + "\n")
    with open(file_name, "rt") as handler:
        lines = handler.readlines()
        for index, line in enumerate(lines):
            if index % 2 == 0:
                print(line, end="")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
