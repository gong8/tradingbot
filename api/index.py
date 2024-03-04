from flask import Flask
import numpy as np
import tensorflow as tf
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    # Create a simple model
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])

    # Compile the model
    model.compile(optimizer='sgd', loss='mean_squared_error')

    # Provide the data
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

    # Train the model
    model.fit(xs, ys, epochs=500)

    # Use the model to make a prediction
    return str(model.predict([10.0]))

@app.errorhandler(500)
def internal_server_error(error):
    app.logger.error('Server Error: %s', (error))
    return "500 error", 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


