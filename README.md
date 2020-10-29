# Coursera-Streamlit-Project

This repro is to host the project I did for the coursera project [Build a Data Science Web App with Streamlit and Python](https://www.coursera.org/projects/data-science-streamlit-python)

## Difference with the proposed projects
In this version we did the following mod to the proposed projects:
* Rather than doing diverse and allowing separate analysis (one for the time one for the #of injured etc) we separate by visualisation and allow multi filter
* Filters are in the side bar
* For the time filter rather than limit to 1h with an int slider we created a slider with time and a min and max time 
* Rather than printing the table with steamlit we use plotly to avoid the time conversion forced by streamlit (as reported [here](https://github.com/streamlit/streamlit/issues/1061))
  * Table to width should look for a x scroll