# import csv

# body_test = []
# tags_actual = []
# with open('TEST.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#     	body_test.append(row[1])
#     	tags_actual.append(row[2])

# f.close()

from training_format import final_tag,hp
from tagged_data import BODY,full_TEXT

body_test = full_TEXT[hp:]
tags_actual = final_tag[hp:]

#print tags_actual
