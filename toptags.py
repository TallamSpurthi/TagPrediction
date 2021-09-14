import pandas as pd
import csv
import math

#Find out the column with names
colnames = ["Tags"]

#Raw_tags = pd.read_csv("StackExchange_40MB.csv", usecols = [2])
Raw_tags = pd.read_csv("updated_60MB.csv", usecols = [3])

List_Tags = list(Raw_tags["Tags"])
#print List_Tags

Tag_counts = {}
for i in List_Tags[:]:
	#print i
	try:
		if math.isnan(float(i)):
			#print "**"
			continue
	except:
		pass
	spt = i.split('><')
	
	# Notags. 
	if len(spt) == 0:
		pass

	#Only if 1 tag. 
	if len(spt) == 1:
		tagg = spt[0][1:-1]
		try: 
			Tag_counts[tagg] += 1
		except:
			Tag_counts[tagg] = 1

	#Multiple tags handled.
	else:
		tagg = spt[0][1:]
		try: 
			Tag_counts[tagg] += 1
		except:
			Tag_counts[tagg] = 1
		for x in spt[1:-1]:
			try: 
				Tag_counts[x] += 1
			except:
				Tag_counts[x] = 1

		tagg = spt[-1][:-1]
		try: 
			Tag_counts[tagg] += 1
		except:
			Tag_counts[tagg] = 1


#print Tag_counts

Top_tags = []
cnt = 0

#getting the dictionary in the decreasing order of the values.
for key, value in sorted(Tag_counts.iteritems(), key=lambda (k,v): (v,k),reverse = True):
	if cnt == 100:
		break
    	Top_tags.append(key)
    	#print "%s: %s" % (key, value)
    	cnt+= 1

#print Top_tags
