# -*- coding: utf-8 -*-

#This module is incomplete.Look at measures carefully and rewrite.
from classifier import tags_Predicted
from testing_format import tags_actual
from sklearn.metrics import f1_score, precision_score, recall_score
from toptags import Top_tags

yes = 0
FN = 0
total = 0
got_tags = 0

def mean(lis):
    return float(sum(lis))/len(lis)

confusion_matrix=[[0,0],[0,0]]

precision=[]
recall=[]
f1_score=[]

for j in range(0,100):
    for i in range(0,len(tags_actual)):
        if(j in tags_actual[i]):
            if(j in tags_Predicted[i]):
                confusion_matrix[0][0]+=1
            else:
                confusion_matrix[0][1]+=1
        else:
            if(j in tags_Predicted[i]):
                confusion_matrix[1][0]+=1
            else:
                confusion_matrix[1][1]+=1

    if(confusion_matrix[0][0]+confusion_matrix[1][0]==0):
        precision_for_label_j=0
    else:
        precision_for_label_j = confusion_matrix[0][0]/float(confusion_matrix[0][0]+confusion_matrix[1][0]) 
    if(confusion_matrix[0][0]+confusion_matrix[0][1]==0):
        recall_for_label_j=0
    else:
        recall_for_label_j = confusion_matrix[0][0]/float(confusion_matrix[0][0]+confusion_matrix[0][1])

    precision.append(precision_for_label_j)
    recall.append(recall_for_label_j)
    if(precision_for_label_j + recall_for_label_j==0):
        f1_score.append(0)
    else:
        f1_score.append(2*precision_for_label_j*recall_for_label_j/float(precision_for_label_j+recall_for_label_j))
    confusion_matrix=[[0,0],[0,0]]



for i in range(0,len(precision)):
    print Top_tags[i], precision[i], recall[i], f1_score[i]
    print "\n"


print mean(precision)
print mean(recall)
print mean(f1_score)

