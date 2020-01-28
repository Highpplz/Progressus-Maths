
#Version 0.1.0 Alpha

#By editing this code you accept any dammages to your installation of this progarm or your computer or data held within it. If you are just inrested in reading this code try the notepad sample code as the progarm
#does nothing with it as it is just there to allow for risk free reading of the sorce code

import os
valid_input = 'false'
reset_stats_version_number = '0.1.1/1.0'
reset_stats_file = open('reset_stats_version.txt','w+')
last_reset_stats_version_ran = reset_stats_file.readline()
version_last_ran = open('version_last_ran.txt','rt')
version_last_ran = version_last_ran.readline()
if last_reset_stats_version_ran != reset_stats_version_number:
    if version_last_ran != 'never':
        print('Your version of the reset stats program is outdated please re-download the installer and fully reinstall the prograrm.')
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
    user_nicknames = open('user_nicknames.txt','wt')
    user_nicknames.close()
    no_reset_file_create = open('no_reset.txt','wt')
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
