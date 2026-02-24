> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/pt-BR.md)

Este nó define o latente de referência para um modelo de edição. Ele recebe dados de condicionamento e uma entrada latente opcional, então modifica o condicionamento para incluir informações do latente de referência. Se o modelo suportar, você pode encadear vários nós ReferenceLatent para definir múltiplas imagens de referência.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem modificados com informações do latente de referência |
| `latent` | LATENT | Não | - | Dados latentes opcionais para usar como referência para o modelo de edição |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | CONDITIONING | Os dados de condicionamento modificados contendo informações do latente de referência |
