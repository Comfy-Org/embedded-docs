# Visão Geral

Este nó permite selecionar manualmente em qual dispositivo GPU o modelo VAE deve ser colocado. Por padrão, o VAE é colocado no dispositivo atribuído pelo carregador de modelos, mas você pode fixá-lo em uma GPU específica (ex.: `gpu:0`, `gpu:1`). Se o dispositivo selecionado não estiver disponível em sua máquina, o nó passará o VAE adiante sem alterações e registrará uma mensagem em vez de falhar.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE a ser atribuído a um dispositivo específico. | VAE | Sim |  |
| `dispositivo` | O dispositivo de destino para o VAE. `"default"` restaura o dispositivo atribuído pelo carregador. `"gpu:N"` fixa o VAE na N-ésima GPU disponível. CPU não é uma opção suportada e será ignorada se fornecida. (padrão: `"default"`) | COMBO | Sim | `"default"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `vae` | O modelo VAE, agora atribuído ao dispositivo selecionado. Se o dispositivo solicitado estiver indisponível ou for inválido, o VAE é passado adiante sem alterações. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`
