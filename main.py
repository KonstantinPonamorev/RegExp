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
    pattern = r"(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)" \
              r"(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)" \
              r"(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)"
    new_pattern = r"+7(\4)\8-\11-\14\15\17\18\19\20"
    for people in contacts_list:
        people[5] = re.sub(pattern, new_pattern, people[5])
    return contacts_list

def delete_doubles():
    new_dic = {}
    for contact in contacts_list:
        if f'{contact[0]} {contact[1]}' not in new_dic:
            new_dic[f'{contact[0]} {contact[1]}'] = contact
        else:
            for i in range(0, len(contact)-1): # for i in range(0, len(contact)):
                if new_dic[f'{contact[0]} {contact[1]}'][i] == '':
                    new_dic[f'{contact[0]} {contact[1]}'][i] = contact[i]
    phonebook = list(new_dic.values())
    return phonebook


def write_file():
    with open("phonebook.csv", "w", encoding='UTF-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(phonebook)


if __name__ == '__main__':
    contacts_list = read_file()
    structure_names()
    subs_phones()
    phonebook = delete_doubles()
    write_file()









