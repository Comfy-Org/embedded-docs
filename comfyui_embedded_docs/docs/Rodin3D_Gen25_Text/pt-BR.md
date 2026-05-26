> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/en.md)

## Visão Geral

Gere um modelo 3D a partir de um prompt de texto usando a API Rodin Gen-2.5. Você pode escolher entre diferentes modos de qualidade (Rápido, Regular ou Ultra-Alto) para equilibrar a velocidade de geração e a qualidade da saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | Máx. 2500 caracteres | Prompt de texto descrevendo o modelo 3D que você deseja gerar. |
| `modo` | COMBO | Sim | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` | O modo de qualidade e velocidade de geração. "Fast" é o mais rápido, "Extreme-High" produz a maior qualidade, mas leva mais tempo. |
| `material` | COMBO | Sim | `"PBR"`<br>`"Matte"`<br>`"Shiny"` | O estilo de material para o modelo 3D gerado. |
| `formato_arquivo_geometria` | COMBO | Sim | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` | O formato de arquivo para o modelo 3D de saída. |
| `modo_textura` | COMBO | Sim | `"None"`<br>`"Generated"`<br>`"Generated+HD"` | Modo de geração de textura. "None" não produz texturas, "Generated" cria texturas padrão, "Generated+HD" cria texturas em alta definição. |
| `semente` | INT | Sim | 0 a 2147483647 | Semente aleatória para resultados reproduzíveis. Usar a mesma semente com as mesmas entradas produzirá a mesma saída. |
| `TAPose` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve aplicar a pose T (braços estendidos) ao modelo gerado. |
| `textura_hd` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve gerar texturas em alta definição para o modelo. |
| `remover_iluminação_textura` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve aplicar realce de textura (qualidade de textura aprimorada) ao modelo. |
| `addon_highpack` | BOOLEAN | Sim | Verdadeiro / Falso | Se deve gerar uma versão de alta poligonagem do modelo além da versão padrão. |
| `largura_bbox` | INT | Sim | 1 a 1000 | A largura da caixa delimitadora em unidades de mundo. |
| `altura_bbox` | INT | Sim | 1 a 1000 | A altura da caixa delimitadora em unidades de mundo. |
| `comprimento_bbox` | INT | Sim | 1 a 1000 | O comprimento da caixa delimitadora em unidades de mundo. |
| `altura_cm` | INT | Sim | 1 a 300 | A altura do modelo gerado em centímetros. |

**Nota:** O parâmetro `prompt` deve ter entre 1 e 2500 caracteres. O parâmetro `seed` tem como padrão 0 (aleatório) se não for especificado.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model_file` | FILE3DANY | O arquivo do modelo 3D gerado no formato especificado. |

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
