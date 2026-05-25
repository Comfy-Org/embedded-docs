> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/en.md)

## Visão Geral

Este nó realiza estimativa de profundidade em imagens panorâmicas equirretangulares. Ele funciona dividindo o panorama em 12 vistas em perspectiva, executando o modelo de estimativa de profundidade MoGe em cada vista e, em seguida, mesclando os resultados em um único mapa de profundidade completo para o panorama original.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `moge_model` | MOGE_MODEL | Sim | | O modelo MoGe a ser usado para inferência. |
| `image` | IMAGE | Sim | | Imagem panorâmica equirretangular (qualquer proporção de aspecto). |
| `resolution_level` | INT | Sim | 0 a 9 | Nível de detalhe por vista. Valores mais altos produzem mapas de profundidade mais detalhados (padrão: 9). |
| `split_resolution` | INT | Sim | 256 a 1024 | Resolução de cada vista em perspectiva após a divisão do panorama (padrão: 512). |
| `merge_resolution` | INT | Sim | 256 a 8192 | Resolução do lado maior do mapa de profundidade equirretangular final mesclado (padrão: 1920). |
| `batch_size` | INT | Sim | 1 a 12 | Número de vistas em perspectiva a serem processadas em cada lote de inferência. O número total de vistas é 12 (padrão: 4). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `moge_geometry` | MOGE_GEOMETRY | Um dicionário contendo a geometria estimada: `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `mask` (máscara de área válida) e `image` (a imagem de entrada). |

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
