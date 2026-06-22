# Carregar Modelo de Upscale Latent

O nó LatentUpscaleModelLoader carrega um modelo especializado projetado para ampliar representações latentes. Ele lê um arquivo de modelo da pasta designada do sistema e detecta automaticamente seu tipo (720p, 1080p ou outro) para instanciar e configurar a arquitetura interna correta do modelo. O modelo carregado fica então pronto para ser usado por outros nós em tarefas de super-resolução no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `nome_do_modelo` | O nome do arquivo do modelo de ampliação latente a ser carregado. As opções disponíveis são preenchidas dinamicamente a partir dos arquivos presentes no diretório `latent_upscale_models` do seu ComfyUI. | STRING | Sim | *Todos os arquivos na pasta `latent_upscale_models`* |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo de ampliação latente carregado, configurado e pronto para uso. | LATENT_UPSCALE_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
