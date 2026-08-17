# Topaz Image Enhance

O nó Topaz Image Enhance fornece upscaling e aprimoramento de imagem de padrão industrial. Ele processa uma única imagem de entrada usando um modelo de IA baseado em nuvem para melhorar qualidade, detalhe e resolução. O nó oferece controle refinado sobre o processo de aprimoramento, incluindo opções para orientação criativa, foco no sujeito e preservação facial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA a ser usado para o aprimoramento de imagem. | COMBO | Sim | `"Reimagine"` |
| `image` | A imagem de entrada a ser aprimorada. Apenas uma imagem é suportada. | IMAGE | Sim | - |
| `prompt` | Prompt de texto opcional para orientação criativa de upscaling (padrão: vazio). | STRING | Não | - |
| `subject_detection` | Controla em qual parte da imagem o aprimoramento se concentra (padrão: "All"). | COMBO | Não | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Aprimora rostos (se presentes) durante o processamento (padrão: True). | BOOLEAN | Não | - |
| `face_enhancement_creativity` | Define o nível de criatividade para o aprimoramento facial (padrão: 0.0). | FLOAT | Não | 0.0 - 1.0 |
| `face_enhancement_strength` | Controla a nitidez dos rostos aprimorados em relação ao fundo (padrão: 1.0). | FLOAT | Não | 0.0 - 1.0 |
| `crop_to_fill` | Por padrão, a imagem recebe letterbox quando a proporção de saída difere. Ative para cortar a imagem e preencher as dimensões de saída (padrão: False). | BOOLEAN | Não | - |
| `output_width` | Valor zero significa cálculo automático (geralmente será o tamanho original ou `output_height` se especificado) (padrão: 0). | INT | Não | 0 - 32000 |
| `output_height` | Valor zero significa gerar a mesma altura da original ou a largura de saída (padrão: 0). | INT | Não | 0 - 32000 |
| `creativity` | Controla o nível geral de criatividade do aprimoramento (padrão: 3). | INT | Não | 1 - 9 |
| `face_preservation` | Preserva a identidade facial dos sujeitos (padrão: True). | BOOLEAN | Não | - |
| `color_preservation` | Preserva as cores originais (padrão: True). | BOOLEAN | Não | - |

**Observação:** Este nó só pode processar uma única imagem de entrada. Fornecer um lote de múltiplas imagens resultará em erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída aprimorada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a4b622ced661dd1dd1c57d4536359874d2203c8d4064c76fa684b9935e265085`
