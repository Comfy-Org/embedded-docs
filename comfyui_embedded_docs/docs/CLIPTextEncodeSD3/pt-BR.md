> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/pt-BR.md)

O nó CLIPTextEncodeSD3 processa entradas de texto para modelos Stable Diffusion 3, codificando múltiplos prompts de texto usando diferentes modelos CLIP. Ele lida com três entradas de texto separadas (`clip_g`, `clip_l` e `t5xxl`) e fornece opções para gerenciar o preenchimento de texto vazio. O nó garante o alinhamento adequado dos *tokens* entre as diferentes entradas de texto e retorna dados de condicionamento adequados para os *pipelines* de geração do SD3.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Obrigatório | - | - | O modelo CLIP usado para a codificação de texto |
| `clip_l` | STRING | Multilinha, Prompts Dinâmicos | - | - | Entrada de texto para o modelo CLIP local |
| `clip_g` | STRING | Multilinha, Prompts Dinâmicos | - | - | Entrada de texto para o modelo CLIP global |
| `t5xxl` | STRING | Multilinha, Prompts Dinâmicos | - | - | Entrada de texto para o modelo T5-XXL |
| `empty_padding` | COMBO | Seleção | - | ["none", "empty_prompt"] | Controla como as entradas de texto vazias são tratadas |

**Restrições dos Parâmetros:**

- Quando `empty_padding` está definido como "none", entradas de texto vazias para `clip_g`, `clip_l` ou `t5xxl` resultarão em listas de *tokens* vazias em vez de preenchimento.
- O nó equilibra automaticamente os comprimentos dos *tokens* entre as entradas `clip_l` e `clip_g` preenchendo a mais curta com *tokens* vazios quando os comprimentos diferem.
- Todas as entradas de texto suportam prompts dinâmicos e entrada de texto multilinha.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento de texto codificados, prontos para uso nos *pipelines* de geração do SD3 |
