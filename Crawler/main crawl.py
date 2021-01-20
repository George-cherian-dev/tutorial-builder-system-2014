import os
import MySQLdb
import sys
import traceback

def main():
	print( 'Number of arguments: {} arguments.'.format(len(sys.argv)))
	print ('Argument List: {}'.format(str(sys.argv)))
	print ('Argument List: {}'.format(sys.argv[1]))
	#cnx = mysql.connector.connect(user='root' ,password='root',  host='127.0.0.1', database='tutorial_clients')
	cnx=MySQLdb.connect(host="localhost",user="root",passwd="root",db="tutorial_clients")
	db = cnx.cursor() 
	s='SELECT term,score FROM terms WHERE sub_id = {}'.format(sys.argv[1])
	
	#cnx1 = mysql.connector.connect(user='root' ,password='root',  host='127.0.0.1', database='tutorial_clients')
	cnx1=MySQLdb.connect(host="localhost",user="root",passwd="root",db="tutorial_clients")
	db1 = cnx1.cursor() 
	s1='SELECT * FROM data WHERE sub_id= {} '.format(sys.argv[1])
	db1.execute(s1)
	#cnx2 = mysql.connector.connect(user='root' ,password='root',  host='127.0.0.1', database='tutorial_clients')
	cnx2=MySQLdb.connect(host="localhost",user="root",passwd="root",db="tutorial_clients")
	db2 = cnx2.cursor() 
			#print(a.encode("UTF-8"))
	for row1 in db1:
		file=open(row1[1])
		data=str(file.read())
		data=data.split()
		score=0
		for a in data:
			db.execute(s)
			for row in db:
				if a==row[0]:
					score=score+(1*row[1])
		print(score)
        
		tscore=350
		
		if score>tscore:
			s3='UPDATE data SET rel_score={} WHERE data_id={} '.format(score,row1[0])
			print s3
			#d3 = (row1[0],row1[1],row1[2],sys.argv[1],score,"N")
			try:
				#db2.execute(s3, d3)
				db2.execute(s3)
			#except mysql.connector.Error as err:
			except:
				traceback.print_exc()
			cnx2.commit()
		else:
			s3='DELETE FROM data WHERE data_id={}'.format(row1[0])
			#d3 = (row1[0],row1[1],row1[2],sys.argv[1],score,"N")
			try:
				#db2.execute(s3, d3)
				db2.execute(s3)
			#except mysql.connector.Error as err:
			except:
				traceback.print_exc()
			cnx2.commit()
			
	db.close()
	cnx.close()
	db1.close()
	cnx1.close()
	db2.close()
	cnx2.close()

if __name__ == "__main__": main()
