# StabilityAudioInpaint

Transforma parte de uma amostra de áudio existente usando instruções de texto. Este nó permite modificar seções específicas do áudio fornecendo prompts descritivos, efetivamente fazendo "inpainting" ou regenerando as partes selecionadas enquanto preserva o restante do áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | O modelo de IA a ser usado para inpainting de áudio. | STRING | Sim | `"stable-audio-2.5"` |
| `prompt` | Descrição em texto que orienta como o áudio deve ser transformado (padrão: vazio). O comprimento máximo é de 10.000 caracteres. | STRING | Sim |  |
| `audio` | Arquivo de áudio de entrada a ser transformado. O áudio deve ter entre 6 e 190 segundos de duração. | AUDIO | Sim |  |
| `duration` | Controla a duração em segundos do áudio gerado (padrão: 190). | INT | Não | 1 a 190 |
| `seed` | A semente aleatória usada para geração (padrão: 0). | INT | Não | 0 a 4294967294 |
| `steps` | Controla o número de etapas de amostragem (padrão: 8). | INT | Não | 4 a 8 |
| `mask_start` | Posição inicial em segundos para a seção de áudio a ser transformada (padrão: 30). | INT | Não | 0 a 190 |
| `mask_end` | Posição final em segundos para a seção de áudio a ser transformada (padrão: 190). | INT | Não | 0 a 190 |

**Nota:** O valor de `mask_end` deve ser maior que o valor de `mask_start`. O áudio de entrada deve ter entre 6 e 190 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `audio` | O áudio transformado de saída com a seção especificada modificada de acordo com o prompt. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`
