# ReferenceLatent

Este nó define o latent guia para um modelo de edição. Ele recebe dados de condicionamento e uma entrada latent opcional, então modifica o condicionamento para incluir informações de latent de referência. Se o modelo oferecer suporte, você pode encadear vários nós Set Reference Latent para definir múltiplas imagens de referência.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `conditioning` | Os dados de condicionamento a serem modificados com informações de latent de referência | CONDITIONING | Sim | - |
| `latent` | Dados latentes opcionais a serem usados como referência para o modelo de edição. Se não forem fornecidos, o condicionamento será retornado sem alterações | LATENT | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Os dados de condicionamento modificados contendo informações de latent de referência | CONDITIONING |

## Notas

- O latent de referência é armazenado como uma lista de tensores de amostra, então conectar vários nós Set Reference Latent em sequência acrescenta referências adicionais em vez de substituir a anterior.
- Quando nenhum `latent` está conectado, o nó passa o `conditioning` recebido sem alterações.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40b02df8ac436480f478fcfa929cc2e13181954507f4bdcd70aade051a25f7d5`
