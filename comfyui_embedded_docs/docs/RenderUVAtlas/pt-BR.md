# RenderUVAtlas

Renderiza o layout de UV de uma malha como uma imagem. Cada região de UV conectada (ilha) é preenchida com uma cor distinta, e os limites das ilhas são delineados em preto sobre um fundo cinza-escuro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D cujo layout de UV será renderizado. A malha deve ter coordenadas de UV; caso contrário, um erro é gerado. | MESH | Sim | - |
| `resolution` | A largura e a altura, em pixels, da imagem renderizada (padrão: 1024). | INT | Sim | 64 a 4096 (passo 64) |

Nota: Se a malha não tiver coordenadas de UV, o nó gera o erro "mesh has no UVs to render. Run UnwrapMesh first." Se a malha contiver uma dimensão de lote (matrizes 3D de UV ou de faces), apenas o primeiro item do lote é renderizado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `imagem` | A imagem do atlas de UV renderizada, com cada ilha colorida e as arestas dos limites das ilhas delineadas em preto. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
