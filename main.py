from functions import get_csv, update_csv, new_csv

if __name__ == '__main__':
    phonebook_raw = 'phonebook_raw.csv'
    contacts_list = get_csv(phonebook_raw)

    updated_contacts_list = update_csv(contacts_list)

    new_csv_name = 'new_phonebook_raw.csv'
    new_csv(new_csv_name, updated_contacts_list)