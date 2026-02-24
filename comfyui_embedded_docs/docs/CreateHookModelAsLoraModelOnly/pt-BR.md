> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/pt-BR.md)

Este nó cria um hook que aplica um modelo LoRA (Low-Rank Adaptation) para modificar apenas o componente de modelo de uma rede neural. Ele carrega um arquivo de checkpoint e o aplica com uma força especificada ao modelo, deixando o componente CLIP inalterado. Este é um nó experimental que estende a funcionalidade da classe base CreateHookModelAsLora.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Sim | Múltiplas opções disponíveis | O arquivo de checkpoint a ser carregado como um modelo LoRA. As opções disponíveis dependem do conteúdo da pasta de checkpoints. |
| `strength_model` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força para aplicar o LoRA ao componente do modelo (padrão: 1.0) |
| `prev_hooks` | HOOKS | Não | - | Hooks anteriores opcionais para encadear com este hook |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `hooks` | HOOKS | O grupo de hooks criado contendo a modificação do modelo LoRA |
