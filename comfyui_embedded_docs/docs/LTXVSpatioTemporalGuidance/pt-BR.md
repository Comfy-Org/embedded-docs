# LTXV Spatio-Temporal Guidance (STG)

Este nó melhora o detalhe espacial e a coerência de movimento da geração de vídeo LTXV executando uma passada extra a cada etapa de amostragem. Durante essa passada, a autoatenção dos blocos transformer selecionados é degradada para uma passagem direta de valores, e a geração é orientada para longe desse resultado degradado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo base ao qual aplicar a orientação espaço-temporal. O modelo é clonado e uma função de orientação pós-CFG é anexada à cópia. | MODEL | Sim | — |
| `scale` | A força da orientação aplicada ao resultado desruído. Quando definida como 0, a orientação não tem efeito. (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |
| `blocks` | Índices de blocos transformer separados por vírgula a serem perturbados. Apenas valores numéricos são usados; quaisquer outros caracteres são ignorados. (padrão: "29") | STRING | Sim | — |
| `start_percent` | A fração do processo de amostragem em que a orientação começa. Este é um parâmetro avançado. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | A fração do processo de amostragem em que a orientação termina. Este é um parâmetro avançado. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |

Nota: A orientação só é aplicada durante o intervalo de amostragem entre `start_percent` e `end_percent`. Fora desse intervalo, o resultado desruído original é retornado sem alterações. Se `scale` for 0 ou `blocks` não contiver valores numéricos, a passada orientada não terá efeito sobre o processo de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O modelo clonado com a função de orientação espaço-temporal anexada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
