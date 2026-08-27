# MeshToFile3D

Este nó serializa uma malha em um objeto de arquivo GLB que pode ser passado para os nós Save 3D ou Preview 3D. Ele carrega todos os dados da malha, incluindo UVs, cores, normais, textura, mapas de normal/oclusão/emissão e configurações de material. Apenas o primeiro item de um lote com vários itens é usado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `mesh` | A malha a ser convertida em um arquivo GLB, incluindo UVs, cores, normais, textura, mapas de normal/oclusão/emissão e material. Apenas um item por lote é suportado; se um lote contiver vários itens, o primeiro é usado. | MESH | Sim | Malha única |

Nota: O nó suporta apenas um item por lote. Se a malha de entrada contiver mais de um item em seu lote, um aviso é registrado e o primeiro item é usado. A malha deve conter pelo menos um vértice e uma face; uma malha vazia gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `model_3d` | Um objeto de arquivo GLB (glTF Binário) contendo a malha serializada, pronto para ser salvo ou visualizado por outros nós 3D. | FILE3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
