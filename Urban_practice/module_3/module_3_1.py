calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    tuple = (len(string), string.upper(),string.lower())
    print(tuple)
    count_calls()

def is_contains(string, list_to_search):
    count_calls()
    for item in list_to_search:
        if item == string:
            print(True)
            return
    print(False)


string_info('HeaDer')
is_contains('Hello',['Hello', 'Yes', 'No'])
is_contains('Hello',['Hello1', 'Yes', 'No'])
is_contains('Hello',['Hello', 'Yes', 'No'])
print(calls)