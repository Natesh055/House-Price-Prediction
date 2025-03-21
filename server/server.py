from flask import Flask, request, jsonify
import util
from flask_cors import CORS  # Importing flask_cors

app = Flask(__name__)

# Enable CORS for all origins
CORS(app)  # This will enable CORS for all routes by default

# Alternatively, you can restrict it to specific origins (like 127.0.0.1:5500)
# CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500"}})

@app.route("/getlocationnames")
def getlocationnames():
    try:
        locations = util.getlocationnames()
        response = jsonify({
            "locations": locations
        })
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/predicthomeprice", methods=['POST'])
def predicthomeprice():
    try:
        # Extracting data from JSON request body
        data = request.get_json()
        total_sqft = float(data['total_sqft'])
        location = data['location']
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        # Calculating the estimated price
        estimated_price = util.getestimatedprice(location, total_sqft, bhk, bath)

        response = jsonify({
            "Estimated Price": estimated_price
        })
        return response

    except KeyError as e:
        return jsonify({"error": f"Missing required field: {str(e)}"}), 400
    except ValueError:
        return jsonify({"error": "Invalid data type for one of the inputs."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run(debug=True)
