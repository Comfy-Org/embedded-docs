> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/pt-BR.md)

Este nó cria um gancho LoRA (Adaptação de Baixa Classificação) que se aplica apenas ao componente do modelo, permitindo que você modifique o comportamento do modelo sem afetar o componente CLIP. Ele carrega um arquivo LoRA e o aplica com uma força especificada ao modelo, mantendo o componente CLIP inalterado. O nó pode ser encadeado com ganchos anteriores para criar pipelines de modificação complexos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `lora_name` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo LoRA a ser carregado da pasta `loras` |
| `strength_model` | FLOAT | Sim | -20.0 a 20.0 | O multiplicador de força para aplicar o LoRA ao componente do modelo (padrão: 1.0) |
| `prev_hooks` | HOOKS | Não | - | Ganchos anteriores opcionais para encadear com este gancho |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `hooks` | HOOKS | O gancho LoRA criado que pode ser aplicado ao processamento do modelo |
