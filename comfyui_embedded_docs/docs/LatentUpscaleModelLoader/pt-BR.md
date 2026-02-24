> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/pt-BR.md)

O nó LatentUpscaleModelLoader carrega um modelo especializado projetado para aumentar a resolução (upscaling) de representações latentes. Ele lê um arquivo de modelo da pasta designada do sistema e detecta automaticamente seu tipo (720p, 1080p ou outro) para instanciar e configurar a arquitetura de modelo interna correta. O modelo carregado fica então pronto para ser usado por outros nós em tarefas de super-resolução no espaço latente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model_name` | STRING | Sim | *Todos os arquivos na pasta `latent_upscale_models`* | O nome do arquivo do modelo de upscale latente a ser carregado. As opções disponíveis são preenchidas dinamicamente a partir dos arquivos presentes no diretório `latent_upscale_models` do seu ComfyUI. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | LATENT_UPSCALE_MODEL | O modelo de upscale latente carregado, configurado e pronto para uso. |
