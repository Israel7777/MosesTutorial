#! /usr/bin/env python


from bin import *
from opencog.pymoses import moses
import csv
import datetime


'''
=============================================
 Importing Data                            ||
=============================================
'''
train_data_setosa = list(csv.reader(open('data/Iris-setosa_training.csv')))
val_data_setosa = list(csv.reader(open('data/finalVal.csv')))
setota_Test_result = list(csv.reader(open('data/finalTest_S_Out.csv')))
train_data_versicolor = list(csv.reader(open('data/Iris-versicolor_training.csv')))
val_data_versicolor = list(csv.reader(open('data/finalVal.csv')))
ve_Test_result = list(csv.reader(open('data/finalTest_Ve_Out.csv')))
train_data_virginica = list(csv.reader(open('data/Iris-virginica_training.csv')))
val_data_virginica = list(csv.reader(open('data/finalVal.csv')))
vi_Test_result = list(csv.reader(open('data/finalTest_Vi_Out.csv')))


val_data2 = val_data_versicolor
val_data = val_data_setosa
val_data3 = val_data_virginica

test_S_ve_vi = list(csv.reader(open('data/finalTest.csv')))



#-------------------------------
moses = moses()	
today = datetime.date.today()
#-------------------------------
#getting Combos
output = moses.run(input=train_data_setosa,args="-W1 -u CLASS -m1000000 --result-count=20", python=True)
output2 = moses.run(input=train_data_versicolor,args="-W1 -u CLASS  -m1000000 --result-count=20", python=True)
output3 = moses.run(input=train_data_virginica,args="-W1 -u CLASS  -m1000000 --result-count=20", python=True)


'''
======================================================
 Validation Testing                                 ||
======================================================
'''
newData  = [ [ None for y in range( 21) ] for x in range( 20) ]
newData2  = [ [ None for y in range( 21) ] for x in range( 20) ]
newData3 = [ [ None for y in range( 21) ] for x in range( 20) ]

# setota Validation -----------------------------
print "--->\nTesting model on data:\n"
for y in xrange(0,len(output)):
#	print "Combo {0}".format(y)
	for x in xrange(0,len(val_data)):
		model = output[y].eval
		newData[y][x] = model(val_data[x])
#		print model(val_data[x])
#	print "\n"
	
# versicolor Validation --------------------------
print "--->\nTesting model on data:\n"
for y in xrange(0,len(output2)):
#	print "Combo {0}".format(y)
	for x in xrange(0,len(val_data2)):
		model = output2[y].eval
		newData2[y][x] = model(val_data2[x])
#		print model(val_data2[x])
#	print "\n"



# virginica Validation ---------------------------
print "--->\nTesting model on data:\n"
for y in xrange(0,len(output3)):
#	print "Combo {0}".format(y)
	for x in xrange(0,len(val_data3)):
		model = output3[y].eval
		newData3[y][x] = model(val_data2[x])
#		print model(val_data3[x])
#	print "\n"

'''
======================================================
The Next Section Scores The 10 Combos based on the  ||
validation data                                     ||
======================================================
'''

score  = [ None for y in range( 20) ] 
score_num = 0
for x in xrange(0,len(newData)):
	for y in xrange(0,len(newData[x])):
		if newData[x][y] == False or newData[x][y]=='0':
			score_num = score_num
		elif newData[x][y] == True or newData[x][y] == '1':
			score_num = score_num +1
	score[x] = score_num
	score_num = 0	
s = sorted(range(len(score)),key=lambda k:score[k])
s.reverse()

#--------------------------------------------------------

score2  = [ None for y in range( 20) ] 
score_num2 = 0
for x in xrange(0,len(newData2)):
	for y in xrange(0,len(newData2[x])):
		if newData2[x][y] == False or newData2[x][y]=='0':
			score_num2 = score_num2
		elif newData2[x][y] == True or newData2[x][y] == '1':
			score_num2 = score_num2 +1
	score2[x] = score_num2
	score_num2 = 0
s2 = sorted(range(len(score2)),key=lambda k:score2[k])
s2.reverse()

#----------------------------------------------------------

