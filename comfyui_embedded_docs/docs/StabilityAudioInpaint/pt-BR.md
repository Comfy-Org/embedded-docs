Transforma parte de uma amostra de áudio existente usando instruções de texto. Este nó permite modificar seções específicas do áudio fornecendo prompts descritivos, efetivamente "inpaintando" ou regenerando partes selecionadas enquanto preserva o restante do áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de IA a ser usado para inpainting de áudio. | COMBO | Sim | "stable-audio-2.5" |
| `prompt` | Descrição textual que orienta como o áudio deve ser transformado (padrão: vazio). | STRING | Sim |  |
| `áudio` | Arquivo de áudio de entrada a ser transformado. O áudio deve ter entre 6 e 190 segundos de duração. | AUDIO | Sim |  |
| `duração` | Controla a duração em segundos do áudio gerado (padrão: 190). | INT | Não | 1-190 |
| `semente` | A semente aleatória usada para geração (padrão: 0). | INT | Não | 0-4294967294 |
| `passos` | Controla o número de etapas de amostragem (padrão: 8). | INT | Não | 4-8 |
| `início_da_mascara` | Posição inicial em segundos da seção de áudio a ser transformada (padrão: 30). | INT | Não | 0-190 |
| `fim_da_mascara` | Posição final em segundos da seção de áudio a ser transformada (padrão: 190). | INT | Não | 0-190 |

**Observação:** O valor de `mask_end` deve ser maior que o valor de `mask_start`. O áudio de entrada deve ter entre 6 e 190 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `áudio` | A saída de áudio transformada com a seção especificada modificada de acordo com o prompt. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6589fdbff8387e403055c711a61bb3000d87e5f8cd3753d6e665b723be6f43e2`
