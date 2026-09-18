import pandas as pd
import matplotlib.pyplot as plt
import json
import matplotlib.dates as mdates

# Lista para armazenar os dados extraídos
data = []

print("Lendo o arquivo JSON...")

with open('baseline-local-v1.json', 'r') as file:
    for line in file:
        try:
            record = json.loads(line.strip())

            # Pega apenas os registros do tipo "Point" (que contém os valores)
            if record.get('type') == 'Point':
                metric_name = record.get('metric')

                # Filtra apenas as métricas de VUs e Duração da requisição
                if metric_name in ['vus', 'http_req_duration']:
                    timestamp = record['data']['time']
                    value = record['data']['value']
                    data.append({
                        'time': timestamp,
                        'metric': metric_name,
                        'value': value
                    })
        except json.JSONDecodeError:
            continue

print(f"Extraídas {len(data)} linhas relevantes. Gerando gráfico...")

# Cria um DataFrame do pandas
df = pd.DataFrame(data)
df['time'] = pd.to_datetime(df['time'])
df = df.sort_values('time')

# Separa os dados de VUs e Duração
df_vus = df[df['metric'] == 'vus']
df_duration = df[df['metric'] == 'http_req_duration']

# Criação do Gráfico (Dois eixos Y na mesma imagem)
fig, ax1 = plt.subplots(figsize=(10, 5))

# Eixo Y esquerdo (Tempo de Resposta em Azul)
color = '#1f77b4' # Azul
ax1.set_xlabel('Tempo do Experimento', fontsize=11)
ax1.set_ylabel('Tempo de Resposta (ms)', color=color, fontsize=11)
# Usamos scatter (pontos) com transparência para ver a densidade das requisições
ax1.scatter(df_duration['time'], df_duration['value'], color=color, alpha=0.3, s=10, label='Latência da Requisição')
ax1.tick_params(axis='y', labelcolor=color)

# Linha de SLA (500ms)
ax1.axhline(y=500, color='red', linestyle='--', linewidth=1.5, label='SLA Alvo (500ms)')

# Eixo Y direito (Usuários Virtuais em Laranja)
ax2 = ax1.twinx()
color = '#ff7f0e' # Laranja
ax2.set_ylabel('Usuários Virtuais Simulados (VUs)', color=color, fontsize=11)
ax2.plot(df_vus['time'], df_vus['value'], color=color, linewidth=2.5, label='Carga de Usuários (VUs)')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_ylim(bottom=0) # Força o eixo de VUs começar do 0

# Formatação do eixo X (Tempo)
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.xticks(rotation=45)

# Título e layout
plt.title('Teste de Carga Preliminar (Ambiente Local)', fontsize=13, fontweight='bold')
fig.tight_layout()

# Juntando as legendas dos dois eixos
lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='upper left')

# Salva o gráfico com alta resolução
plt.savefig('grafico_k6_resultados_v1.png', dpi=300, bbox_inches='tight')
print("✅ Gráfico gerado com sucesso: grafico_k6_resultados.png")
