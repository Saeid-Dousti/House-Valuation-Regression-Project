import pandas as pd


class Reg_Data:
    """
    df_data: the excel file data
    """

    def __init__(self, df_data=None):

        if df_data:
            self.df_data = pd.read_excel(df_data)
        else:
            self.df_data = df_data

    def input(self):
        pass
