> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/pt-BR.md)

O nó TorchCompileModel aplica a compilação PyTorch a um modelo para otimizar seu desempenho. Ele cria uma cópia do modelo de entrada e o encapsula com a funcionalidade de compilação do PyTorch usando o *backend* especificado. Isso pode melhorar a velocidade de execução do modelo durante a inferência.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo a ser compilado e otimizado |
| `backend` | STRING | Sim | "inductor"<br>"cudagraphs" | O *backend* de compilação PyTorch a ser usado para otimização |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo compilado com a compilação PyTorch aplicada |
