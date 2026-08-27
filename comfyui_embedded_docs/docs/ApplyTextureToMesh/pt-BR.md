# ApplyTextureToMesh

Este nó anexa imagens de textura assadas ao layout de UV de uma malha para que possam ser exportadas junto com a malha pelo nó SaveGLB. Conecte a mesma malha com UVs planificados usada durante o processo de assar as texturas, juntamente com os mapas de imagem assados. Mapas opcionais de metálico, rugosidade e oclusão são empacotados em uma única textura ORM, e o fornecimento de um mapa normal também armazena as normais suaves e as tangentes necessárias para a sombreamento correto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha com UVs planificados à qual as texturas assadas serão anexadas. Deve ser a mesma malha usada durante o processo de assar; um erro é gerado se a malha não tiver UVs. | MESH | Sim | — |
| `base_color` | A imagem de cor base assada. Armazenada como textura da malha e limitada ao intervalo de 0 a 1. | IMAGE | Sim | — |
| `metallic` | O mapa de metálico assado. Usado como o canal azul da textura ORM combinada; o padrão é 0 quando não fornecido. | IMAGE | Não | — |
| `roughness` | O mapa de rugosidade assado. Usado como o canal verde da textura ORM combinada; o padrão é 1 quando não fornecido. | IMAGE | Não | — |
| `occlusion` | O mapa de oclusão ambiente assado. Usado como o canal vermelho da textura ORM combinada; o padrão é 1 quando não fornecido. Quando fornecido, a textura ORM também é marcada como a textura de oclusão para o SaveGLB. | IMAGE | Não | — |
| `normal_map` | O mapa normal assado em espaço tangente. Quando fornecido, o nó recalcula a base tangente por vértice e exporta normais de vértice suaves para que o mapa normal sombreie corretamente. | IMAGE | Não | — |

Nota: Quando qualquer um dos parâmetros `metallic`, `roughness` ou `occlusion` estiver conectado, os três serão empacotados em uma única textura ORM glTF, com canais R = oclusão, G = rugosidade, B = metálico. Mapas ausentes são preenchidos com valores padrão (oclusão 1, rugosidade 1, metálico 0), e mapas com resoluções diferentes são redimensionados para a maior largura e altura. Quando `normal_map` estiver conectado, as normais da malha são substituídas por normais de vértice suaves calculadas e uma base tangente é adicionada. Coordenadas de UV que estejam fora do intervalo [0,1] são escaladas uniformemente para o intervalo [0,1], preservando a proporção.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com as imagens de textura anexadas ao seu layout de UV, pronta para ser salva pelo SaveGLB. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
