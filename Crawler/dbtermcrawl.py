
import sqlite3
import MySQLdb
import sys
import os

def insert(db, row, table,cnx):
    s= ("INSERT INTO {} (t1,sno) VALUES (%s, %s)".format(table))
    d = (row['t1'], row['sno'])
    print (d)
    print (s)
    db.execute(s, d)
    cnx.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from data1 where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row,cnx):
    db.execute('update data1 set sno = ? where t1 = ?', (row['sno'], row['t1']))
    cnx.commit()

def delete(db, t1,cnx):
    db.execute('delete from data1 where t1 = ?', (t1,))
    cnx.commit()

def disp_rows(db,table):
    s='select * from {}'.format(table)
    cursor = db.cursor()
    cursor.execute(s)
    for row in cursor:
      print('  {}: {}'.format(row[0], row[1]))

def isNotNum(s):
    try:
        float(s)
        return False
    except ValueError:
        return True
def isNotExist(t,sub):
    try:
        cnx5 = mysql.connector.connect(user='root' ,password='root',  host='127.0.0.1', database='tutorial_clients')
        db5 = cnx5.cursor()
        s5='SELECT * FROM terms WHERE term="{}" AND sub_id={}'.format(t,sub)
        db5.execute(s5)
        for row in db5:
           return False
        return True
    except ValueError:
        return True

def main():
    s= os.path.dirname(__file__)
    print(s)
    print( 'Number of arguments: {} arguments.'.format(len(sys.argv)))
    print ('Argument List: {}'.format((sys.argv)))
    print ('Subject Id: {}'.format(sys.argv[1]))
    cnx = MySQLdb.connect(user='root' ,password='root',  host='127.0.0.1', database='tutorial_clients')
    db = cnx.cursor()
	
    s='SELECT * FROM crawlable WHERE sub_id = {}'.format(sys.argv[1])
    db.execute(s)
    i=0
    term=list(range(100))
    count=list(range(100))
    print('hello1')
    for row in db:
        if i==0:
          print('hello2'+row[2])
		  file=open(row[2])
		  str=file.read()
          str=(str.lower()).split()
          str1=str
          x=len(str)
          print(x)
		  #finding number if terms excluding repeated words
          k=0
          for s in str:
           k1=0
           for s1 in str1:
             if k1<k:
              if s1==s:
                x=x-1
                k1=k
             k1=k1+1
           k=k+1
          print(x)
		  #finding number of terms excluding ignorable words
          f = open('C:\\Users\\George\\Documents\\NetBeansProjects\\Proj\\ignorewords.txt')
          for line in f:
           line=line.lower()
           a=line.split()
           for s in str:
            if(s==a): 
             x=x-1;
             break
           #x=x-row[2].count(a[0])
           #print('{} hello {} loop {}'.format(row[2],row[2].count(a[0]),x))
          str=row[2].split()
          str1=row[2].split()
          term=list(range(x))
          count=list(range(x))
          print(x)
          f = open('C:\\Users\\George\\Documents\\NetBeansProjects\\Proj\\ignorewords.txt')
          j=0
          k=0
		#taking each word in the data
          for s in str:
           k=k+1
           flag=0
           flag1=0
           f = open('C:\\Users\\George\\Documents\\NetBeansProjects\\Proj\\ignorewords.txt')
		   #ignoring ignorable words using flag1
           for line in f:
            line=line.lower()
            a=line.split()
            #print(a[0])
            if s==a[0]:
              flag1=1 
           if flag1==0:
            k1=0
		    #finding if term is repeated using flag
            for s1 in str1:
             k1=k1+1
             if k1<k:
              if s1==s:
               flag=1
			#if not repeated add to terms list 
            if(flag==0):
             term[j]=s
             count[j]=1
             j=j+1
          #print(term)
          #print(count)
                
        else:
          str=(row[2].lower()).split()
          str1=str
          k=0  
          for s in str:
           k1=0
           flag1=0
           flag=0
           for s1 in str1:
             if k1<k:
              if s1==s:
               flag1=1
             k1=k1+1 
           if flag1==0:
            j=0
            for t in term:
             if t==s:
              flag=1
              count[j]=count[j]+1
             j=j+1
            if(flag==0):
             term.append(s);
             count.append(1);
           k=k+1
        i=i+1
    counter=0
    countz=0
    counti=0
    termscore=2
    print(term)
    print(count)
    for t in term:
     x=count[counter]
     try:
      if x > termscore :
           if isNotNum(t) and isNotExist(t,sys.argv[1]): 
            countz=countz+1
            s3='INSERT INTO terms(sub_id,term,score) VALUES(%s,%s,%s)'
            d3 = (sys.argv[1], t,count[counter])
            db.execute(s3, d3)
            cnx.commit()
           #if x > 2:
            #print('hello')
            #counti=counti+1
     except:
      print('error')
     if x > 2 and isNotNum(t):
      print(x,term[counter])
      counti=counti+1
     counter=counter+1;
    s="UPDATE subject SET terms='Y' WHERE sub_id={}".format(sys.argv[1])
    db.execute(s)
    cnx.commit()
    db.close()
    cnx.close()

if __name__ == "__main__": main()
