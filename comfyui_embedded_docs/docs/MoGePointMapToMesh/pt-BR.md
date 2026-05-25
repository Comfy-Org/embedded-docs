> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/pt-BR.md)

# Visão Geral

Este nó converte um mapa de pontos MoGe em uma malha 3D. Ele recebe os dados geométricos produzidos por um nó de estimativa de profundidade MoGe e os triangula em uma malha com coordenadas UV e uma textura opcional.

# Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Sim | N/A | Os dados geométricos MoGe contendo mapas de pontos, profundidade e, opcionalmente, a imagem de origem. |
| `batch_index` | INT | Sim | 0 a 4096 | Qual imagem de uma geometria MoGe em lote será transformada em malha. As contagens de vértices por imagem diferem, portanto os lotes não podem ser empilhados em uma única MESH (padrão: 0). |
| `decimation` | INT | Sim | 1 a 8 | Passo do vértice; 1 = resolução total (padrão: 1). |
| `discontinuity_threshold` | FLOAT | Sim | 0.0 a 1.0 | Descarta pixels cuja variação de profundidade 3x3 exceda esta fração. 0 = desativado (padrão: 0.04). |
| `texture` | BOOLEAN | Sim | Verdadeiro/Falso | Transmite a imagem de origem como textura baseColor (padrão: Verdadeiro). |

# Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `MESH` | MESH | Uma malha 3D com vértices, faces, coordenadas UV e uma textura opcional da imagem de origem. |

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
