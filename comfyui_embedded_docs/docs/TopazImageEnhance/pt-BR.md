# Topaz Image Enhance

O nó Topaz Image Enhance fornece ampliação e aprimoramento de imagem padrão do setor. Ele processa uma única imagem de entrada usando um modelo de IA baseado em nuvem para melhorar a qualidade, o detalhe e a resolução. O nó oferece controle refinado sobre o processo de aprimoramento, incluindo opções para orientação criativa, foco no sujeito e preservação facial.

Este nó é uma versão legada e está marcado como obsoleto na interface.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA a ser usado para aprimoramento de imagem. | COMBO | Sim | `"Reimagine"` |
| `image` | A imagem de entrada a ser aprimorada. Apenas uma imagem é suportada. | IMAGE | Sim | - |
| `prompt` | Prompt de texto opcional para orientação de ampliação criativa (padrão: vazio). | STRING | Não | - |
| `subject_detection` | Controla em qual parte da imagem o aprimoramento se concentra (padrão: "All"). | COMBO | Não | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Aprimora rostos (se houver) durante o processamento (padrão: True). | BOOLEAN | Não | - |
| `face_enhancement_creativity` | Define o nível de criatividade para o aprimoramento de rostos (padrão: 0.0). | FLOAT | Não | 0.0 - 1.0 |
| `face_enhancement_strength` | Controla quão nítidos os rostos aprimorados ficam em relação ao fundo (padrão: 1.0). | FLOAT | Não | 0.0 - 1.0 |
| `crop_to_fill` | Por padrão, a imagem é exibida com tarjas (letterbox) quando a proporção da saída difere. Ative para recortar a imagem a fim de preencher as dimensões de saída (padrão: False). | BOOLEAN | Não | - |
| `output_width` | O valor zero significa calcular automaticamente (normalmente será o tamanho original ou output_height, se especificado) (padrão: 0). | INT | Não | 0 - 32000 |
| `output_height` | O valor zero significa gerar na mesma altura que o original ou a largura de saída (padrão: 0). | INT | Não | 0 - 32000 |
| `creativity` | Controla o nível geral de criatividade do aprimoramento (padrão: 3). | INT | Não | 1 - 9 |
| `face_preservation` | Preserva a identidade facial dos sujeitos (padrão: True). | BOOLEAN | Não | - |
| `color_preservation` | Preserva as cores originais (padrão: True). | BOOLEAN | Não | - |

**Observação:** Este nó só pode processar uma única imagem de entrada. Fornecer um lote com várias imagens resultará em erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída aprimorada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
