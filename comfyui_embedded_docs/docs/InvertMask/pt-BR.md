> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/pt-BR.md)

O nó InvertMask foi projetado para inverter os valores de uma máscara fornecida, efetivamente invertendo as áreas mascaradas e não mascaradas. Esta operação é fundamental em tarefas de processamento de imagem onde o foco de interesse precisa ser alternado entre o primeiro plano e o plano de fundo.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|--------------|-------------|
| `mask`    | MASK         | O parâmetro 'mask' representa a máscara de entrada a ser invertida. É crucial para determinar as áreas a serem invertidas no processo. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|--------------|-------------|
| `mask`    | MASK         | A saída é uma versão invertida da máscara de entrada, onde as áreas anteriormente mascaradas se tornam não mascaradas e vice-versa. |
