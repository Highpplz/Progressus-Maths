
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
    bugfinders_read_file.close
    if disclaimer_read != 'Yes' or credits_read != 'Yes' or bugfinders_read != 'Yes' or changelog_latest_read != 'Yes' or new_account == 'No':
        any_read_files = 'No'
    else:
        any_read_files= 'Yes'
    if version_last_ran == '':
        print('Thank you for installing my maths quiz prograrm.\nPlease contact me if you encounter any bugs or issues but first we need to get some legal stuff out of the way\n.')
        read == 'no'
        new_version = 'Yes'
        new_install = 'Yes'
    elif version_last_ran != current_version:
        print('Thank you for updating the software!\nWe now need to re varifiy the lisense as there may have been changes to it please enshure you re-read it!\nOnce that is done we will show all updated documentation for the program including the change log.')
        read = 'no'
        new_version = 'Yes'
        new_install = 'No'
    elif version_last_ran == current_version:
        new_install = 'No'
        new_version = 'No'
    else:
        print('\nNon crititcal error message: Version not verified as a precution please contact the dev team, automaticly reseting lisence verification.\n')
        read = 'no'
        any_read_files == 'No'
    if read != 'Yes' or new_version == 'Yes' or new_install == 'Yes' or any_read_files == 'No' or new_account == 'Yes':
        open_file_internaly = input('Would you like to read the lisense file in program?\n(Y/N) :')
        if open_file_internaly == 'Y':
            lisense = open('LISENCE.md','rt')
            print (lisense.readlines())
        elif open_file_internaly == 'N':
            print('Please find the file "copyright and lisense.txt" in the game install directory and read it or restart the progarm and have it display the lisense internaly.')
        else:
            print('Attempted bypass of lisense term accepting system detected, now closing prograrm!')
            input('Press enter to exit')
            exit()
        print('Do you accept the lisense terms?')
        accept = input('(Y/N)')
        if accept == 'N':
            print('You have denided the terms you have 24 hrs from the time that you downloaded the software to remove all traces of it from your computer (or any storage devices owned/managed by you) or accept!')
            input('Press enter to exit')
            exit()
        elif accept == 'Y':
            accept = 'Yes'
            print('Thank you for accepting the lisense terms!')
            lisense_read_write = open('lisense_read.txt','wt')
            lisense_read_write.write('Yes')
            lisense_read_write.close()
        else:
            print('Attempted bypass of lisense term accepting system detected, now closing prograrm!')
            input('Press enter to exit')
            exit()
    elif read == 'no' or read == 'No' or read == 'NO':
        print('Attempted bypass of lisense system detected! Will now close the program!')
        input('Press enter to close')
        exit()
    if disclaimer_read != 'Yes' or new_version == 'Yes' or new_install == 'Yes' or disclaimer_read == 'no' or disclaimer_read == 'No' or disclaimer_read == 'NO' or disclaimer_read == 'nO'or new_account == 'Yes':
        disclaimer_file = open('disclaimer.txt','rt')
        disclaimer_data = disclaimer_file.readlines()
        disclaimer_file.close()
        print(disclaimer_data)
        disclaimer_accept = input('Do you accept that you have read and understand this disclaimer? (Y/N) :')
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
            print('Attempt to bypass disclaimer accepance system detected now closing prograrm!')
            input('Press enter to close')
            exit()
    if new_version == 'Yes' or credits_read == 'No' or any_read_files == 'No' or new_account == 'Yes':
        print('\nWould you like to veiw the credits for the prograrm?')
        see_credits = input('(Y/N):')
        if see_credits == 'Y':
            credits_file = open('credits.txt','rt')
            credits_ = credits_file.readline()
            credits_file.close()
            print(credits_)
            credits_record_write = open('credits_read.txt','wt')
            credits_record_write.write('Yes')
            credits_record_write.close()
        elif see_credits == 'N':
            pass
        else:
            pass
        print('\nWould you like to see the bug finder list?')
        see_bug_finders = input('(Y/N):')
        if see_bug_finders == 'Y' or bugfinders_read != 'Yes':
            bug_finder_file = open('Bugfinders.txt','rt')
            bug_finder_data = bug_finder_file.readline()
            print(bug_finder_data)
            bug_finder_record_write = open('bugfinders_read.txt','wt')
            bug_finder_record_write.write('Yes')
            bug_finder_record_write.close()
        elif see_bug_finders == 'N':
            pass
        else:
            pass
        print('\nWould you like to see the full change log?')
        see_full_changelog = input('(Y/N):')
        if see_full_changelog == 'Y':
            latest_changelog_record_write = open('changelog_latest_read.txt','wt')
            latest_changelog_record_write.write('Yes')
            latest_changelog_record_write.close()
            changelog_file = open('changelog.txt','rt')
            changelog_data = changelog_file.readline()
            print(changelog_data)
        elif see_full_changelog == 'N' or changelog_latest_read != 'Yes':
            print('\nWould you like to see the changes in the latest version?')
            see_changelog_latest = input('(Y/N):')
            if see_changeglog_latest == 'Y':
                latest_changelog_file = open('changelog_latest','rt')
                latest_changelog_data = latest_changelog_file.readline()
                print(latest_changelog_data)
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
        print('Your dependencies seem to be older than the version of code you are running./nPlease always fully unzip all files in the zip folder for an update.')
    elif dependencies_up_to_date == 'No' and new_install == 'Yes':
        print('It seems all the .txt files have not been fully un-ziped when you installed this prograrm please try and re-un-zip this prograrm of you are having issues please contact a member of the dev team')
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

question_as_string_compleate_message = question_as_string,'Also please remember to round your answer to the nearest whole number.'

GUI = Tk()
GUI.title('Progressus Maths')
GUI.state('zoomed')

welcome_message = Label(GUI,text = 'Welcome to Progressus Maths!')
welcome_message.pack(side = TOP)

question_entry = Label(GUI,text = question_as_string_compleate_message)

answer_input = Entry(GUI)

GUI.mainloop()
