# Carregar Modelo de Upscale Latent

O nó LatentUpscaleModelLoader carrega um modelo especializado projetado para ampliação (upscaling) de representações latentes. Ele lê um arquivo de modelo da pasta designada do sistema e detecta automaticamente seu tipo (720p, 1080p ou outro) para instanciar e configurar a arquitetura interna correta do modelo. O modelo carregado fica então pronto para ser usado por outros nós em tarefas de super-resolução no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model_name` | O nome do arquivo de modelo de ampliação latente a ser carregado. As opções disponíveis são preenchidas dinamicamente a partir dos arquivos presentes no diretório `latent_upscale_models` do seu ComfyUI. | COMBO | Sim | Todos os arquivos na pasta `latent_upscale_models` |

Observação: o nó detecta automaticamente a arquitetura do modelo a partir do conteúdo do arquivo. Modelos contendo camadas de super-resolução HunyuanVideo 720p são carregados como modelos 720p, modelos com camadas de ampliação estilo 1080p são carregados como modelos 1080p e modelos com outras estruturas de camadas são carregados como modelos LatentUpsampler.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de ampliação latente carregado, configurado e pronto para uso. | LATENT_UPSCALE_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
