# Interest-Level Prediction with Dash - Template
Due to the lacked of data and poor performance of the trained model, I have decided not to deploy this tab. General idea: The user will be able to attach image(s), YOLOv5 will extract additional features of interests, which will (hopefully) helps the ML make a more accurate prediction.

![](https://github.com/mnguyen0226/two_sigma_property_listing/blob/main/dash/assets/photos/experience_ilp_img.png)

## How to run
On your terminal, create a new python environment.
```
conda create -n predict_img_dash python=3.8
conda activate predict_img_dash
```

On your terminal, install all package.
```
pip install -r requirements.txt
```

On your terminal, run the dash application.
```
python dash_app.py
```