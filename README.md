# Publication DataBase
Simple python-flask app to provide a simple html website to  
manage, inject and SQL-query with sqlite3 a database about publication entries.


## Set-Up and Run

* Clone `git clone https://github.com/Bondoki/PublicationDataBase.git`
* Install python3, sqlite3, flask
* Just create in the first step the database:  
```python
    # generates the tables (database)
    
    import sqlite3
    
    conn = sqlite3.connect('ITP_Publication_data.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS itp(id INTEGER PRIMARY KEY AUTOINCREMENT, year TEXT, authors TEXT, title TEXT, datearchived TEXT, type TEXT, pathnetwork TEXT, pathdoxis TEXT, doi TEXT, comment TEXT)''')
    conn.commit()
    conn.close()
```

* run app with flask:  
````bash
    # start the local flask service
    python3 SqliteFlaskPythonQueryInsert_itp.py
````

* open a webbrowser and visit:  
````bash
    firefox http://127.0.0.1:5000
````

* maybe use [sqlitebrowser](https://sqlitebrowser.org/) to view the database

## License

See the [LICENSE](LICENSE) in the root directory.

## Changelog

Major changes are mentioned in the [CHANGELOG](CHANGELOG) file.
