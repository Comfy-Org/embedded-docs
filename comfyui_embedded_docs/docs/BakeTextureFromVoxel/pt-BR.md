# BakeTextureFromVoxel

Este nó assa texturas PBR em uma malha 3D usando o layout de UV existente da malha. Ele amostra atributos de cor e material em um volume esparso de voxels para cada texel e gera uma imagem de cor base, além de mapas de metalicidade e rugosidade. Ele não desdobra a malha, portanto um nó de desdobramento de UV deve ser conectado anteriormente na cadeia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D na qual as texturas serão assadas. Deve já possuir um layout de UV; um nó de desdobramento de UV deve ser conectado antes. | MESH | Sim | |
| `voxel_colors` | Volume esparso de voxels contendo cores por voxel e atributos PBR opcionais (canais de metalicidade e rugosidade). | VOXEL | Sim | |
| `texture_size` | Resolução do atlas de UV quadrado (nome de exibição: "resolution", padrão: 2048). | INT | Sim | 64 a 8192 |
| `reference_mesh` | Malha densa opcional anterior à decimação; projeta cada texel de volta na superfície real antes da amostragem, eliminando efeitos facetados do assamento em malhas grosseiras. | MESH | Não | |

Notas:

- A malha de entrada deve ter UVs. Se não houver UVs, o nó gera um erro. Os UVs devem estar em correspondência de 1:1 com os vértices (um UV por vértice).
- Quando as coordenadas da malha e do voxel contêm uma dimensão de lote, cada item do lote é assado separadamente. Se um item do lote não tiver voxels ou faces, ele é ignorado e uma textura preta é gerada para ele.
- Quando `reference_mesh` é fornecido para um lote, ele é associado pelo índice do lote, a menos que contenha apenas uma única malha; nesse caso, essa malha é usada para todos os itens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de cor base RGB. Os valores são do tipo float no intervalo de 0 a 1. | IMAGE |
| `metallic` | Mapa de metalicidade em escala de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de metalicidade. | IMAGE |
| `roughness` | Mapa de rugosidade em escala de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de rugosidade. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
