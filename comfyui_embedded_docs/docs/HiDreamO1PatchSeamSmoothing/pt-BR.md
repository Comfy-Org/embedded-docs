# Suavização de Emendas de Patches HiDream-O1

Este nó reduz costuras visíveis em imagens geradas pelo modelo HiDream-O1 ao calcular a média da saída do modelo em várias posições deslocadas da grade de patches durante a parte final do processo de amostragem. Ele executa o modelo várias vezes com alinhamentos de imagem ligeiramente diferentes e combina os resultados, o que ajuda a cancelar os artefatos semelhantes a grade que podem aparecer nos limites dos patches.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar a suavização de costuras. | MODEL | Sim | - |
| `percentual_inicial` | Progresso da amostragem (0=início, 1=fim) em que a mistura é ATIVADA. padrão: 0.8 | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `percentual_final` | Progresso da amostragem em que a mistura é DESATIVADA. padrão: 1.0 | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `padrão` | Layout de deslocamento. `single_shift`: uma passagem na grade natural de patches + outras deslocadas. `symmetric`: todas as passagens fora da grade, deslocamentos divididos em torno da origem. padrão: "single_shift" | COMBO | Sim | `"single_shift"`<br>`"symmetric"` |
| `passagens` | Número de passagens por etapa ativada. `2`/`4` = fixo. `ramp_*`: a contagem de passagens aumenta conforme a amostragem se aproxima do fim (mais suavização onde as costuras são mais visíveis). padrão: "2" | COMBO | Sim | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `mesclagem` | `average`: média com pesos iguais. `window`: ponderação com janela de Hann que favorece cada passagem distante de suas bordas de patch. `median`: mediana por pixel, rejeita passagens com valores atípicos de wraparound. padrão: "average" | COMBO | Sim | `"average"`<br>`"window"`<br>`"median"` |
| `força` | Interpolação entre a predição da grade natural (0) e o resultado da média (1). padrão: 1.0 | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

**Nota sobre Restrições de Parâmetros:**
- O efeito de suavização não é aplicado se `strength` for 0.0 ou menos, ou se `end_percent` for menor ou igual a `start_percent`. Nesses casos, o nó retorna o modelo inalterado.
- As opções de rampa do parâmetro `passes` (`ramp_2_4`, `ramp_2_4_8`) só são significativas quando `end_percent` for maior que `start_percent`, porque o número de passagens aumenta conforme a amostragem avança por esse intervalo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o wrapper de suavização de costuras aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
