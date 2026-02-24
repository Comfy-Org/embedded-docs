> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/pt-BR.md)

O nó Batch Latents combina múltiplas entradas latentes em um único lote. Ele recebe um número variável de amostras latentes e as mescla ao longo da dimensão do lote, permitindo que sejam processadas juntas em nós subsequentes. Isso é útil para gerar ou processar múltiplas imagens em uma única operação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sim | N/A | A primeira amostra latente a ser incluída no lote. |
| `latent_2` a `latent_50` | LATENT | Não | N/A | Amostras latentes adicionais a serem incluídas no lote. Você pode adicionar entre 2 e 50 entradas latentes no total. |

**Observação:** Você deve fornecer pelo menos duas entradas latentes para o nó funcionar. O nó criará automaticamente slots de entrada conforme você conecta mais latentes, até um máximo de 50.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | LATENT | Uma única saída latente contendo todas as entradas latentes combinadas em um lote. |
