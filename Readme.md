## JEE Mains 2020 College Predictor 

![Web Demo](data/demo.gif)

## Technology Stack
- Python
- HTML
- CSS
- Bootstrap
- Jinja 
- Flask
- ML Libraries: numpy, pandas, sk-learn, matplotlib

## How it Works
- We take the input the percentile, rank(if provided), gender, quota, home state.
- If the rank is not provided we calaculate it based on the percentile of 2019s data of rank vs percentile using linear regression.
- The dataset found on JoSAAs wesbite is used to determine the college and branch that you are likely to get.
- The dataframe is sent back and the sorting order is based on the user's input.

## For Local Use:
- Clone this Github repository
- Open the command line and get into this repository
- run `pip3 install -r requirements.txt` to grab all the necessary packages required
- If you are using virtual environment for the first time (otherwise skip the first command below):
```
virtualenv venv -p C:/Users/username/AppData/Local/Programs/Python/Python38/python.exe
```
- Then:
```
.\venv\Scripts\activate
cd app
set FLASK_ENV=development
flask run
```
## Todo
- [ ] Mobile Optimization
- [ ] Having more features in dataset
- [ ] SEO Friendly

Pull requests are more than welcome! :octocat:

