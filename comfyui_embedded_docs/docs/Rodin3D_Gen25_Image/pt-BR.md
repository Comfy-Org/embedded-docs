> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/en.md)

## Visão Geral

Este nó gera um modelo 3D a partir de uma a cinco imagens de referência usando a API Rodin Gen-2.5. Você pode escolher entre os modos de qualidade Rápido, Regular ou Extremamente Alto para equilibrar a velocidade de geração e o custo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagens` | IMAGE | Sim | 1 a 5 imagens | Uma a cinco imagens de entrada. A primeira imagem é usada para materiais quando múltiplas imagens são fornecidas. |
| `modo` | COMBO | Sim | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | O modo de qualidade de geração. Modos de qualidade mais alta produzem melhores resultados, mas custam mais. |
| `material` | COMBO | Sim | `"PBR"`<br>`"Matte"` | O tipo de material para o modelo 3D gerado. |
| `formato_arquivo_geometria` | COMBO | Sim | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | O formato de arquivo de saída para a geometria do modelo 3D. |
| `modo_textura` | COMBO | Sim | `"Original"`<br>`"Clean"`<br>`"Style"` | O modo de geração de textura. "Original" preserva as texturas de entrada, "Clean" as remove e "Style" aplica uma textura estilizada. |
| `semente` | INT | Sim | 0 a 2147483647 | Uma semente aleatória para resultados reproduzíveis. Use a mesma semente para obter a mesma saída. |
| `TAPose` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve aplicar a pose T ao modelo gerado. |
| `textura_hd` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve gerar um mapa de textura em alta definição. |
| `remover_iluminação_textura` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve remover a iluminação das imagens de entrada antes da geração da textura. |
| `preservar_alpha_original` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve usar o canal alfa original das imagens de entrada. |
| `addon_highpack` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve gerar uma versão de alta poligonagem do modelo, além da versão padrão. |
| `largura_bbox` | INT | Sim | 1 a 1000 | A largura da caixa delimitadora para o modelo gerado em centímetros. |
| `altura_bbox` | INT | Sim | 1 a 1000 | A altura da caixa delimitadora para o modelo gerado em centímetros. |
| `comprimento_bbox` | INT | Sim | 1 a 1000 | O comprimento da caixa delimitadora para o modelo gerado em centímetros. |
| `altura_cm` | INT | Sim | 1 a 300 | A altura do modelo gerado em centímetros. |

**Nota sobre a Quantidade de Imagens:** O nó aceita entre 1 e 5 imagens. Se você fornecer um lote de imagens (por exemplo, um lote de 4 imagens), cada imagem no lote é tratada como uma imagem de entrada separada. Fornecer mais de 5 imagens resultará em um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | FILE3D | O arquivo de modelo 3D gerado no formato de geometria selecionado. |

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
