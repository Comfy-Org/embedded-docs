> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/pt-BR.md)

O nó TripleCLIPLoader carrega três modelos diferentes de codificador de texto simultaneamente e os combina em um único modelo CLIP. Isso é útil para cenários avançados de codificação de texto onde múltiplos codificadores são necessários, como em fluxos de trabalho SD3 que exigem os modelos clip-l, clip-g e t5 trabalhando juntos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip_name1` | STRING | Sim | Múltiplas opções disponíveis | O primeiro modelo de codificador de texto a ser carregado a partir dos codificadores de texto disponíveis |
| `clip_name2` | STRING | Sim | Múltiplas opções disponíveis | O segundo modelo de codificador de texto a ser carregado a partir dos codificadores de texto disponíveis |
| `clip_name3` | STRING | Sim | Múltiplas opções disponíveis | O terceiro modelo de codificador de texto a ser carregado a partir dos codificadores de texto disponíveis |

**Observação:** Todos os três parâmetros de codificador de texto devem ser selecionados a partir dos modelos de codificador de texto disponíveis em seu sistema. O nó carregará todos os três modelos e os combinará em um único modelo CLIP para processamento.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `CLIP` | CLIP | Um modelo CLIP combinado contendo todos os três codificadores de texto carregados |
