
#Version 0.2.0 Alpha

#By editing this code you accept any dammages to your installation of this progarm or your computer or data held within it. If you are just inrested in reading this code try the notepad sample code as the progarm
#does nothing with it as it is just there to allow for risk free reading of the sorce code

#MIT License

#Copyright (c) 2020 Epig-is-a-llama

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

current_version = '0.2.0.A'
last_version = '0.1.1.A'

import random
#imports random for creating random numbers for the questions and random mathmatcial operation selection

from tkinter import *
#imports tkinter for the progarm GUI

import sys
#imports sys for the 'exit()' command at the end to close the program when the user is done
#or to close the prograrm if a bypass of the lisense system is detected

internal_dependency_number = '3'
number_one_not_even = 'true'
number_two_not_even = 'true'
veiw_error = 'N'
score = 0
quit_yn = 'N'
questions_in_bunch = 0
total_questions = 0
random_operation = 'False'
add = 'No'
subtract = 'No'
times = 'No'
divide = 'No'
validation_loop_variable = 'Not Valid'
dependnency_file = open('dependency_number.txt','rt')
extenal_dependncy_number = dependnency_file.readline()
if internal_dependency_number != extenal_dependncy_number:
    ##print('Your dependency files are out of date or corrupted please try to contact a member of the dev team or re-download the prograrm as the zip file and fully re-install it.')
    dependencies_up_to_date = 'No'
elif  internal_dependency_number == extenal_dependncy_number:
    dependencies_up_to_date = 'Yes'
else:
    ##print('Non critical error message:\n the progarm can not verify if your dependencys are out of date please try to re-download and install the prograrm.')
    dependencies_up_to_date = 'IDK'
dependnency_file.close()

