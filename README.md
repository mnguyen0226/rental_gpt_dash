# RentalGPT Dash App 

[Selected as Plotly’s Top ChatGPT & Generative AI Project](https://plotly.com/examples/generative-ai-chatgpt/)

I present the data analysis, data visualization, and Dash application development called "RentalGPT", an interactive, user friendly dashboard that provides services to multiple stakeholders. Using the "Two Sigma Connect: Rental Listing Inquiries" dataset collected from Kaggle, we can do in-depth data analysis, interactive data visualization, and an app that has predictive analytics and virtual assistance.

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

[Notebooks](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/notebooks)

### EDA
Explore the dataset, reveal underlying information by plotting static plots for processed features. Here's the list of analysis: `outlider detection & removal`, `PCA`, `statistical test` (K-S, Shapiro-Witt, D'K^2), `Bar plot`, `Count plot`, `Pie chart`, `Distribution plot`, `Pair plot`, `Heatmap`, `Histogram with KDE`, `QQ plot`, `KDE`, `Regression plot with scatter representation and regression line`, `Boxen plot`, `Area plot`, `Violin plot`, `Joint plot with KDE and scatter representation`, `Rug plot`, `3D plot`, `Contour plot`, `Cluster map`, `Hexbin`, `Strip plot`, `Swarm plot`, `Subplots`.

[Notebooks](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/notebooks), [Codebase](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/eda)

### ML Modeling
I used Sklearn's SVM, Decision Tree, Random Forest, MLP, KNN.
- **Type 1**: Based on the tabular input of the user (without extracted features from image), can we predict the interest level. 
- **Type 2**: Based on the tabular input of the user and the image, can we predict the interest level.
- **Type 3**: Based on the tabular input of the user (without extracted features from image), can we predict the price. 
- **Type 4**: Based on the tabular input of the user and the image, can we predict the price.

[Notebooks](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/notebooks)

### Dash App
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/rental_gpt_dash_architecture.png)

[Codebase](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/dash)

## How to  Run
Instructions to run Dash app can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/dash).

Instructions run EDA scripts can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/eda).

Pre-run notebooks with results can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/notebooks).

Instructions to run HuggingFace Chatbot with Dash template can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/experimentation/dash_llama_chatbot).

Instructions to run Interest-Level Prediction with Dash template can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/experimentation/interest_level_prediction_with_images).

Instructions to run Interest-Level Prediction with Dash template can be found [here](https://github.com/mnguyen0226/rental_gpt_dash/tree/main/experimentation/streamlit_llama_chatbot).

## Demo
### Overview Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/overview_page.png)

### Apartments Listing Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/apartments_listing_page.png)

### Data Analysis Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_analysis_page.png)

### Data Visualization Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/data_visualization_page.png)

### Interest Level Prediction Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/interest_level_prediction_page.png)

### Rental Cost Prediction
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/rental_cost_prediction_page.png)

### Virtual Assistant Page
![](https://raw.githubusercontent.com/mnguyen0226/rental_gpt_dash/main/dash/assets/photos/virtual_assistant_page.png)

## Presentation & Report
[Presentation](https://drive.google.com/file/d/1HcpBD1MUuS_IeT_DyAOe_HxpaHu78R9W/view?usp=sharing)

[Report](https://github.com/mnguyen0226/rental_gpt_dash/blob/main/docs/report.pdf)

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
