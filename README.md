
# SoundBeat - Microservices Prototype (Submission)

El repositorio contiene un prototipo minimalista para la migración del backend
Incluye dos simple microservicios implementado con Flask:
- users-service: GET /usuarios  (port 5001)
- songs-service: GET /canciones (port 5002)

Cada servicio lee de manera local un archivo JSON y devuelve su contenido. 
El objetivo de esto es demostrar la estructura de los microservicios y APIs simples

Como ejecutar de manera local:
1. Abrir dos terminales (uno por servicio).
2. Para users-service:
   cd users-service
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
3. Para songs-service:
   cd songs-service
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py

Ejemplo de ejecución:
- curl http://localhost:5001/usuarios
- curl http://localhost:5002/canciones
# examenParcial
