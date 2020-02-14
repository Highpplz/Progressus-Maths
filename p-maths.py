
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
#imports random for the random question and operation selectors

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


def logon_system ():
    pass

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

GUI = Tk()
GUI.title('Progressus Maths')
window.state('zoomed')

welcome_message = Label(GUI,text = 'Welcome to Progressus Maths!')
welcome_message.pack(side = TOP)

question_entry = Label(GUI,text = question_as_string,'Also please remember to round your answer to the nearest whole number.')

answer_input = Entry(GUI)

GUI.mainloop()
