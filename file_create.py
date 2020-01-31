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
from zipfile import ZipFile
#create a zipfile object and load zip in it
with ZipFile('do_not_unzip_me.zip', 'r') as zipObj:
    #extract all the contents of zip file into current directory
    zipObj.extractall()
reset_stats_file = open('reset_stats_version.txt','w+')
reset_stats_file.write('never')
reset_stats_file.close()
lisense_file_read = open('lisense_read.txt','w+')
lisense_file_read.write('No')
lisense_file_read.close()
credits_file_read = open('credits_read.txt','w+')
credits_file_read.write('No')
credits_file_read.close()
disclaimer_read_file = open('disclaimer_read.txt','w+')
disclaimer_read_file.write('No')
disclaimer_read_file.close()
version_last_ran_file_read = open('version_last_ran.txt','w+')
version_last_ran_file_read.write('never')
version_last_ran_file_read.close()
changelog_latest_read = open('changelog_latest_read.txt','w+')
changelog_latest_read.write('No')
changelog_latest_read.close()
bugfinders_read_file = open('bugfinders_read.txt','w+')
bugfinders_read_file.write('No')
bugfinders_read_file.close()
number_of_needed_lines_file = open('number_of_needed_lines.txt','w+')
number_of_needed_lines_file.write(15)
number_of_needed_lines_file.close()
logon_data_file = open('logon_data.txt','w+')
logon_data_file.write('#header')
logon_data_file.close()
exit()
