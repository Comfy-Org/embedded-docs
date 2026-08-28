# LTXV Spatio-Temporal Guidance (STG)

Este nó melhora o detalhe espacial e a coerência de movimento da geração de vídeo LTXV ao executar uma passagem extra em cada etapa de amostragem. Durante essa passagem, a autoatenção dos blocos de transformador selecionados é degradada para um valor de passagem direta (value-passthrough), e a geração é direcionada para longe do resultado degradado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model` | O modelo base ao qual aplicar a orientação espaço-temporal. O modelo é clonado e modificado com uma função de orientação pós-CFG. | MODEL | Sim | — |
| `scale` | A intensidade da orientação aplicada ao resultado sem ruído. Quando definido como 0, a orientação não tem efeito. (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |
| `blocks` | Índices de blocos do transformador separados por vírgula para perturbar. Apenas valores numéricos são usados; quaisquer outros caracteres são ignorados. (padrão: "29") | STRING | Sim | — |
| `start_percent` | A fração do processo de amostragem na qual a orientação começa. Este é um parâmetro avançado. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | A fração do processo de amostragem na qual a orientação termina. Este é um parâmetro avançado. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |

Nota: A orientação é aplicada apenas durante o intervalo de amostragem entre `start_percent` e `end_percent`. Se `scale` for 0 ou `blocks` não contiver valores numéricos, a passagem orientada não tem efeito no processo de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `MODEL` | O modelo clonado com a função de orientação espaço-temporal anexada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
