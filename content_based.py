import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def content_based_recommendation(data, item_name, top_n=5):

    if item_name not in data['Name'].values:
        print("Item not found")
        return pd.DataFrame()

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['Tags'])

    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

    index = data[data['Name'] == item_name].index[0]

    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    top_items = scores[1:top_n+1]

    product_indices = [i[0] for i in top_items]

    return data.iloc[product_indices][['Name','Brand','ReviewCount']]