# Bria Remover Fundo da Imagem

Este nó remove o fundo de uma imagem usando o serviço Bria RMBG 2.0. Ele envia a imagem para uma API externa para processamento e retorna o resultado com o fundo removido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `imagem` | A imagem de entrada da qual o fundo será removido. | IMAGE | Sim | - |
| `moderação` | Configurações de moderação. Quando definido como `"true"`, opções adicionais de moderação ficam disponíveis. | COMBO | Não | `"false"`<br>`"true"` |
| `visual_input_moderation` | Ativa a moderação de conteúdo visual na imagem de entrada. Este parâmetro só está disponível quando `moderation` está definido como `"true"`. Padrão: `False`. | BOOLEAN | Não | - |
| `visual_output_moderation` | Ativa a moderação de conteúdo visual na imagem de saída. Este parâmetro só está disponível quando `moderation` está definido como `"true"`. Padrão: `True`. | BOOLEAN | Não | - |
| `semente` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. Padrão: `0`. | INT | Não | 0 a 2147483647 |

**Nota:** Os parâmetros `visual_input_moderation` e `visual_output_moderation` dependem do parâmetro `moderation`. Eles só ficam ativos quando `moderation` está definido como `"true"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `image` | A imagem processada com o fundo removido. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`
