# Set Initial Parameters (W, X), use tf.Variable to track these variables
tf.random.set_seed(1234)  # for consistent results
W = tf.Variable(tf.random.normal((num_users, num_features), dtype=tf.float64), name="W")
X = tf.Variable(
    tf.random.normal((num_movies, num_features), dtype=tf.float64), name="X"
)
b = tf.Variable(tf.random.normal((1, num_users), dtype=tf.float64), name="b")

# Instantiate an optimizer.
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-1)
