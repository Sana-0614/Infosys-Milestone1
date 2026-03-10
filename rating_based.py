import pandas as pd

def rating_recommendation(data, top_n=5):

    top_products = data.sort_values(by='Rating', ascending=False)

    return top_products[['Name','Brand','Rating']].head(top_n)