# IMF_category_harmoniser

This is a POC I did over 3 days as part of a hackathon for the International Monetary Fund. The hackathon was organised by [DataKind](https://www.datakind.org/). It was completed in close collaboration with [Kelly Butler](https://www.linkedin.com/in/kelly-e-butler/)

The code was originally stored on DataKind's Github, where the commits are.

## The project

The IMF wants to examine sex differences in consumption across countries. The IMF measures consumption/spending using predefined categories (e.g. "Health" or "Food and non alcoholic beverages"). The problem is that many countries do not follow the IMF categories and use their own categories! We can of course match them manually, but that is not a scalable solution. Here's where this project comes in!

This code uses OpenAI's latest (at time of coding) Embeddings API "Ada" to get embeddings for the IMF categories, as well as the categories in the target dataset. Then it uses those embeddings to match the categories in your dataset to the IMF ones. It does this by selecting the IMF category that is nearest in embedding space

I have written a simple streamlit app that allows you (or the IMF) to do this without using Python.

Fire it up locally and give it a go! Note that if you want to upload your own dataset, you'll need to input an OpenAI API key because Ada cost (a trivial amount of) money to run.
