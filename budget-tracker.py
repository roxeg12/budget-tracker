import tkinter as tk
from tkinter import messagebox
import pandas as pd

try:
    df = pd.read_csv('./records.csv')
except Exception as e:
    data = {
        "Date" : [],
        "Description" : [],
        "Amount" : [],
        "Type" : [] 
    }

    df = pd.DataFrame(data)

class BudgetTrackerApp: