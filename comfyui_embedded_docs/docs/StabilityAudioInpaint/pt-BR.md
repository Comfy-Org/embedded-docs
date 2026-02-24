> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/pt-BR.md)

Transforma parte de uma amostra de áudio existente usando instruções de texto. Este nó permite modificar seções específicas do áudio fornecendo *prompts* descritivos, efetivamente "preenchendo" ou regenerando porções selecionadas enquanto preserva o restante do áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "stable-audio-2.5"<br> | O modelo de IA a ser usado para o preenchimento de áudio. |
| `prompt` | STRING | Sim |  | Descrição textual que orienta como o áudio deve ser transformado (padrão: vazio). |
| `audio` | AUDIO | Sim |  | Arquivo de áudio de entrada a ser transformado. O áudio deve ter entre 6 e 190 segundos de duração. |
| `duration` | INT | Não | 1-190 | Controla a duração em segundos do áudio gerado (padrão: 190). |
| `seed` | INT | Não | 0-4294967294 | A semente aleatória usada para a geração (padrão: 0). |
| `steps` | INT | Não | 4-8 | Controla o número de etapas de amostragem (padrão: 8). |
| `mask_start` | INT | Não | 0-190 | Posição inicial em segundos para a seção do áudio a ser transformada (padrão: 30). |
| `mask_end` | INT | Não | 0-190 | Posição final em segundos para a seção do áudio a ser transformada (padrão: 190). |

**Observação:** O valor de `mask_end` deve ser maior que o valor de `mask_start`. O áudio de entrada deve ter entre 6 e 190 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | A saída de áudio transformada, com a seção especificada modificada de acordo com o *prompt*. |
