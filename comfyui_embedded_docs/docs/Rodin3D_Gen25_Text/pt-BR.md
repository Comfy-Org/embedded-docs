Esta documentação foi gerada por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/en.md)

## Visão Geral

Gere um modelo 3D a partir de um prompt de texto usando a API Rodin Gen-2.5. Você pode escolher entre diferentes modos de qualidade (Rápido, Regular ou Ultra-Alto) para equilibrar a velocidade de geração e a qualidade da saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto descrevendo o modelo 3D que você deseja gerar. | STRING | Sim | Máx. 2500 caracteres |
| `modo` | O modo de qualidade e velocidade de geração. "Fast" é o mais rápido, "Extreme-High" produz a maior qualidade, mas leva mais tempo. | COMBO | Sim | `"Fast"`<br>`"Regular"`<br>`"Extreme-High"` |
| `material` | O estilo de material para o modelo 3D gerado. | COMBO | Sim | `"PBR"`<br>`"Matte"`<br>`"Shiny"` |
| `formato_arquivo_geometria` | O formato de arquivo para o modelo 3D de saída. | COMBO | Sim | `"glb"`<br>`"obj"`<br>`"stl"`<br>`"usdz"` |
| `modo_textura` | Modo de geração de textura. "None" não produz texturas, "Generated" cria texturas padrão, "Generated+HD" cria texturas em alta definição. | COMBO | Sim | `"None"`<br>`"Generated"`<br>`"Generated+HD"` |
| `semente` | Semente aleatória para resultados reproduzíveis. Usar a mesma semente com as mesmas entradas produzirá a mesma saída. | INT | Sim | 0 a 2147483647 |
| `TAPose` | Se deve aplicar a pose T (braços estendidos) ao modelo gerado. | BOOLEAN | Sim | Verdadeiro / Falso |
| `textura_hd` | Se deve gerar texturas em alta definição para o modelo. | BOOLEAN | Sim | Verdadeiro / Falso |
| `remover_iluminação_textura` | Se deve aplicar realce de textura (qualidade de textura aprimorada) ao modelo. | BOOLEAN | Sim | Verdadeiro / Falso |
| `addon_highpack` | Se deve gerar uma versão de alta poligonagem do modelo além da versão padrão. | BOOLEAN | Sim | Verdadeiro / Falso |
| `largura_bbox` | A largura da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `altura_bbox` | A altura da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `comprimento_bbox` | O comprimento da caixa delimitadora em unidades de mundo. | INT | Sim | 1 a 1000 |
| `altura_cm` | A altura do modelo gerado em centímetros. | INT | Sim | 1 a 300 |

**Nota:** O parâmetro `prompt` deve ter entre 1 e 2500 caracteres. O parâmetro `seed` tem como padrão 0 (aleatório) se não for especificado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model_file` | O arquivo do modelo 3D gerado no formato especificado. | FILE3DANY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/pt-BR.md)

---
**Source fingerprint (SHA-256):** `79fbaf466e9af88cdfdac0f9136a2df17ba4bc2e5bb65a35b9ad2b1181da94db`