score3  = [ None for y in range( 20) ] 
score_num3 = 0
for x in xrange(0,len(newData3)):
	for y in xrange(0,len(newData3[x])):
		if newData3[x][y] == False or newData3[x][y]=='0':
			score_num3 = score_num3
		elif newData3[x][y] == True or newData3[x][y] == '1':
			score_num3 = score_num3 +1
	score3[x] = score_num3
	score_num3 = 0
s3 = sorted(range(len(score3)),key=lambda k:score3[k])
s3.reverse()
	


# Testing
print "{0}\n\n{1}\n{2}\n".format(newData,s,score)
print "{0}\n\n{1}\n".format(newData2,s2)
print "{0}\n\n{1}\n".format(newData3,s3)



'''
=====================================================
Now we have the Best to Worest Combo List          ||
=====================================================
'''
best_combo_list1 = s
best_combo_list2 = s2
best_combo_list3 = s3


'''
=====================================================
Testing on the actual Testing data                ||
=====================================================
'''

# setota Testing -------------------------------------
setota_TP = 0
setota_FN = 0
setota_FP = 0
setota_TN = 0
Setota_Test_File = open("israel/Setota_Testing_File.txt",'w')
Setota_Evaluation_File = open("israel/Setota_Evaluation_File.txt",'w')
Setota_Evaluation_File.write("Date: {0}\nThis Is The Evaluation Data For the Setota Flower Class\n".format(today))
Setota_Test_File.write("This Is The Test Data For the Setota Flower Class \n")
print "----------------------------->"
print "setota : Combo {0} is the Best So Far \n \tand The Scoring Oreder is {1}\n".format(best_combo_list1[0],best_combo_list1)
Setota_Test_File.write("----------------------------->\n setota : Combo {0} is the Best So Far \n \tand The Scoring Oreder is {1}\n".format(best_combo_list1[0],best_combo_list1))
for x in xrange(0,len(test_S_ve_vi)):
	model = output[best_combo_list1[0]].eval
	#print model(test_data_setosa[x])
	print model(test_S_ve_vi[x])
	Setota_Test_File.write("{0}\n".format(model(test_S_ve_vi[x])))
	y = model(test_S_ve_vi[x])
	if (y == True or y == '1') and setota_Test_result[x][0] == '1':
		setota_TP += 1
	elif (y ==  False or y == '0') and setota_Test_result[x][0] == '1':
		setota_FN +=1
	elif (y == True or y == '1') and setota_Test_result[x][0] == '0':
		setota_FP += 1
	elif (y == False or y == '0') and setota_Test_result[x][0] == '0':
		setota_TN +=1


	
Setota_Evaluation_File.write("\n-----------------------------------------------------------\n")
Setota_Evaluation_File.write("\tTP = {0} , FN = {1}\n".format(setota_TP,setota_FN))
Setota_Evaluation_File.write("\tFP = {0} , TN = {1}\n".format(setota_FP,setota_TN))
Setota_Evaluation_File.write("\n-----------------------------------------------------------\n")
Setota_Evaluation_File.write("\nTP Ratio = {0} : {1}\n".format(setota_TP,setota_TP+setota_FN))
Setota_Evaluation_File.write("FP Ratio = {0} : {1}\n".format(setota_FP,setota_FP+setota_TN))
Setota_Evaluation_File.write("TN Ratio = {0} : {1}\n".format(setota_TN,setota_TN+setota_FP))
Setota_Evaluation_File.write("FN Ratio = {0} : {1}\n\n".format(setota_FN,setota_FN+setota_TP))

# versicolor Testing------------------------------------
print "----------------------------->"

