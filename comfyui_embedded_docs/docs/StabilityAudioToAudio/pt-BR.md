> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/pt-BR.md)

Transforma amostras de áudio existentes em novas composições de alta qualidade usando instruções de texto. Este nó recebe um arquivo de áudio de entrada e o modifica com base no seu prompt de texto para criar novo conteúdo de áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "stable-audio-2.5"<br> | O modelo de IA a ser usado para a transformação de áudio |
| `prompt` | STRING | Sim |  | Instruções de texto descrevendo como transformar o áudio (padrão: vazio) |
| `audio` | AUDIO | Sim |  | O áudio deve ter entre 6 e 190 segundos de duração |
| `duration` | INT | Não | 1-190 | Controla a duração em segundos do áudio gerado (padrão: 190) |
| `seed` | INT | Não | 0-4294967294 | A semente aleatória usada para a geração (padrão: 0) |
| `steps` | INT | Não | 4-8 | Controla o número de etapas de amostragem (padrão: 8) |
| `strength` | FLOAT | Não | 0.01-1.0 | Este parâmetro controla o quanto o parâmetro de áudio influencia o áudio gerado (padrão: 1.0) |

**Observação:** O áudio de entrada deve ter entre 6 e 190 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio transformado gerado com base no áudio de entrada e no prompt de texto |
