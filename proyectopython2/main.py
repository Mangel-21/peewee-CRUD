import peewee
from datetime import datetime
# Conexión a la base de datos MySQL
database = peewee.MySQLDatabase('pythonndb', host='localhost', port=3306, user='root', passwd='root')

class User(peewee.Model):
    username=peewee.CharField(max_length=50,unique=True,index=True)
    email=peewee.CharField(max_length=60,null=False)
    active=peewee.BooleanField(default=False) #tiene valores por fault para cuando crear valores en las tablas ya no darle valor a cada fila
    created_at=peewee.DateTimeField(default=datetime.now) #tiene valores por fault para cuando crear valores en las tablas ya no darle valor a cada fila

    class Meta:
        database=database
        db_table='users'

    def __str__(self):
        return self.username

if __name__ == '__main__' :

    if User.table_exists():
       User.drop_table()
    
    User.create_table()  
    """
    user1= User(username='user1',email='angel5602599@gmail.com', active=True)
    user1.save()

    user2=User()
    user2.username='piero'
    user2.email='pierotorres@gmail.com'
    user2.save()

    values={
        'username': 'carlos',
        'email': 'carlosMozombite@gmail.com'
    }
    user3=User(**values)
    user3.save()


    user4=User.create(username='user4',email='user4@gmail.com')
    print(user4.id)   #se creo y se mostro el id de la tabla 4


    query=User.insert(username='user5',email='user5@gmail.com') #crea una query
    print(type(query)) #modeInsert
    query.execute() #crea un registro a travez 
    """
    users=[ #multiples registros mi rey
        {'username':'user1','email':'user1@gmail.com','active': True},
        {'username':'user2','email':'user2@gmail.com'},
        {'username':'user3','email':'user3@gmail.com','active': True} ,
        {'username':'user4','email':'user4@gmail.com'},
        {'username':'user5','email':'user5@gmail.com'},
        {'username':'user6','email':'user6@gmail.com','active': True},
        {'username':'user7','email':'user7@gmail.com','active': True},
    ]  

    query=User.insert_many(users)
    query.execute()

       # try:
        #     user=User.select().where(User.username=='user11').get() # get para obtener sus valores y el try para darle la excepcion si el usuario no ex
        #     print(type(user))
        #     print(user)
        # except User.DoesNotExist as err: 
        #     print('no fue posible obtener al usuario!')     
    
    #1era forma de actualizar un registro
    user=User.select().where(User.id==1).get()
    user.username='Nuevo username'
    user.email='nuevo_valor@gmail.com'
    user.save()

    #ahora a travez de un query 2da forma
    query=User.update(username='user2 nuevo valor',email='user2_nuevovalor@example.com').where(User.id==2)
    query.execute()
     
    #1ERA FORMA DE ELIMINAR 
    user=User.select().where(User.username=='user7').get()
    user.delete_instance()

    #2da forma de elimnar con el metodo delete
    query=User.delete(  ).where(User.id==6)
    query.execute()