# RentalGPT Dash App
I presents the data analysis, data visualization, and Dash application development called "RentalGPT", an interactive, user friendly dashboard that provides services to multiple stakeholders. Using the "Two Sigma Connect: Rental Listing Inquiries" dataset collected from Kaggle, we can do in-depth data analysis, interactive data visualization, and an app that has predictive analytics and virtual assistance.

## Data Science Life Cycle
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_science_life_cycle.png)

### Business Understanding & Data Acquisition
The datasets can be found [here]((https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip)).
- `train.json`: the training set.
- `images_sample.zip`: listing images organized by listing_id (a sample of 100 listings)
- `Kaggle-renthop.7z`: listing images organized by listing_id. Total size: 78.5 GB compressed.

**Note**: for this project, we will consider the training dataset as a full-dataset, as our goal is not to beat the competition, but to build a tool for data analysis and usages.

### Data Processing & Feature Engineering
Using various techniques
- Tabular Feature Extraction.
- Sentimental Extraction via HuggingFace's pretrained BERT (benchmark on SST dataset).
- Image Feature Extraction via PyTorch's YOLO.v5.

Codebase:

### EDA
Explore the dataset, reveal underlying information by plotting static plots for processed features. Here's the list of analysis: `outlider detection & removal`, `PCA`, `statistical test` (K-S, Shapiro-Witt, D'K^2), `Bar plot`, `Count plot`, `Pie chart`, `Distribution plot`, `Pair plot`, `Heatmap`, `Histogram with KDE`, `QQ plot`, `KDE`, `Regression plot with scatter representation and regression line`, `Boxen plot`, `Area plot`, `Violin plot`, `Joint plot with KDE and scatter representation`, `Rug plot`, `3D plot`, `Contour plot`, `Cluster map`, `Hexbin`, `Strip plot`, `Swarm plot`, `Subplots`.

Codebase:

### ML Modeling
I used Sklearn's SVM, Decision Tree, Random Forest, MLP, KNN.

**Type 1**: Based on the tabular input of the user (without extracted features from image), can we predict the interest level. 

Codebase:

**Type 2**: Based on the tabular input of the user and the image, can we predict the interest level.

Codebase:

**Type 3**: Based on the tabular input of the user (without extracted features from image), can we predict the price. 

Codebase:

**Type 4**: Based on the tabular input of the user and the image, can we predict the price.

Codebase:

### Dash App
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/rental_gpt_dash_architecture.png)

## How to  Run

## Deployment
### Deployment on GCP
1. Make sure you have a GCP account with some credit amount.
2. Go to Google Cloud Console > Create a New Project > Activate Cloud Shell
3. Create a new project
4. On the terminal, type `python3 -m venv .venv` to create a new Python environment.
5. On the terminal, type `. .venv/bin/activate` to activate your newly created environment.
6. Open Editor, add code for app.py, requirements.txt, Dockerfile.
7. On the terminal, install package via `pip install -r requirements.txt`
8. On the terminal, enable services through GCP terminal: `gcloud services enable
containerregistry.googleapis.com`
9. On the terminal, enable permission via `gcloud auth configure-docker`
10. On the terminal, build your docker image via `docker build -f Dockerfile -t
gcr.io/your-project/test:test .`
11. On the terminal, push your docker image via `docker push gcr.io/your-project/test:test`
12. On the terminal, deploy your application via `gcloud run deploy dashapp --image
gcr.io/your-project/test:test`
13. Your application has been successfully deployed!

### Deployment on Virginia Tech's Kubernetes Rancher
1. Consider reading through the Documentation - Cloud Quickstart.
2. Make sure you have DockerHub account and access to Virginia Tech's Kubernetes
Rancher (cloud.cs.vt.edu).
3. Make sure you have Docker Desktop installed locally. Open Docker Desktop and sign in
with your DockerHub to enable Docker daemon to run on the background.
4. On the terminal, build your docker image via `docker build -t
your-dockerhub-username/project-name .`
5. On the terminal, push your docker image via `docker push
your-dockerhub-username/project-name`
6. After granted access to cloud.cs.vt.edu via asking admin, create your Workload with the
port that you set on Dockerfile. The name of the image for the server to pull should also
be filled in here (such as your-dockerhub-username/project-name). Here, you can also
define your domain name.
7. Now, create the ingress, and select your workload. Activate 1 pod to initialize and run
your application.
8. Your application has been successfully deployed!

## Demo
### Overview Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/overview_page.png)

### Apartments Listing Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/apartments_listing_page.png)

### Data Analysis Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_analysis_page.png)

### Data Visualization Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_visualization_page.png)

### Interest Level Predicion Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/interest_level_prediction_page.png)

### Rental Cost Prediction
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/rental_cost_prediction_page.png)

### Virtual Assistant Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/virtual_assistant_page.png)


## Presentation & Report
[Presentation]()

[Report]()

## References
[1] “Two Sigma Connect: Rental Listing Inquiries | Kaggle,” Kaggle.com, 2023. https://www.kaggle.com/competitions/two-sigma-connect-rental-listing-inquiries/data?select=train.json.zip (accessed Nov. 23, 2023).

‌[2] [Huging Chat API](https://github.com/Soulter/hugging-chat-api)

[3] [HugChat Chatbot with Streamlit Blog](https://blog.streamlit.io/how-to-build-an-llm-powered-chatbot-with-streamlit/)

[4] [HugChat Chatbot with Streamlit Code](https://github.com/dataprofessor/hugchat/blob/master/app_v3.py)

[5] [OpenAssistant LLaMA 30B SFT 6](https://huggingface.co/OpenAssistant/oasst-sft-6-llama-30b-xor)

[6] [HuggingChat - New Open Source Alternative to ChatGPT](https://www.youtube.com/watch?v=7QChacb3-00)

[7] [Open Assistant](https://open-assistant.io/)

[8] [Dash with ChatGPT Code](https://github.com/plotly/dash-sample-apps/blob/main/apps/dash-gpt3-chatbot/app.py)

[9] [HugChat API Repository](https://github.com/Soulter/hugging-chat-api/tree/master)