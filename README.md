# Analise-de-desempenho-de-frota-atraves-de-dados-de-telemetria
Projeto em Python (Pandas e NumPy) que usa dados de telemetria para listar os 10% de veículos com pior eficiência de aceleração em uma frota de 384 veículos e estimar, em um cenário simulado, a economia de combustível se esses veículos operassem como os demais.

Resultado em uma linha: os 30 veículos críticos consomem em média ~46% mais combustível em aceleração, concentram 35% do consumo em excesso da frota, e levá-los ao consumo médio dos demais representa uma economia projetada de ~R$ 234 mil por ano.

---

### 💡 O Problema de Negócio
Veículos de uma frota podem consumir mais combustível que a média sem que isso apareça em nenhum relatório. Os dados de telemetria registram o comportamento de todos os veículos e permitem comparar um veículo com os demais para decidir quais inspecionar primeiro.

---

### 🧠 Hipóteses que guiaram esse projeto
* **Existem veículos que se destacam dos demais em eficiência de aceleração?**
  * ** Resultado: ✅ Confirmado** Dos 299 veículos analisados, os 30 piores (10%) têm eficiência média de 2,06, contra 4,01 dos demais: cerca de 1,9x pior.
* **Esses veículos consomem mais combustível?**
  * ** Resultado: ✅ Confirmado** Em regime de aceleração, consomem em média 45,7% mais combustível que os demais e concentram 35% do consumo acima da média saudável de toda a frota.
* **A causa é baixa admissão de ar? Não se sustentou.**
  * ** Resultado: ❌ Negativo** A hipótese inicial era que o problema estivesse em uma baixa taxa de admissão de ar. Os dados mostram o contrário: os veículos críticos admitem mais ar (e, portanto, queimam mais combustível) para ganhar menos velocidade. A métrica identifica quais veículos são ineficientes, mas não diz por quê. Descobrir a causa exige inspeção.

## 📈 Impacto de Negócio

📈 Impacto financeiro (cenário simulado)

Se os 30 veículos críticos passassem a operar como os demais:

Critério	Economia por ano	Economia por mês
Consumo (principal): usa a diferença de consumo medida (+45,7%)	R$ 233.773,34	R$ 19.481,11
Eficiência (teto do cenário): usa a razão de eficiência (1,9x)	R$ 362.353,97	R$ 30.196,16

O critério de consumo é o principal porque está ligado ao combustível medido. O critério de eficiência é o limite superior do cenário.

Premissas: 22 dias úteis por mês, 8 horas por dia, 30% do tempo em aceleração, gasolina a R$ 5,89 por litro, razão ar-combustível de 14,7 e densidade de 740 g/L.

---

## 🛠️ Tecnologias e Metodologia
- **Linguagem:** Python
- **Bibliotecas:** Pandas (Tratamento e Agregação) e NumPy (Estatística).
- **Processos:** 1. **Data Cleaning:** Tratamento de sensores de telemetria e normalização.
    2. **Feature Engineering:** Criação de métricas de eficiência (Km/L vs Taxa de Ar).
    3. **Análise de Correlação:** Validação de que a admissão de ar é o fator crítico para o alto consumo.
    4. **Cálculo de ROI:** Projeção financeira baseada na manutenção da frota crítica.

### 🛠️ RoadMap do Projeto

Criação de métricas de desempenho e amostragem global da base de dados:
* **Modelagem dos dados:** Criação de métricas como variação de velocidade (filtrar apenas os veículos acelerando) e eficiência de aceleração.
* **Análise individual por veículo:**  Definindo o limiar de veículos críticos (os 10% piores), listando seus IDs e os agrupando.
* **Impacto Financeiro:**  Definindo consumo dos veículos fora do 10% piores, o consumo dos 10% piores, a média de eficiência de aceleração dos dois grupos e o custo que vai gerar baseado no custo do combustível, dados de estequiometrica química (partes de ar necessárias para acelerar 1km/h).
* **Resultados finais:** Apresentação do impacto dos veículos com baixa eficiência normalizados por mês e ano.


## 💡 Insights Principais

Indicador	Valor
Veículos na frota	384
Veículos analisados (em aceleração)	299
Veículos críticos (10% piores)	30
Eficiência média: saudáveis vs críticos	4,01 vs 2,06 (~1,9x)
Consumo dos críticos vs saudáveis	+45,7%
Parcela do consumo em excesso nos críticos	35%
Economia anual projetada (critério de consumo)	R$ 233.773,34
Economia anual projetada (critério de eficiência, teto)	R$ 362.353,97


## ⚠️ Limitações
É uma triagem, não um diagnóstico. Eficiência baixa pode refletir tipo de veículo, carga ou rota, e não necessariamente defeito.
A economia é um cenário simulado. Assume que os veículos críticos chegariam ao desempenho médio dos demais, e parte das premissas (30% do tempo em aceleração, jornada, preço do combustível) é fixa.
A razão ar-combustível de 14,7 vale para gasolina. Para outros combustíveis ou motores híbridos, a conversão para consumo muda.
Base de dados: [NOME DA BASE E LINK]. Não é uma frota brasileira, e o preço em reais é uma premissa do cenário.


- **Gargalo Técnico:** Veículos com baixa admissão de ar consomem, em média, **18% mais combustível** para manter a mesma performance.
- **Eficiência de Foco:** Realizar a manutenção, e consequentemente, normalizar o consumo dos Top 10% dos piores veículos resolve **60% do desperdício total** da frota.
- **ROI de Manutenção:** A estratégia preditiva baseada em dados mostrou-se **4x mais barata** que a manutenção reativa convencional.

---
## 🎯 Resultado final:

Carros totais na frota: 384
Carros analisados (em aceleração): 299
Carros com anomalia detectada: 30

ESTIMATIVA DE ECONOMIA MENSAL  

Premissa: 22 dias úteis, 8h/dia, 30.0% em aceleração.
Economia Mensal Estimada para a Frota: **R$ 30196.16**
Economia Anual Projetada: **R$ 362353.97**


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
