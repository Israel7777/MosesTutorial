import csv
import numpy as np 



def Binarize(): 
    data = list(csv.reader(open('data/iris.csv')))
    numRow = len(data)
    numCol = len(data[0])
    newData = [ [ None for y in range( 13 ) ] for x in range( numRow) ]
    for x in xrange(0,numRow):
    	for y in xrange(0,numRow):
    		if y == 0:
    			if float(data[x][y]) <= 5.5:
	    			newData[x][0] = 1
	    			newData[x][1] = 0
	    			newData[x][2] = 0
	    		elif 5.5 < float(data[x][y]) < 6.7:
	    			newData[x][0] = 0
	    			newData[x][1] = 1
	    			newData[x][2] = 0
	    		elif float(data[x][y]) >=6.7:
	    			newData[x][0] = 0
	    			newData[x][1] = 0
	    			newData[x][2] = 1
    		elif y == 1:	
	    		if float(data[x][y]) <= 2.8:
	    			newData[x][3] = 1
	    			newData[x][4] = 0
	    			newData[x][5] = 0
	    		elif 2.8 < float(data[x][y]) < 3.6:
	    			newData[x][3] = 0
	    			newData[x][4] = 1	    			
	    			newData[x][5] = 0	    			
	    		elif float(data[x][y])>=3.6:
	    			newData[x][3] = 0	    			
	    			newData[x][4] = 0	    			
	    			newData[x][5] = 1
	    			
	    	elif y == 2:	
	    		if float(data[x][y]) <= 2.97:
	    			newData[x][6] = 1
	    			newData[x][7] = 0
	    			newData[x][8] = 0	    			
	    		elif 2.97 < float(data[x][y]) < 4.94:
	    			newData[x][6] = 0 			
	    			newData[x][7] = 1
	    			newData[x][8] = 0
	    		elif float(data[x][y])>=4.94:
	    			newData[x][6] = 0
	    			newData[x][7] = 0
	    			newData[x][8] = 1
	    	elif y == 3:	
	    		if float(data[x][y]) <= 0.9:
	    			newData[x][9] = 1
	    			newData[x][10] = 0
	    			newData[x][11] = 0	    			
	    		elif 0.9 < float(data[x][y]) < 1.7:
	    			newData[x][9] = 0
	    			newData[x][10] = 1
	    			newData[x][11] = 0	    			
	    		elif float(data[x][y])>=1.7:
	    			newData[x][9] = 0	    			
	    			newData[x][10] = 0	    			
	    			newData[x][11] = 1	    			
	    	elif y == 4:
	    		newData[x][12]=0	    			
	    		
	    			

	    		


    writer = csv.writer(open("data/iris_binarized.csv", 'w'))
    writer.writerows(newData)

def devideBin():
	data = list(csv.reader(open('data/iris_binarized.csv')))
	numRow = len(data)
	numCol = len(data[0])
	newData_for_S  = [ [ None for y in range( 13 ) ] for x in range( numRow/3) ]
	newData_for_ve  = [ [ None for y in range( 13 ) ] for x in range( numRow/3) ]
	newData_for_vi  = [ [ None for y in range( 13 ) ] for x in range( numRow/3) ]
	for x in xrange(0,numRow):
		for y in xrange(0,numCol):
			if x <50:
				if y == (numCol-1):
					newData_for_S[x][y]=1 
				else:
					newData_for_S[x][y]=data[x][y]
				
			elif x >=50 and x <100:
				if y == (numCol-1):
					newData_for_ve[x-50][y]= 1 
				else:
					newData_for_ve[x-50][y]=data[x][y]
				
			elif x >= 100:
				if y == (numCol-1):
					newData_for_vi[x-100][y]= 1 
				else:
					newData_for_vi[x-100][y]=data[x][y]

	writer = csv.writer(open("data/setosa_binarized.csv", 'w'))
	writer.writerows(newData_for_S)

	writer2 = csv.writer(open("data/versicolor_binarized.csv", 'w'))
	writer2.writerows(newData_for_ve)

	writer3 = csv.writer(open("data/virginica_binarized.csv", 'w'))
	writer3.writerows(newData_for_vi)

			
