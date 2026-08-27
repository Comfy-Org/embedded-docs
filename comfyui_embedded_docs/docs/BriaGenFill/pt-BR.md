# BriaGenFill

Este nó gera objetos ou cenas dentro de uma região mascarada de uma imagem usando a API Bria. Ele envia a imagem e a máscara, envia o prompt para o serviço de preenchimento generativo da Bria, aguarda a conclusão da operação e retorna a imagem editada. Esta é uma operação paga da API (US$ 0,0429 por solicitação).
## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `image` | A imagem de entrada para edição. | IMAGE | Sim | - |
| `mask` | Áreas brancas são preenchidas com conteúdo gerado; áreas pretas são preservadas. A máscara é binarizada antes do envio, portanto áreas parcialmente pintadas contam como brancas. Deve ter a mesma proporção da imagem. | MASK | Sim | - |
| `prompt` | Descrição do que gerar dentro da região mascarada. Deve conter pelo menos 1 caractere. | STRING | Sim | - |
| `negative_prompt` | Um prompt que descreve conteúdo a evitar no resultado gerado. Se deixado vazio, não é enviado à API. | STRING | Sim | - |
| `refine_prompt` | Ajusta automaticamente o prompt para melhores resultados; desative para usar o prompt exatamente como escrito. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para o processo de geração. (padrão: 42) | INT | Sim | 1 to 2147483647 |
| `moderação` | Configurações de moderação para a solicitação. Quando definido como "true", as opções de moderação aninhadas descritas abaixo são aplicadas. (padrão: "false") | DYNAMIC_COMBO | Sim | "false"<br>"true" |

### Entradas de moderação

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|---|---|---|---|---|
| `prompt_content_moderation` | Aplica moderação de conteúdo ao prompt. (padrão: false) | BOOLEAN | Não | true<br>false |
| `visual_input_moderation` | Aplica moderação de conteúdo à imagem de entrada. (padrão: false) | BOOLEAN | Não | true<br>false |
| `visual_output_moderation` | Aplica moderação de conteúdo à imagem de saída. (padrão: false) | BOOLEAN | Não | true<br>false |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---|---|---|
| `image` | The resulting image with the masked region filled by the generated content. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
