> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/pt-BR.md)

Este nó remove o fundo de uma imagem usando o serviço Bria RMBG 2.0. Ele envia a imagem para uma API externa para processamento e retorna o resultado com o fundo removido.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada da qual o fundo será removido. |
| `moderation` | COMBO | Não | `"false"`<br>`"true"` | Configurações de moderação. Quando definido como `"true"`, opções adicionais de moderação ficam disponíveis. |
| `visual_input_moderation` | BOOLEAN | Não | - | Habilita a moderação de conteúdo visual na imagem de entrada. Este parâmetro só está disponível quando `moderation` está definido como `"true"`. Padrão: `False`. |
| `visual_output_moderation` | BOOLEAN | Não | - | Habilita a moderação de conteúdo visual na imagem de saída. Este parâmetro só está disponível quando `moderation` está definido como `"true"`. Padrão: `True`. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente que controla se o nó deve ser executado novamente. Os resultados são não determinísticos, independentemente do valor da semente. Padrão: `0`. |

**Observação:** Os parâmetros `visual_input_moderation` e `visual_output_moderation` dependem do parâmetro `moderation`. Eles só estão ativos e são obrigatórios se `moderation` estiver definido como `"true"`.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem processada com seu fundo removido. |