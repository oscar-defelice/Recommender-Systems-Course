# 📚 Recommender Systems Course - Lecture Breakdown

This directory contains materials for each lecture in the **Recommender Systems** course. The course consists of **8 lectures**, each 3 hours long, covering the fundamentals, evaluation metrics, classical approaches, hybrid models, and modern deep learning techniques.

## 📖 Course Lectures

### 1️⃣ **Introduction to Recommender Systems**

📌 Overview of recommender systems and their real-world applications  
📌 Types of recommender systems (content-based, collaborative filtering, hybrid)  
📌 Business impact and challenges in recommendation  
📌 Datasets: MovieLens, Netflix Prize, Amazon Reviews  
📌 Hands-on: Setting up a simple rule-based recommender  

📂 **Materials:** `Lecture1_Intro/`

---

### 2️⃣ **Evaluation Metrics for Recommender Systems**

📌 Offline vs. online evaluation  
📌 Accuracy metrics: Precision, Recall, MAP, NDCG  
📌 Error-based metrics: RMSE, MAE  
📌 Beyond accuracy: diversity, novelty, serendipity, coverage  
📌 A/B testing and online evaluation  
📌 Hands-on: Implementing evaluation metrics in Python  

📂 **Materials:** `Lecture2_Evaluation/`

---

### 3️⃣ **Content-Based Filtering**

📌 How content-based filtering works  
📌 Feature extraction: TF-IDF, embeddings for text, images, audio  
📌 Cosine similarity and nearest neighbours  
📌 Strengths and weaknesses of content-based methods  
📌 Hands-on: Implementing a TF-IDF-based movie recommender  

📂 **Materials:** `Lecture3_ContentBased/`

---

### 4️⃣ **Collaborative Filtering**

📌 User-based vs. item-based collaborative filtering  
📌 Pearson correlation and similarity measures  
📌 Model-based methods: Matrix factorisation (SVD, ALS)  
📌 Cold start and sparsity issues  
📌 Hands-on: Implementing collaborative filtering with user-item data  

📂 **Materials:** `Lecture4_CollaborativeFiltering/`

---

### 5️⃣ **Hybrid Recommender Systems**

📌 Why hybrid models?  
📌 Strategies: weighted, switching, feature combination  
📌 Netflix Prize: How Netflix optimised recommendations  
📌 Hands-on: Implementing a hybrid recommender  

📂 **Materials:** `Lecture5_Hybrid/`

---

### 6️⃣ **LensKit Library for Recommender Systems**

📌 Introduction to LensKit and its advantages  
📌 Implementing content-based and collaborative filtering using LensKit  
📌 Evaluating recommendation models with LensKit  
📌 Hands-on: Training and evaluating models in LensKit  

📂 **Materials:** `Lecture6_LensKit/`

---

### 7️⃣ **Matrix Factorisation & Advanced Techniques**

📌 Matrix factorisation fundamentals: SVD, ALS  
📌 Factorisation Machines and Bayesian Personalised Ranking  
📌 Implicit feedback handling  
📌 Hands-on: Implementing matrix factorisation with Surprise  

📂 **Materials:** `Lecture7_MatrixFactorization/`

---

### 8️⃣ **Deep Neural Networks for Recommender Systems**

📌 Neural Collaborative Filtering (NCF)  
📌 Autoencoders and Variational Autoencoders (VAEs)  
📌 RNNs for sequential recommendations  
📌 Transformers in recommender systems  
📌 Hands-on: Building a deep learning-based recommender  

📂 **Materials:** `Lecture8_DeepLearning/`

---

## 🎯 Final Project

📌 Build and evaluate a custom recommender system  
📌 Apply concepts from previous lectures  
📌 Present results and insights  

📂 **Materials:** `FinalProject/`

---

## 📚 References

This course is built upon a mix of theoretical foundations, industry best practices, and hands-on implementations from various sources. Below are key references used throughout the lectures:

### 📖 **Books**

- Ricci, F., Rokach, L., & Shapira, B. (2015). *Recommender Systems Handbook*. Springer.
- Aggarwal, C. C. (2016). *Recommender Systems: The Textbook*. Springer.
- Okura, K., Tagami, Y., Ono, S., & Tajima, A. (2017). *Deep Neural Networks for YouTube Recommendations*. arXiv.

### 📄 **Academic Papers**

- Resnick, P., & Varian, H. R. (1997). *Recommender Systems*. Communications of the ACM, 40(3), 56-58.
- Sarwar, B. M., Karypis, G., Konstan, J. A., & Riedl, J. (2001). *Item-Based Collaborative Filtering Recommendation Algorithms*. WWW Conference.
- He, X., Liao, L., Zhang, H., Nie, L., Hu, X., & Chua, T. S. (2017). *Neural Collaborative Filtering*. WWW Conference.
- Koren, Y., Bell, R., & Volinsky, C. (2009). *Matrix Factorization Techniques for Recommender Systems*. IEEE Computer.

### 🔨 **Libraries & Tools**

- **[LensKit](https://lkpy.lenskit.org/)** - A Python toolkit for building and experimenting with recommender systems.
- **[Surprise](https://surpriselib.com/)** - A scikit-based Python library for collaborative filtering.
- **[TensorFlow Recommenders](https://www.tensorflow.org/recommenders/)** - TensorFlow-based deep learning models for recommendation tasks.

### 📂 **Datasets**

- **[MovieLens](https://grouplens.org/datasets/movielens/)** - Widely used dataset for evaluating recommender systems.
- **[Netflix Prize](https://www.netflixprize.com/)** - Historic dataset from the Netflix recommendation competition.
- **[Amazon Reviews](https://nijianmo.github.io/amazon/index.html)** - Large-scale e-commerce recommendation dataset.

### 🎓 **Online Courses & Tutorials**

- **[Coursera: Recommender Systems Specialization](https://www.coursera.org/specializations/recommender-systems)** - University of Minnesota.
- **[Fast.ai: Deep Learning for Recommender Systems](https://course.fast.ai/)** - Advanced deep learning applications.
- **[Google's Recommender Systems Course](https://developers.google.com/machine-learning/recommendation)** - Introduction to modern recommender techniques.

---

📌 *If you find useful references or additional resources that complement this course, feel free to contribute by adding them here!*
