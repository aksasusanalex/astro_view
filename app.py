from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return render_template('index.html')  # Your friend will create this

# API route to get space fact
@app.route('/get_fact', methods=['POST'])
def get_fact():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')

    # Example fun fact (you can customize later)
    fact = "Mars sunsets are blue! Learn more at https://mars.nasa.gov"
    location = f"Latitude: {lat}, Longitude: {lon}"

    return jsonify({"location": location, "fact": fact})

if __name__ == "__main__":
    app.run(debug=True)
