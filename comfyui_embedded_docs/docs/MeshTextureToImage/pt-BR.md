# MeshTextureToImage

Este nó extrai as texturas assadas de uma malha e as retorna como imagens separadas: cor base, metálica, rugosidade, oclusão e mapa normal. Canais de textura que não foram assados retornam com padrões neutros — branco para oclusão e azul liso para o mapa normal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha cujas texturas assadas são extraídas. A malha deve ter uma textura de cor base; malhas que possuem apenas cores de vértice (por exemplo, após um nó PaintMesh) não contêm uma textura e causam um erro. | MESH | Sim | — |

Nota: A malha deve ter uma textura de cor base assada. Caso contrário, o nó gera um erro e recomenda executar BakeTextureFromVoxel primeiro. Quando a textura de metálica-rugosidade estiver ausente, as saídas `metallic` e `roughness` são pretas (0). A saída `occlusion` é branca, a menos que a malha contenha oclusão ambiente assada. A saída `normal_map` é um azul neutro liso quando nenhum mapa normal foi assado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `base_color` | A textura de cor base da malha como imagem. | IMAGE |
| `metallic` | O canal metálico da textura de oclusão-rugosidade-metálica da malha, como imagem em escala de cinza. Preto (0) significa não metálico, branco (1) significa totalmente metálico. Preto quando a textura está ausente. | IMAGE |
| `roughness` | O canal de rugosidade da textura de oclusão-rugosidade-metálica da malha, como imagem em escala de cinza. Preto quando a textura está ausente. | IMAGE |
| `occlusion` | O canal de oclusão ambiente da textura de oclusão-rugosidade-metálica da malha, como imagem em escala de cinza. Branco (sem oclusão) quando a oclusão ambiente não foi assada. | IMAGE |
| `normal_map` | A textura de mapa normal da malha. Um mapa normal neutro liso (0.5, 0.5, 1.0, aparecendo como azul liso) quando nenhum mapa normal foi assado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
