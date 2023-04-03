from pprint import pprint
import csv
import re

def get_csv(phonebook_raw):
    with open(phonebook_raw, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

def update_csv(contacts_list):
    pattern = r'(8|\+7)?[-\s]*?\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})[\s\(?]*(доб\.)?\.?\s*(\d+)?\)?'
    subst = r'+7(\2)\3-\4-\5 \6\7'
    
    filtered_dict = {}
    duplicates_dict = {}

    for i in contacts_list:
        name = ' '.join(i[0:3]).split(' ')
        del name[3:]
        i[0:3] = name[0:3]
        i[5] = re.sub(pattern, subst, i[5])
        a = i[0] + ' ' + i[1]
        b = i[2:]
        personal_data_dict = {a: b}
        print(personal_data_dict)
        for k, v in personal_data_dict.items():
            if k not in filtered_dict.keys():
                filtered_dict.update(personal_data_dict)
        else:
            duplicates_dict.update(personal_data_dict)

    for k, v in duplicates_dict.items():
        for k1, v1 in filtered_dict.items():
            if k == k1:
                merged_data = [x or y for x, y in zip(v1, v)]
                filtered_dict[k1] = merged_data
                
    new_contacts_list = []
    for k, v in filtered_dict.items():
        a = k.split() + v
        b = [','.join(a)]
        new_contacts_list.append(b)

    return new_contacts_list

def new_csv(new_phonebook, new_contacts_list):
    with open(new_phonebook, "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f)
        datawriter.writerows(new_contacts_list)