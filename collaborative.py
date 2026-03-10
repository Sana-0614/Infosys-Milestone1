import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def collaborative_recommendation(data, user_id, top_n=5):

    user_item = data.pivot_table(index='ID', columns='Name', values='Rating', fill_value=0)

    similarity = cosine_similarity(user_item)

    similarity_df = pd.DataFrame(similarity, index=user_item.index, columns=user_item.index)

    similar_users = similarity_df[user_id].sort_values(ascending=False)[1:5]

    recommended = []

    for user in similar_users.index:
        products = user_item.loc[user]
        products = products[products > 0].index
        recommended.extend(products)

    recommended = list(set(recommended))

    return recommended[:top_n]