# Dividir Canais de Áudio

O nó SplitAudioChannels separa áudio estéreo em canais esquerdo e direito individuais. Ele recebe uma entrada de áudio estéreo com dois canais e gera dois fluxos de áudio separados, um para o canal esquerdo e outro para o canal direito.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `áudio` | A entrada de áudio estéreo a ser separada em canais | AUDIO | Sim | - |

**Observação:** O áudio de entrada deve ter exatamente dois canais (estéreo). O nó gerará um erro se o áudio de entrada tiver apenas um canal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `left` | O áudio do canal esquerdo separado | AUDIO |
| `right` | O áudio do canal direito separado | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/pt-BR.md)

---
**Source fingerprint (SHA-256):** `48f329f3eb9749e75eda1038c43caf42ee63d8a1fa66ab29ad3d34b5d136e323`
