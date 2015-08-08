CREATE TABLE IF NOT EXISTS positionlogs (
        logid INTEGER PRIMARY KEY AUTOINCREMENT,
        devicename TEXT NOT NULL,
        lng REAL,
        lat REAL,
        ctime DATETIME DEFAULT CURRENT_TIMESTAMP
        );
