import csv, re

def delete_table_header(path):
    with open(path, 'r', encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        contacts_list = []
        for contacts in rows:
            if rows.line_num == 1:
                headers = contacts
                continue
            contacts_list.append(contacts)
    return headers, contacts_list


def sort_the_names(contacts):
    sorting_names = []
    for person in contacts:
        if len(person[0].split(' ')) == 1 and len(person[1].split(' ')) == 2:
            firstname, surname = person[1].split(' ')
            person[1] = firstname
            person[2] = surname
        for i in range(0,3):
            if len(person[i].split(' ')) == 2:
                lastname, firstname = person[i].split(' ')
                person[0] = lastname
                person[1] = firstname
            elif len(person[i].split(' ')) == 3:
                lastname, firstname, surname = person[i].split(' ')
                person[0] = lastname
                person[1] = firstname
                person[2] = surname
    [sorting_names.append(i) for i in contacts]
    return sorting_names


def removes_duplicates(contacts):
    count_1 = 0
    count_2 = 1
    personnes = []
    while count_1 < len(contacts):
        personnes.append(contacts[count_1])
        doublon = contacts[count_1]
        name = contacts[count_1][:2]
        new_list = contacts[count_2:]
        for contact in new_list:
            if name == contact[:2]:
                for y in range(len(doublon)):
                    if doublon[y] == '':
                        doublon[y] = contact[y]
                        del contacts[count_1]                      
        count_1 += 1
        count_2 += 1
    return personnes


def formats_phone_numbers(contacts):
    repl = r'+7(\2)\3-\4-\5 \6\7'
    pattern = (r'(\+\d|\d)?\s*\(?(\d{3})\)*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d+)\s*\(*(\w+.)*\s*(\d+)*\)*')
    for contact in contacts:
        result = re.sub(pattern, repl, contact[5])
        contact[5] = result.strip()
    return contacts
    

if __name__ == '__main__':
    path = "phonebook_raw.csv"
    headers, personnes = delete_table_header(path=path)
    sorting_personnes = sort_the_names(contacts=personnes)
    contacts_list = formats_phone_numbers(removes_duplicates(sorting_personnes))
    contacts_list.insert(0, headers)
with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)