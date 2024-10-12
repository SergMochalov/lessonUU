calls = 0
def count_calls ():
    global calls
    calls += 1
def string_info (string):
    count_calls()
    string_i = len(string), string.upper(), string.lower()
    print(string_i)
def is_contains (string,list_to_search):
    count_calls()
    x=0
    for i in  list_to_search:
        x += 1
        if string.lower() in i.lower():
            return True
        else:
            if x == len(list_to_search):
                return False
            continue


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

