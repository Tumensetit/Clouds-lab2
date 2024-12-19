import math
from flask import Flask, request, jsonify

app = Flask(__name__)

def numerical_integration(lower, upper, n):
    totalArea = 0
    width = (upper - lower) / n

    for i in range(n):
        x = lower + i * width
        height = abs(math.sin(x))
        totalArea += height * width

    return totalArea

@app.route('/<lower>/<upper>', methods=['GET'])
def get_integral(lower, upper):
    lower = float(lower)
    upper = float(upper)
    nValues = [10, 100, 1000, 10000, 100000, 1000000]
    results = []

    for n in nValues:
        result = numerical_integration(lower, upper, n)
        results.append({
            'n': n,
            'result': result
        })
    
    return jsonify({
        'lower': lower,
        'upper': upper,
        'results': results
    })

if __name__ == '__main__':
    app.run(debug=True)
