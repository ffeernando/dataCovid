from datetime import datetime as dt
from datetime import timedelta 

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)

fechaAyer = (dt.today() - timedelta(days = 1)).strftime('%Y%m%d')
fechaHoy = dt.today().strftime('%Y%m%d')
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

condicionesLista = ['Confirmados', 'Sospechosos', 'Negativos', 'Defunciones']

condicion = int(input('¿Qué condición desea analizar?\n 1. Confirmados \n 2. Sospechosos \n 3. Negativos \n 4. Defunciones \n'))

urlEstados = 'https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Estado_Nacional_' + condicionesLista[condicion-1] + '_' + str(fechaAyer) + '.csv'

urlMunicipios = 'https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_' + condicionesLista[condicion-1] + '_' + str(fechaAyer) + '.csv'

pathListadoMunicipios = '/PATH/to/MUNICIPIOS.xlsx' #Tener un Excel que tenga todos los municipios de México ordenados por estados

dFE_COVID = pd.read_csv(urlEstados)
dFM_COVID = pd.read_csv(urlMunicipios)
dFM_LISTA = pd.read_excel(pathListadoMunicipios)

print(dFE_COVID[['cve_ent', 'nombre']])

estado = int(input('Escriba el número de su estado.\n')) 

nombreEstado = dFE_COVID.loc[dFE_COVID['cve_ent'] == estado].values[0][2]

dFM_FILTRADO = dFM_LISTA[['NUMERO_MUNICIPIO', 'MUNICIPIO']].loc[dFM_LISTA['ESTADO'] == estado].iloc[:-1 , :] #Se filtran los municipios del estado correspondiente y se borra ultima fila que no corresponde a ningún municipio 

print(dFM_FILTRADO)

municipio = int(input('Escriba el número de su municipio.\n'))

if (municipio <10):
    strMunicipio = str(0) + str(0) + str(municipio)
elif (municipio>=10 and municipio < 100): 
    strMunicipio = str(0) + str(municipio)
else : 
    strMunicipio = str(municipio)

dFM_PEDIDO = dFM_COVID.loc[dFM_COVID['cve_ent'] == int(str(estado) + strMunicipio)]

nombreMunicipio = dFM_PEDIDO.values[0][2].upper()

print('Los datos de ' + condicionesLista[condicion-1] + ' del municipio de ' + nombreMunicipio + ', ' + nombreEstado + ' se muestran a continuación:\n')

print(dFM_PEDIDO)  #Escribe fila de su municipio


plt.plot(dFM_PEDIDO.columns.values.tolist()[3:], dFM_PEDIDO.values[0][3:])
