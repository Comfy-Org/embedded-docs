# MiniMax H3 Context Windows

Divide a amostragem em janelas de contexto sobrepostas para que um vídeo do MiniMax H3 possa ser mais longo que a janela de passagem única do modelo. As janelas são posicionadas nos blocos de 17 quadros do modelo, o que mantém o vídeo e o áudio gerados alinhados nas fronteiras das janelas. Conecte o modelo retornado ao amostrador no lugar do modelo original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `context_length` | O comprimento da janela de contexto em quadros reais. Deve ser 17*n + 5 (padrão: 124). | INT | Sim | 22 a 16384 (MAX_RESOLUTION), passo 17 |
| `context_overlap` | A sobreposição da janela de contexto em quadros reais. Deve ser 17*n + 5 (padrão: 39). | INT | Sim | 5 ou mais, passo 17 |
| `fuse_method` | O método usado para fundir as janelas de contexto (padrão: `"pyramid"`). | COMBO | Sim | `"pyramid"`<br>`"relative"`<br>`"flat"`<br>`"overlap-linear"` |
| `freenoise` | Se deve aplicar o embaralhamento de ruído FreeNoise, que melhora a mesclagem das janelas (padrão: True, parâmetro avançado). | BOOLEAN | Sim | true<br>false |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados pelo ConditionCombine) para cada janela com base no índice de região (padrão: False, parâmetro avançado). | BOOLEAN | Sim | true<br>false |

Ambos os comprimentos são fornecidos em quadros reais e convertidos para latentes antes da amostragem: `context_length` torna-se 2 latentes em 5 quadros ou menos; caso contrário, `((frames - 5) / 17) * 5 + 2`. `context_overlap` é convertido da mesma forma e então limitado a `context_length` menos 5, de modo que a sobreposição sempre deixa um bloco completo para avançar. O nó sempre usa o agendamento estático com um passo de 1, aplica as janelas na dimensão temporal latente e não adiciona o quadro de correção causal, porque cada janela começa em uma fronteira de bloco. `split_conds_to_windows` espera múltiplos condicionamentos criados pelo nó ConditionCombine.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com a configuração de janelas de contexto aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ContextWindows/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e9e019d0bc870abfe226ef1aafb2607f55c0cc1b297884db35fe98c465cc0d91`