def classify():
	data = list(csv.reader(open('data/setosa_binarized.csv')))
	data2 = list(csv.reader(open('data/versicolor_binarized.csv')))
	data3 = list(csv.reader(open('data/virginica_binarized.csv')))
	item  =[20,34,30,28,32,26,0,5,4,15,24,45,19,33,47,46,13]
	item2 =[10,12,27,9,43,19,6,31,3,46,18,21,24,44,11,14,35]
	#item3 =[27,31,4,48,32,13,46,24,45,20,26,44,38,34,49,5,12]
	item3 =[49,45,44,42,41,40,38,36,29,20,17,15,10,7,4,2,0]
	

	#-------------------------------------------------------------------
	newData_for_S_test  = [ None for x in range( len(item)) ]
	newData_for_S_train_val  = [ None for x in range(len(data)-len(item)) ]
	Count = 0
	Countx = 0
	for x in xrange(0,len(data)):
		if x in item:
			newData_for_S_test[Count] = data[x]
			Count = Count + 1
		if x not in  item:
			newData_for_S_train_val[Countx] = data[x]
			Countx = Countx + 1

		

	newData_for_S_test2  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_S_test)) ]

	for x in xrange(0,len(newData_for_S_test2)):
		for y in xrange(0,len(newData_for_S_test2[2])):
			if y == (len(newData_for_S_test)-1):
				pass
			else:
				newData_for_S_test2[x][y]=newData_for_S_test[x][y]

	newData_for_S_train  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_S_train_val)-7) ]
	newData_for_S_Val  = [ [ None for y in range( 12 ) ] for x in range(7) ]
	Countr = 0
	Countc = 0
	for x in xrange(0,len(newData_for_S_train_val)):
		for y in xrange(0,len(newData_for_S_train_val[x])):
			if x < 26:
				newData_for_S_train[x]=newData_for_S_train_val[x]
			else:
				if y == len(newData_for_S_train_val[x])-1:
					pass
				else:
					newData_for_S_Val[x-26][y]=newData_for_S_train_val[x][y]
					
					
		
	writer2 = csv.writer(open("data/setosa_test.csv", 'w'))
	writer2.writerows(newData_for_S_test2)

	writer3 = csv.writer(open("data/setosa_train.csv", 'w'))
	writer3.writerows(newData_for_S_train)

	writer4 = csv.writer(open("data/setosa_val.csv", 'w'))
	writer4.writerows(newData_for_S_Val)


	#------------------------------------------------------
	newData_for_ve_test  = [ None for x in range( len(item2)) ]
	newData_for_ve_train_val  = [ None for x in range(len(data2)-len(item2)) ]
	Count = 0
	Countx = 0
	for x in xrange(0,len(data2)):
		if x in item2:
			newData_for_ve_test[Count] = data2[x]
			Count = Count + 1
		if x not in  item2:
			newData_for_ve_train_val[Countx] = data2[x]
			Countx = Countx + 1

	newData_for_ve_test2  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_ve_test)) ]

	for x in xrange(0,len(newData_for_ve_test2)):
		for y in xrange(0,len(newData_for_ve_test2[2])):
			if y == (len(newData_for_ve_test)-1):
				pass
			else:
				newData_for_ve_test2[x][y]=newData_for_ve_test[x][y]

	newData_for_ve_train  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_ve_train_val)-7) ]
	newData_for_ve_Val  = [ [ None for y in range( 12 ) ] for x in range(7) ]
	Countr = 0
	Countc = 0
	for x in xrange(0,len(newData_for_ve_train_val)):
		for y in xrange(0,len(newData_for_ve_train_val[x])):
			if x < 26:
				newData_for_ve_train[x]=newData_for_ve_train_val[x]
			else:
				if y == len(newData_for_ve_train_val[x])-1:
					pass
				else:
					newData_for_ve_Val[x-26][y]=newData_for_ve_train_val[x][y]
					
					
		
	writer5 = csv.writer(open("data/versicolor_test.csv", 'w'))
	writer5.writerows(newData_for_ve_test2)

	writer6 = csv.writer(open("data/versicolor_train.csv", 'w'))
	writer6.writerows(newData_for_ve_train)

	writer7 = csv.writer(open("data/versicolor_val.csv", 'w'))
	writer7.writerows(newData_for_ve_Val)

	#------------------------------------------------------
	newData_for_vi_test  = [ None for x in range( len(item3)) ]
	newData_for_vi_train_val  = [ None for x in range(len(data3)-len(item3)) ]
	Count = 0
	Countx = 0
	for x in xrange(0,len(data3)):
		if x in item3:
			newData_for_vi_test[Count] = data2[x]
			Count = Count + 1
		if x not in  item3:
			newData_for_vi_train_val[Countx] = data2[x]
			Countx = Countx + 1

	newData_for_vi_test2  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_vi_test)) ]

	for x in xrange(0,len(newData_for_vi_test2)):
		for y in xrange(0,len(newData_for_vi_test2[2])):
			if y == (len(newData_for_vi_test)-1):
				pass
			else:
				newData_for_vi_test2[x][y]=newData_for_vi_test[x][y]

	newData_for_vi_train  = [ [ None for y in range( 12 ) ] for x in range( len(newData_for_vi_train_val)-7) ]
	newData_for_vi_Val  = [ [ None for y in range( 12 ) ] for x in range(7) ]
	Countr = 0
	Countc = 0
	for x in xrange(0,len(newData_for_vi_train_val)):
		for y in xrange(0,len(newData_for_vi_train_val[x])):
			if x < 26:
				newData_for_vi_train[x]=newData_for_vi_train_val[x]
			else:
				if y == len(newData_for_vi_train_val[x])-1:
					pass
				else:
					newData_for_vi_Val[x-26][y]=newData_for_vi_train_val[x][y]
					
					
		
	writer8 = csv.writer(open("data/virginica_test.csv", 'w'))
	writer8.writerows(newData_for_vi_test2)

	writer9 = csv.writer(open("data/virginica_train.csv", 'w'))
	writer9.writerows(newData_for_vi_train)

	writer10 = csv.writer(open("data/virginica_val.csv", 'w'))
	writer10.writerows(newData_for_vi_Val)

