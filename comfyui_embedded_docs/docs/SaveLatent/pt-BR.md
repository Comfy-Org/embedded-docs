> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/pt-BR.md)

O nó SaveLatent salva tensores latentes no disco como arquivos para uso posterior ou compartilhamento. Ele recebe amostras latentes e as salva no diretório de saída com metadados opcionais, incluindo informações do prompt. O nó gerencia automaticamente a nomeação e organização dos arquivos, preservando a estrutura dos dados latentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | As amostras latentes a serem salvas no disco |
| `filename_prefix` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "latents/ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt para incluir nos metadados (parâmetro oculto) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Informações PNG adicionais para incluir nos metadados (parâmetro oculto) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `ui` | UI | Fornece informações de localização do arquivo para o latente salvo na interface do ComfyUI |
