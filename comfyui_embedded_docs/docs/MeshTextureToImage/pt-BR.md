# Textura da malha para imagem

Este nó extrai as texturas assadas de uma malha e as retorna como imagens separadas: cor base, metálico, rugosidade, oclusão e mapa normal. Canais de textura que não foram assados retornam como padrões neutros — branco para oclusão e um azul uniforme para o mapa normal.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha cujas texturas assadas são extraídas. A malha deve ter uma textura de cor base; malhas que possuem apenas cores de vértice (por exemplo, após um nó PaintMesh) não contêm uma textura e causam um erro. | MESH | Sim | — |

Nota: A malha deve ter uma textura de cor base assada. Se não tiver, o nó gera um erro e recomenda executar BakeTextureFromVoxel primeiro. Quando a textura metallic-roughness estiver ausente, as saídas `metallic` e `roughness` são pretas (0). A saída `occlusion` é branca, a menos que a malha contenha oclusão ambiente assada (o sinalizador occlusion-in-metallic-roughness da malha está definido). A saída `normal_map` é um azul neutro uniforme quando nenhum mapa normal foi assado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `base_color` | A textura de cor base da malha como uma imagem. | IMAGE |
| `metallic` | O canal metálico da textura occlusion-roughness-metallic da malha, como uma imagem em escala de cinza. Preto (0) significa não metálico, branco (1) significa totalmente metálico. Preto quando a textura estiver ausente. | IMAGE |
| `roughness` | O canal de rugosidade da textura occlusion-roughness-metallic da malha, como uma imagem em escala de cinza. Preto quando a textura estiver ausente. | IMAGE |
| `occlusion` | O canal de oclusão ambiente da textura occlusion-roughness-metallic da malha, como uma imagem em escala de cinza. Branco (sem oclusão) quando a oclusão ambiente não foi assada. | IMAGE |
| `normal_map` | A textura de mapa normal da malha. Um mapa normal neutro uniforme (0.5, 0.5, 1.0, parecendo azul uniforme) quando nenhum mapa normal foi assado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
