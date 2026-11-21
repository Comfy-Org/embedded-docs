# Rodin 3D Gen-2.5 - Texto para 3D

## Visão Geral

Gere um modelo 3D a partir de um prompt de texto usando a API Rodin Gen-2.5. Você pode escolher entre diferentes modos de qualidade (Fast, Regular ou Extreme-High) para equilibrar a velocidade de geração e a qualidade da saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para o modelo 3D. | STRING | Sim | 1 a 1024 caracteres |
| `mode` | O modo de qualidade e velocidade de geração. "Fast" é o mais rápido; "Extreme-High" produz a maior qualidade, mas leva mais tempo. | COMBO | Sim | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | O estilo de material para o modelo 3D gerado. | COMBO | Sim | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `geometry_file_format` | O formato de arquivo do modelo 3D de saída. | COMBO | Sim | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `texture_mode` | Modo de geração de textura. "None" não produz texturas, "Generated" cria texturas padrão, "Generated+HD" cria texturas de alta definição. | COMBO | Sim | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `seed` | Semente aleatória para resultados reproduzíveis. Usar a mesma seed com as mesmas entradas produzirá a mesma saída. | INT | Sim | 0 a 2147483647 |
| `TAPose` | Se deve aplicar T-pose (braços estendidos) ao modelo gerado. | BOOLEAN | Sim | True / False |
| `hd_texture` | Se deve gerar texturas de alta definição para o modelo. | BOOLEAN | Sim | True / False |
| `texture_delight` | Se deve aplicar texture delight (qualidade de textura aprimorada) ao modelo. | BOOLEAN | Sim | True / False |
| `addon_highpack` | Se deve gerar uma versão de alto polígono do modelo além da versão padrão. | BOOLEAN | Sim | True / False |
| `bbox_width` | A largura da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `bbox_height` | A altura da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `bbox_length` | O comprimento da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `height_cm` | A altura do modelo gerado em centímetros. | INT | Sim | 1 a 300 |

**Observação:** O parâmetro `prompt` deve ter entre 1 e 1024 caracteres. O parâmetro `seed` assume o valor padrão 0 (aleatório) se não for especificado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model_file` | O arquivo do modelo 3D gerado no formato especificado. | FILE3DANY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/pt-BR.md)

---
**Source fingerprint (SHA-256):** `95d5faa36298f09f0ae4dcda95dfd8913ebb393bb5934ae2c4622acfe79c85d6`
