import openai
import pandas as pd
import streamlit as st

def generate_category_embeddings(categories):
    category_embeddings = openai.Embedding.create(input=categories, engine="text-embedding-ada-002") # create embeddings for all categories, if we pass it a list it 
    return category_embeddings

def clean_embeddings(categories, embeddings):
    cleaned_embeddings = [category['embedding'] for category in embeddings['data']]
    
    embeddings_df = pd.DataFrame(columns=categories)
    
    for i in range(len(categories)):
        embeddings_df[categories[i]] = cleaned_embeddings[i]
    
    return embeddings_df

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

@st.cache_data
def load_IMF_sub_category_embeddings():
    # Loads a dataframe of sub categories and their embeddings
    return pd.read_csv("/Users/ThomasRichardson/Library/CloudStorage/GoogleDrive-thomas.richardson.interesting@gmail.com/My Drive/data science/DataDives/IMF DataDive Sep 2023/category_mapper_app/subcategory_embeddings.csv")

@st.cache_data
def load_IMF_category_mapping_table():
    # Loads in a table that maps sub categories to primary categories
    return pd.read_csv("/Users/ThomasRichardson/Library/CloudStorage/GoogleDrive-thomas.richardson.interesting@gmail.com/My Drive/data science/DataDives/IMF DataDive Sep 2023/category_mapper_app/IMF_categories.csv")

def match_categories(category_embeddings_clean, imf_sub_cats):
    #TODO this function needs to be made, it needs to match categories and return a df of category_embeddings_clean in one col and the imf_sub_cats that best matches in other col
    print(True)
    
    
def map_primary_categories(matched_categories):
    # TODO
    
    # take matched categories and left join on category_mapping_table so we have a df of the data's categories, and the IMF primary and sub categories that match them.
    category_mapping_table = load_IMF_category_mapping_table()
    
    return 

def attach_categories(df, matched_categories):
    
    df_categories_mapped = df.merge()
    
    return df_categories_mapped
