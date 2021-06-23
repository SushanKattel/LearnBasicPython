import sqlite3 as sq

db = sq.connect("database1.db")
db.row_factory = sq.Row  # it allows to specify how rows would be returned from cursor.

# First comment this and test below three !!
db.execute("drop table if exists database1")
db.execute("create table database1 (t1 text, i1 int)")
db.execute("insert into database1 (t1, i1) values (?, ?)", ("One", 1))
db.execute("insert into database1 (t1, i1) values (?, ?)", ("Two", 2))
db.execute("insert into database1 (t1, i1) values (?, ?)", ("Three", 3))
db.execute("insert into database1 (t1, i1) values (?, ?)", ("Four", 4))
db.commit()
#cursor = db.execute("select * from database1 order by t1")

#cursor = db.execute("select i1, t1 from database1 order by t1")  # returns in the order of t1 values

cursor = db.execute("select i1, t1 from database1 order by i1")  # returns in the order of t1 values

for row in cursor:
    #print(row)

    # These belows are for row factory!!
    #print(dict(row))
    #print(row["t1"])
    #print(row["i1"])
    print(row["t1"], row["i1"])
