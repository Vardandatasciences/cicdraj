import sqlite3


def login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # 🚨 Vulnerable: string
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    
    # Execute the query
    cursor.execute(query)
    
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Login failed.")

    conn.close()


# Example usage
login("admin", "1234")



