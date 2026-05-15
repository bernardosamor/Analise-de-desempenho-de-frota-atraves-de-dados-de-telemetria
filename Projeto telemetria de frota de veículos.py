import pandas as pd
import numpy as np

df = pd.read_csv('vehicle_data.csv')

#! 1. MODELAGEM E SANEAMENTO
carros_totais = df['VehId'].nunique()
df['delta_speed'] = df['Vehicle Speed[km/h]'].diff()

#* Eficiência: km/h ganhos por grama de ar
df['eficiência_aceleração'] = df['delta_speed'] / df['MAF[g/sec]'] 
df['eficiência_aceleração'] = df['eficiência_aceleração'].replace([np.inf, -np.inf], np.nan)

#* Filtro: Apenas aceleração real > 0 e motor em carga >2 g/s
df_clean = df[(df['delta_speed'] > 0) & (df['MAF[g/sec]'] > 2)].copy()

############################################################################################################################

#! 2. ANÁLISES POR VEÍCULO
performance_por_veiculo = df_clean.groupby('VehId')['eficiência_aceleração'].mean().reset_index()

#* Definindo o Top 10% Piores
limiar_10_por_cento = performance_por_veiculo['eficiência_aceleração'].quantile(0.10)
veiculos_criticos = performance_por_veiculo[performance_por_veiculo['eficiência_aceleração'] <= limiar_10_por_cento]

#* IDs para os próximos filtros
ids_criticos = veiculos_criticos['VehId'].tolist()

#* Métricas de Contagem
total_veiculos_analisados = performance_por_veiculo['VehId'].nunique()
total_veiculos_com_alerta = len(ids_criticos)
carros_excluídos_contagem = carros_totais - total_veiculos_analisados

############################################################################################################################

#! 3. IMPACTO FINANCEIRO (NORMALIZADO POR HORA)
custo_medio_combustivel = 5.89 #R$
estequiometria_ar_gasolina = 14.7 
densidade_gasolina = 740 # g/L

#* Média de eficiência dos grupos
media_saudavel = performance_por_veiculo[~performance_por_veiculo['VehId'].isin(ids_criticos)]['eficiência_aceleração'].mean()
media_critica = performance_por_veiculo[performance_por_veiculo['VehId'].isin(ids_criticos)]['eficiência_aceleração'].mean()
fator_desperdicio = media_saudavel / media_critica

#* Cálculo do consumo médio por SEGUNDO de cada carro (L/s)
#* MAF / 14.7 = gramas de combustível / densidade = Litros
df_clean['consumo_L_por_sec'] = (df_clean['MAF[g/sec]'] / estequiometria_ar_gasolina) / densidade_gasolina

#* Agrupando para saber o consumo médio de cada ID
consumo_medio_por_id = df_clean.groupby('VehId')['consumo_L_por_sec'].mean()

#* Consumo médio (L/s) apenas do grupo crítico
consumo_medio_criticos_sec = consumo_medio_por_id[consumo_medio_por_id.index.isin(ids_criticos)].mean() #filtrando a tabela por ID

#* Projeção Financeira: Consumo em 1 hora de aceleração (3600 segundos)
custo_por_hora_critico = consumo_medio_criticos_sec * 3600 * custo_medio_combustivel
economia_por_hora = custo_por_hora_critico * (1 - (1 / fator_desperdicio))

############################################################################################################################

#! 4. IMPACTO FINANCEIRO (NORMALIZADO POR MÊS)
dias_úteis = 22
horas_operadas_por_dia = 8
percentual_tempo_acelerando = 0.30 # 30% do tempo de rota é aceleração/carga

horas_aceleracao_mes = dias_úteis * horas_operadas_por_dia * percentual_tempo_acelerando
economia_mensal_frota = (economia_por_hora * total_veiculos_com_alerta) * horas_aceleracao_mes

#! 5. RESULTADOS FINAIS
print("============================================")
print(f"Carros totais na frota: {carros_totais}")
print(f"Carros analisados (em aceleração): {total_veiculos_analisados}")
print(f"Carros com anomalia detectada: {total_veiculos_com_alerta}")
print("============================================")

print("\nRANKING DE INSPEÇÃO PRIORITÁRIA (Top 10% Piores):")
ranking_df = veiculos_criticos.sort_values(by='eficiência_aceleração').reset_index(drop=True)
ranking_df.index = ranking_df.index + 1
print(ranking_df[['VehId', 'eficiência_aceleração']])

print("\n--- ANÁLISE DE IMPACTO FINANCEIRO (PROJEÇÃO POR HORA) ---")
print("-" * 50)

print(f"Eficiência Média Saudável: {media_saudavel:.2f}")
print(f"Eficiência Média Crítica: {media_critica:.2f}")
print(f"Fator de Desperdício: {fator_desperdicio:.1f}x")
print("-" * 50)

print(f"Custo de Combustível Médio/Hora (Carro Crítico): R$ {custo_por_hora_critico:.2f}")
print(f"POTENCIAL DE ECONOMIA por Hora/Carro: R$ {economia_por_hora:.2f}")
print(f"ECONOMIA TOTAL DA FROTA CRÍTICA (30 carros/hora): R$ {economia_por_hora * total_veiculos_com_alerta:.2f}")
print("-" * 50)

print(f"\n--- ESTIMATIVA DE ECONOMIA MENSAL  ---")
print("-" * 50)
print(f"Premissa: {dias_úteis} dias úteis, {horas_operadas_por_dia}h/dia, {percentual_tempo_acelerando*100}% em aceleração.")
print(f"Economia Mensal Estimada para a Frota: R$ {economia_mensal_frota:.2f}")
print(f"Economia Anual Projetada: R$ {economia_mensal_frota * 12:.2f}")