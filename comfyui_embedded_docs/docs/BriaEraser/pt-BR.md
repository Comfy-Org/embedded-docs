# BriaEraser

Bria Eraser remove objetos ou áreas de uma imagem usando a API Bria. Você fornece uma imagem e uma máscara que delimita as regiões a remover; o nó envia ambos para a Bria, executa a tarefa de remoção, aguarda a conclusão e retorna a imagem editada com as áreas mascaradas removidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada contendo os objetos ou áreas a remover. | IMAGE | Sim | - |
| `mask` | Áreas brancas são removidas, áreas pretas são preservadas. A máscara é binarizada antes do envio, portanto áreas parcialmente pintadas contam como brancas. Deve ter a mesma proporção de aspecto da imagem. | MASK | Sim | - |
| `mask_type` | Seleciona como a máscara foi criada. "manual" é para máscaras desenhadas à mão ou com pincel; "automatic" é para máscaras produzidas por modelos de segmentação como SAM. | COMBO | Sim | "manual"<br>"automatic" |
| `moderation` | Configurações de moderação. Defina como "true" para ativar a moderação de conteúdo nas imagens de entrada e/ou saída. | DYNAMIC_COMBO | Sim | "false"<br>"true" |

Nota: Quando `moderation` está definido como "true", duas configurações booleanas adicionais ficam disponíveis:

- `visual_input_moderation` — aplica moderação de conteúdo visual à imagem de entrada (padrão: false)
- `visual_output_moderation` — aplica moderação de conteúdo visual à imagem de saída (padrão: false)

A máscara deve corresponder à proporção de aspecto da imagem, caso contrário, a solicitação falha. A máscara é convertida em uma máscara binária (preto e branco) antes de ser enviada para a API, portanto áreas parcialmente pintadas são tratadas como brancas e serão removidas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem editada com os objetos ou áreas mascarados removidos. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/pt-BR.md)

---
**Source fingerprint (SHA-256):** `557272ecb0e6487796184ce88217ff318de4a5728a82e903aeb3fa3a0d24a664`
