# ModelMergeKrea2

Este nó mescla dois modelos combinando seus componentes internos em um nível granular, permitindo que você controle o quanto de cada parte específica de cada modelo influencia o resultado final. Ele funciona recebendo dois modelos de entrada e aplicando taxas de mesclagem separadas para diferentes seções de sua arquitetura.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `first.` | Taxa de mesclagem para o primeiro bloco de camadas (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `tmlp.` | Taxa de mesclagem para o bloco MLP temporal (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtmlp.` | Taxa de mesclagem para o bloco MLP de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `tproj.` | Taxa de mesclagem para o bloco de projeção temporal (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.layerwise_blocks.0.` | Taxa de mesclagem para o primeiro bloco de fusão de texto por camada (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.layerwise_blocks.1.` | Taxa de mesclagem para o segundo bloco de fusão de texto por camada (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.projector.` | Taxa de mesclagem para o bloco projetor de fusão de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.refiner_blocks.0.` | Taxa de mesclagem para o primeiro bloco refinador de fusão de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `txtfusion.refiner_blocks.1.` | Taxa de mesclagem para o segundo bloco refinador de fusão de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `blocks.0.` a `blocks.27.` | Taxa de mesclagem para cada um dos 28 blocos principais (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `last.` | Taxa de mesclagem para o último bloco (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Cada taxa de mesclagem controla o quanto de `model2` é usado para aquele componente específico, onde 0.0 significa usar apenas `model1`, 1.0 significa usar apenas `model2`, e valores intermediários criam uma mesclagem ponderada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `MODEL` | O modelo mesclado resultante da combinação dos dois modelos de entrada de acordo com as taxas especificadas | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`
