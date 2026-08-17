# ReferenceLatent

Este nó define o latente guia para um modelo de edição. Ele recebe dados de condicionamento e uma entrada latente opcional e, em seguida, modifica o condicionamento para incluir informações de latente de referência. Se o modelo suportar, você pode encadear vários nós ReferenceLatent para definir várias imagens de referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com informações de latente de referência | CONDITIONING | Sim | - |
| `latent` | Dados latentes opcionais para usar como referência para o modelo de edição | LATENT | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Os dados de condicionamento modificados contendo informações de latente de referência | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
