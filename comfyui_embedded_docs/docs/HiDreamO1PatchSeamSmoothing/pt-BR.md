> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/pt-BR.md)

# Visão Geral

Este nó reduz costuras visíveis em imagens geradas pelo modelo HiDream-O1, calculando a média da saída do modelo em múltiplas posições deslocadas da grade de patches durante a parte final do processo de amostragem. Ele funciona executando o modelo várias vezes com alinhamentos de imagem ligeiramente diferentes e combinando os resultados, o que ajuda a cancelar os artefatos semelhantes a grades que podem aparecer nas bordas dos patches.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo HiDream-O1 ao qual aplicar a suavização de costuras. |
| `percentual_inicial` | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) | O progresso da amostragem (0=início, 1=fim) no qual o efeito de suavização é ATIVADO (padrão: 0.8). |
| `percentual_final` | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) | O progresso da amostragem no qual o efeito de suavização é DESATIVADO (padrão: 1.0). |
| `padrão` | COMBO | Sim | `"single_shift"`<br>`"symmetric"` | O layout das posições deslocadas da grade. `single_shift`: uma passagem na grade natural de patches mais outras deslocadas. `symmetric`: todas as passagens são fora da grade, com deslocamentos divididos em torno da origem (padrão: `"single_shift"`). |
| `passagens` | COMBO | Sim | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` | O número de passagens (execuções do modelo) por etapa controlada. `2` ou `4` são contagens fixas. `ramp_2_4` e `ramp_2_4_8` aumentam a contagem de passagens conforme a amostragem se aproxima do fim, proporcionando mais suavização onde as costuras são mais visíveis (padrão: `"2"`). |
| `mesclagem` | COMBO | Sim | `"average"`<br>`"window"`<br>`"median"` | O método usado para combinar os resultados de cada passagem. `average`: média com pesos iguais de todas as passagens. `window`: usa uma janela Hann para dar mais peso ao centro de cada passagem, reduzindo artefatos de borda. `median`: calcula a mediana por pixel, que pode rejeitar passagens discrepantes causadas por envoltório (padrão: `"average"`). |
| `força` | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) | Controla a interpolação entre a saída original do modelo (0.0) e o resultado totalmente suavizado (1.0) (padrão: 1.0). |

**Observação sobre Restrições de Parâmetros:**
- O efeito de suavização não será aplicado se `strength` for 0.0 ou menor, ou se `end_percent` for menor ou igual a `start_percent`.
- As opções de rampa do parâmetro `passes` (`ramp_2_4`, `ramp_2_4_8`) só são significativas quando `start_percent` e `end_percent` definem um intervalo, pois o número de passagens aumenta conforme a amostragem progride através desse intervalo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo modificado com o invólucro de suavização de costuras aplicado. |

---
**Source fingerprint (SHA-256):** `f4d1a617d88f880dcae3afda25699333df023d7b4ec13a22a73512713d6ef18c`
