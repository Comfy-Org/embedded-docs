# Inferência Panorama MoGe

## Visão Geral

Este nó realiza estimativa de profundidade em imagens de panorama equirretangular. Ele divide o panorama em 12 vistas em perspectiva, executa o modelo de estimativa de profundidade MoGe em cada vista e combina os resultados de cada vista novamente em um único mapa de profundidade que cobre o panorama inteiro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim |  |
| `image` | Panorama equirretangular (qualquer proporção). O nó aceita apenas uma única imagem; passar um lote de imagens gera um erro. Apenas os 3 primeiros canais de cor (RGB) são usados. | IMAGE | Sim |  |
| `resolution_level` | Nível de detalhe por vista (0 = mais rápido, 9 = mais detalhado) (padrão: 9). | INT | Sim | 0 a 9 |
| `split_resolution` | Resolução de cada divisão em perspectiva (padrão: 512). | INT | Sim | 256 a 1024 |
| `merge_resolution` | Resolução do lado maior do mapa de distância equirretangular mesclado (padrão: 1920). | INT | Sim | 256 a 8192 |
| `batch_size` | Vistas por lote de inferência (12 divisões no total) (padrão: 4). | INT | Sim | 1 a 12 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `moge_geometry` | Um dicionário contendo a geometria estimada: `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `mask` (máscara de área válida) e `image` (a imagem de entrada). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
