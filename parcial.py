# A ver que sale de esta monda
# crear bases de datos de mongo

# Se debe primero, tener mongo instalado de forma correcta. Esto, con la
# intencion se usar el shell para empezar a operar las bases de datos.
# Nos conectamos al puerto predeterminado de mongo, el 27017.
# Luego, debemos de usar el siguiente comando
"""
use base_estudiantes;
"""
# Para mantener un mejor orden se crea la coleccion "colec1".
"""
db.createCollection("colec1")
"""
# Finalmente, para poder insertar los datos de los estudiantes a la
# base de datos, se usa el siguiente comando con los siguientes
# parametros.
"""
db.base_estudiantes.insert({s_id:'Id', s_name:'Nombre', carrera:'Carrera', sem:'Semestre', prom:'Promedio_notas'});
"""
# Se usaron los siguientes documentos:
"""
 {
    _id: ObjectId("63403d85cfc24024aab07cab"),
    s_id: 1,
    s_name: 'Daniel',
    carrera: 'Ingenieria de datos e inteligencia artificial',
    sem: 3,
    prom: 4.5
  },
  {
    _id: ObjectId("63403f20cfc24024aab07cac"),
    s_id: 2,
    s_name: 'Gustavo',
    carrera: 'Ingenieria mecatronica',
    sem: 6,
    prom: 4.8
  },
  {
    _id: ObjectId("63403f56cfc24024aab07cad"),
    s_id: 3,
    s_name: 'Alejandro',
    carrera: 'Comunicacion social y periodismo',
    sem: 2,
    prom: 4.1
  },
  {
    _id: ObjectId("63403ffecfc24024aab07cae"),
    s_id: 4,
    s_name: 'Atenea',
    carrera: 'Ingenieria en multimedia',
    sem: 4,
    prom: 4.7
  },
  {
    _id: ObjectId("634040dbcfc24024aab07caf"),
    s_id: 5,
    s_name: 'Miguel',
    carrera: 'Ingenieria biomedica',
    sem: 5,
    prom: 3.8
  },
  {
    _id: ObjectId("63404108cfc24024aab07cb0"),
    s_id: 6,
    s_name: 'Angela',
    carrera: 'Musica',
    sem: 4,
    prom: 4.3
  },
  {
    _id: ObjectId("6340417ccfc24024aab07cb1"),
    s_id: 7,
    s_name: 'Camila',
    carrera: 'Diseno de la comunicacion visual',
    sem: 9,
    prom: 4.9
  },
  {
    _id: ObjectId("63404202cfc24024aab07cb2"),
    s_id: 8,
    s_name: 'Henry',
    carrera: 'Psicologia',
    sem: 2,
    prom: 4
  },
  {
    _id: ObjectId("634043d7cfc24024aab07cb3"),
    s_id: 9,
    s_name: 'Sandra',
    carrera: 'Arquitectura',
    sem: 5,
    prom: 3.9
  },
  {
    _id: ObjectId("6340449fcfc24024aab07cb4"),
    s_id: 10,
    s_name: 'Maria',
    carrera: 'Medicina',
    sem: 8,
    prom: 4.6
  }
"""

#Y se uso el comanto insertMany() junto con todos los documentos para poder
#ser insertados en la tabla

"""
db.base_estudiantes.insertMany([
    {
    _id: ObjectId("63403d85cfc24024aab07cab"),
    s_id: 1,
    s_name: 'Daniel',
    carrera: 'Ingenieria de datos e inteligencia artificial',
    sem: 3,
    prom: 4.5
  },
  {
    _id: ObjectId("63403f20cfc24024aab07cac"),
    s_id: 2,
    s_name: 'Gustavo',
    carrera: 'Ingenieria mecatronica',
    sem: 6,
    prom: 4.8
  },
  {
    _id: ObjectId("63403f56cfc24024aab07cad"),
    s_id: 3,
    s_name: 'Alejandro',
    carrera: 'Comunicacion social y periodismo',
    sem: 2,
    prom: 4.1
  },
  {
    _id: ObjectId("63403ffecfc24024aab07cae"),
    s_id: 4,
    s_name: 'Atenea',
    carrera: 'Ingenieria en multimedia',
    sem: 4,
    prom: 4.7
  },
  {
    _id: ObjectId("634040dbcfc24024aab07caf"),
    s_id: 5,
    s_name: 'Miguel',
    carrera: 'Ingenieria biomedica',
    sem: 5,
    prom: 3.8
  },
  {
    _id: ObjectId("63404108cfc24024aab07cb0"),
    s_id: 6,
    s_name: 'Angela',
    carrera: 'Musica',
    sem: 4,
    prom: 4.3
  },
  {
    _id: ObjectId("6340417ccfc24024aab07cb1"),
    s_id: 7,
    s_name: 'Camila',
    carrera: 'Diseno de la comunicacion visual',
    sem: 9,
    prom: 4.9
  },
  {
    _id: ObjectId("63404202cfc24024aab07cb2"),
    s_id: 8,
    s_name: 'Henry',
    carrera: 'Psicologia',
    sem: 2,
    prom: 4
  },
  {
    _id: ObjectId("634043d7cfc24024aab07cb3"),
    s_id: 9,
    s_name: 'Sandra',
    carrera: 'Arquitectura',
    sem: 5,
    prom: 3.9
  },
  {
    _id: ObjectId("6340449fcfc24024aab07cb4"),
    s_id: 10,
    s_name: 'Maria',
    carrera: 'Medicina',
    sem: 8,
    prom: 4.6
  }
  ])
"""

# Para mirar todos los documentos solo debemos poner:
"""
colec1.find().pretty()
"""
# Para ver, por ejemplo, los estudiantes que estudian una carrera
# determinada se tendria que hacer lo siguiente:
"""
db.base_estudiantes.find({carrera: 'Ingenieria biomedica'})
"""
# Para mostrar los 3 mejores estudiantes de acuerdo al promedio:
"""
db.base_estudiantes.find({},{"prom":1}).sort({"prom":-1}).limit(3)
"""
# Donde se usa el sort para poder ordenarlos de forma descendente, y el limit hace que me
# arroje solo 3.
# Ahora, para encontrarla lista de las diferentes carreras en la coleccion:
"""
db.base_estudiantes.find({},{"carrera":1})
"""
# Por ultimo, se le realiza un count al numero de estudiantes de un semestre determinado:
