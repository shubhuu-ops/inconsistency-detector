Setup Instructions

1.
Clone the repository:
git clone https://github.com/your-username/inconsistency-detector.git
cd inconsistency-detector
Create and activate a virtual environment:

2. Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

3. Install dependencies:
pip install -r requirements.txt

4. Add your PowerPoint file:
Place your .pptx file inside the data/ folder.


How to Use
Run the main script to analyze the presentation:

python src/main.py
The inconsistencies will be printed in the terminal.


Project Structure:

data/                # Input PowerPoint files and slide images
outputs/             # Analysis reports
src/                 # Source code modules (extract, OCR, analyze, main)
.gitignore
requirements.txt
README.md
Features
Extracts both typed text and images from slides.

Applies OCR on slide images to capture embedded text.

Uses AI to detect inconsistencies in data and statements across slides.

Provides clear, structured output referencing slide numbers and issue types.

Limitations
Designed for English-language presentations.

Accuracy depends on quality of slides and OCR.

Currently command-line only, no GUI.
