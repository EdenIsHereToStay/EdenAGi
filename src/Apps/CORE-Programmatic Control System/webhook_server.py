from flask import Flask, request
import automate_powershell  # assuming your script is named automate_powershell.py and callable

app = Flask(__name__)

@app.route('/trigger_powershell', methods=['POST'])
def trigger_powershell():
    auth_token = request.headers.get('Authorization')
    if auth_token == 'YourSecureToken':  # Replace 'YourSecureToken' with a real token in practice
        automate_powershell.run_command('echo Hello, World!')  # call your script function
        return 'Command executed successfully!', 200
    return 'Unauthorized', 401

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # Runs in HTTPS mode
