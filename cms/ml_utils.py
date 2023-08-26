# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import array_to_img
from tensorflow.keras.preprocessing.image import load_img

import numpy as np


def perform_detection(file):
    # model = load_model("model.h5")
    # img = image.load_img(file, target_size=(224, 224))
    # img = image.img_to_array(img)
    # img = img / 255
    try:
        model = tf.keras.models.load_model("models/rootcode_model.h5")
        image_size = (150, 150)
        # Load and preprocess the image
        image = load_img(file, target_size=image_size)
        img_array = img_to_array(image)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale to match the range [0, 1]

        # Make a prediction
        prediction = model.predict(img_array)

        # Get the predicted class index
        predicted_class_index = np.argmax(prediction)

        # Map the predicted class index to its label
        class_labels = {
            "category1_tumor": 0,
            "category2_tumor": 1,
            "category3_tumor": 2,
            "no_tumor": 3,
        }
        predicted_label = [
            label
            for label, index in class_labels.items()
            if index == predicted_class_index
        ][0]

        print("Predicted Label:", predicted_label)
        return predicted_label
    except Exception as e:
        print(e)
        return "Benign"


def retrain(file, label):
    X, y = load_dataset()
    new_data = load_and_preprocess_file(file)
    X = np.vstack((X, new_data))
    y = np.append(y, label)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = SVC(kernel="linear")
    model.fit(X_train, y_train)
    trained_model_filename = "trained_model.pkl"
    joblib.dump(model, trained_model_filename)
    model_entry = ModelEntry.objects.get(pk=model_id)
    model_entry.label = label
    model_entry.save()
    return trained_model_filename
