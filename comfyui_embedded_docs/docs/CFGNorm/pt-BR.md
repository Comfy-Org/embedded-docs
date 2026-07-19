# CFGNorm

O nó CFGNorm aplica uma técnica de normalização ao processo de orientação livre de classificador (CFG) em modelos de difusão. Ele ajusta a escala da previsão de ruído reduzido comparando as normas das saídas condicionais e incondicionais, em seguida, aplica um multiplicador de intensidade para controlar o efeito. Isso ajuda a estabilizar o processo de geração, prevenindo valores extremos na escala de orientação.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a normalização CFG | MODEL | obrigatório | - | - |
| `força` | Controla a intensidade do efeito de normalização aplicado à escala CFG | FLOAT | obrigatório | 1.0 | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `patched_model` | Retorna o modelo modificado com a normalização CFG aplicada ao seu processo de amostragem | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGNorm/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af9e5f965500b959ff46f781e9329524fc0a4b94af2ce6d74116fe27b0e9005e`
