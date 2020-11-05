import string
import re
import transformers
import tensorflow as tf
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

def predict_type(text):
    cleaned_ip = clean_text(text)
    new_model = recreate_model()
    tokenizer = transformers.AutoTokenizer.from_pretrained('bert-base-uncased')
    custom_test_ids = [tokenizer.encode(str(cleaned_ip))]
    type_ind = np.argmax(new_model.predict(np.array(custom_test_ids)))
    return (per_types[type_ind])

# new_mod = recreate_model()
# print (new_mod.summary())
# new_mod.save("models/new_BERT.h5",save_format="tf")