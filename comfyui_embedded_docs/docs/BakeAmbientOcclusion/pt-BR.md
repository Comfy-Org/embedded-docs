# BakeAmbientOcclusion

Gera um mapa de oclusão ambiente a partir de uma malha de alta poligonalidade no layout UV de uma malha de baixa poligonalidade. A saída é uma imagem em escala de cinza em que texels brancos representam áreas abertas e texels escuros representam frestas; o mapa é destinado à entrada de oclusão do nó Apply Texture To Mesh. Conecte a malha de baixa poligonalidade com UVs desembrulhados e a malha de alta poligonalidade da qual ela foi decimada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Range |
|-----------|-------------|-----------|----------|-------|
| `low_poly` | A malha de baixa poligonalidade com UVs desembrulhados usada para gerar o mapa. Precisa ter UVs; o nó gera um erro se eles estiverem ausentes. | MESH | Sim | - |
| `high_poly` | A malha de alta poligonalidade da qual a malha de baixa poligonalidade foi decimada, usada como geometria de origem para a oclusão. | MESH | Sim | - |
| `resolution` | Resolução da textura em pixels; cada texel recebe um valor de oclusão. Padrão: 1024. | INT | Sim | 64 a 8192 (passo 64) |
| `samples` | Raios por texel. Mais raios = resultado mais suave, porém mais lento. Aumente se houver granulação. Padrão: 64. | INT | Sim | 4 a 1024 (passo 4) |
| `max_distance` | Comprimento do raio, como fração da diagonal do bounding box. Valores menores = oclusão mais localizada e restrita. Padrão: 0,5. | FLOAT | Sim | 0,01 a 2,0 (passo 0,01) |
| `strength` | Escala a oclusão. >1 escurece, <1 clareia. Padrão: 1,0. | FLOAT | Sim | 0,0 a 2,0 (passo 0,05) |
| `bias` | Elevação da origem do raio em relação à superfície, como fração da diagonal do bounding box. Aumente se superfícies planas apresentarem manchas ou buracos escuros. Padrão: 0,01. | FLOAT | Sim | 0,0001 a 0,2 (passo 0,0005) |

Nota: `low_poly` deve ter coordenadas UV — este nó nunca desembrulha a malha. Se `high_poly` contiver apenas um item de lote, ele será reutilizado para todos os itens de lote de `low_poly`; itens de lote de `low_poly` sem faces são ignorados e substituídos por uma imagem totalmente branca, com um aviso registrado no log.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `occlusion` | Imagem de oclusão ambiente em escala de cinza com valores em [0,1] (branco = aberto, escuro = frestas), uma imagem por item de lote de `low_poly`. Destinada à entrada de oclusão do nó Apply Texture To Mesh (empacotada no mapa ORM / occlusionTexture). | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeAmbientOcclusion/pt-BR.md)

---
**Source fingerprint (SHA-256):** `63ea6ce5289728d351fdd7d722e9a299ebb1283e1128262a817466ec6d23786a`
