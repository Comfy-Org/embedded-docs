> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/pt-BR.md)

O nó CFGZeroStar aplica uma técnica especializada de dimensionamento de orientação a modelos de difusão. Ele modifica o processo de orientação livre de classificador calculando um fator de escala otimizado com base na diferença entre as previsões condicionais e incondicionais. Esta abordagem ajusta a saída final para fornecer um controle aprimorado sobre o processo de geração, mantendo a estabilidade do modelo.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | obrigatório | - | - | O modelo de difusão a ser modificado com a técnica de dimensionamento de orientação CFGZeroStar |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `patched_model` | MODEL | O modelo modificado com o dimensionamento de orientação CFGZeroStar aplicado |
