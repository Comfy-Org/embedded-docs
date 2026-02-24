> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

O nó CFGNorm aplica uma técnica de normalização ao processo de orientação livre de classificador (CFG) em modelos de difusão. Ele ajusta a escala da previsão com ruído removido comparando as normas das saídas condicional e incondicional, e então aplica um multiplicador de intensidade para controlar o efeito. Isso ajuda a estabilizar o processo de geração, prevenindo valores extremos na escala de orientação.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | obrigatório | - | - | O modelo de difusão ao qual aplicar a normalização CFG |
| `strength` | FLOAT | obrigatório | 1.0 | 0.0 - 100.0 | Controla a intensidade do efeito de normalização aplicado à escala CFG |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `patched_model` | MODEL | Retorna o modelo modificado com a normalização CFG aplicada ao seu processo de amostragem |
