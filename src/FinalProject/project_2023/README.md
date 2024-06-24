# Final Project

<p align="center">
    <img width="721" alt="cover-image" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Tom%27s_Restaurant%2C_NYC.jpg/1280px-Tom%27s_Restaurant%2C_NYC.jpg">
</p>

The objective of this project is to build a recommendation engine to predict what restaurants customers are most likely to order from given the customer location, restaurant information, and the customer order history.

You should imagine that this is a client project and that you are working with a team of data scientists to build a recommendation engine. You will be expected to present your work to the client and to the data science team.

This solution will allow your client, an app-based food delivery service, to customise restaurant recommendations for each of their customers and ensure a more positive overall user experience.

## Data

There are ~$10,000$ customers in the test set. These are the customers you will need to recommend a vendor to. Each customer can order from multiple locations, identified by the variable `LOC_NUM`.

There are ~$35,000$ customers in the train set.
Some of these customers have made orders at at least one of $100$ vendors.

As said, the aim of this project is to build a recommendation engine to predict what restaurants customers are most likely to order from, given the customer location, the restaurant, and the customer order history.

Data files are available at [this link](https://mega.nz/file/ZRhgESqR#iuO6pBaZbeEttJ_BGmwbSh2XTg4tnf_zXrzSXcq5W6M) and are structured as follows:

* `test_customers.csv`- customer id’s in the test set.
* `test_locations.csv` - latitude and longitude for the different locations of each customer.
* `train_locations.csv` - customer id’s in the test set.
* `train_customers.csv` - latitude and longitude for the different locations of each customer.
* `orders.csv` - orders that the customers `train_customers.csv` from made.
* `vendors.csv` - vendors that customers can order from.
* `VariableDefinitions.txt` - Variable definitions for the datasets
* `SampleSubmission.csv` - is an example of what your submission file should look like. The order of the rows does not matter, but the names of CID X LOC_NUM X VENDOR must be correct. The column "target" is your prediction.

## Evaluation

The error metric for this competition is the $F_1$ score, which ranges from 0 (total failure) to 1 (perfect score). Hence, the closer your score is to $1$, the better your model.

* **F1 Score**: A performance score that combines both precision and recall. It is a harmonic mean of these two variables. The formula is given as:

$$F_1 = 2 \frac{PR}{P + R}\, .$$

* **Precision**: This is an indicator of the number of items correctly identified as positive out of total items identified as positive. The formula is given as:

$$P = \frac{TP}{TP+FP}\, .$$

* **Recall** / Sensitivity / True Positive Rate (TPR): This is an indicator of the number of items correctly identified as positive out of total actual positives. The formula is given as:

$$R = \frac{TP}{TP+FN}\, .$$

Where:

TP=True Positive
FP=False Positive
TN=True Negative
FN=False Negative

Your submission file should look like:

```csv
CID X LOC_NUM X VENDOR     target
A7B8IGM X 0 X 105            0
NS70FA9 X 0 X 105            1
WTWOE69 X 0 X 105            0
```

Where $1$ indicates that a customer will order from that restaurant and $0$ that they will not order from that restaurant.
