# Pós-processamento Marigold V2

Este nó converte uma predição decodificada do Marigold V2 em uma imagem visualizável. Ele recebe o tensor de predição bruto e o formata dependendo do tipo de predição: profundidade normalizada (objetos próximos aparecem claros), normais de superfície de comprimento unitário ou albedo sRGB.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A predição decodificada do Marigold V2 a ser convertida em uma imagem exibível. | IMAGE | Sim | - |
| `prediction` | O tipo de predição contido na entrada, que determina como os dados são convertidos. `"depth"` normaliza os valores de profundidade de modo que superfícies próximas sejam claras e superfícies distantes sejam escuras, e então copia o resultado para todos os três canais de cor. `"normals"` redimensiona os valores para o intervalo -1..1, normaliza-os em normais de superfície de comprimento unitário e os mapeia de volta para 0..1. `"albedo"` aplica uma conversão linear para sRGB aos valores. | COMBO | Sim | `"depth"`<br>`"normals"`<br>`"albedo"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem processada na representação selecionada: profundidade normalizada (escala de cinza repetida nos três canais), normais de superfície de comprimento unitário ou albedo sRGB. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MarigoldV2PostProcess/pt-BR.md)

---
**Source fingerprint (SHA-256):** `848b29e2dfcd34c44cf9707b9b26cb13c18e82bb16618a15afbe477a1d620e1e`
