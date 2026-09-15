# Gerar Textura a Partir de Voxel

Este nó faz o bake de texturas PBR em uma malha 3D usando o layout UV existente da malha. Ele rasteriza a malha no espaço UV e amostra atributos de cor e material de um volume de voxels esparso em cada texel, produzindo uma imagem de cor base mais mapas de metalicidade e rugosidade. Ele não faz o unwrap da malha, portanto um nó de UV unwrap deve ser conectado a montante; as imagens resultantes devem ser pareadas com a mesma malha em ApplyTextureToMesh para salvamento como GLB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D na qual aplicar as texturas. Deve já ter um layout UV; um nó de UV unwrap deve ser conectado a montante. | MESH | Sim | |
| `voxel_colors` | Volume de voxels esparso contendo cores por voxel e atributos PBR opcionais (canais de metalicidade e rugosidade). | VOXEL | Sim | |
| `texture_size` | Resolução quadrada do atlas UV (nome de exibição: "resolution", padrão: 2048). | INT | Sim | 64 a 8192 |
| `reference_mesh` | Malha densa pré-decimação opcional; retroprojeta cada texel em sua superfície real antes da amostragem, removendo o bake facetado em malhas grosseiras. | MESH | Não | |

Observações:

- A malha de entrada deve ter UVs. Se não houver UVs, o nó gera um erro. As UVs devem ser 1:1 com os vértices (uma UV por vértice).
- Quando as coordenadas da malha e dos voxels contêm uma dimensão de lote, cada item do lote é processado separadamente. Se um item do lote não tiver voxels ou faces, ele será ignorado e uma textura preta será emitida para ele.
- Quando `reference_mesh` é fornecido para um lote, ele é associado pelo índice do lote, a menos que contenha apenas uma única malha; nesse caso, essa malha é usada para todos os itens.
- Texels que não são cobertos por nenhum triângulo UV são preenchidos a partir do texel coberto mais próximo, para que as costuras da textura não puxem preto.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de cor base RGB. Os valores são float no intervalo de 0–1. | IMAGE |
| `metallic` | Mapa de metalicidade em escala de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de metalicidade. | IMAGE |
| `roughness` | Mapa de rugosidade em escala de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de rugosidade. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
