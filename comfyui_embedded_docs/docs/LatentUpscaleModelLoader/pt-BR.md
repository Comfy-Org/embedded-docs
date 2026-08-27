# Carregar Modelo de Upscale Latent

O nó LatentUpscaleModelLoader carrega um modelo especializado em upscaling de representações latentes a partir de um arquivo armazenado na pasta `latent_upscale_models` do ComfyUI. Ele detecta automaticamente o tipo de modelo (720p, 1080p ou outro upsampler latente) a partir do conteúdo do arquivo e configura a arquitetura interna correspondente, deixando o modelo carregado pronto para uso por outros nós.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome_do_modelo` | O nome do arquivo do modelo de upscale latente a ser carregado. As opções disponíveis são preenchidas dinamicamente a partir dos arquivos presentes no diretório `latent_upscale_models` do ComfyUI. | COMBO | Sim | Todos os arquivos na pasta `latent_upscale_models` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de upscale latente carregado, configurado e pronto para uso. | LATENT_UPSCALE_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
