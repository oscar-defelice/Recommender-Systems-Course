# KNN-Based Recommender System on Simulated Search Engine Corpus

# ✅ Import Libraries
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# ✅ 1. Load the Corpus
# (Assuming 'documents' is a list of 150 documents generated earlier)

# Simulated document corpus
# Replace with actual corpus if available
documents = [
    "Machine learning is evolving rapidly with new research.",
    "Quantum computing holds the key to future computational power.",
    "Natural language processing enables machines to understand human text.",
    "Climate change poses significant global challenges.",
    "Cybersecurity is critical in the digital age.",
    "Data science blends statistics and computer science for insights.",
    "Artificial intelligence is reshaping modern industries.",
    "Neural networks mimic human brain functions in AI.",
    "Graph theory is vital in network analysis.",
    "Space exploration pushes the boundaries of human knowledge.",
]

# ✅ 2. Vectorize Documents and Queries
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

# Example queries
queries = [
    "machine learning",
    "quantum computing",
    "natural language processing",
    "climate change",
    "cybersecurity",
    "data science",
    "artificial intelligence",
    "neural networks",
    "graph theory",
    "space exploration",
]

# Vectorize queries
query_vectors = vectorizer.transform(queries)

# ✅ 3. Initialize KNN
knn = NearestNeighbors(n_neighbors=5, metric="cosine")
knn.fit(doc_vectors)


# ✅ 4. Function to Get Top-N Recommendations
# 💡 Complete this function to return top-N nearest documents
def knn_recommender(query_vector, doc_vectors, top_n=5):
    """Return top-N recommendations for a query using KNN."""
    distances, indices = knn.kneighbors(query_vector, n_neighbors=top_n)
    return distances, indices


# ✅ 5. Test KNN with an Example Query
query_index = 0  # "machine learning"
query_vec = query_vectors[query_index]

# Call the KNN recommender
# 💡 Complete the function call below
distances, indices = knn_recommender(query_vec, doc_vectors, top_n=5)

# Display recommendations
print(f"\n🔍 Top 5 Recommendations for Query: '{queries[query_index]}'")
for i, idx in enumerate(indices[0]):
    relevance_score = 1 - distances[0][i]  # Cosine similarity
    print(f"{i+1}. Doc {idx+1} (Relevance Score: {relevance_score:.4f})")
    print(f"Content: {documents[idx]}\n")

# ✅ 6. Evaluate Using Graded Relevance
# 💡 Complete the evaluation metrics


def precision_recall_at_k(graded_relevance, k, threshold=0.3):
    """Compute Precision@K and Recall@K."""
    relevance_at_k = graded_relevance[:k]
    relevant_at_k = sum(score >= threshold for score in relevance_at_k)
    precision = relevant_at_k / k
    recall = (
        relevant_at_k / sum(score >= threshold for score in graded_relevance)
        if sum(score >= threshold for score in graded_relevance) > 0
        else 0
    )
    return precision, recall


# Graded relevance (cosine similarity)
cosine_similarities = cosine_similarity(query_vec, doc_vectors).flatten()

# 💡 Compute Precision@5 and Recall@5
precision, recall = precision_recall_at_k(cosine_similarities[indices[0]], k=5)
print(f"Precision@5: {precision:.2f}")
print(f"Recall@5: {recall:.2f}")


# ✅ 7. NDCG@K (Graded Relevance)
# 💡 Complete the NDCG function
def ndcg_at_k(graded_relevance, k):
    """Compute NDCG@K for ranked documents."""
    r = np.asfarray(graded_relevance)[:k]
    dcg = np.sum(r / np.log2(np.arange(2, r.size + 2)))
    ideal_r = sorted(graded_relevance, reverse=True)[:k]
    idcg = np.sum(np.array(ideal_r) / np.log2(np.arange(2, len(ideal_r) + 2)))
    return dcg / idcg if idcg > 0 else 0


# Calculate NDCG@5
ndcg = ndcg_at_k(cosine_similarities[indices[0]], k=5)
print(f"NDCG@5 (Graded): {ndcg:.2f}")

