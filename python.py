from flask import Flask, render_template, request

app = Flask(__name__)

# Mock data of native plants (replace with actual data)
native_plants_data = {
    'New York': ['Eastern Redbud', 'Red Maple', 'Sugar Maple', 'Eastern White Pine'],
    'California': ['California Poppy', 'California Sagebrush', 'Coast Redwood', 'California Buckeye']
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plants', methods=['POST'])
def get_native_plants():
    location = request.form['location']
    native_plants = native_plants_data.get(location, [])
    return render_template('plants.html', location=location, native_plants=native_plants)

if __name__ == '__main__':
    app.run(debug=True)
