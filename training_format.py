##Converting the data in csv format to numpy array to pass it to classifier.##

import numpy as np
import pandas as pd
from toptags import Top_tags
from tagged_data import WITH_TAGS,BODY,full_TEXT

###First row of Id,Body,tags is missing ####

#Raw_file = pd.read_csv("test_b.csv", usecols = [1,2])
#print list(Raw_tags["Body"])[2]
#tag =  list(Raw_file["Tags"])
#body = list(Raw_file["Body"])

#print np.array(tag)

#STARTED MAIN CODE!!!!!!

maked_dict = {}

inc = 0
for h in Top_tags:
	maked_dict[h] = inc
	inc += 1

#print maked_dict
#print len(maked_dict)

final_tag = []
for f in WITH_TAGS:
	new_each = []
	for ev in f:
		try:
			maked_dict[ev]
			new_each.append(maked_dict[ev])
		except:
			pass
	#print "Neww_each : " 
	#print new_each
	final_tag.append(new_each)

#print final_tag
#print len(BODY)

hp = len(BODY)*80/100
#print hp
#Make Training data as 80% and Testing as 20%.... So x = len(BODY)*80/100 !!
np_body =  np.array(full_TEXT[:hp])
np_tags = np.array(final_tag[:hp])

