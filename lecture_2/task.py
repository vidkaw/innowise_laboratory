def generate_age(age): # fuction for defenition
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    elif 20<=age<=110:
        return "Adult"

try:
    user_name = input("Enter your full name: ")

    while True: # age verification cycle
        birth_year_str = input("Enter your bith year: ")
        birth_year = int(birth_year_str)
        current_age = 2025 - birth_year
        if 110>=current_age>=0:
            break
        else:
            print("Age shell be less than 110 and more than 0!")
            
    hobbies = [] # list of hobbies
    count = 0
    while True: # hobby cycle
        hobby = input("Enter a favourite hobby or type 'stop' to finish: ")
        if (hobby.lower() == "stop") :
            break
        hobbies.append(hobby) # add to end of list
        count+=1

    # summary for person
    print("\n ---")
    print("Profile Summary:")
    # dictionary with user information
    user_profile ={"Name":user_name, "Age":current_age, "Life Stage" : generate_age(current_age) }

    # print hobby list
    for key, value in user_profile.items():
        print(f"{key}: {value}")
    if count == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favourite hobbies({count}): ")
        for hobby in hobbies:
            print(f"- {hobby}")
    print("---")
except Exception as e:
    print(f"Error: {e}")
