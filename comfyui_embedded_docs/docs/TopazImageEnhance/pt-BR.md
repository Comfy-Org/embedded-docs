# Topaz Image Enhance

O nó Topaz Image Enhance fornece ampliação (upscaling) e aprimoramento de imagem de nível profissional. Ele processa uma única imagem de entrada usando um modelo de IA baseado em nuvem para melhorar qualidade, detalhes e resolução. O nó oferece controle refinado sobre o processo de aprimoramento, incluindo opções para orientação criativa, foco no assunto e preservação facial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de IA a ser usado para aprimoramento de imagem. | COMBO | Sim | `"Reimagine"` |
| `imagem` | A imagem de entrada a ser aprimorada. Apenas uma imagem é suportada. | IMAGE | Sim | - |
| `prompt` | Texto opcional para orientação de ampliação criativa (padrão: vazio). | STRING | Não | - |
| `detecção_de_sujeito` | Controla em qual parte da imagem o aprimoramento se concentra (padrão: "All"). | COMBO | Não | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `aprimoramento_de_rostos` | Aprimora rostos (se presentes) durante o processamento (padrão: True). | BOOLEAN | Não | - |
| `criatividade_no_aprimoramento_de_rostos` | Define o nível de criatividade para o aprimoramento facial (padrão: 0.0). | FLOAT | Não | 0.0 - 1.0 |
| `força_do_aprimoramento_de_rostos` | Controla o quão nítidos os rostos aprimorados são em relação ao fundo (padrão: 1.0). | FLOAT | Não | 0.0 - 1.0 |
| `cortar_para_preencher` | Por padrão, a imagem recebe letterbox quando a proporção de aspecto de saída difere. Ative para cortar a imagem e preencher as dimensões de saída (padrão: False). | BOOLEAN | Não | - |
| `largura_de_saida` | Valor zero significa cálculo automático (normalmente será o tamanho original ou a `output_height` se especificada) (padrão: 0). | INT | Não | 0 - 32000 |
| `altura_de_saida` | Valor zero significa gerar com a mesma altura da original ou a `output_width` (padrão: 0). | INT | Não | 0 - 32000 |
| `criatividade` | Controla o nível geral de criatividade do aprimoramento (padrão: 3). | INT | Não | 1 - 9 |
| `preservação_de_rostos` | Preserva a identidade facial dos assuntos (padrão: True). | BOOLEAN | Não | - |
| `preservação_de_cores` | Preserva as cores originais (padrão: True). | BOOLEAN | Não | - |

**Nota:** Este nó só pode processar uma única imagem de entrada. Fornecer um lote com várias imagens resultará em erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída aprimorada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
