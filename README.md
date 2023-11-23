# Property Rental Interest Prediction Web App
A software to predict how popular an apartment retal listing based onthe listing content like text description, photos, number of bedrooms, price,.... The data is provided from renthop.com, an apartment listing site with the apartments are located in New York City.


## About
### Dataset
The datasets can be found [here]((https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip)).
- train.json: the training set.
- images_sample.zip: listing images organized by listing_id (a sample of 100 listings)
- Kaggle-renthop.7z: listing images organized by listing_id. Total size: 78.5 GB compressed.

## Development Phases

### Phase 1. EDA [ANALYSIS]
- Static plots, tables, analysis, and explaination.

### Phase 2. ML Modeling [ANALYSIS]
- Classical ML modeling.

### Phase 3. Image Feature Extraction + Re-train [ANALYSIS]
- Dataset analysis (pretrained model with PyTorch).

### Phase 4. Dash Visualization Development [UI + ANALYSIS]
- Dataset analysis
- What's the possible input-output interaction???

### Phase 5. Real-time Prediction (data, image) with Flask [UI]
- Task 1: Input feature > let stakeholder know if the people might be interested in such features
- Task 2: Input image > let stakeholder knows if the users is interested or not

### Phase 6. ChatGPT Image Generation Integration [UI + UX]
- If have time, may be develop from scratch - diffusion model.
- Initially: has a Q/A > generate images (based on the info we learn) - Model 2
- ChatBox functionality (model)

### Phase 7. Mobile Development [UI + UX]
- Task 1: Upload images and make prediction (help buyer evaluate the house).
- Task 2: Image generation based on input (help client the house)

## Architecture

## Reproduction

## Demo

## Presentation & Report

## References
[1] “Two Sigma Connect: Rental Listing Inquiries | Kaggle,” Kaggle.com, 2023. https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip (accessed Nov. 23, 2023).
‌