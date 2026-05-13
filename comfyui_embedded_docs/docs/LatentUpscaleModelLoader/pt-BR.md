> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/pt-BR.md)

O nó LatentUpscaleModelLoader carrega um modelo especializado projetado para ampliar representações latentes. Ele lê um arquivo de modelo da pasta designada do sistema e detecta automaticamente seu tipo (720p, 1080p ou outro) para instanciar e configurar a arquitetura interna correta do modelo. O modelo carregado fica então pronto para ser usado por outros nós em tarefas de super-resolução no espaço latente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model_name` | STRING | Sim | *Todos os arquivos na pasta `latent_upscale_models`* | O nome do arquivo do modelo de ampliação latente a ser carregado. As opções disponíveis são preenchidas dinamicamente a partir dos arquivos presentes no diretório `latent_upscale_models` do seu ComfyUI. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | LATENT_UPSCALE_MODEL | O modelo de ampliação latente carregado, configurado e pronto para uso. |

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