'''=======================================
Finished making Validation File
=======================================
'''


def multiplex():
	data = list(csv.reader(open('data/setosa_train.csv')))
	data2 = list(csv.reader(open('data/versicolor_train.csv')))
	data3 = list(csv.reader(open('data/virginica_train.csv')))
#-------------------------------------------------------------------------
	newData_for_s_train2  = [ [ None for y in range( 13 ) ] for x in range( len(data))]
	for x in xrange(0,len(data)):
		for y in xrange(0,len(data[x])):
			if y == (len(data[x])-1):
				newData_for_s_train2[x][y] = 0
			else :
				newData_for_s_train2[x][y] = data[x][y]

	writer8 = csv.writer(open("data/setosa_train2.csv", 'w'))
	writer8.writerows(newData_for_s_train2)

#------------------------------------------------------------------------------------
	
	newData_for_ve_train2  = [ [ None for y in range( 13 ) ] for x in range( len(data2))]
	for x in xrange(0,len(data2)):
		for y in xrange(0,len(data2[x])):
			if y == (len(data2[x])-1):
				newData_for_ve_train2[x][y] = 0
			else :
				newData_for_ve_train2[x][y] = data2[x][y]

	writer9 = csv.writer(open("data/versicolor_train2.csv", 'w'))
	writer9.writerows(newData_for_ve_train2)


