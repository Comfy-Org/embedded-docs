> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/pt-BR.md)

Este nó remove o fundo de uma imagem usando o serviço Bria RMBG 2.0. Ele envia a imagem para uma API externa para processamento e retorna o resultado com o fundo removido.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada da qual o fundo será removido. |
| `moderação` | COMBO | Não | `"false"`<br>`"true"` | Configurações de moderação. Quando definido como `"true"`, opções adicionais de moderação ficam disponíveis. |
| `visual_input_moderation` | BOOLEAN | Não | - | Ativa a moderação de conteúdo visual na imagem de entrada. Este parâmetro está disponível apenas quando `moderação` está definido como `"true"`. Padrão: `False`. |
| `visual_output_moderation` | BOOLEAN | Não | - | Ativa a moderação de conteúdo visual na imagem de saída. Este parâmetro está disponível apenas quando `moderação` está definido como `"true"`. Padrão: `True`. |
| `semente` | INT | Não | 0 a 2147483647 | Um valor de semente que controla se o nó deve ser executado novamente. Os resultados são não determinísticos independentemente do valor da semente. Padrão: `0`. |

**Observação:** Os parâmetros `visual_input_moderation` e `visual_output_moderation` dependem do parâmetro `moderation`. Eles só ficam ativos e são necessários se `moderation` estiver definido como `"true"`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem processada com o fundo removido. |

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
