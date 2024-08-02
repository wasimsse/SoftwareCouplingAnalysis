# SoftwareCouplingAnalysis_v01

## Description
Investigate software coupling using modern DNN methods and compare with traditional LSI to align with developers' perceptions for better software maintenance and development insights.

## Project Structure
/SoftwareCouplingAnalysis_v01
├── data/
│ ├── argouml/
│ ├── jhotdraw/
│ ├── jedit/
├── src/
│ ├── preprocessing/
│ │ ├── extract_text.py
│ ├── metrics/
│ │ ├── compute_lsi.py
│ │ ├── compute_transformer.py
│ ├── notebooks/
│ │ ├── compare_coupling.ipynb
├── requirements.txt
├── README.md
└── .gitignore


## Setup Instructions

1. Clone the repository:
    ```
    git clone https://github.com/wasimsse/SoftwareCouplingAnalysis.git
    cd SoftwareCouplingAnalysis_v01
    ```

2. Create and activate a virtual environment:
    ```
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

4. Run the preprocessing script:
    ```
    python src/preprocessing/extract_text.py
    ```

5. Compute coupling metrics:
    ```
    python src/metrics/compute_lsi.py
    python src/metrics/compute_transformer.py
    ```

6. Open the Jupyter notebook for analysis:
    ```
    jupyter notebook src/notebooks/compare_coupling.ipynb
    ```

## Contributions
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
