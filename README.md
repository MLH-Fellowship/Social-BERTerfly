# Social BERTerfly
Social BERTerfly predicts your personality out of the 16 Myers-Briggs Type Personalities by your Twitter Username. It utilizes machine learning classifier and NLP using the state of the art language model - **BERT** (Bidirectional Encoder Representations from Transformers) to predict the personality type of the given user based on their recent tweets.

## About MBTI 
The Myers Briggs Type Indicator (or MBTI for short) is a personality type system that divides everyone into 16 distinct personality types across 4 axis:
- Introversion (I) – Extroversion (E)
- Intuition (N) – Sensing (S)
- Thinking (T) – Feeling (F)
- Judging (J) – Perceiving (P)

It is one of, if not the, the most popular personality test in the world. It is used in businesses, online, for fun, for research and lots more. From scientific or psychological perspective it is based on the work done on cognitive functions by Carl Jung i.e. Jungian Typology. This was a model of 8 distinct functions, thought processes or ways of thinking that were suggested to be present in the mind. Later this work was transformed into several different personality systems to make it more accessible, the most popular of which is of course the MBTI.

## Dataset 
For the [dataset](https://www.kaggle.com/datasnaek/mbti-type), we have used the famous Myers-Briggs Personality Type Dataset that includes a large number of people's MBTI type and content written by them.
This dataset contains over 8600 rows of data, on each row is a person’s:
- Type (This persons 4 letter MBTI code/type)
- A section of each of the last 50 things they have posted (Each entry separated by "|||" (3 pipe characters))

## BERT 
Bidirectional Encoder Representations from Transformers (BERT) is a Transformer-based machine learning technique for natural language processing (NLP) pre-training developed by Google. BERT was created and published in 2018 by Jacob Devlin and his colleagues from Google. As of 2019, Google has been leveraging BERT to better understand user searches.

## Deployment
Uses flask for the backend and model deployment

## Contributors
- [Dipanwita Guhathakurta](https://github.com/susiejojo)
- [Shilpita Biswas](https://github.com/sh-biswas)
- [Vividha](https://github.com/V2dha)
