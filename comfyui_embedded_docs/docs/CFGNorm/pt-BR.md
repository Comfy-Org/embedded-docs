> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

O nó CFGNorm aplica uma técnica de normalização ao processo de orientação livre de classificador (CFG) em modelos de difusão. Ele ajusta a escala da previsão de ruído reduzido comparando as normas das saídas condicionais e incondicionais, em seguida, aplica um multiplicador de intensidade para controlar o efeito. Isso ajuda a estabilizar o processo de geração, prevenindo valores extremos na escala de orientação.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Faixa | Descrição |
|-----------|---------------|-----------------|--------|-------|-----------|
| `model` | MODEL | obrigatório | - | - | O modelo de difusão ao qual aplicar a normalização CFG |
| `strength` | FLOAT | obrigatório | 1.0 | 0.0 - 100.0 | Controla a intensidade do efeito de normalização aplicado à escala CFG |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `patched_model` | MODEL | Retorna o modelo modificado com a normalização CFG aplicada ao seu processo de amostragem |

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
