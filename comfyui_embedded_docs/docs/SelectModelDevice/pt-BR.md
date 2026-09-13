# Selecionar Dispositivo do Modelo

O nó Select Model Device permite escolher manualmente em qual dispositivo (CPU ou uma GPU específica) um modelo de difusão é executado. Ele pode mover um modelo para outro dispositivo e lida automaticamente com conflitos com outros nós multi-GPU. Selecionar `"default"` restaura o dispositivo original escolhido pelo carregador de modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser colocado em um dispositivo específico. | MODEL | Sim |  |
| `device` | O dispositivo de destino para o modelo. As opções são geradas dinamicamente com base nos dispositivos disponíveis na máquina atual. (padrão: `"default"`) | COMBO | Sim | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (uma entrada `"gpu:N"` por GPU detectada) |

**Detalhes dos Parâmetros:**
- `"default"`: Restaura os dispositivos de carregamento e descarregamento atribuídos pelo carregador de modelo, mesmo após uma chamada anterior de Select Model Device.
- `"cpu"`: Fixa tanto o dispositivo de carregamento quanto o de descarregamento em CPU.
- `"gpu:N"`: Fixa o dispositivo de carregamento na N-ésima GPU disponível (por exemplo, `"gpu:0"` para a primeira GPU). O dispositivo de descarregamento é restaurado para a escolha original do carregador.

**Observações Importantes:**
- Se o dispositivo solicitado não existir na máquina atual (por exemplo, um fluxo de trabalho criado em uma máquina com 2 GPUs é aberto em uma máquina com 1 GPU), o nó passa o modelo adiante sem alterações e registra uma mensagem em vez de falhar. Valores `gpu:N` desconhecidos são permitidos durante a validação de entrada para que fluxos de trabalho portáveis não gerem erro antecipadamente.
- Se o modelo já estiver no dispositivo solicitado, o nó usa um caminho rápido e não recarrega o modelo.
- Quando o dispositivo solicitado for diferente do dispositivo em que o modelo de entrada já está, um novo modelo é gerado usando a fábrica de recarregamento do carregador, para que o novo patcher possua pesos independentes no novo dispositivo.
- Se o carregador de modelo não oferecer suporte a multi-GPU (sem fábrica de recarregamento), o nó passa o modelo adiante sem alterações e registra um aviso.
- Quando um clone do MultiGPU CFG Split já ocupa o dispositivo selecionado, esse clone é removido para que dois modelos não sejam vinculados ao mesmo dispositivo.
- Quando um dispositivo não padrão é selecionado (CPU ou GPU), o nó também ajusta o dtype de computação do modelo para um compatível com esse dispositivo.
- Não é recomendado colocar este nó depois de um nó que já consumiu o modelo (por exemplo, um KSampler), porque qualquer estado alterado pelo nó anterior será observado se o dispositivo corresponder ao original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de difusão, agora colocado no dispositivo selecionado. Se o dispositivo era inválido ou indisponível, o modelo é passado adiante sem alterações. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
