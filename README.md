# ConductorAI-TakeHome

## Setup Instructions:

1. Clone the repo and enter it via
```
git clone https://github.com/aLyonsGH/ConductorAI-TakeHome.git
cd ConductorAI-TakeHome
```
2. (Optional) Setup environment

    a. Create a new environment using Anaconda via 
    ```
    conda create -n "ConductorAI" python=3.12 pip
    ```
    b. Activate the environment via
    ```
    conda activate ConductorAI
    ```
3. Install dependencies via 
```
pip install pymupdf argparse tqdm
```

## Instructions for Use:

For a pdf with the path file *path_to_file*, run the following:
```
python greatest_number.py --pdf "path_to_file"
```

For example, for the pdf document included in the repo, run:
```
python greatest_number.py --pdf "FY25 Air Force Working Capital Fund.pdf"
```
