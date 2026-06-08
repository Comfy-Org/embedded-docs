O nó GITSScheduler gera sigmas de agendamento de ruído para o método de amostragem GITS (Etapas Temporais Iterativas Generativas). Ele calcula os valores sigma com base em um parâmetro de coeficiente e no número de etapas, com um fator de remoção de ruído opcional que pode reduzir o total de etapas utilizadas. O nó utiliza níveis de ruído predefinidos e interpolação para criar o agendamento sigma final.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `coeficiente` | O valor do coeficiente que controla a curva do agendamento de ruído (padrão: 1,20) | FLOAT | Sim | 0,80 - 1,50 |
| `etapas` | O número total de etapas de amostragem para gerar sigmas (padrão: 10) | INT | Sim | 2 - 1000 |
| `reduzir_ruído` | Fator de remoção de ruído que reduz o número de etapas utilizadas (padrão: 1,0) | FLOAT | Sim | 0,0 - 1,0 |

**Nota:** Quando `denoise` é definido como 0,0, o nó retorna um tensor vazio. Quando `denoise` é menor que 1,0, o número real de etapas utilizadas é calculado como `round(steps * denoise)`. Para etapas maiores que 20, o nó utiliza interpolação log-linear para estender os níveis de ruído predefinidos até o número desejado de etapas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Os valores sigma gerados para o agendamento de ruído | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b81b85f95236276822429ec7cbc90204c6f4f86ea3e89ed8b7c2aea40597fea9`
