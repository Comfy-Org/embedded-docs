Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/en.md)

## Visão Geral

O nó SelectModelDevice permite que você escolha manualmente em qual dispositivo (CPU ou uma GPU específica) um modelo de difusão será executado. Ele pode mover um modelo para um dispositivo diferente e lida automaticamente com conflitos com outros nós de múltiplas GPUs.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser colocado em um dispositivo específico. | MODEL | Sim |  |
| `device` | O dispositivo de destino para o modelo. As opções são geradas dinamicamente com base nas GPUs disponíveis. (padrão: "default") | COMBO | Sim | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

**Detalhes dos Parâmetros:**
- `"default"`: Restaura o dispositivo atribuído pelo carregador do modelo, mesmo que um nó SelectModelDevice anterior o tenha alterado.
- `"cpu"`: Fixa tanto o dispositivo de carregamento quanto o de descarregamento na CPU.
- `"gpu:N"`: Fixa o dispositivo de carregamento na N-ésima GPU disponível (ex.: `"gpu:0"` para a primeira GPU). O dispositivo de descarregamento é restaurado para a escolha original do carregador.

**Notas Importantes:**
- Se o dispositivo solicitado não existir na máquina atual (por exemplo, um fluxo de trabalho criado em uma máquina com 2 GPUs for aberto em uma máquina com 1 GPU), o nó passará o modelo adiante sem alterações e registrará uma mensagem em vez de falhar.
- Se o modelo já estiver no dispositivo solicitado, o nó segue um caminho rápido e não recarrega o modelo.
- Não é recomendado posicionar este nó *após* um nó que já tenha consumido o modelo (ex.: um KSampler), pois qualquer estado alterado pelo nó anterior será observado se o dispositivo corresponder ao original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo de difusão, agora colocado no dispositivo selecionado. Se o dispositivo for inválido ou estiver indisponível, o modelo é passado adiante sem alterações. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02841975f123cc8ae8152ea86f1798e0e7e68255ecd11e04271da886b75eb0fd`
