# Editar Método de Referência do Modelo

O nó FluxKontextMultiReferenceLatentMethod modifica os dados de condicionamento ao definir um método específico de latentes de referência. Ele anexa o método escolhido à entrada de condicionamento, o que afeta como os latentes de referência são processados nas etapas de geração subsequentes. Este nó é marcado como experimental e faz parte do sistema de condicionamento Flux.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `condicionamento` | Os dados de condicionamento a serem modificados com o método de latentes de referência | CONDITIONING | Sim | - |
| `método_de_latent_de_referência` | O método a ser usado para o processamento de latentes de referência. Se "uxo" ou "uso" for selecionado, ele será convertido para "uxo". Este parâmetro é marcado como avançado. | COMBO | Sim | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento modificados com o método de latentes de referência aplicado | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
