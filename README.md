
# Health Recommendation System

This project is designed to provide health-related recommendations to the public, utilizing machine learning techniques to analyze and suggest appropriate medical advice.

## Technologies Used

- **Programming Languages:**
  - Python
  - HTML

- **Libraries and Frameworks:**
  - Pandas
  - NumPy
  - Scikit-learn
  - TensorFlow
  - Flask

- **Tools:**
  - Jupyter Notebook
  - Git

## Machine Learning Algorithm: Support Vector Classifier (SVC)

The **Support Vector Classifier (SVC)** used in this project is a supervised machine learning algorithm, particularly effective for classification problems. Here’s a detailed breakdown of its role in the Health Recommendation System:

### Features of SVC in this Project

1. **Kernel Trick:**
   - The SVC model employs a kernel function to map the input data into a higher-dimensional space.
   - This mapping enables the algorithm to handle complex, non-linear relationships between the features.
   - Common kernel options include:
     - **Linear Kernel:** For linearly separable data.
     - **RBF (Radial Basis Function) Kernel:** For non-linear data patterns.

2. **Health Dataset and Features:**
   - The model is trained on a structured health dataset containing features such as symptoms, demographic details, and other clinical parameters.
   - The target variable represents a classification of various diseases or health conditions.

3. **Hyperparameter Tuning:**
   - **C (Regularization Parameter):** Controls the trade-off between achieving a low error on the training data and minimizing model complexity to avoid overfitting.
   - **Gamma (RBF Kernel Parameter):** Defines the influence of a single training example, impacting decision boundary smoothness.

4. **Model Training and Testing:**
   - The dataset is split into **training** and **testing** subsets.
   - The SVC is trained on the training set to learn patterns and relationships.
   - The model's performance is evaluated on the test set using metrics such as **accuracy**, **precision**, **recall**, and **F1-score**.

5. **Real-World Application in Health Recommendation System:**
   - Based on input symptoms, the SVC predicts potential health conditions or categories of diseases.
   - This prediction serves as the foundation for recommending appropriate actions, such as consulting a specialist or adopting preventive measures.

### Why SVC?

SVC was chosen for this project due to its robustness in handling both linear and non-linear data. It works well with relatively small datasets and high-dimensional spaces, making it suitable for initial iterations of health recommendation systems.

By leveraging the **RBF kernel** and proper tuning of hyperparameters, the SVC model achieves a balance of generalization and accuracy, ensuring reliable health condition predictions for end-users.

## Project Structure

- **Datasets:** Contains the health-related datasets used for training and testing the model.
- **Models:** Includes the trained machine learning models.
- **Templates:** Houses HTML templates for the web interface.

- **Main Files:**
  - `HealthRecommendationSystem.ipynb`: Jupyter Notebook detailing the data analysis and model training process.
  - `main.py`: The main Python script that runs the Flask web application.
  - `requirements.txt`: Lists the Python dependencies required for the project.
  - `runtime.txt`: Specifies the Python runtime environment.
  - `vercel.json`: Configuration file for deploying the application on Vercel.

## Setup and Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ParamDesai111/Health-Recommendation-System.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd Health-Recommendation-System
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python main.py
   ```

The application will start, and you can access it via `http://localhost:5000` in your web browser.
