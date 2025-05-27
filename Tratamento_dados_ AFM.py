import pandas as pd
import numpy as np

def calcular_rugosidade(arquivo, delimitador='\t', coluna=2):
    """
    Calcula a rugosidade RMS, média e desvio padrão de uma coluna específica em um arquivo TXT.

    Args:
        arquivo (str): Nome do arquivo TXT.
        delimitador (str): Caractere que separa os valores em cada linha (padrão: tabulação).
        coluna (int): Índice da coluna a ser utilizada no cálculo (começando em 0).

    Returns:
        tuple: Rugosidade RMS, rugosidade média e desvio padrão.
    """
    try:
        # Lendo o arquivo como um DataFrame
        df = pd.read_csv(arquivo, sep=delimitador, header=None)

        # Extraindo os valores da coluna especificada
        valores = df[coluna]

        # Calculando rugosidade RMS
        rugosidade_rms = np.sqrt(np.mean(valores**2))

        # Calculando rugosidade média
        rugosidade_media = np.mean(np.abs(valores))
      
        #calculando desvio padrão
        desvio_padrao = np.std(valores)

        return rugosidade_rms, rugosidade_media, desvio_padrao
    except FileNotFoundError:
        print(f"Arquivo '{arquivo}' não encontrado.")
    except pd.errors.ParserError:
        print("Erro ao interpretar o arquivo. Verifique o formato e o delimitador.")
    except KeyError:
        print("Coluna especificada não existe no arquivo.")

# Exemplo de uso
arquivo = 'afm90s.txt'
delimitador = '\t'  # Altere caso o delimitador seja diferente (e.g., ',' ou ' ')
coluna = 2  # Terceira coluna (índice começa em 0)

rms, media, desvio_padrao = calcular_rugosidade(arquivo, delimitador, coluna)
print(f"A rugosidade RMS é: {rms}")
print(f"A rugosidade média é: {media}")
print(f"O desvio padrão dos valores é: {desvio_padrao}")