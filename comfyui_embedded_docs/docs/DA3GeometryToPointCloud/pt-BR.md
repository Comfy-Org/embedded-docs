# Converter Geometria DA3 em Nuvem de Pontos

Este nó converte um mapa de profundidade de um objeto DA3_GEOMETRY em uma nuvem de pontos 3D. Ele aplica filtragem com base em máscaras de confiança e céu, e transforma os pontos em um sistema de coordenadas mundial comum adequado para cenas multivisão.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `da3_geometry` | O objeto DA3_GEOMETRY contendo dados de profundidade e mapas opcionais de imagem, confiança e céu | DA3_GEOMETRY | Sim | - |
| `batch_index` | Qual imagem de um lote converter (padrão: 0) | INT | Sim | 0 a 4096 |
| `confidence_threshold` | Excluir pixels cuja confiança normalizada por imagem esteja abaixo deste valor (0 = manter todos). Usado quando a geometria possui um mapa de confiança (modelos Small/Base). (padrão: 0,1) | FLOAT | Sim | 0,0 a 1,0 |
| `use_sky_mask` | Excluir pixels com probabilidade de céu (céu >= 0,5). Usado quando a geometria possui um mapa de céu (modelos Mono/Metric). (padrão: Verdadeiro) | BOOLEAN | Sim | Verdadeiro ou Falso |
| `downsample` | Pegar cada enésimo pixel (1 = resolução total). Valores maiores geram menos pontos e processamento mais rápido. (padrão: 1) | INT | Sim | 1 a 16 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `point_cloud` | Um objeto de nuvem de pontos contendo pontos 3D filtrados, cores opcionais e valores de confiança opcionais | DA3_POINT_CLOUD |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
