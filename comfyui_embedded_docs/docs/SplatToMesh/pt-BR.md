# Extrair Malha do Splat

Este nó converte um splat Gaussiano 3D em uma superfície de malha colorida. Ele funciona rasterizando os gaussianos em uma grade de densidade, extraindo uma isosuperfície em um nível de densidade escolhido e, em seguida, aplicando suavização e limpeza opcionais para produzir uma malha triangular limpa e colorida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `splat` | O splat gaussiano de entrada para converter em malha | SPLAT | Sim | - |
| `resolução` | Resolução da grade de densidade ao longo do eixo mais longo. Valores maiores produzem detalhes de superfície mais finos, mas exigem mais VRAM e tempo de processamento (cresce com resolução^3). Padrão: 384 | INT | Sim | 64 - 768 (passo 16) |
| `kernel` | Meia largura máxima do splat em voxels. Cada gaussiano é rasterizado em uma janela dimensionada para seu próprio 3-sigma, limitada a este valor. Pequenos surfels permanecem econômicos enquanto os grandes não são truncados. Aumente se splats esparsos deixarem lacunas. Padrão: 5 | INT | Sim | 1 - 8 |
| `suavizar` | Iterações de suavização de malha Taubin. Suaviza a superfície sem encolhê-la (preservando volume), diferente de desfocar a densidade. 0 significa sem suavização. Padrão: 0 | INT | Sim | 0 - 60 |
| `nível` | Nível da isosuperfície. Selecionado automaticamente pela limiarização de Otsu; este valor influencia a seleção automática (1.0 = automático, valores menores produzem superfícies mais cheias/mais conectadas, valores maiores produzem superfícies mais finas/mais justas). Padrão: 0.4 | FLOAT | Sim | 0.0 - 2.0 (passo 0.01) |
| `mín_componente` | Descarta componentes conectadas menores que este número de vértices. Remove bolhas flutuantes destacadas e a casca interna de paredes duplas. 0 mantém todos os componentes. Padrão: 500 | INT | Sim | 0 - 100000 (passo 50) |
| `mín_opacidade` | Ignora gaussianos mais fracos que este valor antes da malhagem. Padrão: 0.02 | FLOAT | Sim | 0.0 - 1.0 (passo 0.01) |
| `nitidez_cor` | Nitidez da textura do vértice. 1.0 fornece mistura fisicamente correta; valores maiores tendem a cor de cada voxel para seu gaussiano dominante em vez de calcular a média dos vizinhos (remove o borrão da textura). Afeta apenas a cor, não a geometria. Padrão: 2.0 | FLOAT | Sim | 1.0 - 8.0 (passo 0.5) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `mesh` | A malha colorida extraída com renderização não iluminada (tipo emissiva) para corresponder à aparência do splat | MESH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToMesh/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5a7060c26252b587ce533e5682abe880a6fcc83f6671232489c3de64b094cd84`
