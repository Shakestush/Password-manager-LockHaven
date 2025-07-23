import sqlite3
import os
from typing import List, Dict, Optional

DATABASE_FILE = "securepass.db"

def init_db():
    """Initialize database with required tables"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                master_key_salt TEXT NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                service TEXT NOT NULL,
                username TEXT NOT NULL,
                encrypted_password TEXT NOT NULL,
                category TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        """)
        conn.commit()

def add_password(user_id: int, service: str, username: str, encrypted_password: str, 
                 category: str = None, notes: str = None):
    """Store a new password entry"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO passwords 
            (user_id, service, username, encrypted_password, category, notes)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (user_id, service, username, encrypted_password, category, notes))
        conn.commit()

def get_passwords(user_id: int) -> List[Dict]:
    """Retrieve all passwords for a user"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, service, username, encrypted_password, category, notes
            FROM passwords WHERE user_id = ?
        """, (user_id,))
        return [dict(row) for row in cursor.fetchall()]

def update_password(password_id: int, service: str = None, username: str = None,
                   encrypted_password: str = None, category: str = None, notes: str = None):
    """Update a password entry"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        updates = []
        params = []
        
        if service:
            updates.append("service = ?")
            params.append(service)
        if username:
            updates.append("username = ?")
            params.append(username)
        if encrypted_password:
            updates.append("encrypted_password = ?")
            params.append(encrypted_password)
        if category:
            updates.append("category = ?")
            params.append(category)
        if notes:
            updates.append("notes = ?")
            params.append(notes)
            
        if updates:
            params.append(password_id)
            query = f"UPDATE passwords SET {', '.join(updates)}, updated_at = CURRENT_TIMESTAMP WHERE id = ?"
            cursor.execute(query, params)
            conn.commit()

def delete_password(password_id: int):
    """Delete a password entry"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM passwords WHERE id = ?", (password_id,))
        conn.commit()

def setup_user(salt: str) -> int:
    """Set up a new user and return user ID"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (master_key_salt) VALUES (?)", (salt,))
        conn.commit()
        return cursor.lastrowid

def get_user_salt(user_id: int) -> Optional[str]:
    """Get the salt for a user"""
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT master_key_salt FROM users WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None
