# Simulador de Gerenciamento de Memória (Python)

## 🎯 Objetivo
O **Simulador de Gerenciamento de Memória** tem como objetivo implementar **três algoritmos de alocação** em uma memória simulada de 128 KB, com particionamento de 2 KB. Este projeto é desenvolvido em Python.

---

## 🧩 Implementação e Etapas do Código
**Importante:** Para executar o código, instale a dependência **PrettyTable** utilizando o seguinte comando: `pip install prettytable`

### Algoritmos Implementados

1. **First Fit**  
    Este algoritmo aloca o processo no **primeiro espaço contínuo livre** que comporta o processo. Ele é utilizado até que a memória fique cheia.
    
2. **Best Fit**  
    Quando a memória atinge sua capacidade, este algoritmo seleciona **o menor espaço livre** que é capaz de comportar o novo processo para **substituição**.
    - Se o espaço a ser substituído for maior que o novo processo, o espaço extra se torna um espaço vazio.
    - Se o próximo espaço for vazio e for criado um novo espaço vazio, esses dois serão combinados.
    
3. **Worst Fit**  
    Este algoritmo aloca o novo processo no **maior espaço livre** disponível, buscando manter blocos menores livres. Ele é utilizado **após** o Best Fit e continua até que a memória se esgote.
    - Em caso de falha, realiza uma chamada para o algoritmo Best Fit.

### 🔴 Falha na Inserção
Uma falha na inserção ocorre quando não há espaço livre suficiente para acomodar o novo processo, resultando no descarte do mesmo.