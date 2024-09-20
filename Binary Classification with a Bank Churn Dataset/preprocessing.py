import pandas as pd
import numpy as np 

"""
데이터 전처리를 위한 함수를 정의하는 모듈.
"""

def get_age_group(age):
    """
    min: 18 
    max: 92
    """
    if age < 10:
        return 0
    
    return int(str(age)[0])
    