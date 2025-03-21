from flask import Flask,request,jsonify
import util
app = Flask(__name__)
@app.route("/getlocationnames")

def getlocationnames():
    response = jsonify({
        "locations" : util.getlocationnames()
    })
    response.headers.add("Access Control Allow Origin",'.')
    return response

@app.route("predicthomeprice",method=['POST'])
def predicthomeprice():
    total_sqft = float(request.form['total_sqft'])
    location = (request.form['location'])
    bhk = float(request.form['bhk'])
    bath = float(request.form['bath'])


response = jsonify({
    "Estimated Price":util.getestimatedprice(location,total_sqft,bhk,bath)
})


if __name__ == "__main__":
    print("Starting Python Flask Server")
    app.run()