# GITSScheduler

O nó GITSScheduler gera sigmas de cronograma de ruído para o método de amostragem GITS (Generative Iterative Time Steps). Ele calcula valores sigma com base em um parâmetro de coeficiente e no número de etapas, com um fator de redução de ruído que pode diminuir o total de etapas utilizadas. O nó utiliza níveis de ruído predefinidos e interpolação para criar o cronograma final de sigmas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `coeficiente` | Parâmetro avançado. O valor do coeficiente que controla a curva do cronograma de ruído (padrão: 1.20). O valor é arredondado para duas casas decimais e seleciona qual tabela de níveis de ruído predefinida é utilizada. | FLOAT | Sim | 0.80 - 1.50 (passo 0.05) |
| `etapas` | O número total de etapas de amostragem para as quais gerar sigmas (padrão: 10). | INT | Sim | 2 - 1000 |
| `reduzir_ruído` | Fator de redução de ruído que diminui o número de etapas utilizadas (padrão: 1.0). | FLOAT | Sim | 0.0 - 1.0 (passo 0.01) |

**Nota:** Quando `denoise` é 0.0 ou menos, o nó retorna um tensor vazio. Quando `denoise` é menor que 1.0, o número real de etapas utilizadas é calculado como `round(steps * denoise)`, e apenas a última parte correspondente do cronograma é mantida. Para etapas entre 2 e 20, o nó seleciona um cronograma de ruído predefinido correspondente. Para etapas maiores que 20, o nó utiliza interpolação log-linear para estender os níveis de ruído predefinidos até o número desejado de etapas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sigmas` | Os valores sigma gerados para o cronograma de ruído. Para N etapas de amostragem, são retornados N+1 valores sigma, e o último sigma é definido como 0. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
