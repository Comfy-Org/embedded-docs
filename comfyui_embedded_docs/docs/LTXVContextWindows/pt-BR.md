# LTXVContextWindows

Este nó define janelas de contexto para modelos similares ao LTXV durante a amostragem. Ele divide o processo de geração de vídeo em janelas sobrepostas para gerenciar o uso de memória e melhorar a coerência temporal.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual aplicar as janelas de contexto durante a amostragem. | MODEL | Sim | - |
| `context_length` | O comprimento da janela de contexto em quadros reais. Deve ser 8*n + 1. (padrão: 145) | INT | Sim | Mínimo: 1<br>Máximo: nodes.MAX_RESOLUTION<br>Passo: 8 |
| `context_overlap` | A sobreposição da janela de contexto em quadros reais. (padrão: 40) | INT | Sim | Mínimo: 0<br>Passo: 8 |
| `context_schedule` | Algoritmo de agendamento dependente de etapa para janelas de contexto. (padrão: UNIFORM_STANDARD) | COMBO | Sim | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | O passo da janela de contexto; aplicável apenas a agendamentos uniformes. (padrão: 1) | INT | Não | Mínimo: 1 |
| `closed_loop` | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop. (padrão: Falso) | BOOLEAN | Não | Verdadeiro<br>Falso |
| `fuse_method` | O método a ser usado para fundir as janelas de contexto. (padrão: PYRAMID) | COMBO | Sim | Opções de comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | Se deve aplicar a mistura de ruído FreeNoise, melhora a mesclagem das janelas. (padrão: Verdadeiro) | BOOLEAN | Não | Verdadeiro<br>Falso |
| `retain_first_frame` | Manter o primeiro quadro latente em cada janela de contexto (pode ajudar a manter a referência inicial). (padrão: Falso) | BOOLEAN | Não | Verdadeiro<br>Falso |
| `split_conds_to_windows` | Se deve dividir múltiplos condicionamentos (criados pelo ConditionCombine) para cada janela com base no índice da região. (padrão: Falso) | BOOLEAN | Não | Verdadeiro<br>Falso |

**Nota:** O parâmetro `context_length` deve seguir a fórmula 8*n + 1, onde n é um número inteiro positivo. O nó ajusta automaticamente o valor para atender a esse requisito convertendo quadros reais em quadros latentes. O `context_overlap` também é convertido de quadros reais para quadros latentes (dividido por 8).

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `MODEL` | O modelo com janelas de contexto aplicadas para amostragem. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad0b8c54acaab1853f6fe98dbad675478f033caf867df954b40b7db5208f5ae4`
