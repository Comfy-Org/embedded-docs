# MoGe Point Map to Mesh

Este nó converte um mapa de pontos do MoGe em uma malha 3D. Ele recebe os dados de geometria produzidos por um nó de estimativa de profundidade MoGe e os triangula em uma malha com coordenadas UV e uma textura opcional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Range |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Os dados de geometria do MoGe contendo mapas de pontos, profundidade e, opcionalmente, a imagem de origem. | MOGE_GEOMETRY | Sim | N/A |
| `batch_index` | Qual imagem de uma geometria MoGe em lote deve ser convertida em malha. Como a contagem de vértices varia por imagem, lotes não podem ser empilhados em um único MESH (padrão: 0). | INT | Sim | 0 a 4096 |
| `decimation` | Passo de vértices; 1 = resolução total (padrão: 1). | INT | Sim | 1 a 8 |
| `discontinuity_threshold` | Descarta os pixels cuja variação de profundidade em uma janela 3x3 exceda esta fração. 0 = desativado (padrão: 0.04). | FLOAT | Sim | 0.0 a 1.0 |
| `texture` | Repassa a imagem de origem como a textura baseColor (padrão: True). | BOOLEAN | Sim | True/False |

Observação: `batch_index` deve ser menor que o tamanho do lote da entrada `moge_geometry`; selecionar um índice fora do intervalo gera um erro. A entrada deve conter uma saída de pontos, caso contrário o nó gera um erro. Se a triangulação produzir uma malha vazia, o nó gera um erro — definir `discontinuity_threshold` como 0 desativa o filtro de descontinuidade de profundidade. A malha de saída é convertida para coordenadas glTF: os dados MoGe em perspectiva (X para a direita, Y para baixo, Z para frente) são invertidos para corresponder ao glTF (Y para cima, Z para trás), e os dados panorâmicos (geometria sem parâmetros intrínsecos) são rotacionados de acordo, com o enrolamento corrigido. Quando `texture` está ativado, a imagem de origem de `moge_geometry` é usada como a textura baseColor.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MESH` | Uma malha 3D com vértices, faces, coordenadas UV e uma textura baseColor opcional proveniente da imagem de origem. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
