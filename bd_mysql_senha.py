import mysql.connector as mysql

conexao = mysql.connect(host='localhost',db='pooii',user='root',passwd = '1234')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios(id integer AUTO_INCREMENT PRIMARY KEY,
nome text NOT NULL,senha VARCHAR(32) NOT NULL, email text NOT NULL);"""

nome = "Ericksulino"
email = "ericksulino@gmail.com"
senha = "teste"

cursor.execute(sql)
#for i in range(5):
cursor.execute("INSERT INTO usuarios (nome,senha,email) VALUES(%s,MD5(%s),%s)", (nome,senha,email))

#cursor.execute("SELECT * FROM usuarios")
cursor.execute("SELECT * FROM usuarios WHERE nome = %s AND senha = MD5(%s)")

for c in cursor:
    print(c)

conexao.commit()
conexao.close()