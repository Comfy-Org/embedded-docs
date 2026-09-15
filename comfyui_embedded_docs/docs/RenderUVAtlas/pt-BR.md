# Renderizar Atlas UV

Renderiza o layout de UV de uma malha como uma imagem. Cada região de UV conectada (chart) é preenchida com uma cor distinta, e as arestas de contorno do chart são delineadas em preto sobre um fundo cinza-escuro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `mesh` | A malha 3D cujo layout de UV será renderizado. A malha deve ter coordenadas UV; caso contrário, o nó gera o erro "mesh has no UVs to render. Run UnwrapMesh first." | MESH | Sim | - |
| `resolution` | A largura e a altura, em pixels, da imagem quadrada renderizada (padrão: 1024). | INT | Sim | 64 a 4096 (passo 64) |

Observação: Se a malha contiver uma dimensão de lote (arrays de UV 3D ou de faces), apenas o primeiro item do lote será renderizado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `image` | A imagem do atlas UV renderizada, retornada como um lote de imagem única. Cada região de UV (chart) é colorida, e as arestas de contorno do chart são delineadas em preto. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
