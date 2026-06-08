O nó InvertMask foi projetado para inverter os valores de uma máscara fornecida, efetivamente trocando as áreas mascaradas e não mascaradas. Esta operação é fundamental em tarefas de processamento de imagem onde o foco de interesse precisa ser alternado entre o primeiro plano e o fundo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `máscara` | O parâmetro 'mask' representa a máscara de entrada a ser invertida. É crucial para determinar as áreas que serão invertidas no processo de inversão. | MASK |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `máscara` | A saída é uma versão invertida da máscara de entrada, com as áreas anteriormente mascaradas tornando-se não mascaradas e vice-versa. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/pt-BR.md)
