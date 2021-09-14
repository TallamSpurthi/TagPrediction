from training_format import np_body,np_tags,maked_dict
from toptags import Top_tags
from testing_format import body_test,tags_actual

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn import svm

#print np_body
#print np_tags

classifier = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('tfidf', TfidfTransformer()),
    ('clf', OneVsRestClassifier(svm.SVC(probability=True)))])


classifier.fit(np_body, np_tags)
predicted = classifier.predict(body_test)

tags_Predicted = []
for item, labels in zip(body_test, predicted):
    output = []
    nums = []
    for x in labels:
	    output.append(Top_tags[x])
            nums.append(x)
    #print output
    tags_Predicted.append(nums)

#print tags_Predicted     
#print tags_actual
