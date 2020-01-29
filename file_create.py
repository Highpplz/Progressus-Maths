
#Version 0.2.0 Alpha

#By editing this code you accept any dammages to your installation of this progarm or your computer or data held within it. If you are just inrested in reading this code try the notepad sample code as the progarm
#does nothing with it as it is just there to allow for risk free reading of the sorce code

import os
from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('do_not_unzip_me.zip', 'r') as zipObj:
    #extract all the contents of zip file into current directory
    zipObj.extractall()
disclaimer_file_read = open('disclaimer_read.txt','w+')
disclaimer_file_read.close()
lisense_file_read = open('lisense_read.txt','w+')
lisense_file_read.close()
credits_file_read = open('credits_read.txt','w+')
credits_file_read.close()
disclaimer_read_file = open('disclaimer_read.txt','w+')
disclaimer_read_file.close()
version_last_ran_file_read = open('version_last_ran.txt','w+')
version_last_ran_file_read.write('never')
version_last_ran_file_read.close()
changelog_latest_read = open('changelog_latest_read.txt','w+')
changelog_latest_read.close()
bugfinders_read_file = open('bugfinders_read.txt','w+')
bugfinders_read_file.close()
number_of_needed_lines_file = open('number_of_needed_lines.txt','w+')
number_of_needed_lines_file.write(15)
number_of_needed_lines_file.close()
logon_data_file = open('logon_data.txt','w+')
logon_data_file.write('#nothing here')
logon_data_file.close()
exit()
