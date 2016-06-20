from flask import Flask
from is_prime import prime

app = Flask(__name__)


@app.route('/')
def hundred_primes():
    return str(prime(100))

if __name__ == '__main__':
    app.run(debug=True)
