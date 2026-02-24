> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TCFG/pt-BR.md)

TCFG (Tangential Damping CFG) implementa uma técnica de orientação que refina as previsões incondicionais (negativas) para melhor alinhá-las com as previsões condicionais (positivas). Este método melhora a qualidade da saída aplicando um amortecimento tangencial à orientação incondicional, com base no artigo de pesquisa referenciado como 2503.18137. O nó modifica o comportamento de amostragem do modelo ajustando a forma como as previsões incondicionais são processadas durante o procedimento de orientação livre de classificador.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar o amortecimento tangencial CFG |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `patched_model` | MODEL | O modelo modificado com o amortecimento tangencial CFG aplicado |
