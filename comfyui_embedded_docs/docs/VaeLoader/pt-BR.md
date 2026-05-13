> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/pt-BR.md)

Este nó detecta modelos localizados na pasta `ComfyUI/models/vae` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para que ele leia os arquivos de modelo da pasta correspondente.

O nó VAELoader foi projetado para carregar modelos de Autoencoder Variacional (VAE), especificamente adaptado para lidar com VAEs padrão e aproximados. Ele suporta o carregamento de VAEs por nome, incluindo tratamento especializado para modelos 'taesd' e 'taesdxl', e se ajusta dinamicamente com base na configuração específica do VAE.

## Entradas

| Campo      | Tipo Comfy        | Descrição                                                                                   |
|------------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]`    | Especifica o nome do VAE a ser carregado, determinando qual modelo VAE é buscado e carregado, com suporte para uma variedade de nomes predefinidos de VAE, incluindo 'taesd' e 'taesdxl'. |

## Saídas

| Campo | Tipo de Dado | Descrição                                                              |
|-------|--------------|--------------------------------------------------------------------------|
| `vae` | `VAE`        | Retorna o modelo VAE carregado, pronto para operações adicionais, como codificação ou decodificação. A saída é um objeto de modelo que encapsula o estado do modelo carregado. |