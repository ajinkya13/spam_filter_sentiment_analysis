*******************************Naive Bayes Classifier***************************************************

SPAM
{
For Spam:
Precision: 0.951482479784
Recall: 0.972451790634
Fscore(Spam): 0.961852861035

For Ham:
Precision: 0.989919354839
Recall: 0.982
Fscore(Ham): 0.9859437751
}

Sentiment
{
For Neg:
Precision: 0.79146567718
Recall: 0.861818181818
Fscore(NEG): 0.825145067698

For Pos:
Precision: 0.848337028825
Recall: 0.772929292929
Fscore(POS): 0.8088794926
}

***************************************SVM*************************************************************

SPAM
{
For Spam:
Precision: 0.956810631229
Recall: 0.793388429752
Fscore(Spam): 0.867469879518

For Ham:
Precision: 0.929378531073
Recall: 0.987
Fscore(Ham): 0.957322987391
}


Sentiment
{
For Neg:
Precision: 0.864029666255
Recall: 0.847272727273
Fscore(NEG): 0.855569155447

For Pos:
Precision: 0.850178359096
Recall: 0.866666666667
Fscore(POS): 0.858343337335
}


***************************************MegaM*************************************************************

SPAM{
For Spam:
Precision: 0.947802197802
Recall: 0.95041322314
Fscore(SPAM): 0.949105914718

For Ham:
Precision: 0.981981981982
Recall: 0.981
Fscore(HAM): 0.981490745373
}


Sentiment
{
For Neg:
Precision: 0.858326429163
Recall: 0.837171717172
Fscore(NEG): 0.847617099611

For Pos:
Precision: 0.841088328076
Recall: 0.861818181818
Fscore(POS): 0.851327080423
}




In case of Naive Bayes classifier, the precision remained almost the same, while the Recall and Fscore reduced. This is because, when we took only 10% of the training data, the number of unknown words increased. As a result, the number of correct classifications decreased, and hence the recall decreased. However, in case of precision, along with the correct classification, the count of total classification also reduced, and hence, there was not much change.
As the recall reduced, the F-score also reduced.

In case of SVM, the Precision, Recall and F-Score remained almost the same.

In case of MegaM, the Precision, Recall and F-score reduced.
