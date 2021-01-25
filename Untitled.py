# To check if the time in the log file is between the start time and the end time passed
def is_time_between(time,start, end):
    return start <= time <= end

import argparse
import os
import sys
import datetime
from urllib.request import urlopen


#to set the positional arguments for the application
parser = argparse.ArgumentParser(description = "Print the statistics of errors from a log file")
parser.add_argument('Path',
                    metavar='path',
                    type=str,
                    help='the path to the log file')
parser.add_argument('Start_time',
                       metavar='start time',
                       type=str,
                       help='start time for the requests')
parser.add_argument('End_time',
                       metavar='end time',
                       type=str,
                       help='start time for the requests')
parser.add_argument('Error_code',
                       metavar='error code',
                       type=str,
                       help='Error code for which the stats are required')

args = parser.parse_args()


st_time = datetime.datetime.strptime(args.Start_time, '%d/%b/%Y:%H:%M:%S') #Getting the start time as datetime
end_time = datetime.datetime.strptime(args.End_time, '%d/%b/%Y:%H:%M:%S')  #Getting the end time as datetime


errors = {}                                       #dictionary to hold the count of errors
file = urlopen(args.Path)          #Reads the content of URL in byteformat
lines = file.readlines()
for line in lines:
    line= line.decode("utf-8")
    i = line.index('[')
    time = line[i+1:i+21]                         #getting the time of the request from the string
    time = datetime.datetime.strptime(time, '%d/%b/%Y:%H:%M:%S') #converting the time to datetime format
    if is_time_between(time, st_time, end_time):  #if the time lies between the start and the end time passed
        l = line.split(" ")                       #parse the string on spaces to give a list of tokens
        if args.Error_code in l:                  #After parsing on spaces, the error code is at the 8th index
            if args.Error_code not in errors:
                errors[args.Error_code] = 1
            else:
                errors[args.Error_code] += 1   
        elif "200" in l:                          #Checking for the 200 responses
            if "200" not in errors:
                errors["200"] = 1
            else:
                errors["200"] += 1
        
        else:
            continue


print("The site has returned a total of "+str(errors['200'])+" 200 responses, and "+str(errors[args.Error_code])+" "+str(args.Error_code)+" responses, out of total "
		+str(len(lines))+" requests between time "+str(args.Start_time)+" and time "+str(args.End_time))
print("This is a "+str((errors[args.Error_code]/len(lines))*100)+"% "+str(args.Error_code)+" errors, and "+str((errors["200"]/len(lines))*100)+"% of 200 responses")
