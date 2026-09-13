# BriaEraseByText

Este nó usa a Bria para remover de uma imagem um objeto descrito em texto simples. A Bria renderiza novamente o quadro inteiro com cerca de 1 megapixel, então o resultado não fica alinhado pixel a pixel com a entrada.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem da qual o objeto nomeado deve ser removido. | IMAGE | Sim | - |
| `object_name` | Nome do objeto a ser removido, como 'a lâmpada'. Vários objetos podem ser nomeados de uma vez, como 'o telefone e os lápis'. Nomear algo que não está na imagem ainda retorna uma imagem renderizada novamente, e a requisição ainda é cobrada. Deve ter pelo menos 1 caractere (padrão: vazio). | STRING | Sim | - |
| `moderation` | Configurações de moderação. Seleciona se os controles opcionais de moderação são exibidos. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação

Esses parâmetros aparecem quando `moderation` é definido como `"true"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Habilita a moderação de conteúdo na imagem de entrada (padrão: false). | BOOLEAN | Não | true<br>false |
| `visual_output_moderation` | Habilita a moderação de conteúdo na imagem de saída gerada (padrão: false). | BOOLEAN | Não | true<br>false |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-----------|-----------|
| `IMAGE` | A imagem renderizada novamente com o objeto nomeado removido. | IMAGE |
| `structured_prompt` | Descrição estruturada da imagem editada, para uma edição posterior com Bria FIBO Image Edit. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`
