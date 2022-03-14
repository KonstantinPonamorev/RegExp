import re
from pprint import pprint
import csv

def read_file():
    with open('phonebook_raw.csv', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list (rows)
    return contacts_list

def structure_names():
    for contact in contacts_list:
        list_name = contact[0].split(' ')
        list_surname = contact[1].split(' ')
        if len(list_name) == 3:
            for i in range(0, 3):
                contact[i] = list_name[i]
        elif len(list_name) == 2:
            for i in range(0, 2):
                contact[i] = list_name[i]
        else:
            if len(list_surname) == 2:
                for i in range(1, 3):
                    contact[i] = list_surname[i-1]
            else:
                ...
    return contacts_list

def subs_phones():
    pattern = r"(8|\+7)?\D*(495)\S*(-|\s)*(\d{3})(-|\s)*(\d{2})(-|\s)*(\d{2})"
    for people in contacts_list:
        people[5] = re.sub(pattern, r"+7(\2)\4-\6-\8", people[5])
    return contacts_list

def delete_doubles():
    new_list = []
    for contact in contacts_list:
        for people in new_list:
            if contact[0] == people[0] and contact[1] == people[1]:
                pass
            else:
                new_list.append(contact)
    return new_list

def write_file():
    with open("phonebook.csv", "w", encoding='UTF-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows()


if __name__ == '__main__':
    contacts_list = read_file()
    structure_names()
    subs_phones()
    new_list = delete_doubles()
    write_file()






