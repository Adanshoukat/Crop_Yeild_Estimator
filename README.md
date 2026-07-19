# Crop Yield Estimator Dashboard

A professional Machine Learning desktop application built with Python and Tkinter that predicts agricultural crop yield based on environmental inputs. The system integrates advanced domain safety constraints to simulate extreme climatic hazards, tracks production analytics dynamically via local CSV logging, and utilizes a maximized, high-contrast user interface optimized for enterprise-grade desktop deployment.

##  Key Architectural Features
- **Core AI Inference Engine:** Leverages a Scikit-Learn Linear Regression model mapped against structured training vectors to instantly generate mathematical yield baselines (Tons).
- **Hybrid Agronomic Constraints:** Eliminates standard regression over-extrapolation during anomalies. Features embedded data logic that detects rainfall over 1500mm, triggering immediate critical waterlogging/flood alerts and safely dampening yields by a realistic 80% fallback margin.
- **Automated Data Persistence:** Seamlessly appends runtime parameters, custom calculated values, and system advisory logs directly into a secure `crop_yield_history.csv` data repository.
- **Production-Ready Enterprise Layout:** Enforces window launch parameters straight into a locked, maximized viewport state (`state('zoomed')`) with adaptive font scalings and centered grid panels to guarantee layout stability across various widescreen displays.

## Topics
- python
- tkinter
- machine-learning
- linear-regression
- gui-application
- rule-based-system
- expert-system
- analytics-dashboard
- academic-portfolio

AI (Gemini) was utilized as an interactive programming mentor during this project. It assisted in designing the maximized, high-contrast UI layout with Tkinter, integrating the rule-based expert constraints for weather anomalies alongside the Linear Regression pipeline, and debugging the dynamic focus traversal system to ensure professional, institution-standard code.


## Installation, Setup & Environment Run
1. **System Requirements & Verification**
Ensure you are using a verified environment with Python 3.8 or higher. You can check your local terminal setup with:

```bash
python --version
```

2. **Dependency Management**
Open a console inside your root repository directory and verify the following core data science libraries are installed:

```bash
pip install numpy pandas scikit-learn
```

3. **Application Execution**
To initialize the full-screen interactive diagnostic dashboard, run the primary entry point:

```bash
python "Crop Yield Estimator.py"
```

## Application Screenshots 

## Main DashBoard 
<img width="1536" height="863" alt="Main Dashboard" src="https://github.com/user-attachments/assets/23a760d5-3dfb-4f33-b127-dc09d2a1d9fb" />

### Live Evaluation Result
<img width="1536" height="862" alt="Evaluation Result  1" src="https://github.com/user-attachments/assets/1b34975d-f463-4c05-ad09-8888682187f7" />
<img width="1534" height="813" alt="Evaluation Result  3" src="https://github.com/user-attachments/assets/22c378b5-4591-4466-8938-035de0572252" />

### Exported Database Report
<img width="1920" height="1020" alt="CSV 2" src="https://github.com/user-attachments/assets/eb0cced0-cbc1-42c6-b6da-40ae06a77ef1" />


