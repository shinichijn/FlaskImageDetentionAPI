import PIL
from flask import Flask, request, jsonify
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import base64
from PIL import Image
from io import BytesIO

# init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(basedir, 'models/model10.h5')


# model, image size
model = load_model(model_path)
width = 255
height = 325
labels = ['butterfly',
          'cat',
          'chicken',
          'cow',
          'dog',
          'horse',
          'sheep',
          'squirrel']


# predict
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # print(request.form.get('image'))
        b64_string = request.form.get('image')
        # img = image.load_img(img, target_size=(width, height))
        img = PIL.Image.open(BytesIO(base64.b64decode(b64_string))).convert('RGB')
        img = img.resize((height, width))
        img = image.img_to_array(img)
        img = img / 255
        img = np.expand_dims(img, axis=0)
        print(img.shape)
        # do image classification here
        animal_class = model.predict_classes(img).tolist()
        animal = labels[animal_class[0]]
        print('Index: ', animal_class)
        print('Animal: ', animal)

        # result
        return jsonify({"animal": animal})


# Run Server
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)