import os

# you will have import error in docker in you do not run docker-compose up
import numpy as np
import pandas as pd

if __name__ == '__main__':
    country = os.environ.get('COUNTRY')

    # If both print none, you werent able to get the ENV variables
    print("COUNTRY: " + str(country))

    # Should be able to print this too
    print(pd.read_csv("example.csv"))