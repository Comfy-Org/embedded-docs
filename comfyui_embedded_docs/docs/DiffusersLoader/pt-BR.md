> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/pt-BR.md)

O nó DiffusersLoader carrega modelos pré-treinados no formato diffusers. Ele busca por diretórios de modelos diffusers válidos que contenham um arquivo model_index.json e os carrega como componentes MODEL, CLIP e VAE para uso no fluxo de trabalho. Este nó faz parte da categoria de carregadores obsoletos e fornece compatibilidade com modelos diffusers do Hugging Face.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_path` | STRING | Sim | Múltiplas opções disponíveis<br>(preenchidas automaticamente a partir das pastas diffusers) | O caminho para o diretório do modelo diffusers a ser carregado. O nó varre automaticamente por modelos diffusers válidos nas pastas diffusers configuradas e lista as opções disponíveis. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `MODEL` | MODEL | O componente de modelo carregado a partir do formato diffusers |
| `CLIP` | CLIP | O componente do modelo CLIP carregado a partir do formato diffusers |
| `VAE` | VAE | O componente VAE (Variational Autoencoder) carregado a partir do formato diffusers |
