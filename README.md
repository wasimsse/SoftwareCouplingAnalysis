# SoftwareCouplingAnalysis_v01

## Description
Investigate software coupling using modern DNN methods and compare with traditional LSI to align with developers' perceptions for better software maintenance and development insights.

## Project Structure
/SoftwareCouplingAnalysis_v01
data/
    argouml/
    argouml.jar
    argouml_commit_log.txt
     argouml_trace.txt
    argouml_semantic.csv
    jhotdraw/
    jhotdraw.jar
    jhotdraw_commit_log.txt
     jhotdraw_trace.txt
    jhotdraw_semantic.csv
│ ├── jedit/
│ │ ├── jedit.jar
│ │ ├── jedit_commit_log.txt
│ │ ├── jedit_trace.txt
│ │ ├── jedit_semantic.csv
├── src/
│ ├── preprocessing/
│ │ ├── extract_text.py
│ │ ├── extract_structural_data.py
│ │ ├── extract_logical_data.py
│ │ ├── extract_dynamic_data.py
│ │ ├── extract_all_data.py
│ ├── metrics/
│ │ ├── compute_lsi_similarity.py
│ │ ├── compute_transformer_similarity.py
│ │ ├── visualize_coupling.py
│ ├── java_agent/
│ │ ├── MANIFEST.MF
│ │ ├── MethodCallLogger.java
│ │ ├── MethodCallLogger.class
│ │ ├── javassist.jar
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

4. Extract data (semantic, structural, logical) using the interactive script:
    ```
    python src/preprocessing/extract_all_data.py
    ```

5. Compute coupling metrics:
    ```
    python src/metrics/compute_lsi_similarity.py
    python src/metrics/compute_transformer_similarity.py
    ```

6. Visualize the coupling metrics:
    ```
    python src/metrics/visualize_coupling.py
    ```

7. Open the Jupyter notebook for further analysis:
    ```
    jupyter notebook src/notebooks/compare_coupling.ipynb
    ```

## Contributions
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
