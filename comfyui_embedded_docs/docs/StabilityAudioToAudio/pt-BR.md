> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/pt-BR.md)

Transforma amostras de áudio existentes em novas composições de alta qualidade usando instruções de texto. Este nó recebe um arquivo de áudio de entrada e o modifica com base no seu prompt de texto para criar novo conteúdo de áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | "stable-audio-2.5"<br> | O modelo de IA a ser usado para transformação de áudio |
| `prompt` | STRING | Sim |  | Instruções de texto descrevendo como transformar o áudio (padrão: vazio) |
| `áudio` | AUDIO | Sim |  | O áudio deve ter entre 6 e 190 segundos de duração |
| `duração` | INT | Não | 1-190 | Controla a duração em segundos do áudio gerado (padrão: 190) |
| `semente` | INT | Não | 0-4294967294 | A semente aleatória usada para geração (padrão: 0) |
| `etapas` | INT | Não | 4-8 | Controla o número de etapas de amostragem (padrão: 8) |
| `força` | FLOAT | Não | 0.01-1.0 | Parâmetro que controla o quanto o áudio de entrada influencia o áudio gerado (padrão: 1.0) |

**Nota:** O áudio de entrada deve ter entre 6 e 190 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `áudio` | AUDIO | O áudio transformado gerado com base no áudio de entrada e no prompt de texto |

---
**Source fingerprint (SHA-256):** `d63ee2585be1ec1a21da72656ecea37f051a56595b15637013e515eb298fc4dc`
