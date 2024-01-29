# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import yfinance as yf

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/search_stocks', methods=['GET'])
def search_stocks():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query provided'}), 400

    # Fetch stock data using yfinance
    stock_info = yf.Ticker(query).info
    if 'error' in stock_info:
        return jsonify({'error': 'Stock not found'}), 404

    return jsonify(stock_info)

@app.route('/portfolio', methods=['GET', 'POST', 'DELETE'])
def manage_portfolio():
    # This function will handle adding, viewing, and removing stocks from the portfolio
    # For demonstration purposes, the portfolio is managed in memory (not persistent)
    if request.method == 'POST':
        # Add stock to portfolio logic here
        pass
    elif request.method == 'DELETE':
        # Remove stock from portfolio logic here
        pass
    else:  # GET method
        # View portfolio logic here
        pass

    return jsonify({'message': 'Portfolio management endpoint'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

# Note: This is a basic setup. In a production environment, more robust error handling, 
# database integration for persistent storage, and security measures would be necessary.
