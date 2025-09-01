from flask import Flask, jsonify
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes import register_routex

app = Flask(__name__)
app.config.from_object(Config)
# PERMITE PETICIONES DESDE EL FRONT
# CORS(app, origins="http://localhost:5175", supports_credentials=True) -------------- viteapp conexion docker 5175
CORS(
    app, origins="http://localhost:5173", supports_credentials=True
)  # ---------- para la app de quantum 5173

# # Permitir múltiples orígenes (local + Railway)
# CORS(
#     app,
#     origins=[
#         "http://localhost:5173",  # Vite local
#         "https://chico-python-flask10.up.railway.app"  # producción
#     ],
#     supports_credentials=True
# )

jwt = JWTManager(app)
# funcion de rutas para funcion inicial del API REST
register_routex(app)

# Start the Server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))  # toma el puerto de Railway, si no existe usa 3000
    app.run(host="0.0.0.0", port=port, debug=True)
    