# ✅ 8. Visualize NDCG Scores Across Queries
ndcg_scores = []

for i, query in enumerate(queries):
    query_vec = query_vectors[i]
    distances, indices = knn_recommender(query_vec, doc_vectors, top_n=5)
    graded_relevance = 1 - distances[0]
    ndcg = ndcg_at_k(graded_relevance, k=5)
    ndcg_scores.append(ndcg)

# Plot the results
plt.figure(figsize=(10, 6))
plt.barh(queries, ndcg_scores, color="skyblue")
plt.xlabel("NDCG@5 (Graded)")
plt.title("KNN Recommender: NDCG@5 Scores Across Queries")
plt.show()

# ✅ STUDENT TASKS:
# 1. Complete the knn_recommender function.
# 2. Implement the evaluation functions.
# 3. Test different K values in KNN.
# 4. Experiment with TF-IDF parameters (e.g., ngram_range).
# 5. Bonus: Implement user-defined relevance thresholds.


def precision_recall_at_k(
    graded_relevance: list[float],
    ground_truth: list[float],
    k: int,
    threshold: float = 0.3,
) -> tuple[float, float]:
    """precision_recall_at_k

    Parameters
    ----------
    graded_relevance : list[float]
        The graded relevance scores (e.g., from TF-IDF or cosine similarity) of the documents.
    ground_truth : list[float]
        The ground truth relevance scores for the documents (e.g., binary or graded).
    k : int
        The number of top documents to consider.
    threshold : float, optional
        The relevance threshold for a document to be considered highly relevant, by default 0.3

    Returns
    -------
    tuple[float, float]
        The precision and recall at k.
    """
    # Select top-k documents based on graded relevance
    relevance_at_k = graded_relevance[:k]

    # Count true positives (documents that are both recommended and relevant in ground truth)
    true_positives = sum(
        1
        for idx, score in enumerate(relevance_at_k)
        if score >= threshold and ground_truth[idx] > 0
    )

    # Precision: proportion of recommended documents that are relevant
    precision = true_positives / k

    # Recall: proportion of all relevant documents retrieved in top-k
    total_relevant = sum(1 for score in ground_truth if score > 0)
    recall = true_positives / total_relevant if total_relevant > 0 else 0

    return precision, recall


def average_precision_at_k(
    graded_relevance: list[float], k: int, threshold: float = 0.3
) -> float:
    """average_precision_at_k

    Parameters
    ----------
    graded_relevance : list[float]
        The graded relevance scores of the documents.
    k : int
        The number of top documents to consider.
    threshold : float, optional
        The relevance threshold for a document to be considered highly relevant, by default 0.3

    Returns
    -------
    float
        The average precision at k.
    """
    precision_at_k = []
    for i in range(1, k + 1):
        precision, _ = precision_recall_at_k(graded_relevance, i, threshold)
        precision_at_k.append(precision)
    return sum(precision_at_k) / k


def ndcg_at_k(
    graded_relevance: list[float], ground_truth: list[float], k: int
) -> float:
    """Compute Normalized Discounted Cumulative Gain (NDCG) at rank k comparing TF-IDF scores to ground truth.

    Parameters
    -----------
    graded_relevance : list[float]
       The graded relevance scores of the documents.
    ground_truth : list[float]
        The ground truth relevance scores of the documents.
    k : int
        The number of top documents to consider.

    Returns
    -------
    float
        The NDCG@k score.
    """
    r = np.asfarray(graded_relevance)[:k]  # TF-IDF relevance scores for the top-k items
    dcg = np.sum(r / np.log2(np.arange(2, r.size + 2)))

    # Ideal DCG using ground truth relevance scores
    ideal_r = sorted(ground_truth, reverse=True)[:k]
    idcg = np.sum(np.array(ideal_r) / np.log2(np.arange(2, len(ideal_r) + 2)))

    return dcg / idcg if idcg > 0 else 0
