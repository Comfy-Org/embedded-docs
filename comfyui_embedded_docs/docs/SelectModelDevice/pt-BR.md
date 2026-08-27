# Selecionar Dispositivo do Modelo

## Visão geral

O nó SelectModelDevice permite que você escolha manualmente em qual dispositivo (CPU ou uma GPU específica) um modelo de difusão será executado. Ele pode mover um modelo para um dispositivo diferente e lida automaticamente com conflitos com outros nós multi-GPU.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser colocado em um dispositivo específico. | MODEL | Sim |  |
| `device` | O dispositivo de destino para o modelo. As opções são geradas dinamicamente com base nas GPUs disponíveis. (padrão: "default") | COMBO | Sim | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (uma entrada `"gpu:N"` para cada GPU detectada) |

**Detalhes do parâmetro:**
- `"default"`: Restaura o dispositivo atribuído pelo carregador do modelo, mesmo que um nó SelectModelDevice anterior o tenha alterado.
- `"cpu"`: Fixa o dispositivo de carregamento e o de descarregamento (offload) na CPU.
- `"gpu:N"`: Fixa o dispositivo de carregamento na N-ésima GPU disponível (por exemplo, `"gpu:0"` para a primeira GPU). O dispositivo de descarregamento (offload) é restaurado para a escolha original do carregador.

**Notas importantes:**
- Se o dispositivo solicitado não existir na máquina atual (por exemplo, um fluxo de trabalho criado em uma máquina com 2 GPUs for aberto em uma máquina com 1 GPU), o nó repassa o modelo inalterado e registra uma mensagem em vez de falhar.
- Se o modelo já estiver no dispositivo solicitado, o nó usa um caminho rápido e não recarrega o modelo.
- Se o carregador do modelo não oferecer suporte a multi-GPU (sem fábrica de recarga), o nó repassa o modelo inalterado e registra um aviso.
- Quando um clone do MultiGPU CFG Split já ocupa o dispositivo selecionado, esse clone é removido para que dois modelos não fiquem vinculados ao mesmo dispositivo.
- Quando um dispositivo específico é selecionado, o nó também ajusta o dtype de computação do modelo para um tipo compatível com esse dispositivo.
- Não é recomendado posicionar este nó *após* um nó que já consumiu o modelo (por exemplo, um KSampler), pois qualquer estado alterado pelo nó anterior será observado se o dispositivo corresponder ao original.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `model` | O modelo de difusão, agora colocado no dispositivo selecionado. Se o dispositivo for inválido ou indisponível, o modelo é repassado inalterado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
