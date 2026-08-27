# TextEncodeAceStepAudio

O nó TextEncodeAceStepAudio processa entradas de texto para condicionamento de áudio, combinando tags e letras em tokens e, em seguida, codificando-os com força de letras ajustável. Ele recebe um modelo CLIP juntamente com descrições de texto e letras, tokeniza-os juntos e gera dados de condicionamento adequados para tarefas de geração de áudio. O nó permite ajustar finamente a influência das letras por meio de um parâmetro de força que controla seu impacto na saída final.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `tags` | Tags de texto ou descrições para condicionamento de áudio (suporta entrada de múltiplas linhas e prompts dinâmicos) | STRING | Sim | - |
| `lyrics` | Texto das letras para condicionamento de áudio (suporta entrada de múltiplas linhas e prompts dinâmicos) | STRING | Sim | - |
| `lyrics_strength` | Controla a força da influência das letras na saída do condicionamento (padrão: 1.0, passo: 0.01) | FLOAT | Sim | 0.0 - 10.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `conditioning` | Os dados de condicionamento codificados que contêm os tokens de texto processados com a força das letras aplicada | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`
