# Stability AI Text To Audio

Gera música e efeitos sonoros de alta qualidade a partir de descrições textuais. Este nó utiliza a tecnologia de geração de áudio da Stability AI para criar conteúdo de áudio com base em suas instruções textuais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de geração de áudio a ser utilizado (padrão: "stable-audio-2.5") | COMBO | Sim | `"stable-audio-2.5"` |
| `prompt` | A descrição textual usada para gerar o conteúdo de áudio (padrão: string vazia) | STRING | Sim | - |
| `duration` | Controla a duração em segundos do áudio gerado (padrão: 190) | INT | Não | 1-190 |
| `seed` | A semente aleatória usada para a geração (padrão: 0) | INT | Não | 0-4294967294 |
| `steps` | Controla o número de etapas de amostragem (padrão: 8) | INT | Não | 4-8 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio` | O arquivo de áudio gerado com base na instrução textual | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5185241ca7a9b4bc38dfa8bafdae63ec3c151a3038a26ffe8e35492c0550fa88`
