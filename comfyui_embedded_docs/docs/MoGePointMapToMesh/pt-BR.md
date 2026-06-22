# MoGe Point Map to Mesh

Este nó converte um mapa de pontos MoGe em uma malha 3D. Ele recebe os dados geométricos produzidos por um nó de estimativa de profundidade MoGe e os triangula em uma malha com coordenadas UV e uma textura opcional.

# Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Os dados geométricos MoGe contendo mapas de pontos, profundidade e, opcionalmente, a imagem de origem. | MOGE_GEOMETRY | Sim | N/A |
| `batch_index` | Qual imagem de uma geometria MoGe em lote será transformada em malha. As contagens de vértices por imagem diferem, portanto os lotes não podem ser empilhados em uma única MESH (padrão: 0). | INT | Sim | 0 a 4096 |
| `decimation` | Passo do vértice; 1 = resolução total (padrão: 1). | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta pixels cuja variação de profundidade 3x3 exceda esta fração. 0 = desativado (padrão: 0.04). | FLOAT | Sim | 0.0 a 1.0 |
| `texture` | Transmite a imagem de origem como textura baseColor (padrão: Verdadeiro). | BOOLEAN | Sim | Verdadeiro/Falso |

# Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MESH` | Uma malha 3D com vértices, faces, coordenadas UV e uma textura opcional da imagem de origem. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
