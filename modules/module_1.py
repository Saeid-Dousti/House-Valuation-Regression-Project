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
            self.df_data = pd.DataFrame([])

    def read_excel(self, excel_data):
        self.df_data = pd.read_excel(excel_data)
        self.df_data.columns = ['No', 'X1_transaction_date', 'X2_house_age',
                                'X3_distance_to_the_nearest_MRT_station',
                                'X4_number_of_convenience_stores', 'X5_latitude', 'X6_longitude',
                                'Y_house_price_of_unit_area'] # to make it addressable by pydeck
