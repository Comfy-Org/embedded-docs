> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/pt-BR.md)

O nó Mahiro modifica a função de orientação (guidance) para focar mais na direção do prompt positivo, em vez da diferença entre os prompts positivo e negativo. Ele cria um modelo modificado (patched) que aplica uma abordagem personalizada de escalonamento de orientação usando a similaridade de cosseno entre as saídas normalizadas condicionais e incondicionais do processo de remoção de ruído. Este nó experimental ajuda a direcionar a geração de forma mais forte para a direção pretendida pelo prompt positivo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | | O modelo a ser modificado com a função de orientação alterada |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `patched_model` | MODEL | O modelo modificado com a função de orientação Mahiro aplicada |
