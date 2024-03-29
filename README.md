# House Valuation Regression Project

[![GitHub issues](https://img.shields.io/github/issues/Saeid-Dousti/House-Valuation-Regression-Project)](http://github.com/Saeid-Dousti/House-Valuation-Regression-Project/issues)
[![GitHub forks](https://img.shields.io/github/forks/Saeid-Dousti/House-Valuation-Regression-Project)](http://github.com/Saeid-Dousti/House-Valuation-Regression-Project/network)

<p align="left">
  <img src="config\logo.jfif">
</p>

In this application Real Estate Valuation dataset (https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set) is used for evaluation of various regression algorithms.

This application is developed using streamlit app and can be easily installed and used by the user.

This project is comprised of two main sections. In the first section data is explored and visualized. 

The following outlier detection methods are provided to user for outlier detection.
Z_score method, Isolation Forest, and Local Outlier Factor.

## Dependencies and Installation

Inclusion of streamlit is required.

- [Streamlit](streamlit.io)

To run locally, clone this repository:
```
git clone https://github.com/Saeid-Dousti/House-Valuation-Regression-Project
cd House-Valuation-Regression-Project
pip install -r requirements.txt
python setup.py install
```
To run the code
```
streamlit run app.py
```

The data visualization includes a 3D plot powered by pydeck library using the geo location data.

<p align="left">
  <img src="config\3d_GIO.jpg">
</p>





