# Bria Eraser

Bria Eraser remove objetos ou áreas de uma imagem usando a API da Bria. Você fornece uma imagem e uma máscara que delineia as regiões a remover; o nó envia ambas para a Bria, executa a tarefa de apagamento, aguarda a conclusão e retorna a imagem editada com as áreas mascaradas apagadas.

## Entradas

| Parâmetro | Descrição | Tipo de dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada que contém os objetos ou áreas a remover. | IMAGE | Sim | - |
| `mask` | As áreas brancas são apagadas; as áreas pretas são preservadas. A máscara é binarizada antes do envio com um corte de 50%: apenas áreas pintadas com opacidade acima de 50% contam como brancas. Deve ter a mesma proporção de aspecto que a imagem. | MASK | Sim | - |
| `mask_type` | O tipo de origem da máscara. "manual" é para máscaras desenhadas à mão ou com pincel; "automatic" é para máscaras produzidas por modelos de segmentação, como SAM. | COMBO | Sim | "manual"<br>"automatic" |
| `moderation` | Configurações de moderação. Defina como "true" para habilitar a moderação de conteúdo visual nas imagens de entrada e/ou saída. | DYNAMIC_COMBO | Sim | "false"<br>"true" |

Quando `moderation` estiver definido como "true", duas configurações booleanas adicionais ficam disponíveis:

- `visual_input_moderation` — aplica moderação de conteúdo visual à imagem de entrada (padrão: false)
- `visual_output_moderation` — aplica moderação de conteúdo visual à imagem de saída (padrão: false)

Nota: A máscara deve corresponder à proporção de aspecto da imagem, caso contrário a requisição falha. A máscara é convertida em uma máscara binária (preto e branco) antes de ser enviada à API: áreas pintadas com menos de metade da opacidade são ignoradas, e áreas parcialmente pintadas são tratadas como brancas e serão apagadas. A máscara deve conter pelo menos alguma área branca; uma máscara vazia faz a requisição falhar porque não há nada para apagar.

## Saídas

| Nome da saída | Descrição | Tipo de dado |
|-------------|-------------|-----------|
| `image` | A imagem editada com os objetos ou áreas mascarados removidos. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraser/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5528b7a3cb4d0a7b1b28acbc642a8bd21e2eacf5aa225403d6344c29f0cdba80`
