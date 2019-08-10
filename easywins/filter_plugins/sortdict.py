class FilterModule(object):
    def dicsort(self, list, sortkey):
        return sorted(list, key=lambda i: i[sortkey])

    def test(self, value):
        return value+" "+"asher"

    def filters(self):
        return {
            'dicsort': self.dicsort,
            'test': self.test
        }
