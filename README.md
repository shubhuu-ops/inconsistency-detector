Inconsistency Detector for PowerPoint Slides-
This project extracts text and images from PowerPoint presentations and detects inconsistencies (numerical, factual, logical, timeline) between slides.

Setup-
Clone the repo and go inside the folder.

Create and activate a Python virtual environment.

Install dependencies with:

nginx
Copy
Edit
pip install -r requirements.txt
Put your PPTX file inside the data/ folder.

Usage
Run the main script:

css
Copy
Edit
python src/main.py
This will analyze the PPTX, print inconsistencies in the terminal, and save a report in outputs/analysis_report.txt.

Project Structure
data/ — input PPTX files

outputs/ — reports and extracted images

src/ — source code (extractor, analyzer, main script)

.gitignore

requirements.txt

