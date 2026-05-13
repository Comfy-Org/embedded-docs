> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/pt-BR.md)

O nó Topaz Image Enhance fornece ampliação de escala e aprimoramento de imagem de nível profissional. Ele processa uma única imagem de entrada usando um modelo de IA baseado em nuvem para melhorar qualidade, detalhes e resolução. O nó oferece controle refinado sobre o processo de aprimoramento, incluindo opções para orientação criativa, foco no assunto e preservação facial.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | COMBO | Sim | `"Reimagine"` | O modelo de IA a ser usado para aprimoramento de imagem. |
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser aprimorada. Apenas uma imagem é suportada. |
| `prompt` | STRING | Não | - | Um prompt de texto opcional para orientação criativa de ampliação (padrão: vazio). |
| `detecção_de_sujeito` | COMBO | Não | `"All"`<br>`"Foreground"`<br>`"Background"` | Controla em qual parte da imagem o aprimoramento se concentra (padrão: "All"). |
| `aprimoramento_de_rostos` | BOOLEAN | Não | - | Ative para aprimorar rostos, se presentes na imagem (padrão: True). |
| `criatividade_no_aprimoramento_de_rostos` | FLOAT | Não | 0.0 - 1.0 | Define o nível de criatividade para aprimoramento facial (padrão: 0.0). |
| `força_do_aprimoramento_de_rostos` | FLOAT | Não | 0.0 - 1.0 | Controla o quão nítidos os rostos aprimorados ficam em relação ao fundo (padrão: 1.0). |
| `cortar_para_preencher` | BOOLEAN | Não | - | Por padrão, a imagem recebe letterbox quando a proporção de saída difere. Ative para cortar a imagem e preencher as dimensões de saída (padrão: False). |
| `largura_de_saida` | INT | Não | 0 - 32000 | A largura desejada da imagem de saída. Um valor 0 significa que será calculado automaticamente, geralmente com base no tamanho original ou na `altura_de_saida` se especificada (padrão: 0). |
| `altura_de_saida` | INT | Não | 0 - 32000 | A altura desejada da imagem de saída. Um valor 0 significa que será calculado automaticamente, geralmente com base no tamanho original ou na `largura_de_saida` se especificada (padrão: 0). |
| `criatividade` | INT | Não | 1 - 9 | Controla o nível geral de criatividade do aprimoramento (padrão: 3). |
| `preservação_de_rostos` | BOOLEAN | Não | - | Preserva a identidade facial dos sujeitos na imagem (padrão: True). |
| `preservação_de_cores` | BOOLEAN | Não | - | Preserva as cores originais da imagem de entrada (padrão: True). |

**Nota:** Este nó só pode processar uma única imagem de entrada. Fornecer um lote de múltiplas imagens resultará em erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `imagem` | IMAGE | A imagem de saída aprimorada. |

---
**Source fingerprint (SHA-256):** `69f2c929f2cd11f13557e064e30a4514e3862e127a2bdb3a3f40ec92023f255d`
