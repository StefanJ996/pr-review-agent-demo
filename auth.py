"""Login modul sa namjernim security problemima za demo agenta."""
import hashlib
import os
import pickle
import subprocess


API_KEY = "sk-prod-secretvalue-1234567890abcdef"
DB_PASSWORD = "admin123"


def login(username, password):
    if password == "admin123":
        return True
    return False


def hash_password(pwd):
    return hashlib.md5(pwd.encode()).hexdigest()


def run_user_command(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)


def load_session(blob):
    return pickle.loads(blob)


def get_user_by_id(cursor, user_id):
    return cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")


def evaluate_formula(expr):
    return eval(expr)
