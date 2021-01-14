import pandas as pd


class Reg_Data:
    """
    df_data: the excel file data
    """

    def __init__(self, excel_data):
        # self.df_data = pd.read_excel(df_data)
        if excel_data:
            self.read_excel(excel_data)
        else:
            self.raw_data = pd.DataFrame([])

        self.no_index_data = None

        self.outlier_data = None

    def read_excel(self, excel_data):
        self.raw_data = pd.read_excel(excel_data)
        self.raw_data.columns = ['_'.join(col.split()) for col in self.raw_data.columns]

    def drop_index(self):
        self.no_index_data = self.raw_data.drop('No', axis=1,inplace=False)