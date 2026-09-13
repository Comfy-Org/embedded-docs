# Pré-visualizar Áudio

The Preview Audio node lets you listen to audio directly inside ComfyUI without saving it to the output directory. It receives an audio input, checks that audio data is actually present, and then plays it through a preview player in the interface while passing the same audio on as its output.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `audio` | Os dados de áudio a serem pré-visualizados. Se esta entrada for None, o nó gera um ValueError, o que pode acontecer quando o vídeo de origem não possui faixa de áudio. | AUDIO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio` | Os dados de áudio repassados sem alteração a partir da entrada, de modo que o nó pode ser colocado no meio de um workflow. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02dbc5cb7d6924aae63c59e926a8ea265eb0889dbc2e6b47ff60f666a55d1adf`
