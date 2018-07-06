#!/usr/bin/env python
import sqlite3

def isUserExist(userId):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(1) FROM users WHERE userId=?', [str(userId)])
    text = c.fetchone()
    conn.close()
    
    if text[0] == 1:
        return True
    else:
        return False
        
def getUserLastQuoteIndex(userId):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT lastQuoteIndex FROM users WHERE userId=?', [str(userId)])
    text = c.fetchone()
    conn.close()
    
    return text[0]

def createNewUser(userId, quoteIndex, userName):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (userId, lastQuoteIndex, userName) VALUES (?, ?, ?)', [str(userId), str(quoteIndex), userName])
    conn.commit()
    conn.close()
	
def setUserLastQuoteIndex(userId, newIndex):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('UPDATE users SET lastQuoteIndex=? WHERE userId=?', [str(newIndex), str(userId)])
    conn.commit()
    conn.close()
	