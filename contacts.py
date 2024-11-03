# Since: 2024-11-02, Ishan Karpe

'''
NOTE: 
I create my programs with lots of comments so that:
    1. I can understand what I did when I come back to it later.
    2. Others can understand what I did when they read my code.
    3. I like teaching the concepts and demonstarting them in my code.
    4. It is a win-win for everyone.
    5. I am expanding my knowledge and understanding of Python.
'''


'''Create a dictionary to store contacts, empty at first
# This dictionary will be used to store contacts in the format:
# {name: number}
# The name will be the key and the number will be the value'''
contacts = {}

# Main loop (no functions)
# This loop will run until the user chooses to exit

try:
    while True:
        print('\nContacts')
        print('========')
        print('1. Add contact')
        print('2. Search contact')
        print('3. Delete contact')
        print('4. View all contacts')
        print('5. Exit')

        choice = input('Enter your choice:')

        # Step 1 is adding a contact, if it exists, will not add it
        if choice == '1':
            name = input('Enter name:')
            number = int(input('Enter number:'))

            if name in contacts:
                print('\nContact already exists')
            else:
                # dictionary_name[key] = value
                # the value is assigned to the key in the dictionary
                contacts[name] = number
                print(f'Contact added: {name}, {number}')

        # Step 2 is searching for a contact
        elif choice == '2':
            name = input('Enter name:')
            if name in contacts:
                print(f'\nNumber for {name} is {contacts[name]}')
            else:
                print('\nContact not found')

        # Step 3 is deleting a contact
        elif choice == '3':
            name = input('Enter name:')
            if name in contacts:
                # delete by the key not the value
                # del dictionary_name[key]
                del contacts[name]
                print('\nContact deleted')
            else:
                print('\nContact not found')

        # Step 4 is viewing all contacts
        elif choice == '4':
            # items() returns a list of tuples for the list
            for name, number in contacts.items():
                print(f'{name}: {number}')
            if not contacts:
                print('\nNo contacts')

        # Step 5 is exiting the program
        elif choice == '5':
            print('Thanks for using the contacts program! Star on my GitHub!')
            break

        # If the user enters an invalid choice
        else:
            print('Invalid choice')
except ValueError:
    print('Please enter a valid number')
    
    

'''
        So a quick recap of the program:
        Contacts dictionary is created to store contacts.
        to add a contact (or anything to a dict) use the following formula: dictionary_name[key] = value
        to delete a contact (or anything from a dict) use the following "   del dictionary_name[key]

        Add Contact: Prompts for a name and phone number, checks for duplicates, and adds the contact if it does not already exist.
        View Contacts: Displays all contacts if any are saved.
        Search Contact: Prompts for a name and displays the contact if it exists.
        Delete Contact: Prompts for a name and deletes the contact if found.
        Exit: Breaks the loop, ending the program.
        ''' 

'''quit() vs break
        quit() is used to exit the program, while break is used mainly in while loops.
        '''
        
        
'''try and except
        try and except are used to catch errors in Python. If an error occurs in the try block, the except block will run.
        '''

'''items() vs keys() vs values()
        items() returns a list of tuples for the list
        keys() returns a list of keys for the list
        values() returns a list of values for the list
        '''