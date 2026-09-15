# BriaAddObject

Este nó insere um objeto descrito em texto simples em uma imagem usando Bria. A Bria renderiza novamente o quadro inteiro com cerca de 1 megapixel, portanto o resultado não fica alinhado pixel a pixel com a entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem à qual o objeto descrito é adicionado. O canal alfa é descartado antes de a imagem ser enviada. | IMAGE | Sim | - |
| `instruction` | O que adicionar e onde, como 'Coloque um vaso vermelho com flores sobre a mesa'. Não deve ficar vazio. Padrão: "" (string vazia). | STRING | Sim | - |
| `seed` | A Bria não aceita seed aqui e reimagina a edição a cada chamada, então execuções repetidas podem diferir. O valor nunca é enviado: ele apenas altera a chave de cache deste nó, para que um grafo de outro modo idêntico execute a edição novamente em vez de retornar o resultado em cache. Padrão: 42. | INT | Sim | 0 a 2147483647 |
| `moderation` | Configurações de moderação. Escolha "true" para revelar os sinalizadores de moderação abaixo. | DYNAMIC_COMBO | Sim | "false"<br>"true" |

### Entradas de moderação ativada

Disponível quando `moderation` está definido como "true".

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Ativa a moderação de conteúdo na imagem de entrada. Padrão: False. | BOOLEAN | Não | True / False |
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem de saída gerada. Padrão: False. | BOOLEAN | Não | True / False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem editada com o objeto descrito adicionado. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição subsequente com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/pt-BR.md)

---
**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`
