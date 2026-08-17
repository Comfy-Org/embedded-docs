# AlignYourStepsScheduler

O nó AlignYourStepsScheduler cria os valores sigma usados durante o processo de denoising para diferentes tipos de modelo de difusão. Ele seleciona os níveis de ruído base para o modelo escolhido, ajusta o número de etapas com base na configuração `denoise` e retorna um tensor de valores sigma que termina em 0.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_type` | O tipo de modelo usado para selecionar os níveis de ruído base (padrão: "SD1") | COMBO | Sim | `"SD1"`<br>`"SDXL"`<br>`"SVD"` |
| `steps` | O número total de etapas de amostragem a serem geradas (padrão: 10) | INT | Sim | 1 a 10000 |
| `denoise` | Controla quanto do processo de amostragem é usado: 1.0 usa todas as etapas, valores menores usam menos etapas, e 0.0 retorna um tensor sigma vazio (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Os valores sigma calculados para o processo de denoising. Se `denoise` for 0.0, um tensor vazio é retornado. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3adbe1016c1ff4b9b7ad3737f50b168f54444d4ca355488e60537d1136f85d3f`
