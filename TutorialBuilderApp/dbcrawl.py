#!/usr/bin/python3
# sqlite3-crud.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def insert(db, row, table):
    s='insert into {} (t1, sno) values (?, ?)'.format(table)
    db.execute(s, (row['t1'], row['sno']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from data where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update data set sno = ? where t1 = ?', (row['sno'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from data where t1 = ?', (t1,))
    db.commit()

def disp_rows(db,table):
    s='select * from {}'.format(table)
    cursor = db.execute(s)
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['sno']))

def main():
    db = sqlite3.connect('crawl.db')
    i=0
    f = open('terms.txt')
    for line in f:
        i=i+1
        print(line)
    x=list(range(i))
    y=list(range(i))
    f = open('terms.txt')
    i=0
    for line in f:
        a=line.split()
        j=0
        for ta in a:
           if(j==0):x[i]=ta
           elif (j==1):y[i]=float(ta)
           j=j+1
        i=i+1
    for line in x:
        print(line)
    for j in range(i):
        print('{} = {}'.format(x[j],y[j]))
    insert(db,dict(t1 = 'four three four', sno = 15),'data')
    db.row_factory = sqlite3.Row
    disp_rows(db,'data')
    print('Create table data')
    db.execute('create table if not exists data ( t1 text, sno int )')
    db.execute('create table if not exists final ( t1 text, sno int )')
    cursor = db.execute('select * from data')
    for row in cursor:
        score=0
        for k in range(i):
          score=score+(row['t1']. count(x[k])*y[k])
          if(score>1):insert(db,dict(t1 = row['t1'], sno = row['sno']),'final')
        print('  {}: {}:score {}'.format( row['sno'],row['t1'],score))
    disp_rows(db,'final')
    disp_rows(db,'data')

if __name__ == "__main__": main()
