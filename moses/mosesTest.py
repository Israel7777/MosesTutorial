#! /usr/bin/env python



from opencog.pymoses import moses
import csv

'''
=============================================
 Importing Data                            ||
=============================================
'''
train_data_setosa = list(csv.reader(open('data/Iris-setosa_training.csv')))
val_data_setosa = list(csv.reader(open('data/setosa_val.csv')))
train_data_versicolor = list(csv.reader(open('data/Iris-versicolor_training.csv')))
val_data_versicolor = list(csv.reader(open('data/versicolor_val.csv')))
train_data_virginica = list(csv.reader(open('data/Iris-virginica_training.csv')))
val_data_virginica = list(csv.reader(open('data/virginica_val.csv')))

val_data2 = val_data_versicolor
val_data = val_data_setosa
val_data3 = val_data_virginica

test_S_ve_vi = list(csv.reader(open('data/finalTest.csv')))



#-------------------------------
moses = moses()	
#-------------------------------
#getting Combos
output = moses.run(input=train_data_setosa,args="-W1 -u CLASS -m1000000 --result-count=20", python=False)
output2 = moses.run(input=train_data_versicolor,args="-W1 -u CLASS  -m1000000 --result-count=20", python=False)
output3 = moses.run(input=train_data_virginica,args="-W1 -u CLASS  -m1000000 --result-count=20", python=False)


Setota_Training_Score_File = open("israel/Setota_Training_Score_File.txt",'w')
versicolor_Training_Score_File = open("israel/versicolor_Training_Score_File.txt",'w')
virginica_Training_Score_File = open("israel/virginica_Training_Score_File.txt",'w')







Setota_Training_Score_File.write("Setota Training Score\n")
for i in xrange(0,len(output)):
	Setota_Training_Score_File.write("Combo {0} ".format(i) + "\t"+output[i].program + "\t\t Score {0}\n".format(output[i].score))

versicolor_Training_Score_File.write("versicolor Training Score\n")
for i in xrange(0,len(output2)):
	versicolor_Training_Score_File.write(("Combo {0} ".format(i) + "\t"+output2[i].program + "\t\t Score {0}\n".format(output[i].score)))

virginica_Training_Score_File.write("virginica Training Score \n")
for i in xrange(0,len(output3)):
	virginica_Training_Score_File.write(("Combo {0} ".format(i) + "\t"+output3[i].program + "\t\t Score {0}\n".format(output[i].score)))