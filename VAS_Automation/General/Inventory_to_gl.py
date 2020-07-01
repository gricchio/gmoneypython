import os
import pandas as pd


project_folder = r"C:\Users\gino.ricchio\Desktop\Python Projects\Inventory to GL"
File_name = 'Inventory.xlsx'

os.chdir(project_folder)

full_path = os.path.join(project_folder,File_name)

xl = pd.read_excel(File_name,
                   header=7,                
                   )
xl = xl.dropna(how='all')

xl = xl.sort_values(by='Inv. Value Posted to G/L')


#new
xl = xl.loc[xl['Invoiced Value'] != 0]


xl.to_excel("modded.xlsx")

