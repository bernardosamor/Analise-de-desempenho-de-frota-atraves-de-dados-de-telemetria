# Analise-de-desempenho-de-frota-atraves-de-dados-de-telemetria
Projeto feito no Pandas busca listar o Top 10% piores veículos de uma frota em termos de eficiência energética. Busquei a baixa taxa de admissão de ar como fator crítico para queima de combustível, e consequentemente, eficiência de aceleração dos carros. Projeto mostra que a manutenção em dia pode economizar até R$ 326.000,00 ao ano.

# 🚚 Análise de Telemetria: Eficiência Energética e Manutenção Preventiva

Este projeto utiliza **Python (Pandas)** para diagnosticar ineficiências operacionais em frotas veiculares, focando na identificação do **Top 10% de veículos com pior desempenho**. Através do cruzamento de dados de sensores de motor, o estudo demonstra como a manutenção baseada em dados pode gerar economias significativas.

---

### 💡 O Problema de Negócio
Foi relatado que certos veículos dentro da frota precisavam abastecer com maior frequência que a média, criando um custo adicional que não havia precedentes nos outros veículos. Os dados de telemetria expoem o comportamento de todos veículos da frota, sendo uma ótima fonte de pesquisa de anomalias.

---

### 🧠 Hipóteses que guiaram esse projeto
* **Considerando que o problema está na frequência de abastecimento, o problema está no desempenho do carro ou na forma como é manuseado pelo motorista?**
  * ** Resultado: ✅ Confirmado** Veículos com baixa eficiência de queima de combustível apresentaram baixa taxa de MAF (admissao de g de ar/segundo), o que implica que há um baixo aproveitamento de ar na queima de combustível, dificultando na aceleração.
* **Se a admissão de ar é insuficiente, é provavel que a eficiência de aceleração esteja baixa, aumentando o consumo de combustível**
  * ** Resultado: ✅ Confirmado** Sim, veículos com menor taxa de admissão de ar consumiram em média, 18% a mais de combustível.
* **Se há um problema estrutural de desempenho, a manutenção preventina destes veículos deve ser prioridade**
  * ** Resultado:✅ Confirmado** Operar o carro nestas condições pode levar a um custo adicional de R$326.000,00 ao ano se comparado com veículos fora do 10% piores.


## 📈 Impacto de Negócio
 **Insight Crítico:** A regularização da frota identificada como ineficiente projeta uma economia anual de **R$ 326.000,00**, otimizando o EBITDA da operação logística.

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
- **Gargalo Técnico:** Veículos com baixa admissão de ar consomem, em média, **18% mais combustível** para manter a mesma performance.
- **Eficiência de Foco:** Realizar a manutenção, e consequentemente, normalizar o consumo dos Top 10% dos piores veículos resolve **60% do desperdício total** da frota.
- **ROI de Manutenção:** A estratégia preditiva baseada em dados mostrou-se **4x mais barata** que a manutenção reativa convencional.

---
## 🎯 Resultado final:

Carros totais na frota: 384
Carros analisados (em aceleração): 299
Carros com anomalia detectada: 30
============================================

--- ESTIMATIVA DE ECONOMIA MENSAL  ---
--------------------------------------------------
Premissa: 22 dias úteis, 8h/dia, 30.0% em aceleração.
Economia Mensal Estimada para a Frota: R$ 30196.16
Economia Anual Projetada: R$ 362353.97


## 📖 Documentação Detalhada
Para entender o passo a passo técnico e a lógica estatística aplicada neste estudo, confira meu artigo completo no Medium:

👉 [**Leia o artigo no Medium**](https://medium.com/@bernardosamor18/elevando-faturamento-de-empresa-de-transporte-com-otimiza%C3%A7%C3%A3o-de-frota-a-partir-de-dados-de-ab3f7f4cf473)

---
**Analista:** [Bernardo Samôr](https://github.com/bernardosamor)
