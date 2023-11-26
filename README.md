# Property Rental Interest Prediction Web App
A software to predict how popular an apartment retal listing based onthe listing content like text description, photos, number of bedrooms, price,.... The data is provided from renthop.com, an apartment listing site with the apartments are located in New York City. Specifically, for a listing_id, we want to know whether the customer has a `low`, `medium`, or `high` interest.

Research Questions:
- 1. Data Analysis (DONE)
- 2. Model 1: Based on the tabular input of the user (without extracted features from image), can we predict the interest level. 
  - Customer: Agent
  - Classical ML.
- 3. Model 2: Based on the tabular input of the user and the image, can we predict the interest level.
  - Customer: Agent
  - Yolo
  - Classical ML
  - Dataset with images only
- 4. Model 3: Based on the input data, can we generate the image of the room?
  - Fine-tune Deep Learning
  - Customer: Agent
- 5. Model 4: Usage of ChatGPT 
  - Customer: Renter
  - Customer service bot to answer the FAQs about the NYC rental market using the dataset as knowledge base and analysis.
  - Hard: from the chat, provide the listing of the relevant property to select?
    - https://www.youtube.com/watch?v=EE1Y2enHrcU
    - https://www.youtube.com/watch?v=4qNwoAAfnk4&t=17s

## About
### Dataset
The datasets can be found [here]((https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip)).
- `train.json`: the training set.
- `images_sample.zip`: listing images organized by listing_id (a sample of 100 listings)
- `Kaggle-renthop.7z`: listing images organized by listing_id. Total size: 78.5 GB compressed.

**Note**: for this project, we will consider the training dataset as a full-dataset, as our goal is not to beat the competition, but to build a tool for data analysis and usages.

## Development Phases

### Phase 1. EDA [ANALYSIS]
- Explore the dataset, reveal underlying information by plotting static plots for the following feature type, and preprocess the dataset.


### Phase 2. Image Feature Extraction + Re-train [ANALYSIS]
- Dataset analysis (pretrained model with PyTorch).

### Phase 3. ML Modeling [ANALYSIS]
- Classical ML modeling.

### Phase 4. Dash Visualization Development [UI + ANALYSIS]
- Dataset analysis
- What's the possible input-output interaction???

### Phase 5. Real-time Prediction (data, image) with Flask [UI]
- Task 1: Input feature > let stakeholder know if the people might be interested in such features
- Task 2: Input image > let stakeholder knows if the users is interested or not
- **Question: Why do we need to store the database in the first place? What are we storing though?**
  - Maybe to retrain the model? (new tab for new dataset to be added).

### Phase 6. ChatGPT Image Generation Integration [UI + UX]
- If have time, may be develop from scratch - diffusion model.
- Initially: has a Q/A > generate images (based on the info we learn) - Model 2
- ChatBox functionality (model)

### Phase 7. Mobile Development [UI + UX]
- Task 1: Upload images and make prediction (help buyer evaluate the house).
- Task 2: Image generation based on input (help client the house)

### Phase 8. PyTest

## Architecture

## Reproduction

## Demo

## Presentation & Report

## References
[1] “Two Sigma Connect: Rental Listing Inquiries | Kaggle,” Kaggle.com, 2023. https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip (accessed Nov. 23, 2023).
‌