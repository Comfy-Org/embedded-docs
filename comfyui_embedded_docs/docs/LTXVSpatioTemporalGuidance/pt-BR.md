# LTXVSpatioTemporalGuidance

Este nó melhora o detalhe espacial e a coerência do movimento na geração de vídeos LTXV ao executar uma passagem extra em cada etapa de amostragem. Durante essa passagem, a autoatenção dos blocos de transformador selecionados é degradada para uma passagem direta de valor, e a geração é afastada do resultado degradado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `model` | O modelo base ao qual aplicar a orientação espaço-temporal. O modelo é clonado e modificado com uma função de orientação pós-CFG. | MODEL | Sim | — |
| `scale` | A intensidade da orientação aplicada ao resultado com ruído removido. Quando definido como 0, a orientação não tem efeito. (padrão: 1.0) | FLOAT | Sim | 0.0 a 100.0 (passo 0.01) |
| `blocks` | Índices dos blocos do transformador a serem perturbados, separados por vírgula. Somente valores numéricos são usados; quaisquer outros caracteres são ignorados. (padrão: "29") | STRING | Sim | — |
| `start_percent` | A fração do processo de amostragem em que a orientação começa. (padrão: 0.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | A fração do processo de amostragem em que a orientação termina. (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |

Observação: A orientação é aplicada somente durante o intervalo de amostragem entre `start_percent` e `end_percent`. Se `scale` for 0 ou `blocks` não contiver valores numéricos, a passagem orientada não terá efeito sobre o processo de amostragem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `MODEL` | O modelo clonado com a função de orientação espaço-temporal anexada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
