# Suavização de Emendas de Patches HiDream-O1

Este nó reduz emendas visíveis em imagens geradas pelo modelo HiDream-O1 ao calcular a média da saída do modelo em várias posições deslocadas da grade de patches durante a parte final do processo de amostragem. Ele funciona executando o modelo várias vezes com alinhamentos de imagem ligeiramente diferentes e combinando os resultados, o que ajuda a eliminar os artefatos de grade que podem aparecer nas bordas dos patches.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo HiDream-O1 ao qual aplicar a suavização de emendas. | MODEL | Sim | - |
| `percentual_inicial` | O progresso da amostragem (0=início, 1=fim) no qual o efeito de suavização é ativado (padrão: 0.8). | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `percentual_final` | O progresso da amostragem no qual o efeito de suavização é desativado (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |
| `padrão` | O layout das posições deslocadas da grade. `single_shift`: uma passada na grade natural de patches mais outras deslocadas. `symmetric`: todas as passadas são fora da grade, com deslocamentos divididos em torno da origem (padrão: `"single_shift"`). | COMBO | Sim | `"single_shift"`<br>`"symmetric"` |
| `passagens` | O número de passadas (execuções do modelo) por etapa controlada. `2` ou `4` são contagens fixas. `ramp_2_4` e `ramp_2_4_8` aumentam a contagem de passadas conforme a amostragem se aproxima do fim, fornecendo mais suavização onde as emendas são mais visíveis (padrão: `"2"`). | COMBO | Sim | `"2"`<br>`"4"`<br>`"ramp_2_4"`<br>`"ramp_2_4_8"` |
| `mesclagem` | O método usado para combinar os resultados de cada passada. `average`: média com pesos iguais de todas as passadas. `window`: usa uma janela de Hann para dar mais peso ao centro de cada passada, reduzindo artefatos de borda. `median`: calcula a mediana por pixel, que pode rejeitar passadas atípicas causadas por wraparound (padrão: `"average"`). | COMBO | Sim | `"average"`<br>`"window"`<br>`"median"` |
| `força` | Controla a interpolação entre a saída original do modelo (0.0) e o resultado totalmente suavizado (1.0) (padrão: 1.0). | FLOAT | Sim | 0.0 a 1.0 (step: 0.01) |

**Nota sobre restrições de parâmetros:**

- O efeito de suavização não será aplicado se `strength` for 0.0 ou menos, ou se `end_percent` for menor ou igual a `start_percent`. Nesses casos, o nó retorna o modelo inalterado.
- As opções de rampa do parâmetro `passes` (`ramp_2_4`, `ramp_2_4_8`) só são significativas quando `start_percent` e `end_percent` definem um intervalo, pois o número de passadas aumenta conforme a amostragem progride por esse intervalo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com o invólucro de suavização de emendas aplicado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1PatchSeamSmoothing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02a2256fbf1868cc033a00f15066e9a896a7685ecdca0564ceec5b5b618b6a3c`
