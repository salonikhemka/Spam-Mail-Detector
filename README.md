# Spam Mail Detector

## Introduction:  
This project uses scikit-learn's machine learning methods to create a spam email detection system.  An automated method to identify and filter spam emails is quite helpful because they might be a serious issue.

 This project's methodology is adaptable and practical for a range of email platforms and applications since it can identify different kinds of spam emails.

---

## Features: 
- Utilizes machine learning techniques from **scikit-learn**  
- Accurate detection of spam emails  
- Easy to use and extend  

---

## Requirements: 
To run this project, you will need:  
- Python 3.x  
- `scikit-learn` library  

---

### Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/salonikhemka/Spam-Mail-Detector.git
2. Navigate to the project directory:
   ```bash
   cd Spam-Mail-Detector
3. Install required Python libraries:
   ```bash
   pip install scikit-learn
4. Run the spam detector script:
   ```bash
   python spam.py

---


### How it works:

The system uses a Count Vectorizer to convert email text into numerical features, then applies a machine learning model to classify the email as spam or not.

---

### Files Description:

- **spam.py:** Main script to test email spam detection.
- **train_spam_detector.py:** Script to train the model with your dataset.
- **spam_data.csv:** Dataset used for training the model.
- **count_vectorizer.pickle:** Saved vectorizer object for transforming text data.
- **spam_detector.pickle:** Saved trained spam classification model.

---

### Model Performance:

The spam detector model achieves around 98% accuracy on the test data after training with a sufficiently large dataset.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.
---

