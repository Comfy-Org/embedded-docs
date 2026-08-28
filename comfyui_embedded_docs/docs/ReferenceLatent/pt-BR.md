# ReferenceLatent

Este nó define o latente de orientação para um modelo de edição. Ele recebe dados de condicionamento e uma entrada latente opcional e, em seguida, modifica o condicionamento para incluir informações do latente de referência. Se o modelo suportar, você pode encadear vários nós ReferenceLatent para definir múltiplas imagens de referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com informações do latente de referência | CONDITIONING | Sim | - |
| `latent` | Dados latentes opcionais para usar como referência para o modelo de edição. Se não for fornecido, o condicionamento é retornado inalterado | LATENT | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Os dados de condicionamento modificados contendo informações do latente de referência | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
