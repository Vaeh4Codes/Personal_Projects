import sqlite3

CREATE_THREADS_TABLE = """
    --This table will store data from each individual message thread
    --This will be the data that gets queried for the daily digest
    
    CREATE TABLE IF NOT EXISTS threads (
      thread_id TEXT PRIMARY KEY,
      subject TEXT,
      last_message_at INTEGER, --timestamp of most recent message in thread
      needs_reply INTEGER NOT NULL DEFAULT 0 CHECK (needs_reply IN (0,1)), -- sets default as does not need reply (0)
      has_replied INTEGER NOT NULL DEFAULT 0 CHECK (has_replied IN (0,1)), -- sets default as has not replied (0)
      next_due_at INTEGER NULL, --soonest due date extracted
      priority_score INTEGER, -- priority decided and computed daily
      last_synced_at INTEGER -- when the thread was last refreshed from gmail
    );

    -- One row per message inside a thread (needed for parsing + replied detection)
    CREATE TABLE IF NOT EXISTS messages (
        message_id TEXT PRIMARY KEY,
        thread_id TEXT NOT NULL REFERENCES threads(thread_id),
        sent_at INTEGER, --timestamp of message
        from_email TEXT, 
        to_emails TEXT,
        cc_emails TEXT,
        is_from_me INTEGER NOT NULL DEFAULT 0 CHECK (is_from_me IN (0,1)), -- sets default as is not from me (0)
        body_text TEXT, -- plain text body to be stored
        snippet TEXT
      );

      CREATE TABLE IF NOT EXISTS labels (
        label_id TEXT PRIMARY KEY, -- gmail internal label id
        name TEXT NOT NULL -- "STARRED", "INBOX", "UNREAD", "SENT"
      );

      CREATE TABLE IF NOT EXISTS message_labels (
        message_id TEXT NOT NULL REFERENCES messages(message_id),
        label_id TEXT NOT NULL REFERENCES labels(label_id)
      );

      CREATE TABLE IF NOT EXISTS extracted_dates (
        id INTEGER PRIMARY KEY,
        thread_id TEXT NOT NULL REFERENCES threads(thread_id),
        message_id TEXT NOT NULL REFERENCES messages(message_id),
        date_at INTEGER, 
        kind TEXT, -- e.g "due_date" or "class_deadline"
        source_text TEXT --the phrase that triggured it
      );
      """

#initalizes a new sqlite database
def get_connection():
  conn = sqlite3.connect("storedMail.db")
  conn.execute("PRAGMA foreign_keys = ON;")
  return conn

def init_db():
  conn = get_connection()
  try:
    conn.executescript(CREATE_THREADS_TABLE)
    conn.commit()
  except sqlite3.OperationalError as e:
    print("Failed to open database:", e)
  finally:
    conn.close()


if __name__ == "__main__":
  init_db()