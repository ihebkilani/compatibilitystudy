<h1 align="center">Welcome to users compatibility study 👋</h1>
<p>
We want to study the compatibility of a user called A with another user B.
I am interested in calculating similarity between 2 vectors of users traits: UserB(T1_B,T2_B) and OptUser(Rot(T1_A),-Rot(T2_A)). I used cosine_similarity as distance metric. However this similarity has to be a number between 0 and 1. Therefore cosine can't be the perfect metric (it is between -1 and 1). So, I opt to use angular distance metric. It can be used to compute a similarity function bounded between 0 and 1, inclusive. 
 * angular_distance = cos^-1(cosine_similarity)/Pi
 * angular_similarity = 1- angular_distance 
</p>

## Install
```sh
pip install -r requirements.txt
```


## Requirements
Setting environment variables of `flask` : 
```sh
export FLASK_ENV=development
export FLASK_APP=$(pwd)/app.py
```

## Run project 
```sh
flask run
```


## Author

👤 **Iheb KILANI**
