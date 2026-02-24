> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/pt-BR.md)

O nó TextEncodeAceStepAudio processa entradas de texto para condicionamento de áudio, combinando tags e letras em tokens e, em seguida, codificando-os com uma força de letra ajustável. Ele recebe um modelo CLIP junto com descrições de texto e letras, tokeniza-os juntos e gera dados de condicionamento adequados para tarefas de geração de áudio. O nó permite ajustar a influência das letras por meio de um parâmetro de força que controla seu impacto na saída final.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP usado para tokenização e codificação |
| `tags` | STRING | Sim | - | Tags de texto ou descrições para condicionamento de áudio (suporta entrada multilinha e prompts dinâmicos) |
| `lyrics` | STRING | Sim | - | Texto da letra para condicionamento de áudio (suporta entrada multilinha e prompts dinâmicos) |
| `lyrics_strength` | FLOAT | Não | 0.0 - 10.0 | Controla a força da influência da letra na saída de condicionamento (padrão: 1.0, passo: 0.01) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Os dados de condicionamento codificados contendo tokens de texto processados com a força da letra aplicada |
