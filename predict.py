import sys
import argparse
import numpy as np
from PIL import Image
import os
import cv2


from keras.preprocessing import image
from keras.models import load_model
from keras.applications.inception_v3 import preprocess_input

target_size = (100, 100)  # fixed size for InceptionV3 architecture


def predict(model, img, target_size):
    """Run model prediction on image
    Args:
      model: keras model
      img: PIL format image
      target_size: (w,h) tuple
    Returns:
      list of predicted labels and their probabilities
    """
    if img.size != target_size:
        img = img.resize(target_size)

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return preds[0]



if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--image", help="path to image")
    a.add_argument("--image_array")
    a.add_argument("--model")
    args = a.parse_args()

    if args.image is None:
        a.print_help()
        sys.exit(1)

    model = load_model(args.model)
    if args.image is not None:
        img = Image.open(args.image)
        preds = predict(model, img, target_size)
        print np.argmax(preds)