versicolor_TP = 0
versicolor_FN = 0
versicolor_FP = 0
versicolor_TN = 0
versicolor_Test_File = open("israel/versicolor_Testing_File.txt",'w')
versicolor_Evaluation_File = open("israel/versicolor_Evaluation_File.txt",'w')
versicolor_Test_File.write("This Is The Test Data For the versicolor Flower Class \n")
versicolor_Evaluation_File.write("Date: {0}\nThis Is The Evaluation Data For the versicolor Flower Class\n".format(today))
print "versicolor : Combo {0} is the Best So Far\n \tand The Scoring Oreder is {1}\n".format(best_combo_list2[0],best_combo_list2)
versicolor_Test_File.write("----------------------------->\n versicolor : Combo {0} is the Best So Far \n \tand The Scoring Oreder is {1}\n".format(best_combo_list2[0],best_combo_list2))
for x in xrange(0,len(test_S_ve_vi)):
	model = output2[best_combo_list2[0]].eval
	#print model(test_data_versicolor[x])
	print model(test_S_ve_vi[x])
	versicolor_Test_File.write("{0}\n".format(model(test_S_ve_vi[x])))
	y = model(test_S_ve_vi[x])
	num1=len(test_S_ve_vi)/3
	num2=num1*2
	if (y == True or y == '1') and ve_Test_result[x][0] == '1':
		versicolor_TP += 1
	elif (y ==  False or y == '0') and ve_Test_result[x][0] == '1':
		versicolor_FN +=1
	elif (y == True or y == '1') and ve_Test_result[x][0] == '0':
		versicolor_FP += 1
	elif (y == False or y == '0') and ve_Test_result[x][0] == '0':
		versicolor_TN +=1
	
versicolor_Evaluation_File.write("\n-----------------------------------------------------------\n")
versicolor_Evaluation_File.write("\tTP = {0} , FN = {1}\n".format(versicolor_TP,versicolor_FN))
versicolor_Evaluation_File.write("\tFP = {0} , TN = {1}\n".format(versicolor_FP,versicolor_TN))
versicolor_Evaluation_File.write("\n-----------------------------------------------------------\n")
versicolor_Evaluation_File.write("\nTP Ratio = {0} : {1}\n".format(versicolor_TP,versicolor_TP+versicolor_FN))
versicolor_Evaluation_File.write("FP Ratio = {0} : {1}\n".format(versicolor_FP,versicolor_FP+versicolor_TN))
versicolor_Evaluation_File.write("TN Ratio = {0} : {1}\n".format(versicolor_TN,versicolor_TN+versicolor_FP))
versicolor_Evaluation_File.write("FN Ratio = {0} : {1}\n\n".format(versicolor_FN,versicolor_FN+versicolor_TP))


# virginica Testing -------------------------------------

virginica_TP = 0
virginica_FN = 0
virginica_FP = 0
virginica_TN = 0
virginica_Test_File = open("israel/virginica_Testing_File.txt",'w')
virginica_Evaluation_File = open("israel/virginica_Evaluation_File.txt",'w')
virginica_Test_File.write("This Is The Test Data For the virginica Flower Class \n")
virginica_Evaluation_File.write("Date: {0}\nThis Is The Evaluation Data For the virginica Flower Class\n".format(today))
print "----------------------------->"
print "virginica : Combo {0} is the Best So Far\n \tand The Scoring Oreder is {1}\n".format(best_combo_list3[0],best_combo_list3)
virginica_Test_File.write("----------------------------->\n virginica: Combo {0} is the Best So Far \n \tand The Scoring Oreder is {1}\n".format(best_combo_list3[0],best_combo_list3))
for x in xrange(0,len(test_S_ve_vi)):
	model = output3[best_combo_list3[0]].eval
	#print model(test_data_versicolor[x])
	print model(test_S_ve_vi[x])
	virginica_Test_File.write("{0}\n".format(model(test_S_ve_vi[x])))
	y = model(test_S_ve_vi[x])
	num1=len(test_S_ve_vi)/3
	num2=num1*2
	if (y == True or y == '1') and vi_Test_result[x][0] == '1':
		virginica_TP += 1
	elif (y ==  False or y == '0') and vi_Test_result[x][0] == '1':
		virginica_FN +=1
	elif (y == True or y == '1') and vi_Test_result[x][0] == '0':
		virginica_FP += 1
	elif (y == False or y == '0') and vi_Test_result[x][0] == '0':
		virginica_TN +=1

	
			
virginica_Evaluation_File.write("\n-----------------------------------------------------------\n")
virginica_Evaluation_File.write("\tTP = {0} , FN = {1}\n".format(virginica_TP,virginica_FN))
virginica_Evaluation_File.write("\tFP = {0} , TN = {1}\n".format(virginica_FP,virginica_TN))
virginica_Evaluation_File.write("\n-----------------------------------------------------------\n")
virginica_Evaluation_File.write("\nTP Ratio = {0} : {1}\n".format(virginica_TP,virginica_TP+virginica_FN))
virginica_Evaluation_File.write("FP Ratio = {0} : {1}\n".format(virginica_FP,virginica_FP+virginica_TN))
virginica_Evaluation_File.write("TN Ratio = {0} : {1}\n".format(virginica_TN,virginica_TN+virginica_FP))
virginica_Evaluation_File.write("FN Ratio = {0} : {1}\n\n".format(virginica_FN,virginica_FN+virginica_TP))

