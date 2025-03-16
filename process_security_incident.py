import csv #imports the csv

with open('security_incidents.csv', 'r', newline='') as file: #opens security_incidents.csv in read mode
    reader = csv.reader(file) #variable reader is csv data
    incidents = list(reader) #varible incidents formats variable reader(csv data) as a list(I think), using list class

status_column = "Status" #variable for new column
status_value = "Pending" #variable for new value that goes under a colum

header = incidents[0] + [status_column] #creates a new column in the header i think and takes name of status_colum

rows = [row + [status_value] for row in incidents[1:]] #creates new rows using value under variable attatched to status_value

with open('security_incidents_modified.csv', 'w', newline='') as outfile: #opens security_incidents_modified.csv in write mode and makes it the output area 
    writer = csv.writer(outfile) #variable writer is csv data 
    writer.writerow(header) #writes a new row according to variable header, which adds a column
    writer.writerows(rows) #writes new rows accoridng to variable rows, which add rows
        
        