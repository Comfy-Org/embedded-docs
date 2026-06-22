# Inferência Panorama MoGe

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/en.md)

## Visão Geral

Este nó realiza estimativa de profundidade em imagens panorâmicas equirretangulares. Ele funciona dividindo o panorama em 12 vistas em perspectiva, executando o modelo de estimativa de profundidade MoGe em cada vista e, em seguida, mesclando os resultados em um único mapa de profundidade completo para o panorama original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim |  |
| `image` | Imagem panorâmica equirretangular (qualquer proporção de aspecto). | IMAGE | Sim |  |
| `resolution_level` | Nível de detalhe por vista. Valores mais altos produzem mapas de profundidade mais detalhados (padrão: 9). | INT | Sim | 0 a 9 |
| `split_resolution` | Resolução de cada vista em perspectiva após a divisão do panorama (padrão: 512). | INT | Sim | 256 a 1024 |
| `merge_resolution` | Resolução do lado maior do mapa de profundidade equirretangular final mesclado (padrão: 1920). | INT | Sim | 256 a 8192 |
| `batch_size` | Número de vistas em perspectiva a serem processadas em cada lote de inferência. O número total de vistas é 12 (padrão: 4). | INT | Sim | 1 a 12 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `moge_geometry` | Um dicionário contendo a geometria estimada: `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `mask` (máscara de área válida) e `image` (a imagem de entrada). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3a701e3679bc35cd5fddc54868ac9c4bc9b4e23a5b97bbf61e46b7309e43600b`
