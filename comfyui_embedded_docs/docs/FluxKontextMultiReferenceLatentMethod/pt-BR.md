# Editar Método de Referência do Modelo

O nó FluxKontextMultiReferenceLatentMethod atualiza dados de condicionamento armazenando um método de latentes de referência escolhido dentro deles. O método armazenado é então usado quando latentes de referência são processados em etapas de geração posteriores. Este nó está marcado como experimental e pertence ao sistema de condicionamento Flux.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com o método de latentes de referência | CONDITIONING | Sim | - |
| `reference_latents_method` | O método usado para o processamento de latentes de referência. Se um valor contendo "uxo" ou "uso" for selecionado, ele é convertido para "uxo" antes de ser armazenado. Este parâmetro está marcado como avançado. | COMBO | Sim | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com o método de latentes de referência aplicado | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
