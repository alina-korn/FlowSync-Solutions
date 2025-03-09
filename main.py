# document_service/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import asyncpg
from datetime import datetime

app = FastAPI(title="DocumentService", version="1.0")

# Модель данных для создания документа
class DocumentCreate(BaseModel):
    title: str
    content: str
    creator_id: int

# Модель данных для ответа
class DocumentResponse(BaseModel):
    id: int
    title: str
    content: str
    creator_id: int
    status: str
    created_at: datetime

# Подключение к базе данных
async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="password",
        database="flowsync_db",
        host="localhost"
    )

# Инициализация таблицы при старте
@app.on_event("startup")
async def startup():
    conn = await get_db_connection()
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            creator_id INT NOT NULL,
            status TEXT DEFAULT 'draft',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    await conn.close()

# Создание документа
@app.post("/documents", response_model=DocumentResponse)
async def create_document(doc: DocumentCreate):
    conn = await get_db_connection()
    try:
        row = await conn.fetchrow(
            '''
            INSERT INTO documents (title, content, creator_id)
            VALUES ($1, $2, $3)
            RETURNING id, title, content, creator_id, status, created_at
            ''',
            doc.title, doc.content, doc.creator_id
        )
        return DocumentResponse(**row)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating document: {str(e)}")
    finally:
        await conn.close()

# Получение документа по ID
@app.get("/documents/{doc_id}", response_model=DocumentResponse)
async def get_document(doc_id: int):
    conn = await get_db_connection()
    try:
        row = await conn.fetchrow(
            '''
            SELECT id, title, content, creator_id, status, created_at
            FROM documents WHERE id = $1
            ''',
            doc_id
        )
        if not row:
            raise HTTPException(status_code=404, detail="Document not found")
        return DocumentResponse(**row)
    finally:
        await conn.close()

# Изменение статуса документа
@app.put("/documents/{doc_id}/status")
async def update_status(doc_id: int, status: str):
    conn = await get_db_connection()
    try:
        row = await conn.fetchrow(
            '''
            UPDATE documents SET status = $1
            WHERE id = $2
            RETURNING id, title, content, creator_id, status, created_at
            ''',
            status, doc_id
        )
        if not row:
            raise HTTPException(status_code=404, detail="Document not found")
        return DocumentResponse(**row)
    finally:
        await conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)