# Selecionar Dispositivo do Modelo

O nó SelectModelDevice permite que você escolha em qual dispositivo (CPU ou uma GPU específica) um modelo de difusão é executado. Dependendo da opção selecionada, ele restaura o dispositivo original do carregador, fixa o modelo na CPU ou o move para uma GPU específica, e lida automaticamente com conflitos com outros nós multi-GPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão a ser colocado em um dispositivo específico. | MODEL | Sim |  |
| `device` | O dispositivo de destino para o modelo. As opções são geradas dinamicamente com base nas GPUs disponíveis. (padrão: `"default"`) | COMBO | Sim | `"default"`<br>`"cpu"`<br>`"gpu:N"` para cada GPU disponível (ex.: `"gpu:0"`, `"gpu:1"`, ...) |

**Detalhes do Parâmetro:**

- `"default"`: Restaura o dispositivo atribuído pelo carregador do modelo, mesmo que um nó SelectModelDevice anterior o tenha alterado.
- `"cpu"`: Fixa tanto o dispositivo de carregamento quanto o de descarregamento na CPU.
- `"gpu:N"`: Fixa o dispositivo de carregamento na enésima GPU disponível (ex.: `"gpu:0"` para a primeira GPU). O dispositivo de descarregamento é restaurado para a escolha original do carregador.

**Notas Importantes:**

- Valores desconhecidos de `"gpu:N"` são aceitos no momento da validação para que fluxos de trabalho portáveis não falhem em máquinas com menos GPUs. Em tempo de execução, um dispositivo indisponível faz com que o modelo seja passado adiante sem alterações, com uma mensagem de log.
- Se o dispositivo solicitado não existir na máquina atual (ex.: um fluxo de trabalho criado em uma máquina com 2 GPUs é aberto em uma máquina com 1 GPU), o nó passa o modelo adiante sem alterações e registra uma mensagem em log em vez de falhar.
- Se o modelo já estiver no dispositivo solicitado, o nó segue um caminho rápido e não recarrega o modelo.
- Quando o dispositivo solicitado difere do atual, um novo modelo é criado usando a fábrica de recarga do carregador, de modo que o modelo retornado tenha pesos independentes no novo dispositivo. Carregadores que não suportam isso fazem o nó passar o modelo adiante sem alterações, com um aviso.
- Se o fluxo de trabalho já tiver MultiGPU CFG Split aplicado e a GPU escolhida corresponder a um dos clones multigpu existentes, esse clone é removido para que dois patchers não fiquem vinculados ao mesmo dispositivo.
- Posicionar este nó *após* um nó que já consumiu o modelo (ex.: um KSampler) não é recomendado, pois qualquer estado alterado pelo nó anterior será observado se o dispositivo corresponder ao original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de difusão, agora colocado no dispositivo selecionado. Se o dispositivo for inválido ou indisponível, o modelo é passado adiante sem alterações. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