def lisense_system():
    validation_loop_variable = 'Not Valid'
    lisense_read = open('lisense_read.txt','rt')
    read = lisense_read.readline()
    lisense_read.close()
    version_last_ran_file = open('version_last_ran.txt','rt')
    version_last_ran = version_last_ran_file.readline()
    version_last_ran_file.close()
    disclaimer_read_file = open('disclaimer_read.txt','rt')
    disclaimer_read = disclaimer_read_file.readline()
    disclaimer_read_file.close()
    changelog_latest_read_file = open('changelog_latest_read.txt','rt')
    changelog_latest_read = changelog_latest_read_file.readline()
    changelog_latest_read_file.close()
    credits_read_file = open('credits_read.txt','rt')
    credits_read = credits_read_file.readline()
    credits_read_file.close()
    bugfinders_read_file = open('bugfinders_read.txt','rt')
    bugfinders_read = bugfinders_read_file.readline()
    bugfinders_read_file.close()
    if disclaimer_read != 'Yes' or credits_read != 'Yes' or bugfinders_read != 'Yes' or changelog_latest_read != 'Yes' or new_account == 'No':
        any_read_files = 'No'
    else:
        any_read_files= 'Yes'
    if version_last_ran == 'New Install':
        ##print('Thank you for installing my maths quiz prograrm.\nPlease contact me if you encounter any bugs or issues but first we need to get some legal stuff out of the way\n.')
        read == 'no'
        new_version = 'Yes'
        new_install = 'Yes'
    elif version_last_ran != current_version:
        ##print('Thank you for updating the software!\nWe now need to re varifiy the lisense as there may have been changes to it please enshure you re-read it!\nOnce that is done we will show all updated documentation for the program including the change log.')
        read = 'no'
        new_version = 'Yes'
        new_install = 'No'
    elif version_last_ran == current_version:
        new_install = 'No'
        new_version = 'No'
    else:
        ##print('\nNon crititcal error message: Version not verified as a precution please contact the dev team, automaticly reseting lisence verification.\n')
        read = 'no'
        any_read_files == 'No'
    if read != 'Yes' or new_version == 'Yes' or new_install == 'Yes' or any_read_files == 'No' or new_account == 'Yes':
        open_file_internaly = input('Would you like to read the lisense file in program?\n(Y/N) :')
        if open_file_internaly == 'Y':
            lisense = open('lisense(.txt_version).txt,'rt')
            ##print (lisense.readlines())
        elif open_file_internaly == 'N':
            pass
            ##print('Please find the file "copyright and lisense.txt" in the game install directory and read it or restart the progarm and have it display the lisense internaly.')
        else:
            ##print('Attempted bypass of lisense term accepting system detected, now closing prograrm!')
            ##input('Press enter to exit')
            exit()
        print('Do you accept the lisense terms?')
        ##accept = input('(Y/N)')
        if accept == 'N':
            ##print('You have denided the terms you have 24 hrs from the time that you downloaded the software to remove all traces of it from your computer (or any storage devices owned/managed by you) or accept!')
            ##input('Press enter to exit')
            exit()
        elif accept == 'Y':
            accept = 'Yes'
            ##print('Thank you for accepting the lisense terms!')
            lisense_read_write = open('lisense_read.txt','wt')
            lisense_read_write.write('Yes')
            lisense_read_write.close()
        else:
            ##print('Attempted bypass of lisense term accepting system detected, now closing prograrm!')
            ##input('Press enter to exit')
            exit()
    elif read == 'no' or read == 'No' or read == 'NO':
        ##print('Attempted bypass of lisense system detected! Will now close the program!')
        ##input('Press enter to close')
        exit()
    if disclaimer_read != 'Yes' or new_version == 'Yes' or new_install == 'Yes' or disclaimer_read == 'no' or disclaimer_read == 'No' or disclaimer_read == 'NO' or disclaimer_read == 'nO'or new_account == 'Yes':
        disclaimer_file = open('disclaimer.txt','rt')
        disclaimer_data = disclaimer_file.readlines()
        disclaimer_file.close()
        print(disclaimer_data)
        ##disclaimer_accept = input('Do you accept that you have read and understand this disclaimer? (Y/N) :')
        if disclaimer_accept == 'Y':
            print('Thank you for accepting the disclaimer')
            disclaimer_read_file_write = open('disclaimer_read.txt','wt')
            disclaimer_read_file_write.write('Yes')
            disclaimer_read_file_write.close()
        elif disclaimer_accept == 'N':
            print('You have declined the disclaimer policy you may not use this software until you accept it.\nNow closing program')
            disclaimer_read_file_write = open('disclaimer_read.txt','wt')
            disclaimer_read_file_write.write('no')
            disclaimer_read_file_write.close()
            input('Press enter to close')
            exit()
        else:
            ##print('Attempt to bypass disclaimer accepance system detected now closing prograrm!')
            ##input('Press enter to close')
            exit()
    if new_version == 'Yes' or credits_read == 'No' or any_read_files == 'No' or new_account == 'Yes':
        print('\nWould you like to veiw the credits for the prograrm?')
        ##see_credits = input('(Y/N):')
        if see_credits == 'Y':
            credits_file = open('credits.txt','rt')
            credits_ = credits_file.readline()
            credits_file.close()
            ##print(credits_)
            credits_record_write = open('credits_read.txt','wt')
            credits_record_write.write('Yes')
            credits_record_write.close()
        elif see_credits == 'N':
            pass
        else:
            pass
        ##print('\nWould you like to see the bug finder list?')
        ##see_bug_finders = input('(Y/N):')
        if see_bug_finders == 'Y' or bugfinders_read != 'Yes':
            bug_finder_file = open('Bugfinders.txt','rt')
            bug_finder_data = bug_finder_file.readline()
            ##print(bug_finder_data)
            bug_finder_record_write = open('bugfinders_read.txt','wt')
            bug_finder_record_write.write('Yes')
            bug_finder_record_write.close()
        elif see_bug_finders == 'N':
            pass
        else:
            pass
        ##print('\nWould you like to see the full change log?')
        ##see_full_changelog = input('(Y/N):')
        if see_full_changelog == 'Y':
            latest_changelog_record_write = open('changelog_latest_read.txt','wt')
            latest_changelog_record_write.write('Yes')
            latest_changelog_record_write.close()
            changelog_file = open('changelog.txt','rt')
            changelog_data = changelog_file.readline()
            ##print(changelog_data)
        elif see_full_changelog == 'N' or changelog_latest_read != 'Yes':
            ##print('\nWould you like to see the changes in the latest version?')
            ##see_changelog_latest = input('(Y/N):')
            if see_changeglog_latest == 'Y':
                latest_changelog_file = open('changelog_latest','rt')
                latest_changelog_data = latest_changelog_file.readline()
                ##print(latest_changelog_data)
                latest_changelog_record_write = open('changelog_latest_read.txt','wt')
                latest_changelog_record_write.write('Yes')
                latest_changelog_record_write.close()
            elif see_changelog_latest == 'N':
                pass
            else:
                pass
        else:
            pass
    if dependencies_up_to_date == 'No' and new_version == 'Yes' and new_install == 'No':
        ##print('Your dependencies seem to be older than the version of code you are running./nPlease always fully unzip all files in the zip folder for an update.')
    elif dependencies_up_to_date == 'No' and new_install == 'Yes':
        ##print('It seems all the .txt files have not been fully un-ziped when you installed this prograrm please try and re-un-zip this prograrm of you are having issues please contact a member of the dev team')
    version_file_write = open('version_last_ran.txt','wt')
    version_file_write.write(current_version)
    version_file_write.close()

def logon_system ():
    valid_answer = 'No' #prepares the variable used to enshure the user's answer is of use to the prograrm
    ##print(' ') #to create a space the the input command doesn't seem to like having '\n' in the string it displays
    while valid_answer == 'No': #will run until the user answers in the Y/N format
        ##user_already_has_account = input('Do you already have an account (Y/N) :') #asks the user if they already have an account
        if user_already_has_account == 'Y': #sees if the user answered yes to the question
            logon_data = open('logon_data.txt','w+')#opens the file for reading
            logon_data_list = logon_data.readlines() #puts all data from all lines of the file into a list with each line as its own entry
            ##username = input('Please input your username :') #asks the user for their username
            valid_answer = 'Yes'
            try:
                user_login_index_number = logon_data.index(username) #trys to find the index value for the  username
            except Exception as e: #if it errors it will alow the user to be told before it crashes
                ##print('\nYou the account name you put in does not exist leading to this error:',e,'\n try making a new account\n') #tells the user what the error is and what they did to lead to it
                ##input('Press enter to close the program') #gets the user to exit the prograrm due to the error future versions might have it fully reset it but that would be a large job
                exit() #closes the progarm when run
            user_password = logon_data[user_login_index_number + 1] #as the user's password is below their username in the file it can be acessed by adding one to index value of the username
            password_correct = 'false'
            #preps the varible above and below this line for the loop
            trys = 0
            while password_correct == 'false': #gives the user 3 tries to get their password correct
                ##user_input_password = input('Please input your password.')
                trys = trys + 1
                if user_input_password == user_password: #only runs the code if the user hasn't ran out of trys and they have gave the system the correct password
                    ##print('\nYour password is correct\n')
                    user_nickname = username
                else:
                    ##print('\nYour password is wroung you have now used :',trys,'out of 3 trys\n') #tells the user their answer is wroung and how many attempts they have left
                    if trys >= 3: #if the user is on their 3rd try and get it wroung they will be told that and the prograrm will close
                        ##print('As you have now input the wroung password 3 times the prograrm will now lock for 5 mins.\n')
                        sleep(300)
        elif user_already_has_account == 'N': #only runs if the user says they don't have an account this system will allow the user to create an account
            ##print('\nAs you do not yet have an logon for this prograrm please create one following the instructions.\nIf you answered no to the queston by mistake just close the program and reopen it and answer again.\n') #displays a message to tell the user that they need to make a logon and also what to do if they selected this setting by mistake.
            ##new_username = input('Please select a name for your account :')
            account_name_taken = 'Yes'
            valid_answer = 'Yes'
            try:
                test = username_data.index(new_username)
            except Exception as e:
                account_name_taken = 'No'
            if account_name_taken == 'Yes':
                ##print('\nSorry this user account alredy exists the progarm will now close.\n')
                ##input('Press enter to close the progarm :')
                exit()
            ##print('\nYour account name is not yet taken\n')
            valid_password = 'No'
            while valid_password == 'No':
                ##new_password = input('Please set a memrobale password for your account :')
                ##print('Are you shure you whant to set : ',new_password, 'as your password?')
                password_confirmation = input('(Y/N)')
                if password_confirmation == 'Y':
                    valid_password = 'Yes'
            ##print('Creating account...\n')
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
            ##print(times_ran,' out of ',number_of_needed_lines,'of blank space has been reseved for your account\n')
            ##print('\nAccount has been created with the settings of :\n',new_username,'as your usename and ',new_password,'as your password.\nIf there is a mistake please restart the progarm and use the delate account option to remove your account before then later recreating it.')#tells the user the settings of their new account as well as instuctions for if there is a mistake in the settings.
        else: #only runs if the user's input wasn't in the form the progarm requested
            ##print('\nSorry your answer is invalid please answer in the form requested.\n') #tells the user that their answer was in an invalid format
            valid_answer = 'No'
    ##print('\nWelcome to my maths quiz program ',user_nickname,'\n')

def stat_update():
    total_questions = open('total_questions.txt','wt')
    total_questions.write('0')
    total_questions.close()
    total_score = open('total_score.txt','wt')
    total_score.write('0')
    total_score.close()
    no_reset_file_create = open('no_reset.txt','wt')
    no_reset_file_create.write('N')
    no_reset_file_create.close()
    logon_data_file_wipe = open('logon_data.txt','wt')
    logon_data_file_wipe.write('#Header')
    logon_data_file_wipe.close()
    ##print('Stat reset compleate!')

def reset_stats_system ():
    valid_input = 'false'
    reset_stats_version_number = '0.2.0.A'
    reset_stats_file = open('reset_stats_version.txt','w+')
    last_reset_stats_version_ran = reset_stats_file.readline()
    version_last_ran_file = open('version_last_ran.txt','rt')
    version_last_ran = version_last_ran_file.readline()
    version_last_ran_file.close()
    if last_reset_stats_version_ran != reset_stats_version_number:
        if version_last_ran != 'never':
            ##print('Your version of the reset stats program is of a different version to the main game please re-download the installer and/or fully reinstall the prograrm.')
            ##input('Press enter to contininute')
            pass
    reset_stats_file.write(reset_stats_version_number)
    reset_stats_file.close()
    if version_last_ran == 'never':
        stat_update()
        stat_update_YN = 'Y'
    else:
        stat_update_YN = 'N'
    no_reset_file_read = open('no_reset.txt','rt')
    no_reset = no_reset_file_read.readline()
    if no_reset == 'N' and version_last_ran != 'never':
        ##print('Would you like to reset your stats for the game?')
        while valid_input == 'false':
            ##stat_update_YN = input('(Y/N) :')
            if stat_update_YN == 'Y':
                stat_update()
                valid_input = 'true'
            elif stat_update_YN == 'N':
                valid_input = 'true'
            else:
                valid_input = 'false'
                ##print('\nPlease answer in the Y/N format.\n')
    valid_input = 'false'
    while valid_input =='false' and stat_update_YN == 'N':
        ##print('Would you like to stop seeing this message? (If you chose this you will not be able to reset your stats without using the "reset_stats.bat")')
        ##stop_seeing = input('(Y/N) :')
        if stop_seeing == 'N':
            valid_input = 'true'
        elif stop_seeing == 'Y':
            no_reset_file = open('no_reset.txt','wt')
            no_reset_file.write('Y')
            no_reset_file.close()
            valid_input = 'true'
        else:
            valid_input = 'false'
            ##print('\nPlease answer in the Y/N format.\n')

def difficlty_setting_system():
    validation_loop_variable = 'Not Valid'
    while validation_loop_variable == 'Not Valid':
        is_int = 'True'
        ##difficulty = input('\nPlease select a number between 1 and 10 to be a diffiulcty (1 being the easyest and 10 being the hardest):')
        #to avoid a crash the code will first test to see if the input is an interger before trying to convert therefore accomodating for user error or attempts to crash the program
        try:
           difficulty = int(difficulty)
        except Exception as e:
            ##print('Your did not input in the correct format leading to this error :',e)
            is_int = 'False'
        if is_int == 'True':
            if difficulty > 10 or difficulty < 0:
                ##print('\nInvalid input please only enter a number between 1 and 10 next time.\n')
                #enshures yet again that the user's input will be of use to the computer
                validation_loop_variable = 'Not Valid'
            else:
                ##print('\nYou have selected a difficulty of: ',difficulty,'\n')
                validation_loop_variable = 'Valid'
        else:
            pass
            #this runs if the input isn't an interger and therefore can't be converted
            ##print('\nPlease input only a number (so no letters puntuation etc)')

def mathmatcial_operation_selection_system():
    validation_loop_variable = 'Not Valid'
    while validation_loop_variable == 'Not Valid':
        #lets the user chose to practice a specific mathmatical operation or to have the computer randomly chose one
        ##user_operation_input=input('Please enter a mathmatical operation symbol to select that to practice or you can enter: "?" to have one randomly selected each question:\n')
        if user_operation_input == '+':
            system_operation = '+'
            validation_loop_variable = 'Valid'
            #all this if-elif-else statement is to convert the user's input of the operation symbol into an interger from a string for the computer to use at a later point in the code
        elif user_operation_input == '-':
            system_operation = '-'
            validation_loop_variable = 'Valid'
        elif user_operation_input == '*' or user_operation_input == 'x' or user_operation_input == 'X':
            system_operation = '*'
            validation_loop_variable = 'Valid'
        elif user_operation_input == '/':
            system_operation = '/'
            validation_loop_variable = 'Valid'
        elif user_operation_input == '?':
            system_operation = 'Random'
            random_operation = 'True'
            validation_loop_variable = 'Valid'
        else:
            ##print('Invalid input!\nPlease re-read the question.')
            validation_loop_variable = 'Not Valid'
    validation_loop_variable = 'Not Valid'
    #preps the validation loop for next useage
    print('\nYou have selected :',system_operation,' as your mathmatcial operation of choice to practice')

def question_creation_system():
    #this loop will run 10 times to give the user a batch of 10 questions before letting them change their settings and see their score
    while questions_in_bunch < 10:
                random_number = random.randint(1,10)
                number_1 = random_number*difficulty
                random_number = random.randint(1,10)
                #gets 2 random numbers between 1 and 10 to be used to randomly form the mathmatical sum
                number_2 = random_number*difficulty
                if random_operation == 'True':
                    #looks to see if the user has the computer set to pick a random operation
                    random_number = random.randint(1,4)
                    random_operation_number = random_number
                    if random_operation_number == 1:
                        system_operation = '+'
                    elif random_operation_number == 2:
                        #uses a randint command to make a random number between 1 and 4 each number coresponding to a math matical operation
                        system_operation = '-'
                    elif random_operation_number == 3:
                        system_operation = '*'
                    elif random_operation_number == 4:
                        system_operation = '/'
                    else:
                        ##print('Invalid value for "random_operation_number"')
                elif random_operation == 'False':
                    pass
                else:
                    validation_loop_variable = 'Not Valid'
                    while validation_loop_variable == 'Not Valid':
                        ##print('\n!!!\nError:\nvariable issue: "random_operation" variable has not been set to either True of False!\n!!!\nWould you like to try and veiw what the variable has been set to? (WARNING: This runs a risk of crashing the program)')
                        view_error = input('(Y/N): ')
                        if veiw_error == 'Y':
                            ##print('The variable "random_operation" is set to: ',random_operation)
                            ##input('Press any key to continute ...')
                            validation_loop_variable = 'Valid'
                        elif veiw_error == 'N':
                            validation_loop_variable = 'Valid'
                        else:
                            validation_loop_variable = 'Not Valid'
                            ##print('Please read the question carefuly this time!')
                validation_loop_variable = 'Not Valid'
                if system_operation == '+':
                    number_1 = number_1 * 2
                    number_2 = number_2 * 2
                    question_as_string = number_1,' + ',number_2,' = '
                    computer_answer = number_1 + number_2
                elif system_operation == '-':
                    question_as_string = number_1,' - ',number_2,' = '
                    computer_answer = number_1 - number_2
                elif system_operation == '*':
                    number_1 = number_1 * 2
                    number_2 = number_2 * 2
                    question_as_string = number_1,' X ',number_2,' = '
                    computer_answer = number_1 * number_2
                elif system_operation == '/':
                    while number_one_not_even == 'true':
                        even_value = number_1 % 2
                        if even_value == 1:
                            number_1 = random.randint(1,10)
                        elif even_value == 0:
                            number_one_not_even = 'false'
                        else:
                            pass
                            ##print('Minor error:\n Variable "number_1" could not be identifed as even or odd will now assume it is odd')
                    while number_two_not_even == 'true':
                        even_value = number_2 % 2
                        if even_value == 1:
                            number_2 = random.randint(1,10)
                        elif even_value == 0:
                            number_two_not_even = 'false'
                        else:
                            pass
                            ##print('Minor error:\n Variable "number_2" could not be identifed as even or odd will now assume it is odd')
                    number_1 = number_1 / 2
                    number_2 = number_2 / 2
                    question_as_string = number_1,' / ',number_2,' = '
                    computer_answer = number_1 / number_2
                else:
                    pass
                    ##print('Warning!: Invalid value assigned to the variable "system_operation" is is currently set to: ',system_operation,'\nThis may lead to a crash of the program if the program continutes to run')
                    ##input('Press enter to continute . . .')
                question_as_string_compleate_message = question_as_string,'Also please remember to round your answer to the nearest whole number.'
                ##print(question_as_string,' \n\nRemember if the answer is a decimal to round to the nearest whole number.')
                ##user_answer = input('Please input your answer here :')

def question_scoring_system():
    is_int = 'True'
    try:
        user_answer = int(user_answer)
    except Exception as e:
        is_int = 'False'
    computer_answer = (round(computer_answer))
    if is_int == 'True':
        user_answer = int(user_answer)
        if user_answer == computer_answer:
            ##print('\nYour answer was correct! ',user_nickname,'+1 Point!\n')
            score = score + 1
            #adds score to both the session score and the question bunch score
            #bunch refers to a batch of 10 questions the computer generates for the user
        else:
            pass
            ##print('\nYour answer was wroung the correct answer was: ',computer_answer,' Better luck next time',user_nickname)
            #tells the user their answer was wroung and informs them of the corecct answer while nor adding or deducting...
            #points from them but still stating the question has being wroung for the user to see at the end of that question bunch
    else:
        pass
        ##print('\nYou did not input an interger into the progarm (defulting to wroung answer)')
        ##print('\nYour answer was wroung the correct answer was: ',computer_answer,' Better luck next time',user_nickname
    total_questions = total_questions + 1
    questions_in_bunch = questions_in_bunch + 1
    percentage = score_this_bunch / 10
    precentage = percentage * 100

def bunch_ending_system():
    #calulates the user's percentage for the last 10 questions and tells the user that as well as their score over the same 10 questions
    ##print('Weldone you have compleated 10 questions out of these 10 you got:\n',score_this_bunch,' correct\n That means a percentage of: ',percentage*100,'% correct')
    valdation_loop_variable = 'Not Valid'
    while validation_loop_variable == 'Not Valid':
            ##print('Would you like to quit now to see your results for this whole session?')
            ##quit_yn = input('Please answer in the format (Y/N): ')
            #asks the user if they whant to end their session of the program
            if quit_yn == 'Y':
                percentage = score / total_questions
                percentage = precentage
                #gives the user their percentage for this whole instance that the program has beem ran
                ##print('\nDuring this whole session you did a total of: ',total_questions,' questions.\nAnd a total of: ',score,' were correct.\nThat leaves you with a percentage of: ',percentage,'% correct.\n')
                total_questions_file_read = open('total_questions.txt','rt')
                total_questions_all_time =  total_questions_file_read.readline()
                total_questions_all_time = int(total_questions_all_time)
                total_questions = total_questions + total_questions_all_time
                #calculates then displays the total questions ever done using this program by fetching data from a .txt file in the game directory
                ##print('Out of all the time you have been using this program you have compeated:\nA total of: ',total_questions,' questions!\n')
                total_score_file_read = open('total_score.txt','rt')
                score_all_time = total_score_file_read.readline()
                score_all_time = int(score_all_time)
                score = score + score_all_time
                ##print('And a total of: ',score,' were correct.\n')
                #does the same as the last comment but this time fore score
                percentage = score / total_questions
                percentage = percentage * 100
                ##print('That makes for an all time percentage of: ',percentage,'% correct.\n')
                #uses the 2 above mentioned stats to make an all time percentage
                total_score_file_read.close()
                total_questions_file_read.close()
                score = str(score)
                total_questions = str(total_questions)
                total_score_file_write = open('total_score.txt','wt')
                #writes the new updated stats to the .txt file for future useage
                total_questions_file_write = open('total_questions.txt','wt')
                total_questions_file_write.write(total_questions)
                total_score_file_write.write(score)
                total_score_file_write.close()
                total_questions_file_write.close()
                ##print('Your score and questions done have been sucessfully saved!')
                #tells the user they have been saved then exits the loop
                validation_loop_variable = 'Valid'
            elif quit_yn == 'N':
                validation_loop_variable = 'Valid'
                ##print('Thank you for choosing to continute to play!\n')
            else:
                ##print('Please use the (Y/N) format for your answer')
                validation_loop_variable = 'Not Valid'
        ##print('The progarm has finsished running.')
        ##input('Press enter to exit')
        #uses an input so the program waits before closing to give the user time to acknowlege the messages that have been sent before closing
        exit()

GUI = Tk()
GUI.title('Progressus Maths')
GUI.state('zoomed')

welcome_message = Label(GUI,text = 'Welcome to Progressus Maths!')
welcome_message.pack(side = TOP)

question_entry = Label(GUI,text = question_as_string_compleate_message)

answer_input = Entry(GUI)

GUI.mainloop()
