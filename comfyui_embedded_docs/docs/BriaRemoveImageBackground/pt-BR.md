Este nó remove o fundo de uma imagem usando o serviço Bria RMBG 2.0. Ele envia a imagem para uma API externa para processamento e retorna o resultado com o fundo removido.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada da qual o fundo será removido. | IMAGE | Sim | - |
| `moderação` | Configurações de moderação. Quando definido como `"true"`, opções adicionais de moderação ficam disponíveis. | COMBO | Não | `"false"`<br>`"true"` |
| `visual_input_moderation` | Ativa a moderação de conteúdo visual na imagem de entrada. Este parâmetro está disponível apenas quando `moderação` está definido como `"true"`. Padrão: `False`. | BOOLEAN | Não | - |
| `visual_output_moderation` | Ativa a moderação de conteúdo visual na imagem de saída. Este parâmetro está disponível apenas quando `moderação` está definido como `"true"`. Padrão: `True`. | BOOLEAN | Não | - |
| `semente` | Um valor de semente que controla se o nó deve ser executado novamente. Os resultados são não determinísticos independentemente do valor da semente. Padrão: `0`. | INT | Não | 0 a 2147483647 |

**Observação:** Os parâmetros `visual_input_moderation` e `visual_output_moderation` dependem do parâmetro `moderation`. Eles só ficam ativos e são necessários se `moderation` estiver definido como `"true"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem processada com o fundo removido. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2b2dd3ca0d026af1a2bf3f7222165928527b05b65817073b50230ff18d39bc6c`
