name = input('What\'s your name?: )
pieces = name.split()

if len(pieces) == 3:
    first_name = pieces[0]
    middle_name = pieces[1]
    last_name = pieces[2]
    first_initial = first_name[0] + '.'
    middle_initial = middle_name[0] + '.'
    
    print(last_name + ', ' + first_initial + middle_initial)
elif len(pieces) == 2:
    first_name = pieces[0]
    last_name = pieces[1]
    first_initial = first_name[0] + '.'
    
    print(last_name + ', ' + first_initial)
    
else:
    print(pieces[-1])
