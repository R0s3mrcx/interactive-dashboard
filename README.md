# AMD Stock Data Web Application

<p align="center">
A web application to visualize AMD stock data interactively.
</p>

![interactive-dashboard](https://github.com/user-attachments/assets/38b5773a-5735-417d-8823-fb0d301d21d3)

# Features

* Responsive design optimized for mobile and desktop.
* Utilizes Plotly for interactive stock candlestick charts.
* Provides options to filter stock data by month.
* Developed using the Reflex framework with pure Python.

# Local Execution

1. Create a Python virtual environment:
```
python -m venv .venv
```

2. Activate the virtual environment:

Windows:
```
.venv\Scripts\activate
```
MacOS/Linux:
```
source .venv/bin/activate
```

3. Install the required dependencies:
```
pip install reflex
pip install pandas
pip install plotly==5.22.0
```

4. Initialize Reflex:
```
reflex init
```

5. Run the application using Reflex:
```
reflex run
```

> [!NOTE]
> Access http://localhost:3000/ to view the web application.
