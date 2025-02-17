from flask import Flask, request, jsonify, render_template
import re
import bcrypt
from collections import Counter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# List of common passwords (this can be expanded)
COMMON_PASSWORDS = [
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "qwerty", "abc123", "111111", "123123", "admin", "letmein", "welcome"
]

# Rate limiting to prevent brute-force attacks
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["10 per minute"]
)

def is_password_strong(password):
    # Check password length
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check for uppercase, lowercase, digits, and special characters
    if not re.search(r'[A-Z]', password):
        return "Password should contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password should contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Password should contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password should contain at least one special character."

    # Check for common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "Password is too common. Please choose a stronger password."

    # Check for repetitive characters (e.g., "aaaaaa")
    counter = Counter(password)
    if max(counter.values()) > len(password) // 2:
        return "Password contains too many repetitive characters."

    # If all checks pass, the password is strong
    return "Password is strong!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
@limiter.limit("5 per minute")  # Limit password checks to 5 per minute per IP
def check_password():
    try:
        data = request.get_json()
        password = data.get('password', '')

        # Evaluate password strength
        result = is_password_strong(password)

        # Return the result as JSON
        return jsonify({'result': result})
    except Exception as e:
        print(f"Error: {e}")  # Log the error for debugging
        return jsonify({'result': 'An error occurred. Please try again.'}), 500

if __name__ == '__main__':
    app.run(debug=True)