from flask import Flask, request, jsonify
from database.db_init import db_init
from libs.appointment.usecase.index import get_available_slots_usecase, book_slot_usecase
from flask_cors import CORS

app = Flask(__name__)

# Set cors to allow api requests
CORS(app)

@app.route('/api/available-slots', methods=['GET'])
def available_slots():
    body = {"date": request.args.get('date')}

    try:
        response = get_available_slots_usecase(body)
        return jsonify(response), 200
    except Exception as e:
        return jsonify(e.args), 400


@app.route('/api/book', methods=['POST'])
def book_appointment():
    body = request.json

    try:
        response = book_slot_usecase(body)
        return jsonify(response), 200
    except Exception as e:
        return jsonify(e.args), 400


if __name__ == '__main__':
    db_init()
    app.run(debug=True)
