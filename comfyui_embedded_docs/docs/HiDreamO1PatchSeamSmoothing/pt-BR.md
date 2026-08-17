# Suavização de Emendas de Patches HiDream-O1

## Visão Geral

Este nó reduz emendas visíveis em imagens geradas pelo modelo HiDream-O1 ao calcular a média da saída do modelo em várias posições da grade de patches deslocadas durante a parte final do processo de amostragem. Ele funciona executando o modelo várias vezes com alinhamentos de imagem ligeiramente diferentes e combinando os resultados, o que ajuda a cancelar os artefatos semelhantes a uma grade que podem aparecer nos limites dos patches.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo HiDream-O1 ao qual aplicar o encapsulador de suavização de emendas. | MODEL | Sim | - |
| `start_percent` | Progresso da amostragem (0=início, 1=fim) no qual a mistura é ativada (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `end_percent` | Progresso da amostragem no qual a mistura é desativada (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `pattern` | Layout de deslocamento. `single_shift`: uma passada na grade natural de patches e outras deslocadas. `symmetric`: todas as passadas fora da grade, com deslocamentos divididos em torno da origem (padrão: `"single_shift"`). | COMBO | Sim | `"single_shift"`<br>`"symmetric"` |
| `passes` | Número de passadas por etapa no intervalo ativo. `2`/`4` = fixo. `ramp_*`: o número de passadas aumenta conforme a amostragem se aproxima do fim (mais suavização onde as emendas são mais visíveis) (padrão: `"2"`). | COMBO | Sim | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `blend` | `average`: média com pesos iguais. `window`: ponderação com janela de Hann que favorece cada passada longe dos limites de seus patches. `median`: mediana por pixel, rejeita passadas discrepantes por wraparound (padrão: `"average"`). | COMBO | Sim | `"average"`<br>`"window"`<br>`"median"` |
| `strength` | Interpolação entre a previsão da grade natural (0) e o resultado médio (1) (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

**Notas sobre restrições:**

- O efeito de suavização não é aplicado se `strength` for 0.0 ou menor, ou se `end_percent` for menor ou igual a `start_percent`; nesses casos, o nó retorna o modelo inalterado.
- As opções de rampa de `passes` (`ramp_2_4`, `ramp_2_4_8`) aumentam o número de passadas conforme a amostragem avança em direção a `end_percent` dentro do intervalo ativo, portanto só fazem sentido quando `start_percent` e `end_percent` definem um intervalo não vazio.
- O resultado médio é misturado de volta à saída do modelo apenas longe das bordas da imagem: uma máscara mantém a previsão original na faixa de 32 pixels ao longo de cada borda (com um esmaecimento de 4 pixels), evitando a contaminação por wraparound causada pelas passadas deslocadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o encapsulador de suavização de emendas de patches aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
