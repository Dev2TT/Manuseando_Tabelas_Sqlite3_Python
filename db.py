import sqlite3
from Usuario import Usuario as User

connect=sqlite3.connect('HotelPlus.db')
cursor=connect.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY,
            nome VARCHAR(50),
            email VARCHAR(50)
        )

    '''
)
connect.commit()

print("-=-=-=--=TESTE-=-=-=-=")

usuarios=list()

for i in range(4,6):
    print(f'Criando usuario {i+1}')
    nome_aux = input("Digite o nome: ")
    email_aux=input("Digite o e-mail: ")

    usuario_aux=User(i+1,nome_aux,email_aux)

    usuarios.append(usuario_aux)

for usuario in usuarios:
    cursor.execute(
        '''
            INSERT INTO usuarios(id,nome,email) 
            VALUES (?,?,?)

        ''',(usuario.id,usuario.nome,usuario.email)
    )

connect.commit()

connect.close()