[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/jdenos/coursera-streamlit-project/main/main.py)
# Coursera-Streamlit-Project

This repro is to host the project I did for the coursera project [Build a Data Science Web App with Streamlit and Python](https://www.coursera.org/projects/data-science-streamlit-python)
 
[Certificate](https://coursera.org/share/7877dc0441be5e2a70a1e0241894c784)
## Difference with the proposed projects
In this version we did the following mod to the proposed projects:
* Rather than doing diverse and allowing separate analysis (one for the time one for the #of injured etc) we separate by visualisation and allow multi filter
* Filters are in the side bar
* For the time filter rather than limit to 1h with an int slider we created a slider with time and a min and max time 
* Rather than printing the table with steamlit we use plotly to avoid the time conversion forced by streamlit (as reported [here](https://github.com/streamlit/streamlit/issues/1061))
  * Table to width should look for a x scroll
* Not using the dataset provided but using the website csv