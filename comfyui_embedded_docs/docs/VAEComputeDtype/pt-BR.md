# VAE Compute Dtype

Este nó define o dtype de computação usado quando uma VAE codifica ou decodifica, sem alterar o restante do grafo do modelo. Ele retorna uma cópia da VAE de entrada com a precisão solicitada, para que um fluxo de trabalho possa executar uma ramificação com maior precisão enquanto as outras permanecem inalteradas. `"default"` mantém o dtype de computação que a VAE de entrada já utiliza.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | VAE a ajustar. O nó opera sobre uma cópia, portanto a VAE conectada não é modificada. | VAE | Sim | - |
| `dtype` | Dtype de computação para codificação e decodificação da VAE. `"default"` mantém o dtype de computação da VAE de entrada (padrão: `"default"`). | COMBO | Sim | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `vae` | A cópia da VAE com o dtype de computação selecionado aplicado. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/pt-BR.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`
