### Employee Account Puzzle
from datetime import date

class EmployeeAccount:
    def __init__ (self, username, email, department):
        self.username = username
        self.email = email
        self.department = department
        self.is_active = True
        self.failed_logon_attempt = 0
        self.group_membership = []
    def add_group(self, group):
        self.group_membership.append(group)
    def fail_logon(self):
        self.failed_logon_attempt = self.failed_logon_attempt + 1
        if self.failed_logon_attempt == 5:
            self.is_active = False
    def reset_logon_attempt(self):
        self.failed_logon_attempt = 0
    def disable_account(self):
        self.is_active = False
        self.disabled_date = date.today()
    def __str__(self):
        return f"Username: {self.username}\nEmail: {self.email}\nDepartment: {self.department}\nActive?: {self.is_active}\nNumber of Groups: {len(self.group_membership)}"

class ContractorAccount(EmployeeAccount):
    def __init__(self, username, email, department, end_date):
        super().__init__(username, email, department)
        self.end_date = end_date


employee1 = EmployeeAccount("zparmentier", "zparmentier@company.com", "IT")
employee2 = EmployeeAccount("sparmentier", "sparmentier@company.com", "Finance")
employee1.add_group("VPN-Users")
employee1.add_group("IT-Admins")
employee2.add_group("Finance-Reports")
employee2.fail_logon()
employee2.fail_logon()
employee2.fail_logon()
employee2.fail_logon()
employee2.fail_logon()
employee1.disable_account()
print(employee1)
print("Disabled?:")
print(hasattr(employee1, "disabled_date"))
print(employee2)
print("Disabled?")
print(hasattr(employee2, "disabled_date"))

contractor1 = ContractorAccount("jdoe", "jdoe@company.com", "Engineering", "2027-06-30")
contractor1.add_group("VPN-Users")
print(contractor1)
print(f"Contract ends: {contractor1.end_date}")