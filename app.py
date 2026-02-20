from flask import Flask, render_template, request, jsonify
from optimizer import optimise_portfolio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/optimise', methods=['POST'])
def optimise():
    data = request.get_json()
    
    tickers = [t.strip().upper() for t in data['tickers'].split(',')]
    
    if len(tickers) < 2:
        return jsonify({'error': 'Please enter at least 2 stock symbols.'})
    
    try:
        result = optimise_portfolio(tickers)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': f'Could not fetch data for one or more symbols. Please check your inputs. ({str(e)})'})

if __name__ == '__main__':
    app.run(debug=True)