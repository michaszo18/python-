def double(x):
    return 2 * x


def root(x):
    return x**2


def negative(x):
    return -x


def div2(x):
    return x/2


number = 8
sequence = [double, root, div2, negative]
tmp_return_value = number

for step in sequence:
    tmp_return_value = step(tmp_return_value)
    print(tmp_return_value)

print("#" * 60)

def bake(what):
    return f"Baking {what}"

def cook(actvity, obj):
    return actvity(obj)

print(cook(bake, 'pizza'))

print("#" * 60)

def generate_values(fun1, list_of_numbers):
    result_list = list()
    
    for i in list_of_numbers:
        result_list.append(fun1(i))

    return result_list 


print(generate_values(div2, [4,6,7,8,9,123]))

print("#" * 60)

def create_function(kind):
    source = f'''
def f(*args):
    result = 0
    for a in args:
        result {kind}= a
    return result
'''
    exec(source, globals())
    return f

f_add = create_function('+')
print(f_add(1,2,3,4,5))

f_mul = create_function('*')
print(f_mul(1,2,3,4,5))


print("#" * 60)

def create_fun_2(kind):
    source = f"""
def f(date_1, date_2):
    sub = date_1 - date_2
    return sub * {kind}
"""
    exec(source, globals())
    return f


diff_in_days = create_fun_2('1')
diff_in_hours = create_fun_2('24')
diff_in_min = create_fun_2('3600')

print(diff_in_days(20-11-2020, 12-11-2020))
print(diff_in_hours(20-11-2020, 12-11-2020))
print(diff_in_min(20-11-2020, 12-11-2020))