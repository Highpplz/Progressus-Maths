import os #imports os for the 'exit()' command
valid_answer = 'No' #prepares the variable used to enshure the user's answer is of use to the prograrm
print(' ') #to create a space the the input command doesn't seem to like having '\n' in the string it displays
while valid_answer == 'No': #will run until the user answers in the Y/N format
    user_already_has_account = input('Do you already have an account (Y/N) :') #asks the user if they already have an account
    if user_already_has_account == 'Y': #sees if the user answered yes to the question
        logon_data = open('logon_data.txt','w+')#opens the file for reading
        logon_data_list = logon_data.readlines() #puts all data from all lines of the file into a list with each line as its own entry
        username = input('Please input your username :') #asks the user for their username
        valid_answer = 'Yes'
        try:
            user_login_index_number = logon_data.index(username) #trys to find the index value for the  username
        except Exception as e: #if it errors it will alow the user to be told before it crashes
            print('\nYou the account name you put in does not exist leading to this error:',e,'\n try making a new account\n') #tells the user what the error is and what they did to lead to it
            input('Press enter to close the program') #gets the user to exit the prograrm due to the error future versions might have it fully reset it but that would be a large job
            exit() #closes the progarm when run
        user_password = logon_data[user_login_index_number + 1] #as the user's password is below their username in the file it can be acessed by adding one to index value of the username
        password_correct = 'false'
        #preps the varible above and below this line for the loop
        trys = 0
        while password_correct == 'false': #gives the user 3 tries to get their password correct
            user_input_password = input('Please input your password.')
            trys = trys + 1
            if user_input_password == user_password: #only runs the code if the user hasn't ran out of trys and they have gave the system the correct password
                print('\nYour password is correct\n')
            else:
                print('\nYour password is wroung you have now used :',trys,'out of 3 trys\n') #tells the user their answer is wroung and how many attempts they have left
                if trys >= 3: #if the user is on their 3rd try and get it wroung they will be told that and the prograrm will close
                    print('As you have now input the wroung password 3 times the prograrm will now close.\n')
                    input('Press enter to close :')
                    exit()
    elif user_already_has_account == 'N': #only runs if the user says they don't have an account this system will allow the user to create an account
        print('\nAs you do not yet have an logon for this prograrm please create one following the instructions.\nIf you answered no to the queston by mistake just close the program and reopen it and answer again.\n') #displays a message to tell the user that they need to make a logon and also what to do if they selected this setting by mistake.
        new_username = input('Please select a name for your account :')
        account_name_taken = 'Yes'
        valid_answer = 'Yes'
        try:
            test = username_data.index(new_username)
        except Exception as e:
            account_name_taken = 'No'
        if account_name_taken == 'Yes':
            print('\nSorry this user account alredy exists the progarm will now close.\n')
            input('Press enter to close the progarm :')
            exit()
        print('\nYour account name is not yet taken\n')
        valid_password = 'No'
        while valid_password == 'No':
            new_password = input('Please set a memrobale password for your account :')
            print('Are you shure you whant to set : ',new_password, 'as your password?')
            password_confirmation = input('(Y/N)')
            if password_confirmation == 'Y':
                valid_password = 'Yes'
        print('Creating account...\n')
        number_of_needed_lines_file = open('number_of_needed_lines.txt','rt')
        number_of_needed_lines = number_of_needed_lines_file.readline()
        number_of_needed_lines = int(number_of_needed_lines)
        number_of_needed_lines_file.close()
        username_data = open('logon_data.txt','a+')
        username_data.write(new_username+"\n")
        username_data.write(new_password+"\n")
        #appends the user's new account name and password to the document for later refrance
        username_data.close()
        times_ran = 0
        while number_of_needed_lines > times_ran:
            username_data = open('logon_data.txt','a+')
            username_data.write(' \n')
            username_data.close()
            times_ran = times_ran + 1
        print(times_ran,' out of ',number_of_needed_lines,'of blank space has been reseved for your account\n')
        print('\nAccount has been created with the settings of :\n',new_username,'as your usename and ',new_password,'as your password.\nIf there is a mistake please restart the progarm and use the delate account option to remove your account before then later recreating it.')#tells the user the settings of their new account as well as instuctions for if there is a mistake in the settings.
    else: #only runs if the user's input wasn't in the form the progarm requested
        print('\nSorry your answer is invalid please answer in the form requested.\n') #tells the user that their answer was in an invalid format
        valid_answer = 'No'
