> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/pt-BR.md)

O nó Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos durante a amostragem. Ele cria segmentos de contexto sobrepostos com comprimento, sobreposição e padrões de agendamento especificados para processar dados em blocos gerenciáveis, mantendo a continuidade entre os segmentos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar as janelas de contexto durante a amostragem. |
| `context_length` | INT | Não | 1+ | O comprimento da janela de contexto (padrão: 16). |
| `context_overlap` | INT | Não | 0+ | A sobreposição da janela de contexto (padrão: 4). |
| `context_schedule` | COMBO | Não | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | O padrão de agendamento para as janelas de contexto. |
| `context_stride` | INT | Não | 1+ | O passo (stride) da janela de contexto; aplicável apenas a agendamentos uniformes (padrão: 1). |
| `closed_loop` | BOOLEAN | Não | - | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop (padrão: False). |
| `fuse_method` | COMBO | Não | `PYRAMID`<br>`LIST_STATIC` | O método a ser usado para fundir as janelas de contexto (padrão: PYRAMID). |
| `dim` | INT | Não | 0-5 | A dimensão à qual aplicar as janelas de contexto (padrão: 0). |

**Restrições dos Parâmetros:**

- `context_stride` é usado apenas quando agendamentos uniformes são selecionados
- `closed_loop` é aplicável apenas a agendamentos em loop
- `dim` deve estar entre 0 e 5, inclusive

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com as janelas de contexto aplicadas durante a amostragem. |
