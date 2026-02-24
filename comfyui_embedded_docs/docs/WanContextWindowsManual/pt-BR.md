> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/pt-BR.md)

O nó WAN Context Windows (Manual) permite configurar manualmente janelas de contexto para modelos do tipo WAN com processamento bidimensional. Ele aplica configurações personalizadas de janela de contexto durante a amostragem, especificando o comprimento da janela, sobreposição, método de agendamento e técnica de fusão. Isso oferece controle preciso sobre como o modelo processa informações em diferentes regiões de contexto.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo ao qual aplicar as janelas de contexto durante a amostragem. |
| `context_length` | INT | Sim | 1 a 1048576 | O comprimento da janela de contexto (padrão: 81). |
| `context_overlap` | INT | Sim | 0 a 1048576 | A sobreposição da janela de contexto (padrão: 30). |
| `context_schedule` | COMBO | Sim | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | O agendamento (passo) da janela de contexto. |
| `context_stride` | INT | Sim | 1 a 1048576 | O passo (stride) da janela de contexto; aplicável apenas a agendamentos uniformes (padrão: 1). |
| `closed_loop` | BOOLEAN | Sim | - | Se deve fechar o loop da janela de contexto; aplicável apenas a agendamentos em loop (padrão: False). |
| `fuse_method` | COMBO | Sim | "pyramid" | O método a ser usado para fundir as janelas de contexto (padrão: "pyramid"). |

**Observação:** O parâmetro `context_stride` afeta apenas agendamentos uniformes, e `closed_loop` aplica-se apenas a agendamentos em loop. Os valores de comprimento e sobreposição de contexto são ajustados automaticamente para garantir valores mínimos válidos durante o processamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo com a configuração de janela de contexto aplicada. |
