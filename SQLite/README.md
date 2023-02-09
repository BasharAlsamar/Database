### What is SQLite ?
#### `SQLite:` is a software library that provides a relational database management system. The lite in SQLite means lightweight in terms of setup, database administration, and required resources.

### Serverless
#### Normally, an RDBMS such as MySQL, PostgreSQL, etc., requires a separate server process to operate. The applications that want to access the database server use TCP/IP protocol to send and receive requests. This is called client/server architecture.

#### The following diagram illustrates the RDBMS client/server architecture:
![1](images/1.png)

### - SQLite does NOT work this way.

### - SQLite does NOT require a server to run.

### - SQLite database is integrated with the application that accesses the database. The applications interact with the SQLite database read and write directly from the database files stored on disk.

### - The following diagram illustrates the SQLite server-less architecture:
![2](images/2.png)


### Download SQLite tools:
#### To download SQLite, you open the [download page](https://www.sqlite.org/download.html) of the SQlite official website.
- #### To work with SQLite on Windows, you download the command-line shell program as shown in the screenshot below.
![3](images/3.png)

### Run SQLite tools:
#### Installing SQLite is simple and straightforward.

#### First, create a new folder e.g., `C:\sqlite`.
#### Second, extract the content of the file that you downloaded in the previous section to the C:\sqlite folder. You should see three programs in the `C:\sqlite` folder as shown below:
![4](images/4.png)

### 1. open the command line window:
![5](images/5.png)

### 2. navigate to the `C:\sqlite` folder.
```bash
C:\cd c:\sqlite
C:\sqlite>
```
### 3. type `sqlite3` and press enter, you should see the following output:
```bash
C:\sqlite>sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```
### 4. to quit the sqlite>, you use  `.quit` command as follows:
```bsah
sqlite> .quit
```
## SQLite Commands:
* ### To start the sqlite3, you type the `sqlite3` as follows:
```bash
>sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
```

* ### To open a database file, you use the `.open FILENAME` command. The following statement opens the chinook.db database:
 ```bash
sqlite> .open c:\sqlite\db\chinook.db
```

* ### Show tables in a database
#### To display all the tables in the current database, you use the `.tables` command. The following commands open a new database connection to the chinook database and display the tables in the database.
```bash
>sqlite3 c:\sqlite\db\chinook.db
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .tables
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
sqlite>
```
* ### To exit the sqlite3 program, you use the `.exit` command.
```bash
sqlite>.exit
```
* ### To find tables based on a specific pattern, you use the `.table` pattern command. The sqlite3 uses the `LIKE` operator for pattern matching.

### For example, the following statement returns the table that ends with the string `es`.
```bash
sqlite> .table '%es'
employees    genres       invoices     media_types
sqlite>
```

* ### Show the structure of a table

### The following command shows the structure of the albums table.
```bash
sqlite> .schema albums
CREATE TABLE "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);
sqlite>
```

* ### To show all indexes of the current database
```bash
sqlite> .indexes
```

* ### To show the indexes of a specific table, you use the `.indexes TABLE` command. For example, to show indexes of the `albums` table, you use the following command:

```bash
sqlite> .indexes albums
```

* ### Save the result of a query into a file:
   ###  To save the result of a query into a file, you use the `.output FILENAME` command. Once you issue the `.output` command, all the results of the subsequent queries will be saved to the file that you specified in the `FILENAME` argument. If you want to save the result of the next single query only to the file, you issue the `.once FILENAME` command.

   ### To display the result of the query to the standard output again, you issue the `.output` command without arguments.

    ### The following commands select the `title` from the `albums` table and write the result to the ``albums.txt` file.

```bash
sqlite> .output albums.txt
sqlite> SELECT title FROM albums;
```

- ### Execute SQL statements from a file
  ### Suppose we have a file named `commands.txt` in the `c:\sqlite\` folder with the following content:

```bash
SELECT albumid, title
FROM albums
ORDER BY title
LIMIT 10;
```
- ### To execute the SQL statements in the `commands.txt` file, you use the `.read FILENAME` command as follows:

```bash
sqlite> .mode column
sqlite> .header on
sqlite> .read c:/sqlite/commands.txt
AlbumId     Title
----------  ----------------------
156         ...And Justice For All
257         20th Century Masters -
296         A Copland Celebration,
94          A Matter of Life and D
95          A Real Dead One
96          A Real Live One
285         A Soprano Inspired
139         A TempestadeTempestade
203         A-Sides
160         Ace Of Spades
```

## **SQLITE TUTORIAL**:
> ### 1. SQLite Select

- ### Querying data from a table using the SELECT statement
  ### We often use the SELECT statement to query data from one or more table. The syntax of the SELECT statement is as follows:

```bash
SELECT DISTINCT column_list
FROM table_list
  JOIN table ON join_condition
WHERE row_filter
ORDER BY column
LIMIT count OFFSET offset
GROUP BY column
HAVING group_filter;
```
- #### Use `SELECT` statement that allows you to query data from a single table.
- #### Use `ORDER` BY clause to sort the result set.
- #### Use `DISTINCT` clause to query unique rows in a table.
- #### Use `WHERE` clause to filter rows in the result set.
- #### Use `LIMIT OFFSET` clauses to constrain the number of rows returned.
- #### Use `INNER JOIN` or `LEFT JOIN` to query data from multiple tables using join.
- #### Use `GROUP BY` to get the group rows into groups and apply aggregate function for each group.
- #### Use `HAVING` clause to filter groups.

* ### To get data from the tracks table such as trackid, track name, composer, and unit price, you use the following statement:
```bash
SELECT
	trackid,
	name,
	composer,
	unitprice
FROM
	tracks;
```

  ### SQLite returns the following result: 
  ![6](images/6.png)

* ### To get data from all columns: 
```bash
SELECT * FROM tracks;
```

> - ### NOTE: You should use the asterisk (*) for the testing purpose only, not in the real application development. Becaus When you develop an application, you should control what SQLite returns to your application. Suppose, a table has 3 columns, and you use the asterisk (*) to retrieve the data from all three columns. What if someone removes a column, your application would not be working properly, because it assumes that there are three columns returned and the logic to process those three columns would be broken.


