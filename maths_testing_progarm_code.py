#
#Version 0.2.0 Alpha
#
#By editing this code you accept any dammages to your installation of this progarm or your computer or data held within it. If you are just inrested in reading this code try the notepad sample code as the progarm
#does nothing with it as it is just there to allow for risk free reading of the sorce code
#
#MIT License
#
#Copyright (c) 2020 Epig-is-a-llama
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
#
global current_version
current_version = '0.2.0.A'
global last_version
last_version = '0.1.1.A'
import random
#imports random for the random question and operation selectors
import sys
#imports sys for the 'exit()' command at the end to close the program when the user is done
#or to close the prograrm if a bypass of the lisense system is detected
#from Tkinter import *
global user_nickname
global old_nickmame
global use_old_nickname
global nickname_prompt
global difficlty
global nickname
global questions_in_bunch
global random_operation_selector
global system_operation
global user_operation_input
global validation_loop_variable
global random_number
#used to enshure no variables are left not declared and to make any futrure port to python 2 very easy
global number_1
global score_all_time
global total_questions_all_time
global number_2
global view_error
global score
global quit_yn
global see_credits
global see_bug_finders
global accept
global open_file_internaly
global read
global question_as_string
global user_answer
global computer_answer
global  internal_dependency_number
global see_changelog_latest
global credits_
global see_full_changelog
global version_last_ran
global score_this_bunch
global questions_in_bunch
global random_operation_number
global total_questions
global disclaimer_data
global new_version
global changelog_data
global latest_changelog_data
global bug_finder_data
global disclaimer_accept
global new_install
global disclaimer_read
global any_read_files
global credits_read
global bugfinders_read
global changelog_latest_read
global number_one_not_even
global number_two_not_even
internal_dependency_number = '3'
number_one_not_even = 'true'
number_two_not_even = 'true'
veiw_error = 'N'
score = 0
quit_yn = 'N'
questions_in_bunch = 0
total_questions = 0
random_operation = 'False'
#program = Tk()
#program.title('Maths Practice Game')
#label = Label(program, text='Welcome to my maths practice game!')
#label.grid(column=5,row=1)
#program.mainloop()
validation_loop_variable = 'Not Valid'
dependnency_file = open('dependency_number.txt','rt')
extenal_dependncy_number = dependnency_file.readline()
if internal_dependency_number != extenal_dependncy_number:
    print('Your dependency files are out of date or corrupted please try to contact a member of the dev team or re-download the prograrm as the zip file and fully re-install it.')
    dependencies_up_to_date = 'No'
elif  internal_dependency_number == extenal_dependncy_number:
    dependencies_up_to_date = 'Yes'
else:
    print('Non critical error message:\n the progarm can not verify if your dependencys are out of date please try to re-download and install the prograrm.')
    dependencies_up_to_date = 'IDK'
dependnency_file.close()
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
        lisense = open('lisense(.txt_version).txt','rt')
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
nickname_file = open('user_nicknames.txt','rt')
#looks to see if the user has used the file before to be able to offer that their nickname is automaticly set to their most recent one
old_nickname = nickname_file.readline()
if old_nickname != '':
    #if the user has used the program before it will offer the user the option to use their old nickname or create a new one
    while validation_loop_variable == 'Not Valid':
        nickname_prompt = 'In the past you have used ',old_nickname,' as your nickname would you like to create a new nickname? (Y/N) :'
        print('In the past you have used ',old_nickname,' as your nickname would you like to create a new nickname?')
        use_old_nickname = input('(Y/N) :')
        if use_old_nickname == 'N' or use_old_nickname == 'n':
            validation_loop_variable = 'Valid'
            user_nickname = old_nickname
        elif use_old_nickname == 'Y' or use_old_nickname == 'y':
            validation_loop_variable = 'Valid'
            user_nickname = input('Create a new nickname. :\n')
            nickname_file.close()
            nickname_file = open('user_nicknames.txt','wt')
            nickname_file.write(user_nickname)
            #writes new nickname to the file for future use
            nickname_file.close()
        else:
            print('Please answer Y or N to the question')
            #enshures the user answers the question in a way that the computer can use the user's reponse
