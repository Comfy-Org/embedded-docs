# GITSScheduler

O nó GITSScheduler gera sigmas de agendamento de ruído para o método de amostragem GITS (Generative Iterative Time Steps). Ele calcula valores de sigma com base em um parâmetro de coeficiente e no número de passos, com um fator de denoising opcional que pode reduzir o total de passos utilizados. O nó usa níveis de ruído pré-definidos e interpolação para criar o agendamento final de sigmas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `coeficiente` | O valor do coeficiente que controla a curva do agendamento de ruído (padrão: 1.20). O valor é arredondado para duas casas decimais e seleciona qual tabela de níveis de ruído pré-definidos será usada. | FLOAT | Sim | 0.80 - 1.50 (passo 0.05) |
| `etapas` | O número total de passos de amostragem para gerar os sigmas (padrão: 10) | INT | Sim | 2 - 1000 |
| `reduzir_ruído` | Fator de denoising que reduz o número de passos utilizados (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Observação:** Quando `denoise` é 0.0 ou menor, o nó retorna um tensor vazio. Quando `denoise` é menor que 1.0, o número real de passos utilizados é calculado como `round(steps * denoise)`, e apenas a parte final correspondente do agendamento é mantida. Para passos entre 2 e 20, o nó seleciona um agendamento de ruído pré-definido correspondente. Para passos maiores que 20, o nó usa interpolação log-linear para estender os níveis de ruído pré-definidos até o número desejado de passos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `sigmas` | Os valores de sigma gerados para o agendamento de ruído. Para N passos, N+1 valores de sigma são retornados, e o último sigma é definido como 0. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GITSScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f46681970fece985f6a4b62d0817d1ea306f1ca9a20189f937512dd5717f458b`
