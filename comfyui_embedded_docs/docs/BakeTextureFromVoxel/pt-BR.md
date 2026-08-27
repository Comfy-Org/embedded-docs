# BakeTextureFromVoxel

Este nó realiza o bake de texturas PBR em uma malha 3D usando o layout de UV existente da malha. Ele amostra atributos de cor e material de um volume de voxels esparso em cada texel e gera uma imagem de cor base, além de mapas de metálico e rugosidade. Ele não desembrulha a malha, portanto um nó de desembrulhamento de UV deve estar conectado a montante.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-----------|
| `mesh` | A malha 3D na qual as texturas serão aplicadas pelo bake. Deve já possuir um layout de UV; um nó de desembrulhamento de UV deve estar conectado a montante. | MESH | Sim | |
| `voxel_colors` | Volume de voxels esparso contendo cores por voxel e atributos PBR opcionais (canais de metálico e rugosidade). | VOXEL | Sim | |
| `texture_size` | Resolução do atlas de UV quadrado (nome de exibição: "resolution", padrão: 2048). | INT | Sim | 64 a 8192 |
| `reference_mesh` | Malha densa anterior à decimação, opcional; projeta cada texel de volta à sua superfície real antes da amostragem, eliminando o aspecto facetado do bake em malhas grosseiras. | MESH | Não | |

Notas:

- A malha de entrada deve ter UVs. Se não houver UVs, o nó gera um erro. Os UVs devem estar na proporção 1:1 com os vértices (um UV por vértice).
- Quando as coordenadas da malha e dos voxels contêm uma dimensão de lote, cada item do lote é submetido ao bake separadamente. Se um item do lote não tiver voxels nem faces, ele é ignorado e uma textura preta é emitida para ele.
- Quando `reference_mesh` é fornecido para um lote, ele é correspondido pelo índice do lote, a menos que contenha apenas uma única malha; nesse caso, essa malha é usada para todos os itens.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_color` | Mapa de textura de cor base RGB. Os valores são do tipo float no intervalo de 0 a 1. | IMAGE |
| `metallic` | Mapa de metálico em tons de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de metálico. | IMAGE |
| `roughness` | Mapa de rugosidade em tons de cinza (float, 0–1). Preto quando as cores dos voxels não contêm canal de rugosidade. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `419f9e064edaeb9db8d5e052cf57a3b8b77bf7e025e8a0fc9aa0e1919c06b51c`
