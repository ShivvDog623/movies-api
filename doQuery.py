from app import db


conn = db.getConnection()
cur = db.getCursor()

def doQuery(sql, params):
    cur.execute(sql, params)
    result = cur.fetchone()
    conn.commit()
    return result