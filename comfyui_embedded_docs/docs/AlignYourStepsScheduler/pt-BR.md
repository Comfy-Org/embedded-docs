# AlignYourStepsScheduler

O nó AlignYourStepsScheduler gera valores de sigma para o processo de remoção de ruído com base em diferentes tipos de modelo. Ele calcula níveis de ruído adequados para cada etapa do processo de amostragem e ajusta o número total de etapas de acordo com o parâmetro `denoise`. Isso ajuda a alinhar as etapas de amostragem aos requisitos específicos de diferentes modelos de difusão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `tipo_de_modelo` | Especifica o tipo de modelo a ser usado para o cálculo do sigma (padrão: "SD1") | COMBO | Sim | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `passos` | O número total de etapas de amostragem a serem geradas (padrão: 10) | INT | Sim | 1 a 10000 |
| `reduzir_ruído` | Controla o quanto remover o ruído da imagem, onde 1.0 usa todas as etapas e valores menores usam menos etapas (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

Observação: Cada tipo de modelo possui uma escala de níveis de ruído integrada contendo 11 valores de sigma (para 10 etapas). Quando `denoise` é 0.0, o nó retorna um tensor de sigma vazio. Quando `denoise` está entre 0.0 e 1.0, o número efetivo de etapas é calculado como `round(steps × denoise)`, e apenas a parte final correspondente da escala de sigma é usada. Se o valor de `steps` solicitado não corresponder ao tamanho da escala integrada, os níveis de ruído são interpolados log-linearmente para corresponder ao número de etapas solicitado. O valor final de sigma é sempre definido como 0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Retorna os valores de sigma calculados para o processo de remoção de ruído | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
