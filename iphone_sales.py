import pandas as pd
import plotly.express as px
import statsmodels.api as sm

# Load the data
data = pd.read_csv("apple_products.csv")

# Filter the highest rated products
highest_rated = data.sort_values(by="Star Rating", ascending=False).head(10)

# Number of Ratings of Highest Rated iPhones
fig_ratings = px.bar(highest_rated, x="Product Name", y="Number Of Ratings", 
                     title="Number of Ratings of Highest Rated iPhones")
fig_ratings.show()

# Number of Reviews of Highest Rated iPhones
fig_reviews = px.bar(highest_rated, x="Product Name", y="Number Of Reviews", 
                     title="Number of Reviews of Highest Rated iPhones")
fig_reviews.show()

# Relationship between Sale Price and Number of Ratings of iPhones
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Sale Price", size="Discount Percentage", 
                    trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()

# Relationship between Discount Percentage and Number of Ratings of iPhones
figure = px.scatter(data_frame = data, x="Number Of Ratings",
                    y="Discount Percentage", size="Sale Price", 
                    trendline="ols", 
                    title="Relationship between Discount Percentage and Number of Ratings of iPhones")
figure.show()
