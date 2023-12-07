import mysql.connector
import yaml
from call_api import read_api

# getting data from call_api
def get_data():
    articles = read_api()
    return articles



# Read api key and Mysql connection from env.yml
def connector_with_mysql():
    with open('env.yml','r') as file:
        conf = yaml.safe_load(file)

    
    mysql_conf = {
        'host' : conf.get('mysql_host'),
        'user' : conf.get('mysql_user'),
        'password' : conf.get('mysql_password'),
        'database' : conf.get('mysql_database')
    }
    
    connection = mysql.connector.connect(**mysql_conf)
    return connection


 # function is responsiable for create a table and load data into table
def append_table():
    #   CREATING TABLE IF IT NOT EXISTS
    create_table ="""
    CREATE TABLE IF NOT EXISTS articles(
        source_id TEXT,
        source_name TEXT,
        author TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        urltoimage TEXT,
        publishedat TEXT,
        content TEXT
        )"""
    cursor.execute(create_table)
    #inserting data into table
    for article in articles:

        insert_column = """INSERT INTO articles 
        (source_id, source_name,
        author, title, 
        description, url, 
        urltoimage, publishedat, 
        content)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        # valuse 
        data_to_insert =(article['source']['id'], article['source']['name'],article['author'], article['title'], article['description'], article['url'], article['urlToImage'],article['publishedAt'],article['content'] )

        #storing values in table 
        cursor.execute(insert_column, data_to_insert)
    connection.commit()
    connection.close()
    print('Data inserted successfully')


#getting data through get_data function
articles = get_data()


# calling connector and getting cursor #
connection = connector_with_mysql()
# getting cursor 
cursor = connection.cursor()

# adding data into table

add = append_table()
