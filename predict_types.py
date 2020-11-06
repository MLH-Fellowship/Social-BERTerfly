import string
import re
import transformers
import tensorflow as tf
from scipy import stats
import pandas as pd
import numpy as np

maxlen = 1500
per_types = ['ENFJ','ENFP','ENTJ','ENTP','ESFJ','ESFP','ESTJ','ESTP','INFJ','INFP','INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP']


def clean_text(text):
    regex = re.compile('[%s]' % re.escape('|'))
    text = regex.sub(" ", text)
    words = str(text).split()
    words = [i.lower() + " " for i in words]
    words = [i for i in words if not "http" in i]
    words = " ".join(words)
    words = words.translate(words.maketrans('', '', string.punctuation))
    return words


def recreate_model(): 
    input_word_ids = tf.keras.layers.Input(shape=(maxlen,), dtype=tf.int32,
                                           name="input_word_ids")
    # bert_layer = transformers.TFBertModel.from_pretrained('bert-base-uncased')
    bert_layer = transformers.TFBertModel.from_pretrained("bert-base-uncased")
    bert_outputs = bert_layer(input_word_ids)[0]
    pred = tf.keras.layers.Dense(16, activation='softmax')(bert_outputs[:,0,:])
    
    model = tf.keras.models.Model(inputs=input_word_ids, outputs=pred)
    loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(
    learning_rate=0.00001), metrics=['accuracy'])
    model.load_weights("models/bert_base_model.h5")
    return model

new_model = recreate_model()
tokenizer = transformers.AutoTokenizer.from_pretrained('bert-base-uncased')

def predict_type(text):
    cleaned_ip = clean_text(text)
    custom_test_ids = [tokenizer.encode(str(cleaned_ip))]
    type_ind = np.argmax(new_model.predict(np.array(custom_test_ids)))
    return (per_types[type_ind])

def predict_tweet(username):
    tweet_path = "twitter_data/tweets_"+str(username)+".csv"
    tweet_csv = pd.read_csv(tweet_path)
    tweet_csv = tweet_csv[["0"]]
    tweet_csv["cleaned"] = tweet_csv["0"].apply(clean_text)
    tweet_ids = [tokenizer.encode(str(i), max_length = 50 , pad_to_max_length = True) for i in tweet_csv.cleaned.values]
    tweet_vals = new_model.predict(np.array(tweet_ids))
    tweet_ind = tweet_vals.argmax(axis=1)
    return (per_types[stats.mode(tweet_ind).mode[0]])



# new_mod = recreate_model()
# print (new_mod.summary())
# new_mod.save("models/new_BERT.h5",save_format="tf")