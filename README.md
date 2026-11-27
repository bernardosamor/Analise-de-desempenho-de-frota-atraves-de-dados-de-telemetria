# Analise-de-desempenho-de-frota-atraves-de-dados-de-telemetria
Projeto em Python (Pandas e NumPy) que usa dados de telemetria para listar os 10% de veículos com pior eficiência de aceleração (30 de 299 veículos analisados, em uma base de 384) e estimar, em um cenário simulado, a economia de combustível se esses veículos operassem como os demais.

Resultado: os 30 veículos críticos consomem em média ~46% mais combustível em aceleração, concentram 35% do consumo em excesso da frota, e levá-los ao consumo médio dos demais representa uma economia projetada de ~R$ 234 mil por ano (cenário simulado).

---

### 💡 O Problema de Negócio
Veículos de uma frota podem consumir mais combustível que a média sem que isso apareça em nenhum relatório. Os dados de telemetria registram o comportamento de todos os veículos e permitem comparar um veículo com os demais para decidir quais inspecionar primeiro.

---

### 🧠 Hipóteses que guiaram esse projeto
* **Existem veículos que se destacam dos demais em eficiência de aceleração?**
  * ** Resultado: ✅ Confirmada** Dos 299 veículos analisados, os 30 piores (10%) têm eficiência média de 2,06, contra 4,01 dos demais: cerca de 1,9x pior.
* **Esses veículos consomem mais combustível?**
  * ** Resultado: ✅ Confirmada** Em regime de aceleração, consomem em média 45,7% mais combustível que os demais e concentram 35% do consumo em excesso (acima da média dos demais) de toda a frota.
* **A causa é baixa admissão de ar?**
  * ** Resultado: ❌ Refutada** A hipótese inicial era que o problema estivesse em uma baixa taxa de admissão de ar. Os dados mostram o contrário: os veículos críticos admitem mais ar (e, portanto, queimam mais combustível) para ganhar menos velocidade. A métrica identifica quais veículos são ineficientes, mas não diz por quê. Descobrir a causa exige inspeção.


### 📈 Impacto financeiro (cenário simulado)

Se os 30 veículos críticos passassem a operar como os demais:

| Critério | Economia anual | Economia mensal |  
| :--- | :---: | :---: |
| Consumo: diferença de consumo estima entre veículos saudáveis e críticos (+45,7%) | R$ 234.773,34 | R$ 19.481,11 |
| Eficiência (teto do cenário): usando a razão de eficiência média entre veículo saudáveis e críticos (1,9x) | R$ 362.353,97 | R$ 30.196,16 |

O critério de consumo é o principal porque está diretamente ligado ao combustível. O critério de eficiência é o limite superior do cenário.

Premissas: 22 dias úteis por mês, 8 horas por dia, 30% do tempo em aceleração (52,8 h/mês por veículo), gasolina a R$ 5,89 por litro, razão ar-combustível de 14,7 e densidade de 740 g/L.

**Como o número é calculado:**
 *  Consumo estimado a partir de ar admitido: MAF (g/s) ÷ 14,7 ÷ 740 g/L = litros por segundo.
 *  Custo por hora de aceleração de uma veículo crítico: litros/s × 3.600 × R$ 5,89
 *  Economia por hora: custo por hora × (1 − 1/razão), onde a razão é 1,46 (consumo) ou 1,9 (eficiência).
 *  Escala: economia por hora  × 30 veículos × 52,8 h/mês × 12 meses.

---

## 💡 Insights Principais

| Indicador | Valor | 
| :--- | :---: |
| Veículos na base | 384 | 
| Veículos avaliados  | 299 | 
| Veículos críticos | 30 | 
| Eficiência média: demais vs críticos | 4,01 vs 2,01 (~1,9x) | 
| Consumo dos críticos vs demais | +45,7% | 
| Parcela do consumo em excesso nos críticos | 35% | 
| Economia anual projetada (critério de consumo) | R$ 233.773,34 | 
| Economia anual projetada (critério de eficiência, teto) | R$ 362.353,97 | 

---

## 🛠️ Tecnologias e Metodologia
- **Linguagem:** Python
- **Bibliotecas:** Pandas (Tratamento e Agregação) e NumPy (Estatística).
- **Processos:** 1. **Data Cleaning:** Tratamento de sensores de telemetria e normalização.
    2. **Feature Engineering:** Criação de métricas de eficiência (Km/L vs Taxa de Ar).
    3. **Análise de Correlação:** Validação de que a admissão de ar é o fator crítico para o alto consumo.
    4. **Cálculo de ROI:** Projeção financeira baseada na manutenção da frota crítica.

--- 

### 🛠️ RoadMap do Projeto

Criação de métricas de desempenho e amostragem global da base de dados:
* **Modelagem dos dados:** variação de velocidade entre leituras consecutivas e eficiência de aceleração (km/h ganhos por g/s de ar admitido). Filtro: apenas aceleração real (variação de velocidade > 0) e motor em carga (MAF > 2 g/s).
* **Consumo estimado:** conversão do ar admitido em litros de combustível (razão ar-combustível e densidade), comparação do consumo médio dos críticos com o dos demais e cálculo da parcela do excesso concentrada nos críticos.
* **Análise individual por veículo:**  média da eficiência de cada veículo e definição do limiar dos 10% piores (quantil 10%), listando os IDs críticos.
* **Impacto Financeiro:**  custo por hora de aceleração e projeção mensal e anual, pelos dois critérios (consumo e eficiência).

---

## ⚠️ Limitações
* **É uma triagem, não um diagnóstico.** Eficiência baixa pode refletir tipo de veículo, carga ou rota, e não necessariamente defeito.
* **A economia é um cenário simulado.** Assume que os veículos críticos chegariam ao desempenho médio dos demais, e parte das premissas (30% do tempo em aceleração, jornada, preço do combustível) é fixa e igual para todos os veículos.
* **O consumo é estimado, não medido.** Vem do ar admitido (MAF) com mistura ideal, não de um medidor de combustível.
* **A razão ar-combustível de 14,7 vale para gasolina.** Para outros combustíveis ou motores híbridos, a conversão para consumo muda.

---


▶️ Como executar
bash
pip install pandas numpy
python telemetria_frota.py vehicle_data.csv

O arquivo telemetria_frota.py concentra as premissas no bloco de configuração do início, e o resultado completo aparece no terminal.

📖 Documentação detalhada

Passo a passo técnico e lógica estatística no artigo do Medium:

👉 Leia o artigo no Medium

Analista: Bernardo Samôr


## 📖 Documentação Detalhada
Para entender o passo a passo técnico e a lógica estatística aplicada neste estudo, confira meu artigo completo no Medium:

👉 [**Leia o artigo no Medium**](https://medium.com/@bernardosamor18/elevando-faturamento-de-empresa-de-transporte-com-otimiza%C3%A7%C3%A3o-de-frota-a-partir-de-dados-de-ab3f7f4cf473)

---
**Analista:** [Bernardo Samôr](https://github.com/bernardosamor)
