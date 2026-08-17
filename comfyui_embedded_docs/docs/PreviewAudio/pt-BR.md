# Pré-visualizar Áudio

O nó PreviewAudio permite pré-visualizar áudio diretamente na interface, sem salvá-lo no diretório de saída do ComfyUI. Ele recebe dados de áudio como entrada e exibe um widget de player de áudio que você pode usar para ouvir o resultado. Se o áudio de entrada for None, o nó gera um erro, o que pode acontecer quando o vídeo de origem não possui trilha de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | Os dados de áudio a serem pré-visualizados. O nó gera um erro se o áudio for None, o que pode acontecer quando o vídeo de origem não possui trilha de áudio. | AUDIO | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `audio` | Os dados de áudio que foram passados pelo nó. Um widget de player de áudio é exibido na interface para pré-visualizar o áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
