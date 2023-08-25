

# importing the needed libraries
import skops.io as sio
import re
from fastapi import FastAPI
import uvicorn
 
# creating the app
app = FastAPI()

# loading the model
with open('model.bin', 'rb') as f_in:
    model = sio.load(f_in, trusted=True)

# using the same preprocessor function for the new data as for the train data
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text

# function for the classification
def classify_message(model, message):
    message = preprocessor(message)
    label = model.predict([message])[0]
    spam_prob = model.predict_proba([message])
    return {'label': label, 'spam_probability': spam_prob[0][1]}

# Writing a function for the landing page with a fastapi decorator            
@app.get('/')
def get_root():
	return {'message': 'Welcome to the spam detection API'}

# Writing a function for the prediction with a fastapi decorator that fetches the message  
@app.get('/spam_detection_path/{message}')
async def detect_spam_path(message: str):
	return classify_message(model, message)

# run the app
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9697)
