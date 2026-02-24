> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/pt-BR.md)

O nó LatentApplyOperation aplica uma operação especificada a amostras latentes. Ele recebe dados latentes e uma operação como entradas, processa as amostras latentes usando a operação fornecida e retorna os dados latentes modificados. Este nó permite transformar ou manipular representações latentes em seu fluxo de trabalho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | As amostras latentes a serem processadas pela operação |
| `operation` | LATENT_OPERATION | Sim | - | A operação a ser aplicada às amostras latentes |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | As amostras latentes modificadas após a aplicação da operação |
