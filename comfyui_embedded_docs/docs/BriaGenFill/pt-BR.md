# Bria Generative Fill

Este nó gera objetos ou cenários dentro de uma região mascarada de uma imagem usando a Bria. Ele faz upload da imagem e da máscara, envia o prompt ao serviço de preenchimento generativo da Bria, aguarda a conclusão da operação e retorna a imagem editada. Esta é uma operação de API paga (US$ 0,0429 por solicitação).

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser editada. | IMAGE | Sim | - |
| `mask` | Áreas brancas são preenchidas com conteúdo gerado; áreas pretas são preservadas. A máscara é binarizada antes do envio, então áreas parcialmente pintadas contam como brancas. Deve ter a mesma proporção de aspecto que a imagem. | MASK | Sim | - |
| `prompt` | Descrição do que deve ser gerado dentro da região mascarada. Deve conter pelo menos 1 caractere. (padrão: "") | STRING | Sim | - |
| `negative_prompt` | Um prompt que descreve conteúdo a ser evitado no resultado gerado. Se deixado vazio, não é enviado à API. (padrão: "") | STRING | Sim | - |
| `refine_prompt` | Ajusta automaticamente o prompt para obter melhores resultados; desative para usar o prompt exatamente como escrito. (padrão: true) | BOOLEAN | Sim | true<br>false |
| `seed` | Semente para o processo de geração. (padrão: 42) | INT | Sim | 1 a 2147483647 |
| `moderação` | Configurações de moderação. Quando definido como "true", as opções de moderação abaixo são aplicadas. (padrão: "false") | DYNAMIC_COMBO | Sim | "false"<br>"true" |

### Entradas de moderação (quando `moderation` = "true")

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | Aplica moderação de conteúdo ao prompt. (padrão: false) | BOOLEAN | Não | true<br>false |
| `visual_input_moderation` | Aplica moderação de conteúdo à imagem de entrada. (padrão: false) | BOOLEAN | Não | true<br>false |
| `visual_output_moderation` | Aplica moderação de conteúdo à imagem de saída. (padrão: false) | BOOLEAN | Não | true<br>false |

**Nota:** O `prompt` não pode estar vazio. A `mask` deve ter a mesma proporção de aspecto que a `image`. A máscara é binarizada com 50% de opacidade, então áreas pintadas com menos de metade da opacidade são ignoradas; se a máscara não contiver áreas brancas após a binarização, o nó lança um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `image` | A imagem resultante com a região mascarada preenchida pelo conteúdo gerado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`
