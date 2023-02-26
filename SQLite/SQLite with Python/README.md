## Using  SQLite with Python:
 <br />

### 1. Import sqlite library:
```python
import sqlite3
```


### 2. Create a new database and connect to it:
```python
conn = sqlite3.connect('./file_name.db')
```
### 3.  Create the cursor:
```python
cursor = conn.cursor() 
```

### 4. Store the SQL-statments into variables as String:
```python
var = 'sql_statments'
```

### 5. Execute the Sql-statments:
```python
cursor.execute(var)
```

### 6. Commit the changes to the database:
```python
conn.commit()
```

### 7. Get the results:
```python
rows = cursor.fetchall()
```

### 8. Print the results:
```python
for row in rows:
    print(f'{row[0]}, {row[1]}, ... {row[n]})
```
