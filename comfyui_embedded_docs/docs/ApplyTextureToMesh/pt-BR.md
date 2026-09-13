# Aplicar Textura à Malha

Este nó anexa imagens de textura geradas por bake ao layout de UV de uma malha para que possam ser exportadas junto com a malha pelo nó SaveGLB. Conecte a ele a mesma malha com UVs desdobradas da qual você gerou as texturas por bake, juntamente com os mapas de imagem gerados por bake. Mapas opcionais de metalicidade, rugosidade e oclusão são empacotados em uma única textura ORM, e fornecer um mapa de normais também armazena as normais suaves dos vértices e a base de tangentes necessárias para o sombreamento correto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha com UVs desdobradas à qual as texturas geradas por bake serão anexadas. Deve ser a mesma malha usada durante o bake; um erro é gerado se a malha não tiver UVs. | MESH | Sim | — |
| `base_color` | A imagem de cor base gerada por bake. Armazenada como a textura da malha e limitada ao intervalo 0-1. | IMAGE | Sim | — |
| `metallic` | O mapa de metalicidade gerado por bake. Usado como o canal azul da textura ORM combinada; o padrão é 0 quando não fornecido. | IMAGE | Não | — |
| `roughness` | O mapa de rugosidade gerado por bake. Usado como o canal verde da textura ORM combinada; o padrão é 1 quando não fornecido. | IMAGE | Não | — |
| `occlusion` | O mapa de oclusão ambiente gerado por bake. Usado como o canal vermelho da textura ORM combinada; o padrão é 1 quando não fornecido. Quando fornecido, a textura ORM também é marcada como a textura de oclusão para o SaveGLB. | IMAGE | Não | — |
| `normal_map` | O mapa de normais em espaço tangente gerado por bake. Quando fornecido, o nó recalcula as tangentes por vértice e exporta normais suaves dos vértices para que o mapa de normais faça o sombreamento corretamente. | IMAGE | Não | — |

Observação: A entrada `mesh` deve ter coordenadas UV; se não tiver, o nó gera um erro solicitando que você conecte a mesma malha com UVs desdobradas usada para o bake.

Observação: Quando qualquer um dos mapas `metallic`, `roughness` ou `occlusion` estiver conectado, todos os três são empacotados em uma única textura ORM do glTF com canais R = oclusão, G = rugosidade, B = metalicidade. Mapas ausentes são preenchidos com padrões (oclusão 1, rugosidade 1, metalicidade 0), e mapas com resoluções diferentes são redimensionados para a maior largura e altura entre os mapas fornecidos.

Observação: Quando `normal_map` está conectado, as normais armazenadas da malha são substituídas por normais suaves dos vértices calculadas e uma base de tangentes por vértice é adicionada. Coordenadas UV que ficam fora do intervalo [0,1] são escaladas uniformemente para dentro de [0,1], preservando a proporção; um aviso é registrado se a extensão de UV parecer um layout em tiles/UDIM. Para malhas em lote, a normalização de UV é aplicada separadamente a cada item do lote usando a mesma lógica da etapa de bake, para que ambos permaneçam alinhados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `mesh` | A malha de entrada com as imagens de textura anexadas ao seu layout de UV, pronta para ser salva pelo SaveGLB. | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7492922c9c7c0117366cb8b9017fc192eb8dd6b6594fd429044d60408693210e`
