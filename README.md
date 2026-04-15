# Movie Recommendation System

## Description
This is a content-based movie recommendation system built using NLP techniques and cosine similarity. It analyzes movie metadata such as genres, keywords, cast, and crew to recommend similar movies. The backend is built using FastAPI.

## Important Note
The project includes FastAPI backend code for deployment, but the API is not currently deployed. This is because the model files (especially similarity.pkl) are large (~100MB+), which exceed GitHub upload limits. Therefore, model files are not included in the repository and must be generated locally.

## Tech Stack
- **Python** - Core programming language
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning library
- **FastAPI** - Modern web framework for building APIs
- **NLP** - Natural Language Processing (Bag of Words, CountVectorizer)
- **Cosine Similarity** - Vector similarity calculation

## Project Structure
```
movie-recommendation-system/
├── app/
│   └── main.py                          # FastAPI application
├── notebook/
│   └── movie-recommender-training.ipynb # Model building and preprocessing
├── models/                              # Stores model files (ignored in Git)
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

## Features
- **Content-Based Recommendation System** - Recommends movies based on metadata and features
- **NLP-Based Vectorization** - Uses Bag of Words and CountVectorizer for text processing
- **Cosine Similarity Matching** - Calculates similarity between movies to find recommendations
- **Movie Metadata Analysis** - Analyzes genres, keywords, cast, and crew information
- **FastAPI Backend** - RESTful API endpoint for retrieving recommendations

## API Usage

### POST /recommend

Get movie recommendations based on a movie title.

**Request Body:**
```json
{
  "movie": "Avatar"
}
```

**Response:**
```json
{
  "movie": "Avatar",
  "recommendations": [
    "Titan A.E.",
    "Small Soldiers",
    "Battle: Los Angeles",
    "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe"
  ]
}
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/rohitnath-dev/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate model files:**
   - Run the Jupyter notebook: `notebook/movie-recommender-training.ipynb`
   - This will generate `movies.pkl` and `similarity.pkl`
   - Place these files in the `models/` folder

4. **Run the FastAPI application:**
   ```bash
   uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`

5. **Access API documentation:**
   - Swagger UI: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

## Limitations
- **Model Files Not Included** - Model files (~100MB+) exceed GitHub upload limits and must be generated locally
- **API Not Deployed** - The API is not currently deployed due to hosting and model size constraints
- **Local Setup Required** - Users must generate model files locally before running the API

## Future Improvements
- Deploy API using cloud storage solutions (AWS S3, Google Cloud Storage) for model files
- Add frontend interface (Streamlit or React)
- Implement model compression techniques to reduce file size
- Add user-based collaborative filtering
- Optimize model training and inference speed
- Implement caching for frequently requested recommendations

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License
This project is open source and available under the MIT License.
