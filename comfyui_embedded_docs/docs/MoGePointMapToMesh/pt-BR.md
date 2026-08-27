# MoGe Point Map to Mesh

Este nó converte um mapa de pontos MoGe em um mesh 3D. Ele recebe os dados geométricos produzidos por um nó de estimativa de profundidade MoGe e os triangula em um mesh com coordenadas UV e uma textura opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Os dados geométricos MoGe contendo mapas de pontos, profundidade e, opcionalmente, a imagem de origem. | MOGE_GEOMETRY | Sim | N/D |
| `batch_index` | Qual imagem de uma geometria MoGe em lote será transformada em mesh. Como as contagens de vértices diferem por imagem, os lotes não podem ser empilhados em um único MESH (padrão: 0). | INT | Sim | 0 a 4096 |
| `decimation` | Passo entre vértices; 1 = resolução total (padrão: 1). | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta pixels cuja extensão de profundidade 3x3 exceda essa fração. 0 = desativado (padrão: 0.04). | FLOAT | Sim | 0.0 a 1.0 |
| `texture` | Transmite a imagem de origem como textura baseColor (padrão: True). | BOOLEAN | Sim | True/False |

Nota: `batch_index` deve ser menor que o tamanho do lote da `moge_geometry` de entrada; selecionar um índice fora do intervalo gera um erro. Se a triangulação produzir um mesh vazio, o nó gera um erro — definir `discontinuity_threshold` como 0 desativa o filtro de descontinuidade de profundidade. O mesh de saída é convertido para coordenadas glTF: dados MoGe em perspectiva (X direita, Y para baixo, Z para frente) são invertidos para corresponder ao glTF (Y para cima, Z para trás), e dados panorâmicos são rotacionados de acordo. Quando `texture` está habilitado, a imagem de origem de `moge_geometry` é usada como textura baseColor.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MESH` | Um mesh 3D com vértices, faces, coordenadas UV e uma textura baseColor opcional proveniente da imagem de origem. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
