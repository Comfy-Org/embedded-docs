> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/pt-BR.md)

O nó LoadLatent carrega representações latentes previamente salvas a partir de arquivos .latent no diretório de entrada. Ele lê os dados do tensor latente do arquivo e aplica quaisquer ajustes de escala necessários antes de retornar os dados latentes para uso em outros nós.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `latent` | STRING | Sim | Todos os arquivos .latent no diretório de entrada | Seleciona qual arquivo .latent carregar dentre os arquivos disponíveis no diretório de entrada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Retorna os dados da representação latente carregados a partir do arquivo selecionado |
