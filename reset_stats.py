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
import os
valid_input = 'false'
reset_stats_version_number = '0.2.0.A/1.0'
reset_stats_version_number_split = reset_stats_version_number.split("/")
reset_stats_file = open('reset_stats_version.txt','w+')
last_reset_stats_version_ran = reset_stats_file.readline()
version_last_ran_file = open('version_last_ran.txt','rt')
version_last_ran = version_last_ran_file.readline()
version_last_ran_file.close()
if last_reset_stats_version_ran != reset_stats_version_number_split[0]:
    if version_last_ran != 'never':
        print('Your version of the reset stats program is of a different version to the main game please re-download the installer and/or fully reinstall the prograrm.')
        input('Press enter to contininute')
reset_stats_file.write(reset_stats_version_number)
reset_stats_file.close()
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
    print('Install compleate!')
if version_last_ran == 'never':
    stat_update()
    stat_update_YN = 'Y'
else:
    stat_update_YN = 'N'
no_reset_file_read = open('no_reset.txt','rt')
no_reset = no_reset_file_read.readline()
if no_reset == 'N' and version_last_ran != 'never':
    print('Would you like to reset your stats for the game?')
    while valid_input == 'false':
        stat_update_YN = input('(Y/N) :')
        if stat_update_YN == 'Y':
            stat_update()
            valid_input = 'true'
        elif stat_update_YN == 'N':
            valid_input = 'true'
        else:
            valid_input = 'false'
            print('\nPlease answer in the Y/N format.\n')
valid_input = 'false'
while valid_input =='false' and stat_update_YN == 'N':
    print('Would you like to stop seeing this message? (If you chose this you will not be able to reset your stats without using the "reset_stats.bat")')
    stop_seeing = input('(Y/N) :')
    if stop_seeing == 'N':
        valid_input = 'true'
    elif stop_seeing == 'Y':
        no_reset_file = open('no_reset.txt','wt')
        no_reset_file.write('Y')
        no_reset_file.close()
        valid_input = 'true'
    else:
        valid_input = 'false'
        print('\nPlease answer in the Y/N format.\n')
exit()
