#!/usr/bin/env python
import sqlite3

def isQuoteExist(quoteId):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('SELECT COUNT(1) FROM quotes WHERE id=?', [str(quoteId)])
    text = c.fetchone()
    conn.close()
    
    if text[0] == 1:
        return True
    else:
        return False

def getQuote(quoteId):
    conn = sqlite3.connect('quotes.db')
    c = conn.cursor()
    c.execute('SELECT text FROM quotes WHERE id=?', [str(quoteId)])
    text = c.fetchone()
    conn.close()
    return text[0]