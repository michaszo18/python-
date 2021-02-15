class Employ():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def change_sallary(self, new_salary, is_bonus=False):
        if is_bonus:
            print(f"{self.name}'s bonus is {new_salary}.")
        else:
            self.salary = new_salary
            print(f"{self.name}'s new salary is {self.salary}.")
        return True

    


def create_function_with_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        print("***** Function called *****")
        result = func(*args, **kwargs)
        print("***** Function end *****")
        return result

employ = Employ("Roman", 15000)
employ.change_sallary(20000, True)
employ.change_sallary(20000)

change_salary_with_log = create_function_with_wrapper(employ.change_sallary)

change_salary_with_log(1000, True)