import sqlite3




import ss


cx = sqlite3.connect("F:/test.db")

cu = cx.cursor()




cu.execute('create table test(id integer integer,name varchar(20))')

cu.execute('insert into test values(1,"ss")')

cx.commit()