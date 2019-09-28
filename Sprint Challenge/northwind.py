import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')
CURS = CONN.cursor()

#What are the top 10 most expensive(per unit price) items?
CURS.execute('SELECT * FROM product ORDER BY UnitPrice DESC LIMIT 10;')
#Calculate average age at hire
CURS.execute('SELECT AVG(strftime("%Y", Hiredate) - strftime("%Y", Birthdate)) FROM Employee;')
avg_at_hire = CURS.fetchall()

#Find 10 most expensive items, and their suppliers
CURS.execute('''SELECT CompanyName, ProductName, UnitPrice FROM Product, Supplier
                WHERE Supplier.Id = SupplierId
                ORDER BY UnitPrice DESC
                LIMIT 10;''')
top_ten_supps = CURS.fetchall()

#Find largest category
CURS.execute('''SELECT CategoryId, COUNT(*) FROM Product
             GROUP BY CategoryId
             ORDER BY 2 DESC
             LIMIT 1;''')
lrgst_cat = CURS.fetchall()

#Print final results
print(top_ten_supps, lrgst_cat)

print('''4.1: I Believe that kind of relationship is parent child,
         as that table only exists to hold information for the first.
         4.2: MongoDB is appropriate when the data doesn't need to be
         the most well organized, but may have many features we can't
         predict. It's not appropriate for hard data with fixed features,
         like a videogame and it's stats and scores.
         4.3: NewSQL is a relational database seeking to provide the
         fluidity of Mongo, with the ACID requirements of more traditional
         systems.''')