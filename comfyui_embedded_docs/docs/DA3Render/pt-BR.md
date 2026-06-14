# Render Depth Anything 3

Este nó renderiza uma visualização a partir dos dados geométricos do Depth Anything 3. Ele pode gerar mapas de profundidade, mapas de confiança ou máscaras de céu, dependendo do modo de saída selecionado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | O pacote de dados geométricos do Depth Anything 3 contendo profundidade e, opcionalmente, tensores de céu e confiança | DA3_GEOMETRY | Sim | - |
| `output` | O tipo de visualização a ser renderizada. As opções incluem depth, depth_colored, sky_mask e confidence. Cada opção possui seu próprio conjunto de subparâmetros. | COMBO | Sim | `"depth"`<br>`"depth_colored"`<br>`"sky_mask"`<br>`"confidence"` |

### Subparâmetros para opções de `output`

Quando `output` está definido como `"depth"` ou `"depth_colored"`:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `normalization` | O método de normalização de profundidade. v2_style usa normalização média/desvio padrão para resultados perceptualmente equilibrados (padrão). min_max estende toda a faixa de profundidade para [0, 1] para máximo contraste. raw preserva unidades métricas para o modelo Metric sem escalonamento. | COMBO | Sim | `"v2_style"`<br>`"min_max"`<br>`"raw"` |
| `apply_sky_clip` | Recorta a profundidade da região do céu para o percentil 99 da profundidade do primeiro plano antes da normalização. Requer uma chave de céu na entrada da3_geometry (apenas para modelos Mono/Metric). Padrão: False | BOOLEAN | Sim | True<br>False |

Quando `output` está definido como `"sky_mask"`:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `colored` | Aplica o mapa de cores Turbo à máscara de céu. Padrão: False | BOOLEAN | Sim | True<br>False |

Quando `output` está definido como `"confidence"`:

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `colored` | Aplica o mapa de cores Turbo ao mapa de confiança. Padrão: False | BOOLEAN | Sim | True<br>False |

### Restrições de Parâmetros

- Quando `apply_sky_clip` está definido como True, a entrada `da3_geometry` deve conter um tensor de céu. Isso está disponível apenas ao usar modelos Mono ou Metric. Se o tensor de céu estiver ausente, o nó gerará um erro.
- A opção de saída `sky_mask` requer um tensor de céu na entrada `da3_geometry`. Isso está disponível apenas com modelos Mono ou Metric.
- A opção de saída `confidence` requer um tensor de confiança na entrada `da3_geometry`. Isso está disponível apenas com modelos Small ou Base.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `IMAGE` | A visualização renderizada como um tensor de imagem. Para saídas de profundidade, retorna um mapa de profundidade em escala de cinza ou colorido. Para sky_mask e confidence, retorna uma visualização em escala de cinza ou colorida, dependendo do parâmetro colored. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`
