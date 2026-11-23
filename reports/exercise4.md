# Bug reports for exercise4.py

Line: 7
Problem: The docstring states "true if the password is the admin password", but the function returns True only if the password is not empty and equals ADMIN_PASSWORD. It incorrectly returns True when the password is empty or not equal to ADMIN_PASSWORD. The logic is flawed because it checks for password != "" which is always true for non-empty strings, and the condition is not correctly aligned with the docstring.
Example: check_admin("") returns True, expected False
Fix: return password == ADMIN_PASSWORD

Line: 14
Problem: The function uses string formatting to directly insert the username into a SQL query without escaping, which makes it vulnerable to SQL injection attacks. This is a critical security flaw and violates safe database query practices.
Example: find_user(db, "'; DROP TABLE users; --") executes malicious SQL
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
