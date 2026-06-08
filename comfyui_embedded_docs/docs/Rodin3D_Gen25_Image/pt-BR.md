Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/en.md)

## Visão Geral

Este nó gera um modelo 3D a partir de uma a cinco imagens de referência usando a API Rodin Gen-2.5. Você pode escolher entre os modos de qualidade Rápido, Regular ou Extremamente Alto para equilibrar a velocidade de geração e o custo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagens` | Uma a cinco imagens de entrada. A primeira imagem é usada para materiais quando múltiplas imagens são fornecidas. | IMAGE | Sim | 1 a 5 imagens |
| `modo` | O modo de qualidade de geração. Modos de qualidade mais alta produzem melhores resultados, mas custam mais. | COMBO | Sim | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | O tipo de material para o modelo 3D gerado. | COMBO | Sim | `"PBR"`<br>`"Matte"` |
| `formato_arquivo_geometria` | O formato de arquivo de saída para a geometria do modelo 3D. | COMBO | Sim | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `modo_textura` | O modo de geração de textura. "Original" preserva as texturas de entrada, "Clean" as remove e "Style" aplica uma textura estilizada. | COMBO | Sim | `"Original"`<br>`"Clean"`<br>`"Style"` |
| `semente` | Uma semente aleatória para resultados reproduzíveis. Use a mesma semente para obter a mesma saída. | INT | Sim | 0 a 2147483647 |
| `TAPose` | Se deve aplicar a pose T ao modelo gerado. | BOOLEAN | Sim | Verdadeiro / Falso |
| `textura_hd` | Se deve gerar um mapa de textura em alta definição. | BOOLEAN | Sim | Verdadeiro / Falso |
| `remover_iluminação_textura` | Se deve remover a iluminação das imagens de entrada antes da geração da textura. | BOOLEAN | Sim | Verdadeiro / Falso |
| `preservar_alpha_original` | Se deve usar o canal alfa original das imagens de entrada. | BOOLEAN | Sim | Verdadeiro / Falso |
| `addon_highpack` | Se deve gerar uma versão de alta poligonagem do modelo, além da versão padrão. | BOOLEAN | Sim | Verdadeiro / Falso |
| `largura_bbox` | A largura da caixa delimitadora para o modelo gerado em centímetros. | INT | Sim | 1 a 1000 |
| `altura_bbox` | A altura da caixa delimitadora para o modelo gerado em centímetros. | INT | Sim | 1 a 1000 |
| `comprimento_bbox` | O comprimento da caixa delimitadora para o modelo gerado em centímetros. | INT | Sim | 1 a 1000 |
| `altura_cm` | A altura do modelo gerado em centímetros. | INT | Sim | 1 a 300 |

**Nota sobre a Quantidade de Imagens:** O nó aceita entre 1 e 5 imagens. Se você fornecer um lote de imagens (por exemplo, um lote de 4 imagens), cada imagem no lote é tratada como uma imagem de entrada separada. Fornecer mais de 5 imagens resultará em um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O arquivo de modelo 3D gerado no formato de geometria selecionado. | FILE3D |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Image/pt-BR.md)

---
**Source fingerprint (SHA-256):** `65f755a2c3bd2317eb61c4681a406b51b06f960e36864d3602c3d03a44aa4878`
