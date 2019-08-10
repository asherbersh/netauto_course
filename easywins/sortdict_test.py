mylist = [{'name': 'asher', 'id': '065669384'}, {'name': 'natali', 'id': '12345'}, {'name': 'moshe', 'id': '80808'}]

def dicsort(list, sortkey):
    return sorted(list, key=lambda i: i[sortkey])


print(dicsort(mylist, "name"))


