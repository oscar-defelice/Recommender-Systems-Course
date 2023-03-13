# Final project

Here we propose a final project for the course.

---

## Goals and motivations

This is meant as an extended exercise collecting and summarising the content of the whole course.
The aim is to give each student the freedom to choose the best solution he is comfortable with and to justify the choice with some data-driven consideration.

## Project scheme

Here we describe how the project should be developed, or better what are the expected inputs and outputs.
Each student should deliver a project that corresponds to the project scheme.
We are inspired by [Kaggle Competitions](https://www.kaggle.com/competitions), so we will use the same format.

### Inputs

Data are provided by the course.
The idea is to use such data to solve a problem.

We will use the following data structures:

- **DataProject**: a directory containing one or more csv files.
  - `train.csv`: training data with labels.
  - `test.csv`: test data with no labels.
  - `sample_submission.csv`: sample submission.
- **Data description**: a csv file containing a description of the data.

### Outputs

These are the expected outputs of the project.

- **Submission**: a csv file containing the results of the project, according to the sample submission format.
- **FinalProject_Notebook**: a notebook file containing analysis, relevant choices and results comments and explanations.
- **_Optional_**:
  - **{NAME}\_model.joblib**: a file containing the trained model in the form of a pipeline.
  - **{NAME}\_model.h5**: a file containing the trained model in the form of a keras model.
  - **{NAME}\_model**: a directory containing the trained model in the form of a tensorflow SavedModel.

---

#### Hint to save the model

##### Sklearn pipeline

One can save the model pipeline (so all the relevant feature engineering and preprocessing steps can be executed automatically) in a file with the following example code:

```python
from sklearn.externals import joblib
pipe = Pipeline([
                ('scaler', StandardScaler()),
                ('model', LogisticRegression())
                ])

pipe.fit(X_train, y_train)
pipe.predict(X_test) # Not compulsory to save the model.

joblib.dump(pipe, '{NAME}_model.joblib')
```

##### Tensorflow and keras models

For tensorflow and keras models there are a few different ways to save the model on a file.
One can have a look at [this useful link](https://www.tensorflow.org/tutorials/keras/save_and_load) with examples from official documentation.

One of the most popular and intuitive way of saving the model is using the keras api of tensorflow.

```python
# Create and train a new model instance.
model = create_model()
model.fit(train_images, train_labels, epochs=5)

# Save the entire model as a SavedModel.
model.save('path_to_model_dir/my_model')
```
