#!/usr/bin/env python3
"""
Setup script for WIM Matchmaking Platform
Creates admin user and initializes database
"""

import sqlite3
import hashlib
from datetime import datetime

def hash_password(password):
    """Hash a password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def setup_admin():
    """Create default admin user."""
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            admin_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT,
            created_date TIMESTAMP
        )
    ''')
    
    # Insert default admin
    try:
        c.execute('''
            INSERT INTO admin_users (admin_id, email, password_hash, name, created_date)
            VALUES (?, ?, ?, ?, ?)
        ''', ('admin_001', 'admin@kam.co.ke', hash_password('admin123'), 'KAM Admin', datetime.now()))
        
        conn.commit()
        print("✅ Admin user created!")
        print("   Email: admin@kam.co.ke")
        print("   Password: admin123")
        print("   ⚠️  CHANGE THIS PASSWORD IMMEDIATELY IN PRODUCTION!")
    
    except sqlite3.IntegrityError:
        print("⚠️  Admin user already exists")
    
    conn.close()

if __name__ == "__main__":
    setup_admin()
