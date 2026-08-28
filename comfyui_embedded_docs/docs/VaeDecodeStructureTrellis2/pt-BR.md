# VaeDecodeStructureTrellis2

Este nó converte amostras latentes de estrutura Trellis em uma grade de voxels 3D usando o decodificador de estrutura de uma VAE. Ele lê apenas os primeiros 8 canais do latente, reconstrói a ocupação dos voxels e ajusta a resolução de saída para 32 ou 64, conforme solicitado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `Amostras` | A representação latente da estrutura a ser decodificada. Apenas os primeiros 8 canais do latente são usados para decodificação. | LATENT | Sim | - |
| `vae` | A VAE cujo decodificador de estrutura converte o latente em uma grade de voxels. A decodificação é realizada em lotes. | VAE | Sim | - |
| `Resolução` | A resolução espacial alvo da grade de voxels de saída (padrão: "32"). Se a grade decodificada tiver uma resolução diferente, ela é reduzida para corresponder. | COMBO | Sim | "32"<br>"64" |

Nota: Quando a resolução da grade de voxels decodificada difere da `resolution` selecionada, a grade é reduzida usando max pooling 3D para o tamanho solicitado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `Voxel` | Uma grade de ocupação de voxels binária como um tensor float com formato [batch, profundidade, altura, largura]. Os valores são 1.0 para voxels ocupados e 0.0 para voxels vazios. | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
