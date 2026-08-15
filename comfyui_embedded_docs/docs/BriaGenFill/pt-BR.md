# BriaGenFill

Este nó gera objetos ou cenas dentro de uma região mascarada de uma imagem usando a API Bria. Ele envia a imagem e a máscara, envia o prompt para o serviço de preenchimento generativo da Bria, aguarda a conclusão da operação e retorna a imagem editada. Esta é uma operação paga da API (US$ 0,0429 por solicitação).

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada para edição. | IMAGE | Sim | - |
| `mask` | Áreas brancas são preenchidas com conteúdo gerado; áreas pretas são preservadas. A máscara é binarizada antes do envio, portanto áreas parcialmente pintadas contam como brancas. Deve ter a mesma proporção da imagem. | MASK | Sim | - |
| `prompt` | Descrição do que gerar dentro da região mascarada. Deve conter pelo menos 1 caractere. | STRING | Sim | - |
| `negative_prompt` | Um prompt que descreve conteúdo a evitar no resultado gerado. Se deixado vazio, não é enviado à API. | STRING | Sim | - |
| `refine_prompt` | Ajusta automaticamente o prompt para melhores resultados; desative para usar o prompt exatamente como escrito. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para o processo de geração. (padrão: 42) | INT | Sim | 1 a 2147483647 |
| `moderation` | Configurações de moderação para a solicitação. Quando definido como "true", as opções de moderação aninhadas descritas abaixo são aplicadas. (padrão: "false") | COMBO | Sim | "false"<br>"true" |

Nota: o `prompt` não deve estar vazio, e a `mask` deve ter a mesma proporção da `image`. A máscara é binarizada com 50% de opacidade, portanto áreas pintadas com menos da metade da opacidade são ignoradas; se a máscara não contiver áreas brancas após a binarização, o nó gera um erro.

Quando `moderation` está definido como "true", as seguintes opções booleanas aninhadas estão disponíveis:
- `prompt_content_moderation` (padrão: false): Aplica moderação de conteúdo ao prompt.
- `visual_input_moderation` (padrão: false): Aplica moderação de conteúdo à imagem de entrada.
- `visual_output_moderation` (padrão: false): Aplica moderação de conteúdo à imagem de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem resultante com a região mascarada preenchida pelo conteúdo gerado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
