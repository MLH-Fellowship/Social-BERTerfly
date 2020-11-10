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
    per_op = per_types[stats.mode(tweet_ind).mode[0]]
    op_json = {}
    op_json["name"] = str(username)
    op_json["type"] = str(per_op)
    et = np.sum(tweet_vals,axis = 0)
    summer = np.sum(et)
    intro = np.sum(et[8:])/np.sum(et)*100
    intui = np.sum(et[0:4]+et[8:12])/summer*100
    feeli = np.sum(et[0:2]+et[4:6] + et[8:10] + et[12:14])/summer*100
    judgi = np.sum(et[::2]/summer*100)
    info_df = pd.read_csv("reference_data/MBTI.csv")
    op_json["introvertism"] = int(intro)
    op_json["extrovertism"] = int(100-intro)
    op_json["intuition"] = int(intui)
    op_json["sensing"] = int(100-intui)
    op_json["feeling"] = int(feeli)
    op_json["thinking"] = int(100-feeli)
    op_json["judging"] = int(judgi)
    op_json["perceiving"] = int(100-judgi)
    op_json["traits"] = info_df[info_df["type"]==per_op]["traits"].values[0]
    op_json["career"] = info_df[info_df["type"]==per_op]["career"].values[0]
    op_json["people"] = info_df[info_df["type"]==per_op]["eminent personalities"].values[0]
    op_json["per_name"] = info_df[info_df["type"]==per_op]["name"].values[0]
    perfile = open("static/results.js","w")
    perstr = "var personality_data="+str(op_json)+"\n"
    perfile.write(perstr)
    perfile.close()
    predict_follow(username)
    return op_json

def predict_follow(username):
    follow_df = pd.read_csv("twitter_data/fol_"+str(username)+".csv")
    follow_json = {}
    follow_ids = {}
    for i in range(5):
        list_j = follow_df.tweets.iloc[i].split(", \'")
        new_list = []
        for j in list_j:
            new_list.append(clean_text(j))
        tweet_ids = [tokenizer.encode(str(k), max_length = 100 , pad_to_max_length = True) for k in new_list]
        tweet_vals = new_model.predict(np.array(tweet_ids))
        tweet_ind = tweet_vals.argmax(axis=1)
        print (per_types[stats.mode(tweet_ind).mode[0]])
        follow_json[str(i)] = per_types[stats.mode(tweet_ind).mode[0]]
        follow_ids[str(i)] = follow_df.follower.iloc[i]
        perfile = open("static/results2.js","w")
        perstr = "var follower_data="+str(follow_json)+"\n"
        folstr = "var follower_ids="+str(follow_ids)+"\n"
        perfile.write(perstr)
        perfile.write(folstr)
        perfile.close()
    return follow_json
    

# new_mod = recreate_model()
# print (new_mod.summary())
# new_mod.save("models/new_BERT.h5",save_format="tf")