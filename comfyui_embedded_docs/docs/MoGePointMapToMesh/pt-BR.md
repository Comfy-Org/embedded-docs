# MoGe Point Map to Mesh

Este nó converte um mapa de pontos MoGe em uma malha 3D. Ele recebe os dados geométricos produzidos por um nó de estimativa de profundidade MoGe e triangula uma imagem deles em uma malha com coordenadas UV e uma textura opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Os dados geométricos MoGe contendo mapas de pontos, profundidade e, opcionalmente, a imagem de origem. | MOGE_GEOMETRY | Sim | N/A |
| `batch_index` | Qual imagem de uma geometria MoGe em lote deve ser transformada em malha. As contagens de vértices por imagem diferem, portanto os lotes não podem ser empilhados em um único MESH (padrão: 0). | INT | Sim | 0 a 4096 |
| `decimation` | Passo de vértice; 1 = resolução completa (padrão: 1). | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta pixels cuja variação de profundidade 3x3 exceda esta fração. 0 = desativado (padrão: 0.04). | FLOAT | Sim | 0.0 a 1.0 |
| `texture` | Transmite a imagem de origem como textura baseColor (padrão: True). | BOOLEAN | Sim | True/False |

Nota: `batch_index` deve ser menor que o tamanho do lote do `moge_geometry` fornecido. A geometria de entrada deve conter dados de pontos e, se a malha gerada estiver vazia, o nó retorna um erro sugerindo `discontinuity_threshold = 0`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MESH` | Uma malha 3D com vértices, faces, coordenadas UV e uma textura opcional da imagem de origem. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
