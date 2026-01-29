import sqlite3

#sets the location of where the database is
DB_PATH = "/Users/nevaehdickerson/Personal_Projects/emailremind/storedMail.db"


def get_db_connection():
  conn = sqlite3.connect(DB_PATH) #opens a connection to the database based on it's path
  conn.row_factory = sqlite3.Row #alows databse to be indexible foy column name and positoin
  return conn #returns the established connection to be used throughout the script

  
def init_db():
	try:
		conn = get_db_connection()
		cur = conn.cursor() #cursor is what actually communicates to the databse, sends SQL commands, fetch results, move through rows
		conn.execute("PRAGMA foreign_keys = ON;")

		#these next few curr.execute() statments initalize the schema for the tables in the databse
		cur.execute("""
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
		""")

		cur.execute("""
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
		""")

		cur.execute("""
			CREATE TABLE IF NOT EXISTS labels (
				label_id TEXT PRIMARY KEY, -- gmail internal label id
				name TEXT NOT NULL -- "STARRED", "INBOX", "UNREAD", "SENT"
			);
		""")

		cur.execute("""
			CREATE TABLE IF NOT EXISTS message_labels (
				message_id TEXT NOT NULL REFERENCES messages(message_id),
				label_id TEXT NOT NULL REFERENCES labels(label_id),
				PRIMARY KEY (message_id, label_id)
			);
		""")

		cur.execute("""
			CREATE TABLE IF NOT EXISTS extracted_dates (
				id INTEGER PRIMARY KEY,
				thread_id TEXT NOT NULL REFERENCES threads(thread_id),
				message_id TEXT NOT NULL REFERENCES messages(message_id),
				date_at INTEGER, 
				kind TEXT, 									-- e.g "due_date" or "class_deadline"
				source_text TEXT --the phrase that triggured it
			);
		""")
	except sqlite3.OperationalError as e:
		print("DB init failed.", e)
	finally:
		if 'conn' in locals():
			conn.commit()
			conn.close()


if __name__ == "__main__":
  init_db()