class Employee:

    def __init__(self):
        print('Employee hired')
    def __del__(self):
        print('Destructor called')

def Create_obj():
    print("Making Employee")
    obj = Employee()
    print('Function End...')
    return obj

print("Calling function")
obj = Create_obj()
print('Program end...')
         
