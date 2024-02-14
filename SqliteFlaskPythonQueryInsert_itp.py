from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_query_insert_itp.html')

@app.route('/query', methods=['POST'])
def query():
    query = request.form['query']
    result = execute_query(query)
    
    table_name = 'itp'
    columns = get_column_names(table_name)
    
    #columns = ["id", "file", "comment", "data"] # list of column name for query
    
    return render_template('index_query_insert_itp.html', columns=columns, result=result, query=query)

@app.route('/insert', methods=['POST'])
def insert():
    # year TEXT, authors TEXT, title TEXT, datearchived TEXT, type TEXT, pathnetwork TEXT, pathdoxis TEXT, doi TEXT, comment TEXT
    I_year = request.form['year']
    I_authors = request.form['authors']
    I_title = request.form['title']
    I_date = request.form['datearchived'] #datetime.now()
    I_type_of_work = request.form['type_of_work']
    I_path = request.form['path']
    I_doxis = request.form['doxis']
    I_doi = request.form['doi']
    I_comment = request.form['comment']
    
    print(I_year, I_authors, I_title, I_date, I_type_of_work, I_path, I_doxis, I_doi, I_comment)
    insert_data(I_year, I_authors, I_title, I_date, I_type_of_work, I_path, I_doxis, I_doi, I_comment)
    return render_template('index_query_insert_itp.html', success=True)

def execute_query(pattern):
    conn = sqlite3.connect('ITP_Publication_data.db')  # Replace with your database file path
    cursor = conn.cursor()
    # Define the pattern
    pattern_query = '%'+pattern+'%'

    # Execute the query
    table_name = 'itp'
    column_name = 'authors'
    #query = "SELECT * FROM itp WHERE comment LIKE ?"
    print(pattern)
    
    if pattern == '*':
        #query = "SELECT "+column_name+" FROM "+table_name
        query = "SELECT * FROM "+table_name
        cursor.execute(query)
    else:
        query = "SELECT * FROM "+table_name+" WHERE "+column_name+" LIKE ?"
        cursor.execute(query, (pattern_query,))
    
    
    print(len(pattern))
    
    #cursor.execute(query)
    result = cursor.fetchall()
    print(len(result))
    print(result)
    
    conn.close()
    return result

def insert_data(year, authors, title, datearchived, type_of_work, pathnetwork, pathdoxis, doi, comment):
    conn = sqlite3.connect('ITP_Publication_data.db')  # Replace with your database file path
    cursor = conn.cursor()
    query = "INSERT INTO itp (year, authors, title, datearchived, type, pathnetwork, pathdoxis, doi, comment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"  # Replace with your table name
    cursor.execute(query, (year, authors, title, datearchived, type_of_work, pathnetwork, pathdoxis, doi, comment))
    conn.commit()
    conn.close()

def get_column_names(table_name):
    conn = sqlite3.connect('ITP_Publication_data.db')  # Replace with your database file path
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = cursor.fetchall()
    conn.close()
    return [column[1] for column in columns]

if __name__ == '__main__':
    app.run()


