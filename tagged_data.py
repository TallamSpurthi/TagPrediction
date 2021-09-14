### Get the rows from the data, which has atleast some of top tags ####

from toptags import Top_tags
import csv

#print Top_tags

out_file  = open('questions_tag.csv', "wb")
writer = csv.writer(out_file)

Count_tags_questions = {}
total_questions = 0
WITH_TAGS = []
TITLE = []
BODY = []
full_TEXT = []
with open('updated_60MB.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	row[3] = row[3].split('><')
    	if len(row[3]) == 0:
    		pass
    	elif len(row[3]) == 1:
    		row[3][0] = row[3][0][1:-1]
    	else:
    		row[3][0] = row[3][0][1:]
    		row[3][-1] = row[3][-1][:-1]

    	updated_tags = []
    	for y in row[3]:
        	for x in Top_tags:
        		if y == x:
        			updated_tags.append(y)
        			try:
        				Count_tags_questions[y] += 1
        			except:
        				Count_tags_questions[y] = 1
        			break

        row[3]=updated_tags
        if len(row[3])!= 0:
		#Just dont consider if zero tags are present.
        	#!print row[3]
            	WITH_TAGS.append(updated_tags)
		TITLE.append(row[1])
                BODY.append(row[2])
	        full_TEXT.append(row[1]+row[2])
		total_questions += 1
        	writer.writerow(row)         

#print total_questions
#print Count_tags_questions
#print len(Count_tags_questions)

f.close()
out_file.close()
