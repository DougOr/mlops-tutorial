import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("models/model_v1.h5")

# Simulate deployment
print("Model deployed successfully!")
