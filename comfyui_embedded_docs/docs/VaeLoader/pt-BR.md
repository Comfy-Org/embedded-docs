> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAELoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/vae` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó VAELoader é projetado para carregar modelos de Autoencoder Variacional (VAE), especificamente adaptado para lidar com VAEs padrão e aproximados. Ele suporta o carregamento de VAEs por nome, incluindo tratamento especializado para modelos 'taesd' e 'taesdxl', e ajusta-se dinamicamente com base na configuração específica do VAE.

## Entradas

| Campo   | Tipo Comfy       | Descrição                                                                                   |
|---------|-------------------|-----------------------------------------------------------------------------------------------|
| `vae_name` | `COMBO[STRING]`    | Especifica o nome do VAE a ser carregado, determinando qual modelo VAE é buscado e carregado, com suporte a uma variedade de nomes de VAE predefinidos, incluindo 'taesd' e 'taesdxl'. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `vae`  | `VAE`       | Retorna o modelo VAE carregado, pronto para operações posteriores, como codificação ou decodificação. A saída é um objeto de modelo que encapsula o estado do modelo carregado. |
