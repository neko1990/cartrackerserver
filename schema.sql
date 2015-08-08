CREATE TABLE IF NOT EXISTS positionlogs (
        logid INTEGER PRIMARY KEY AUTOINCREMENT,
        devicename TEXT NOT NULL,
        lng REAL,
        lat REAL,
        ctime REAL DEFAULT ((julianday('now') - 2440587.5) * 86400.0)
        );
