class User:
    def __init__(self, username, password_hash, email):
        self.username = username
        self.password_hash = password_hash
        self.email = email