import pandas as pd
from scipy import stats

# Dados fornecidos (três valores medidos de cada parâmetro)
data = []
for tratamento, valores in {
    'Controle': {
        'pH': (5.93, 6.08, 6.23),
        'TDS': (5109, 5250, 5412),
        'ORP': (42.5, 43.6, 44.7),
        'Condutividade': (12.8, 13.1, 13.53),
        'Salinidade': (7.15, 7.31, 7.46)
    },
    'Ar Comprimido': {
        'pH': (2.65, 2.72, 2.79),
        'TDS': (5800, 5970, 6137),
        'ORP': (237, 243.5, 249.7),
        'Condutividade': (14.5, 14.9, 15.33),
        'Salinidade': (7.65, 7.83, 8.007)
    },
    'Mistura': {
        'pH': (2.99, 3.06, 3.13),
        'TDS': (5000, 5225, 5450),
        'ORP': (205, 216, 226.7),
        'Condutividade': (12.8, 13.1, 13.46),
        'Salinidade': (7.70, 7.93, 8.16)
    },
    'Argonio': {
        'pH': (2.83, 2.91, 2.99),
        'TDS': (4900, 5143, 5386),
        'ORP': (215, 226, 237.6),
        'Condutividade': (12.6, 12.9, 13.23),
        'Salinidade': (7.70, 7.86, 8.018)
    }
}.items():
    for i in range(3):
        data.append({
            'Tratamento': tratamento,
            'pH': valores['pH'][i],
            'TDS': valores['TDS'][i],
            'ORP': valores['ORP'][i],
            'Condutividade': valores['Condutividade'][i],
            'Salinidade': valores['Salinidade'][i]
        })

df = pd.DataFrame(data)

# --- Teste ANOVA ---
print("\n--- Teste ANOVA ---")
anova_results = {}
for column in ['pH', 'TDS', 'ORP', 'Condutividade', 'Salinidade']:
    print(f"\n{column}:")
    groups = [df[column][df['Tratamento'] == t] for t in df['Tratamento'].unique()]
    anova_result = stats.f_oneway(*groups)
    anova_results[column] = anova_result
    print(f"  Estatística F: {anova_result.statistic:.3f}")
    print(f"  Valor p: {anova_result.pvalue:.3f}")