#------------------------------------------------------------------------------------

	newData_for_vi_train2  = [ [ None for y in range( 13 ) ] for x in range( len(data3))]
	for x in xrange(0,len(data3)):
		for y in xrange(0,len(data3[x])):
			if y == (len(data3[x])-1):
				newData_for_vi_train2[x][y] = 0
			else :
				newData_for_vi_train2[x][y] = data3[x][y]

	writer9 = csv.writer(open("data/virginica_train2.csv", 'w'))
	writer9.writerows(newData_for_vi_train2)

	data_ = list(csv.reader(open('data/setosa_train2.csv')))
	data2_ = list(csv.reader(open('data/versicolor_train2.csv')))
	data3_ = list(csv.reader(open('data/virginica_train2.csv')))

#==========================================================================================

	header = [['SL','SL2','SL3','SW1','SW2','SW3','PL1','PL2','PL3','PW1','PW2','PW3','CLASS']]

	writer_1 = csv.writer(open("data/Iris-setosa_training.csv", 'w'))
	writer_1.writerows(header)
	writer_1.writerows(data)
	writer_1.writerows(newData_for_ve_train2)
	writer_1.writerows(newData_for_vi_train2)

	writer_2 = csv.writer(open("data/Iris-versicolor_training.csv", 'w'))
	writer_2.writerows(header)
	writer_2.writerows(newData_for_s_train2)
	writer_2.writerows(data2)
	writer_2.writerows(newData_for_vi_train2)

	writer_3 = csv.writer(open("data/Iris-virginica_training.csv", 'w'))
	writer_3.writerows(header)
	writer_3.writerows(newData_for_s_train2)
	writer_3.writerows(newData_for_ve_train2)
	writer_3.writerows(data3)

	_data_ = list(csv.reader(open('data/setosa_test.csv')))
	_data2_ = list(csv.reader(open('data/versicolor_test.csv')))
	_data3_ = list(csv.reader(open('data/virginica_test.csv')))


	writer_4 = csv.writer(open("data/finalTest.csv", 'w'))
	writer_4.writerows(_data_)
	writer_4.writerows(_data2_)
	writer_4.writerows(_data3_)

	t=[1]
	f=[0]
	writer_6 = csv.writer(open("data/finalTest_S_Out.csv", 'w'))
	for i in range(0,len(_data_)):
		writer_6.writerow(t)
	for i in range(0,len(_data2_)):
		writer_6.writerow(f)
	for i in range(0,len(_data3_)):
		writer_6.writerow(f)

	writer_7 = csv.writer(open("data/finalTest_Ve_Out.csv", 'w'))
	for i in range(0,len(_data_)):
		writer_7.writerow(f)
	for i in range(0,len(_data2_)):
		writer_7.writerow(t)
	for i in range(0,len(_data3_)):
		writer_7.writerow(f)

	writer_8 = csv.writer(open("data/finalTest_Vi_Out.csv", 'w'))
	for i in range(0,len(_data_)):
		writer_8.writerow(f)
	for i in range(0,len(_data2_)):
		writer_8.writerow(f)
	for i in range(0,len(_data3_)):
		writer_8.writerow(t)



	_data1_ = list(csv.reader(open('data/setosa_val.csv')))
	_data12_ = list(csv.reader(open('data/versicolor_val.csv')))
	_data13_ = list(csv.reader(open('data/virginica_val.csv')))	

	writer_5 = csv.writer(open("data/finalVal.csv", 'w'))
	writer_5.writerows(_data1_)
	writer_5.writerows(_data12_)
	writer_5.writerows(_data13_)

'''	
===================================================================traing Data Done 
'''


Binarize()
devideBin()
classify()
multiplex()

print "All Task Related to Binarization and test_training_and_validation file production Complete \n"