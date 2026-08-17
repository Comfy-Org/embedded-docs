# Inferência Panorama MoGe

Este nó realiza estimativa de profundidade em imagens panorâmicas equiretangulares. Ele funciona dividindo o panorama em 12 vistas em perspectiva, executando o modelo de estimativa de profundidade MoGe em cada vista e, em seguida, mesclando os resultados em um único mapa de profundidade completo para o panorama original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `moge_model` | O modelo MoGe a ser usado para inferência. | MOGE_MODEL | Sim |  |
| `image` | Panorama equiretangular (qualquer proporção). Aceita apenas uma única imagem. | IMAGE | Sim |  |
| `resolution_level` | Detalhe por vista (0 = mais rápido, 9 = mais detalhado). Padrão: 9. | INT | Sim | 0 a 9 |
| `split_resolution` | Resolução de cada divisão em perspectiva. Padrão: 512. | INT | Sim | 256 a 1024 |
| `merge_resolution` | Resolução do lado maior do mapa de distância equiretangular mesclado. Padrão: 1920. | INT | Sim | 256 a 8192 |
| `batch_size` | Vistas por lote de inferência (12 divisões no total). Padrão: 4. | INT | Sim | 1 a 12 |

Nota: Este nó aceita apenas uma única imagem. Passar um lote de imagens gera um erro. O panorama é sempre dividido em 12 vistas em perspectiva; `batch_size` apenas controla quantas dessas vistas são processadas por lote de inferência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `moge_geometry` | Um dicionário contendo a geometria estimada: `points` (nuvem de pontos 3D), `depth` (mapa de profundidade), `mask` (máscara de área válida) e `image` (a imagem de entrada). | MOGE_GEOMETRY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d35b6d42a5bb17c184bc56fe3867d3a183017084dc81649c0663a9fba2362770`
