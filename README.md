# Packaging Strength Prediction API

This project provides a Flask-based API for predicting packaging strength using a machine learning model. The model is trained with XGBoost and scikit-learn, and is suitable for deployment on platforms like Render.

## Features
- Predicts packaging strength category (Light, Medium, Heavy) based on input features
- REST API endpoint for easy integration
- Ready for cloud deployment (Render)

## Project Structure
```
.
├── app.py                      # Flask API application
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment configuration
├── packaging_strength_model.pkl # Trained ML model
├── label_encoder.pkl           # Label encoder for target classes
├── .gitignore                  # Git ignore rules
└── README.md                   # Project documentation
```

## Setup (Local)
1. **Clone the repository:**
   ```sh
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   # On Windows:
   .\venv\Scripts\Activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask app:**
   ```sh
   python app.py
   ```

## API Usage
### Endpoint
- `POST /predict`

### Request Body Example
```json
{
  "features": {
    "layer": 0,
    "num_boxes": 10,
    "avg_box_weight": 5.0,
    "total_weight_above": 0,
    "box_material": "corrugated",
    "box_thickness": 5,
    "fragile": 0
  }
}
```

### Response Example
```json
{
  "prediction": [2]
}
```

> **Note:** The prediction is a numeric label. See the notebook or use the label encoder to map it to the class name (e.g., 2 = "Medium").

## Deployment on Render
1. **Push your code to GitHub.**
2. **Create a new Web Service on [Render](https://dashboard.render.com/):**
   - Connect your GitHub repo
   - Render will auto-detect `render.yaml` and set up the service
   - Or set manually:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
3. **Access your API at the public Render URL.**

## License
MIT 