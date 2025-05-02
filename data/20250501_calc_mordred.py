from rdkit import Chem
from mordred import Calculator, descriptors
import pandas as pd
from typing import Union
import os

def calc_mordred(aqsol_csv: Union[str, os.PathLike]):
    aqsol_df = pd.read_csv(aqsol_csv)
    mols = [Chem.AddHs(Chem.MolFromSmiles(x)) for x in aqsol_df['SMILES']]
    calc = Calculator(descriptors, ignore_3D=True)
    mordred_df = calc.pandas(mols)
    res_df = pd.concat([aqsol_df, mordred_df], axis = 1)
    res_df.to_csv('./processed/aqsol_db_mordred_descs.csv', index = False)
    return res_df

if __name__ == '__main__':
    calc_mordred('./raw/20250502_AqSolDB_DatasetA.csv')

