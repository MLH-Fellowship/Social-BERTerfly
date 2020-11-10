# Social BERTerfly 🦋

![Open In Colab](https://img.shields.io/github/issues-closed/MLH-Fellowship/Social-BERTerfly?style=for-the-badge)
![](https://img.shields.io/github/issues-pr-closed/MLH-Fellowship/Social-BERTerfly?color=green&style=for-the-badge)
 
*Predicts your personality out of the 16 Myers-Briggs Type Personalities by your Twitter handle and compares your personality types with your followers*

> It utilizes machine learning classifier and NLP using the state of the art language model - **BERT** (Bidirectional Encoder Representations from Transformers) to predict the personality type of the given user based on their recent tweets.

## Getting Started: 🙌

### How to run locally:

Follow the below steps to run and explore your personality types, as well as that of your friends!

- `git clone https://github.com/MLH-Fellowship/Social-BERTerfly.git`

- Install our model weights from the following Drive link:

  [BERT_base_model](https://drive.google.com/file/d/1yDt-fs0lYFGgplwlteKRd7xSxH8RVcIf/view?usp=sharing)

- Place the downloaded `.h5` model under `server/models/`.
- Navigate to the server folder by:

  `cd server/`
- Install dependencies by: 

  `pip install -r requirements.txt`
(you can install the packages in a virtualenv if you prefer)

- Run the following in your terminal:

  `flask run`
  
  or,
  `python app.py`
  
- Wait around 15 seconds for the model to load.
- Visit the application at `http://127.0.0.1:5000/` and enjoy exploring various personality traits for you and your followers!

### An Example:

<pls put screenshots here>


### Start contributing! 📣 

If you wish to contribute to our model, you can take a look at our notebook, and provide suggestions or comments.

  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/10Dj-ySjfZVqOWg25ywmPsdrnk9XJoFP-?usp=sharing)
  
## Tech Stack:

- Twitter API for fetching tweets 
- `tweepy` for connecting the API with Python (https://pypi.org/project/tweepy/)
- Flask for the backend server
- Google colaboratory for collaborating on the model and accessing the free TPU 😂
- Keras for training and testing the BERT model
- BERT as a SOTA model for tweet predictions. (https://arxiv.org/abs/1810.04805)
 - Bootstrap for the homepage and the dashboard UI
 - `chartjs` for displaying graphs on the Dashboard

## Implementation Details:

P.S: If you ain't into the boring stuff, head on over to the next section to contribute to our model and the app!

### About MBTI 
The Myers Briggs Type Indicator (or MBTI for short) is a personality type system that divides everyone into 16 distinct personality types across 4 axis:

![img](https://i1.wp.com/www.honorsgradu.com/wp-content/uploads/2020/02/mbtifinal.jpg?resize=400%2C380&ssl=1)

- Introversion (I) – Extroversion (E)
- Intuition (N) – Sensing (S)
- Thinking (T) – Feeling (F)
- Judging (J) – Perceiving (P)

It is one of, if not the, the most popular personality test in the world. It is used in businesses, online, for fun, for research and lots more. From scientific or psychological perspective it is based on the work done on cognitive functions by Carl Jung i.e. Jungian Typology. This was a model of 8 distinct functions, thought processes or ways of thinking that were suggested to be present in the mind. Later this work was transformed into several different personality systems to make it more accessible, the most popular of which is of course the MBTI.

### Dataset 

For the [dataset](https://www.kaggle.com/datasnaek/mbti-type), we have used the famous **Myers-Briggs Personality** Type Dataset that includes a large number of people's MBTI type and content written by them.
This dataset contains over **8600** rows of data, on each row is a person’s:
```
- Type (This persons 4 letter MBTI code/type)
- A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))
```

### BERT 
Bidirectional Encoder Representations from Transformers (BERT) is a Transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google. BERT was created and published in 2018 by Jacob Devlin and his colleagues from Google. As of 2019, Google has been leveraging BERT to better understand user searches.

### Data Fetching:

Using `tweepy` and Twitter API, we fetch the 50 latest tweets posted by the user according to the username entered. These tweets are stored in a .csv file and sent for preprocessing, and finally the cleaned texts are sent to the Keras model.

### Data preprocessing:

We have used `regex` to detect special characters like '@,emojis' etc. from the posts, remove stopwords and punctuation, convert the text to lowercase and stemming to extract the root of words. The preprocessed data is split using `train_test split` and sent to the Keras model for predictions. 

### BERT Model summary:

```
Layer (type)                 Output Shape              Param #   
=================================================================
input_word_ids (InputLayer)  [(None, 1500)]            0         
_________________________________________________________________
tf_bert_model_1 (TFBertModel ((None, 1500, 768), (None 109482240)) 
_________________________________________________________________
tf_op_layer_strided_slice_1  [(None, 768)]             0         
_________________________________________________________________
dense_1 (Dense)              (None, 16)                12304     
=================================================================
Total params: 109,494,544
Trainable params: 109,494,544
Non-trainable params: 0
```

### Results achieved:

We tested using a LSTM model, and BERT-base to contrast accuracies.

| Model      | Train accuracy | Validation accuracy
| ----------- | ----------- | ---------------| 
| LSTM baseline      |  18.96%       | 16.9%|
| BERT-base-uncased   | 85%        | 79%|

### Deployment:

Uses flask for the backend and model deployment and Bootstrap for building the Dashboard and the Homepage UI. 

## Contributing:

Social BERTerfly is fully Open-Source and open for contributions! We request you to respect our contribution guidelines as defined in our [CODE OF CONDUCT](https://github.com/MLH-Fellowship/Social-BERTerfly/blob/main/CODE_OF_CONDUCT.md) and [CONTRIBUTING GUIDELINES](https://github.com/MLH-Fellowship/Social-BERTerfly/blob/main/CONTRIBUTING.md). 


## Contributors
- [Dipanwita Guhathakurta](https://github.com/susiejojo)
- [Shilpita Biswas](https://github.com/sh-biswas)
- [Vividha](https://github.com/V2dha)

Made with ❤️️ by Team Social-BERTerfly as part of MLH Explorer Fall Fellowship 2020 Sprint3.
