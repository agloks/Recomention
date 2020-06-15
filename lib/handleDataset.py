import pandas as pd
import numpy as np
import os

class SetCodenation():

  def __init__(self):
    self.market = None
    self.client = None
    self.path = self.getPath()
    self.features_ramo = [
        "de_ramo",
        "setor",
        "nm_divisao",
        "nm_segmento",
      ]
    self.features_burocracia = [
          "natureza_juridica_macro",
          "de_natureza_juridica",
          "fl_optante_simples"
      ]
    self.features_consolidada = [
          "de_faixa_faturamento_estimado", 
          "de_faixa_faturamento_estimado_grupo",
          "idade_emp_cat"
      ]
    self.features_dependecy = [
        "id"
      ]

  def getPath(self):
    file_directory = os.path.realpath(__file__)
    file_directory_splited = file_directory.split("/")
    file_directory_without_file = "/".join(file_directory_splited[:-2])
      
    return file_directory_without_file

  def selectSet(self, number = "two", level = "A", full = True):
    client = None
    if(full):
      client = pd.read_csv(f"{self.path}/data/datasets/full_client_{number}_{level}.csv", encoding= 'unicode_escape')
    else:
      client = pd.read_csv(f"{self.path}/data/datasets/client_{number}_{level}.csv", encoding= 'unicode_escape')

    return client

  def getMarket(self):
    pass
    # market = pd.read_csv("../1.Original/estaticos_market.csv")
    # features = self.features_dependecy + self.features_ramo + self.features_burocracia + self.features_consolidada
    
    # market = market[features]
    # market = market.astype('category')
    
    # return market


class HandlerDataset():
  
  def __init__(self, dataframe):
    self.client_df = dataframe
    self.client_obj_array = []
    self.features = ["id", "setor", "nm_divisao", "nm_segmento", "natureza_juridica_macro",
                      "de_natureza_juridica", "fl_optante_simples", "de_faixa_faturamento_estimado",
                      "de_faixa_faturamento_estimado_grupo", "idade_emp_cat"]
    self.client_df_empty = False

    self.madeTops()

  def handleNull(self, dict_client):
    null_options = [np.nan, "np.nan", "", None]

    for key in dict_client:
      if(dict_client[key] in null_options):
        print("I Feel here")
        dict_client[key] = "Dados Insuficientes"
      
      #problem unicode dataset
      if(key == 'setor'):
        if(dict_client[key][0:4] == 'SERV'):
          dict_client[key] = 'SERVIÇOS'

    return dict_client

  def madeTops(self):
    #DataFrame empty rows
    if(self.client_df.shape[0] == 0):
      obj = {}

      obj["empty"] = True
      self.client_df_empty = True  
      self.client_obj_array.append(obj)
      return obj

    #limit number of object...
    for idx in range(0, 7):
      obj = {}

      for key in self.features:
        obj[key] = self.client_df.iloc[idx][key]
      
      obj["number"] = idx + 1
      obj["empty"] = False
      obj = self.handleNull(obj)
      self.client_obj_array.append(obj)

    

## Only for sample debug and tests...
if __name__ == '__main__':

  setCodenation = SetCodenation()  
  message = setCodenation.selectSet(full=False, number="two", level="A")
  h = HandlerDataset(message)

  # print(len(h.client_obj_array))
  print(h.client_obj_array)