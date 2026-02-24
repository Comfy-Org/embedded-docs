> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextGenerateLTX2Prompt/pt-BR.md)

O nó TextGenerateLTX2Prompt é uma versão especializada de um nó de geração de texto. Ele recebe um prompt de texto do usuário e o formata automaticamente com instruções específicas do sistema antes de enviá-lo a um modelo de linguagem para aprimoramento ou conclusão. O nó pode operar em dois modos: apenas texto ou com referência de imagem, usando diferentes prompts do sistema para cada caso.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | Sim | | O modelo CLIP usado para a codificação do texto. |
| `prompt` | STRING | Sim | | A entrada de texto bruta do usuário que será aprimorada ou completada. |
| `max_length` | INT | Sim | | O número máximo de tokens que o modelo de linguagem tem permissão para gerar. |
| `sampling_mode` | COMBO | Sim | `"greedy"`<br>`"top_k"`<br>`"top_p"`<br>`"temperature"` | A estratégia de amostragem usada para selecionar o próximo token durante a geração de texto. |
| `image` | IMAGE | Não | | Uma imagem de entrada opcional. Quando fornecida, o nó usa um prompt do sistema diferente que inclui um espaço reservado para contexto de imagem. |

**Observação:** O comportamento do nó muda com base na presença da entrada `image`. Se uma imagem for fornecida, o prompt gerado será formatado para uma tarefa de imagem-para-vídeo. Se nenhuma imagem for fornecida, a formatação será para uma tarefa de texto-para-vídeo.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | STRING | A string de texto aprimorada ou completada gerada pelo modelo de linguagem. |
