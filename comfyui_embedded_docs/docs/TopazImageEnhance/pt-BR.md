> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/pt-BR.md)

O nó Topaz Image Enhance oferece upscaling e aprimoramento de imagem de padrão industrial. Ele processa uma única imagem de entrada usando um modelo de IA baseado em nuvem para melhorar a qualidade, os detalhes e a resolução. O nó oferece controle refinado sobre o processo de aprimoramento, incluindo opções para orientação criativa, foco no assunto e preservação facial.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | `"Reimagine"` | O modelo de IA a ser usado para o aprimoramento da imagem. |
| `image` | IMAGE | Sim | - | A imagem de entrada a ser aprimorada. Apenas uma imagem é suportada. |
| `prompt` | STRING | Não | - | Um prompt de texto opcional para orientação criativa no upscaling (padrão: vazio). |
| `subject_detection` | COMBO | Não | `"All"`<br>`"Foreground"`<br>`"Background"` | Controla em qual parte da imagem o aprimoramento se concentra (padrão: "All"). |
| `face_enhancement` | BOOLEAN | Não | - | Ative para aprimorar rostos, se presentes na imagem (padrão: True). |
| `face_enhancement_creativity` | FLOAT | Não | 0.0 - 1.0 | Define o nível de criatividade para o aprimoramento facial (padrão: 0.0). |
| `face_enhancement_strength` | FLOAT | Não | 0.0 - 1.0 | Controla o quão nítidos os rostos aprimorados ficam em relação ao fundo (padrão: 1.0). |
| `crop_to_fill` | BOOLEAN | Não | - | Por padrão, a imagem recebe "letterbox" quando a proporção de saída difere. Ative para recortar a imagem para preencher as dimensões de saída (padrão: False). |
| `output_width` | INT | Não | 0 - 32000 | A largura desejada para a imagem de saída. Um valor de 0 significa que será calculada automaticamente, geralmente com base no tamanho original ou na `output_height` se especificada (padrão: 0). |
| `output_height` | INT | Não | 0 - 32000 | A altura desejada para a imagem de saída. Um valor de 0 significa que será calculada automaticamente, geralmente com base no tamanho original ou na `output_width` se especificada (padrão: 0). |
| `creativity` | INT | Não | 1 - 9 | Controla o nível geral de criatividade do aprimoramento (padrão: 3). |
| `face_preservation` | BOOLEAN | Não | - | Preserva a identidade facial dos sujeitos na imagem (padrão: True). |
| `color_preservation` | BOOLEAN | Não | - | Preserva as cores originais da imagem de entrada (padrão: True). |

**Observação:** Este nó só pode processar uma única imagem de entrada. Fornecer um lote com várias imagens resultará em um erro.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída aprimorada. |