else:
    user_nickname = input('Create a nickname:\n')
    nickname_file.close()
    nickname_file = open('user_nicknames.txt','wt')
    #if no old nickname can be found it will ask the user to create a new nickname
    nickname_file.write(user_nickname)
    nickname_file.close()
print('\nWelcome to my maths quiz program ',user_nickname,'\n')
#the while loop is as once the intital setup has been run the main bluck of the code just has to be run in a cycle
while quit_yn == 'N':
    questions_in_bunch = 0
    score_this_bunch = 0
    validation_loop_variable = 'Not Valid'
    while validation_loop_variable == 'Not Valid':
        #lets the user chose to practice a specific mathmatical operation or to have the computer randomly chose one
        user_operation_input=input('Please enter a mathmatical operation symbol to select that to practice or you can enter: "?" to have one randomly selected each question:\n')
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
            print('Invalid input!\nPlease re-read the question.')
            validation_loop_variable = 'Not Valid'
    validation_loop_variable = 'Not Valid'
    #preps the validation loop for next useage
    print('\nYou have selected :',system_operation,' as your mathmatcial operation of choice to practice')
    is_int = 'True'
    while validation_loop_variable == 'Not Valid':
        is_int = 'True'
        difficulty = input('\nPlease select a number between 1 and 10 to be a diffiulcty (1 being the easyest and 10 being the hardest):')
        #to avoid a crash the code will first test to see if the input is an interger before trying to convert therefore accomodating for user error or attempts to crash the program
        try:
           difficulty = int(difficulty)
        except Exception as e:
            print('Your did not input in the correct format leading to this error :',e)
            is_int = 'False'
        if is_int == 'True':
            if difficulty > 10 or difficulty < 0:
                print('\nInvalid input please only enter a number between 1 and 10 next time.\n')
                #enshures yet again that the user's input will be of use to the computer
                validation_loop_variable = 'Not Valid'
            else:
                print('\nYou have selected a difficulty of: ',difficulty,'\n')
                validation_loop_variable = 'Valid'
        else:
            #this runs if the input isn't an interger and therefore can't be converted
            print('\nPlease input only a number (so no letters puntuation etc)')
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
                    print('Invalid value for "random_operation_number"')
            elif random_operation == 'False':
                pass
            else:
                validation_loop_variable = 'Not Valid'
                while validation_loop_variable == 'Not Valid':
                    print('\n!!!\nError:\nvariable issue: "random_operation" variable has not been set to either True of False!\n!!!\nWould you like to try and veiw what the variable has been set to? (WARNING: This runs a risk of crashing the program)')
                    view_error = input('(Y/N): ')
                    if veiw_error == 'Y':
                        print('The variable "random_operation" is set to: ',random_operation)
                        input('Press any key to continute ...')
                        validation_loop_variable = 'Valid'
                    elif veiw_error == 'N':
                        validation_loop_variable = 'Valid'
                    else:
                        validation_loop_variable = 'Not Valid'
                        print('Please read the question carefuly this time!')
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
                        print('Minor error:\n Variable "number_1" could not be identifed as even or odd will now assume it is odd')
                while number_two_not_even == 'true':
                    even_value = number_2 % 2
                    if even_value == 1:
                        number_2 = random.randint(1,10)
                    elif even_value == 0:
                        number_two_not_even = 'false'
                    else:
                        print('Minor error:\n Variable "number_2" could not be identifed as even or odd will now assume it is odd')
                number_1 = number_1 / 2
                number_2 = number_2 / 2
                question_as_string = number_1,' / ',number_2,' = '
                computer_answer = number_1 / number_2
            else:
                print('Warning!: Invalid value assigned to the variable "system_operation" is is currently set to: ',system_operation,'\nThis may lead to a crash of the program if the program continutes to run')
                input('Press enter to continute . . .')
            print(question_as_string,' \n\nRemember if the answer is a decimal to round to the nearest whole number.')
            user_answer = input('Please input your answer here :')
            is_int = 'True'
            try:
                user_answer = int(user_answer)
            except Exception as e:
                is_int = 'False'
            computer_answer = (round(computer_answer))
            if is_int == 'True':
                user_answer = int(user_answer)
                if user_answer == computer_answer:
                    print('\nYour answer was correct! ',user_nickname,'+1 Point!\n')
                    score = score + 1
                    #adds score to both the session score and the question bunch score
                    score_this_bunch = score_this_bunch + 1
                    #bunch refers to a batch of 10 questions the computer generates for the user
                else:
                    print('\nYour answer was wroung the correct answer was: ',computer_answer,' Better luck next time',user_nickname)
                    total_quesions = total_questions + 1
                    #tells the user their answer was wroung and informs them of the corecct answer while nor adding or deducting...
                    #points from them but still stating the question has being wroung for the user to see at the end of that question bunch
            else:
                print('\nYou did not input an interger into the progarm (defulting to wroung answer)')
                print('\nYour answer was wroung the correct answer was: ',computer_answer,' Better luck next time',user_nickname)
                total_quesions = total_questions + 1
            total_questions = total_questions + 1
            questions_in_bunch = questions_in_bunch + 1
            percentage = score_this_bunch / 10
            precentage = percentage * 100
        #calulates the user's percentage for the last 10 questions and tells the user that as well as their score over the same 10 questions
    print('Weldone you have compleated 10 questions out of these 10 you got:\n',score_this_bunch,' correct\n That means a percentage of: ',percentage*100,'% correct')
    valdation_loop_variable = 'Not Valid'
    while validation_loop_variable == 'Not Valid':
            print('Would you like to quit now to see your results for this whole session?')
            quit_yn = input('Please answer in the format (Y/N): ')
            #asks the user if they whant to end their session of the program
            if quit_yn == 'Y':
                percentage = score / total_questions
                percentage = precentage
                #gives the user their percentage for this whole instance that the program has beem ran
                print('\nDuring this whole session you did a total of: ',total_questions,' questions.\nAnd a total of: ',score,' were correct.\nThat leaves you with a percentage of: ',percentage,'% correct.\n')
                total_questions_file_read = open('total_questions.txt','rt')
                total_questions_all_time =  total_questions_file_read.readline()
                total_questions_all_time = int(total_questions_all_time)
                total_questions = total_questions + total_questions_all_time
                #calculates then displays the total questions ever done using this program by fetching data from a .txt file in the game directory
                print('Out of all the time you have been using this program you have compeated:\nA total of: ',total_questions,' questions!\n')
                total_score_file_read = open('total_score.txt','rt')
                score_all_time = total_score_file_read.readline()
                score_all_time = int(score_all_time)
                score = score + score_all_time
                print('And a total of: ',score,' were correct.\n')
                #does the same as the last comment but this time fore score
                percentage = score / total_questions
                percentage = percentage * 100
                print('That makes for an all time percentage of: ',percentage,'% correct.\n')
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
                print('Your score and questions done have been sucessfully saved!')
                #tells the user they have been saved then exits the loop
                validation_loop_variable = 'Valid'
            elif quit_yn == 'N':
                validation_loop_variable = 'Valid'
                print('Thank you for choosing to continute to play!\n')
            else:
                print('Please use the (Y/N) format for your answer')
                validation_loop_variable = 'Not Valid'
print('The progarm has finsished running.')
input('Press enter to exit')
#uses an input so the program waits before closing to give the user time to acknowlege the messages that have been sent before closing
exit()
