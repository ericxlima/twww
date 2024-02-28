# cell 1

import pandas as pd
df = pd.read_csv('microdados_ed_basica_2022.csv', encoding='latin1', sep=";")

df.info

# cell 2

df_pernambuco = df.loc[df['SG_UF'] == 'SP']

"""
TP_DEPENDENCIA: 1 - Federal
                2 - Estadual
                3 - Municipal
                4 - Privada
"""
df_PE_privada = df_pernambuco.loc[df_pernambuco["TP_DEPENDENCIA"] == 4]


"""
TP_SITUACAO_FUNCIONAMENTO: 1 - Em Atividade
                           2 - Paralisada
                           3 - Extinta (ano do Censo)
                           4 - Extinta em Anos Anteriores
"""
df_PE_privada_funcionando = df_PE_privada.loc[df_PE_privada['TP_SITUACAO_FUNCIONAMENTO'] == 1]

df_PE_privada_funcionando_medio = df_PE_privada_funcionando.loc[df_PE_privada_funcionando["IN_MED"] == 1]

df_PE_privada_funcionando_medio.shape[0]


## Cell 3

filtro = ["NO_REGIAO", "NO_UF", "NO_MUNICIPIO", "NO_ENTIDADE", "CO_ENTIDADE", "TP_DEPENDENCIA", 
          "TP_CATEGORIA_ESCOLA_PRIVADA", "TP_LOCALIZACAO", "DS_ENDERECO", "NU_ENDERECO", 
          "DS_COMPLEMENTO", "NO_BAIRRO", "CO_CEP", "NU_DDD", "NU_TELEFONE", 
          "TP_SITUACAO_FUNCIONAMENTO", "IN_AUDITORIO", "QT_SALAS_UTILIZADAS", 
          "IN_REDES_SOCIAIS", "IN_MEDIACAO_PRESENCIAL", "IN_MEDIACAO_SEMIPRESENCIAL", 
          "IN_MEDIACAO_EAD", "IN_REGULAR", "IN_MED", "QT_MAT_BAS", "QT_MAT_MED", 
          "QT_MAT_EJA_MED", "QT_MAT_BAS_FEM", "QT_MAT_BAS_MASC", "QT_DOC_MED", "QT_TUR_MED",
]


df_filtrado = df_PE_privada_funcionando_medio[filtro]
#df_filtrado.to_excel('output.xlsx', index=False)
df_filtrado

# Cell 4

municipios_unicos = df_filtrado['NO_MUNICIPIO'].unique()
print(len(municipios_unicos))
