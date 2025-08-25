class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def test_team_lead():
    lead = TeamLead('Nazar', 35000, 'Backend', 'Java', 7)

    assert lead.name == 'Nazar'
    assert lead.salary == 35000
    assert lead.department == 'Backend'
    assert lead.programming_language == 'Java'
    assert lead.team_size == 7

    print("All tests passed successfully!")