import pandas as pd
import selenium

from selenium.webdriver.common.by import By
from pathlib import Path

data_folder = Path("C:/Users/rdosa/source/repos/PythonApplication12/")

#In accordance with Style Guide for Python Naming Conventions, the variables in this project are in CapWords.

driver = selenium.webdriver.Chrome(executable_path='chromedriver')

driver.get("https://www.fundsexplorer.com.br/ranking")

driver.implicitly_wait(30)

driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/div[2]/a').click()

#https://sqa.stackexchange.com/questions/44298/how-to-print-the-text-of-all-elements-from-list-in-selenium-python

NomeFundos = driver.find_elements(By.XPATH, '//*[@id="upTo--default-fiis-table"]/div/table/tbody/tr/td[1]')

#QuantidadeToken = driver.find_elements(By.XPATH, '//*[@class="tablet:hidden"]')

ListaDeNome = []
#ListaDeQuantidade = []

for i in NomeFundos:
    list_Name = (i.get_attribute("textContent").strip(' .0123456789+'))
    ListaDeNome.append(list_Name)

driver.quit()

# Transformando dataframe

df = pd.DataFrame({'Token':ListaDeNome})

print(df)

#  Query https://stackoverflow.com/questions/28236305/how-do-i-sum-values-in-a-column-that-match-a-given-condition-using-pandas
#        https://stackoverflow.com/questions/31187194/sum-of-float-numbers-in-a-list-in-python
#        https://blog.finxter.com/how-to-convert-a-string-list-to-an-integer-list-in-python/


#  Fim do Query
#  Resultado do Query em Formato Lista/string pra o Google Sheets



#  Transformando dataframe em Formato Listas pra o Google Sheets

df_Tokens = pd.DataFrame(data={'Token':ListaDeNome})


TokensEmLista = df_Tokens.values.tolist()


print(TokensEmLista)

#  Salvando os valores em arquivo