print "-----------------------------------------------------------------------"

print "=============== Fianl Evaluation OutPut =========================="
'''============================
accuracy = (Tp+Tn)/all
percision = Tp/(Tp+Fp)
Recall = Tp/(Tp+Fn)
'''
Setota_Evaluation_File.write(">> Setota Best Combo Evaluation =====================\n")
Setota_Evaluation_File.write( "\tAccuracy  = {0:.2f} %\n".format(100*(float((setota_TP+setota_TN)/float(setota_TP+setota_TN+setota_FP+setota_FN)))))
Setota_Evaluation_File.write("\tPercision = {0:.2f} %\n".format(100*(float(setota_TP)/float((setota_TP+setota_FP)))))
Setota_Evaluation_File.write("\tRecall = {0:.2f} %\n ".format(100*(float(setota_TP)/float((setota_TP+setota_FN)))))

versicolor_Evaluation_File.write( ">> Versicolr Best Combo Evaluation =====================\n")
versicolor_Evaluation_File.write( "\tAccuracy  = {0:.2f} %\n".format(100*(float((versicolor_TP+versicolor_TN))/float(versicolor_TP+versicolor_TN+versicolor_FP+versicolor_FN))))
versicolor_Evaluation_File.write( "\tPercision = {0:.2f} %\n".format(100*(float(versicolor_TP)/float((versicolor_TP+versicolor_FP)))))
versicolor_Evaluation_File.write( "\tRecall = {0:.2f} %\n".format(100*(float(versicolor_TP)/float((versicolor_TP+versicolor_FN)))))


virginica_Evaluation_File.write( ">> virginica Best Combo Evaluation =====================\n")
virginica_Evaluation_File.write("\tAccuracy  = {0:.2f} %\n".format(100*(float((virginica_TP+virginica_TN)/float(virginica_TN+virginica_TP+versicolor_FN+versicolor_FP)))))
virginica_Evaluation_File.write( "\tPercision = {0:.2f} %\n".format(100*(float(virginica_TP)/float((virginica_TP+virginica_FP)))))
virginica_Evaluation_File.write( "\tRecall = {0:.2f}%\n".format(100*(float(virginica_TP)/float((virginica_TP+virginica_FN)))))
'''
setota_model = output[best_combo_list1[0]].eval
versicolor_model =output2[best_combo_list2[0]].eval
virginica_model =output3[best_combo_list3[0]].eval



print "setota >> {0}".format(setota_model([1,0,0,0,0,1,1,0,0,1,0,0]))

'''
#--------------------------------------------------------------------------------#
#------------------------------ Majority Voting ---------------------------------#
#--------------------------------------------------------------------------------#
data_this = [1,0,0,0,1,0,1,0,0,1,0,0]

countS = 0
for x in xrange(0,len(output)):
	setota_model = output[x].eval
	value = setota_model(data_this)
	if value == True or value == '1':
		countS = countS + 1
	else:
		pass

print countS 


countVe = 0
for x in xrange(0,len(output2)):
	versicolor_model = output3[x].eval
	value = versicolor_model(data_this)
	if value == True or value == '1':
		countVe = countVe + 1
	else:
		pass

print countVe 

countVi = 0
for x in xrange(0,len(output3)):
	virginica_model = output3[x].eval
	value = virginica_model(data_this)
	if value == True or value == '1':
		countVi = countVi + 1
	elif value == False or value == '0':
		pass

print countVi

this_array = [countS,countVe,countVi]
max_value =  this_array.index(max(this_array))

print "\nThis Is The Prediction Section\n"

if max_value == 0:
	print "\tthis Is Setosa Flower"
elif max_value == 1:
	print "\tthis Is versicolor Flower"
elif max_value == 2:
	print "\tthis Is virginica Flower"
else:
	print "\tSome Error Occured !"