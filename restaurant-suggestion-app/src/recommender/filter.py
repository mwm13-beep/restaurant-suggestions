import pandas as pd
import os

if not os.path.exists('data'):
    os.mkdir('data')

# Load the business data
print('Loading business data...')
businesses = pd.read_json(r'C:\Users\mwm13\OneDrive\Desktop\data\yelp\yelp_academic_dataset_business.json', lines=True)

# Keep only the businesses that are restaurants
print('Filtering out non-restaurants...')
restaurants = businesses[businesses['categories'].str.contains('Restaurants', na=False)]

# Free memory by deleting the original business data
del businesses

# Load the tip data
print('Loading tip data...')
tips = pd.read_json(r'C:\Users\mwm13\OneDrive\Desktop\data\yelp\yelp_academic_dataset_tip.json', lines=True)

# Keep only the tips that are about restaurants
print('Filtering out non-restaurant tips...')
restaurant_tips = tips[tips['business_id'].isin(restaurants['business_id'])]

del tips

merged_data = pd.merge(restaurant_tips, restaurants, on='business_id', how='inner')

# Load the review data in chunks
chunksize = 10 ** 6  # adjust this value depending on your available memory
chunks = []
count = 1
print('Loading review data in chunks...')
for chunk in pd.read_json(r'C:\Users\mwm13\OneDrive\Desktop\data\yelp\yelp_academic_dataset_review.json', lines=True, chunksize=chunksize):
    print(f'Processing chunk {count}...')
    # Filter out reviews about non-restaurants
    chunk = chunk[chunk['business_id'].isin(restaurants['business_id'])]
    chunks.append(chunk)
    count += 1

# Merge the review chunks
print('Concatenating chunks...')
reviews = pd.concat(chunks, ignore_index=True)

# Keep only the reviews that are about restaurants
print('Filtering out reviews about non-restaurants...')
restaurant_reviews = reviews[reviews['business_id'].isin(restaurants['business_id'])]

# Load the checkin data
print('Loading checkin data...')
checkins = pd.read_json(r'C:\Users\mwm13\OneDrive\Desktop\data\yelp\yelp_academic_dataset_checkin.json', lines=True)

# Keep only the tips that are about restaurants
print('Filtering out non-restaurant checkins...')
restaurant_checkins = checkins[checkins['business_id'].isin(restaurants['business_id'])]

# Load the user data in chunks
chunksize = 10 ** 6  # adjust this value depending on your available memory
chunks = []
count = 1
print('Loading user data in chunks...')
for chunk in pd.read_json(r'C:\Users\mwm13\OneDrive\Desktop\data\yelp\yelp_academic_dataset_user.json', lines=True, chunksize=chunksize):
    print(f'Processing chunk {count}...')
    chunks.append(chunk)
    count += 1

# Merge the user chunks
print('Concatenating chunks...')
users = pd.concat(chunks, ignore_index=True)
