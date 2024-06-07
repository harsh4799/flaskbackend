from flask import Flask, jsonify
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/financials', methods=['GET'])
@cross_origin()
def get_financials():
    data = {
        "ticker": "AAPL",
        "market_ap": 2.5,
        "shares_outstanding": 317,
        "pe_ratio": 1.2,
        "ps_ratio": 33.5,
        "pb_ratio": 7.9,
        "peg_ratio": 5.5,
        "current_ratio": 7.1,
        "debt_to_equity_ratio": 2.1,
        "eps": 1.7,
        "news": {
            "article1": {"sentiment": {"score": 0.9, "value": "positive"}, "summary": "This is Article1"},
            "article2": {"sentiment": {"score": 0.67, "value": "negative"}, "summary": "This is Article2"},
            "article3": {"sentiment": {"score": 0.559, "value": "positive"}, "summary": "This is Article3"}
        },
        "analyst_estimates": {
            "Citibank": 6.5,
            "Goldman Sachs": 7.9,
            "Morgan Stanley": 9.87,
            }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)