import MySQLdb as mydatabase
conn = mydatabase.connect(host='117.25.155.149', port=3306, user='gelinroot', passwd='glt#789A', db='db_dolphin', charset='utf8')
cursor = conn.cursor()

cursor.execute('DELETE FROM py_product_comments_tmp')
cursor.execute('DELETE FROM py_keyword_main')
cursor.execute('DELETE FROM py_keyword_main_tmp')
cursor.execute('DELETE FROM py_keyword_word_count')
cursor.execute('DELETE FROM py_keyword_count')

conn.commit()