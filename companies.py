

class Company:
    def __init__(self, name, country, spec):
        self.name = name
        self.country = country
        self.spec = spec
    def print_info(self):
        print(f"Company {self.name} is from {self.country}.")
        print(f"   Main business: {self.spec}")

company1 = Company(name = "Haas", country = "US", spec = "machine tools")
company2 = Company(name = "Kern", country = "DE", spec = "machine tools")

company1.print_info()
company2.print_info()
