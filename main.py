from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

result_list = []
check_copy = []
i = 0
while i != len(contacts_list):
    my_list = contacts_list[i]
    while '' in my_list:
        my_list.remove("")
    converted_list = ' '.join(my_list)
    converted_str = list(converted_list.split(' '))
    if converted_str[0] in check_copy:
        i += 1
    else:
        check_copy.append(converted_str[0])
        result = f"""{converted_str[0]},{converted_str[1]},{converted_str[2]},{converted_str[3]}"""
        result_list.append(list(result.split(",")))
        i += 1

check_copy2 = []
position = []

i = 0
while i != len(contacts_list):
    my_list = contacts_list[i]
    while '' in my_list:
        my_list.remove("")
    converted_list = ' '.join(my_list)
    converted_str = list(converted_list.split(' '))

    j = 0

    while not ".ru" in converted_str[j] and not "8" in converted_str[j] and (
    not "+7" in converted_str[j]) and not "org" in converted_str[j]:
        # print(converted_str[j])
        position.append(converted_str[j])
        if converted_str[j] == converted_str[-1]:
            break
        j += 1
        # print(position)

    l = 0

    while l < len(result_list):
        if position[0] == result_list[l][0]:
            if len(position) > 4:
                if not position[0] in check_copy2:
                    check_copy2.append(position[0])
                    unite_position = []
                    k = 4
                    while k < len(position):
                        unite_position.append(position[k])
                        if position[k] == position[-1]:
                            break
                        k += 1

                    unite_position2 = " ".join(unite_position)
                    add_position = []
                    add_position.append(position[0])
                    add_position.append(unite_position2)
                    f = 0
                    while f < len(result_list):
                        if add_position[0] == result_list[f][0]:
                            result_list[f].append(add_position[1])

                        f += 1

        l += 1

    position = []
    i += 1

result_position = " ".join(position)
print(result_position)

# print(contacts_list)
m = 0
while m < len(contacts_list):
    n = 0
    while n < len(contacts_list[m]):
        if '+7' in contacts_list[m][n] or '8' in contacts_list[m][n] and not '.ru' in contacts_list[m][n]:
            text_sub = contacts_list[m][n]
            if 'доб' in contacts_list[m][n]:
                pattern = r"(\+7|8)(\s+)?\(?(\d{3,3})(\))?(\s+|\-)?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})\s+(\()?(\доб.)\s+(\d+)(\))?"
                substitution = r"+7(\3)\6-\7-\8 \10\11"
                result_sub = re.sub(pattern, substitution, text_sub)
                z = 0
                while z < len(result_list):
                    if result_list[z][0] in contacts_list[m][0]:
                        result_list[z].append(result_sub)
                    z += 1

            else:
                pattern = r"(\+7|8)(\s+)?\(?(\d{3,3})(\))?(\s+|\-)?(\d{3,3})\-?(\d{2,2})\-?(\d{2,2})"
                substitution = r"+7(\3)\6-\7-\8"
                result_sub = re.sub(pattern, substitution, text_sub)
                z = 0
                while z < len(result_list):
                    if result_list[z][0] in contacts_list[m][0]:
                        result_list[z].append(result_sub)
                    z += 1

        n += 1
    m += 1

i = 0
while i != len(contacts_list):
    if '.ru' in contacts_list[i][-1] or 'email' in contacts_list[i][-1]:
        z = 0
        while z < len(result_list):
            if result_list[z][0] in contacts_list[i][0]:
                result_list[z].append(contacts_list[i][-1])
            z += 1
        i += 1
    else:
        i += 1

result_list.pop(0)
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(result_list)
