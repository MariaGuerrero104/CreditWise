from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI(title="CreditWise API", version="1.0")

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="creditwise"
    )

class Usuario(BaseModel):
    documento: int
    nombre: str
    gmail: str
    contrasena: str
    puntaje: int

@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO usuarios (documento, nombre, gmail, contrasena, puntaje)
        VALUES (%s, %s, %s, %s, %s)
    """, (usuario.documento, usuario.nombre, usuario.gmail, usuario.contrasena, usuario.puntaje))
    db.commit()
    cursor.close()
    db.close()
    return {"mensaje": "Usuario creado exitosamente"}
