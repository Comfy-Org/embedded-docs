> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNETLoader/pt-BR.md)

O nó UNETLoader é projetado para carregar modelos U-Net pelo nome, facilitando o uso de arquiteturas U-Net pré-treinadas dentro do sistema.

Este nó detectará modelos localizados na pasta `ComfyUI/models/diffusion_models`.

## Entradas

| Parâmetro   | Tipo de Dados | Descrição |
|-------------|--------------|-------------|
| `unet_name` | COMBO[STRING] | Especifica o nome do modelo U-Net a ser carregado. Este nome é usado para localizar o modelo dentro de uma estrutura de diretórios predefinida, permitindo o carregamento dinâmico de diferentes modelos U-Net. |
| `weight_dtype` | ... | 🚧  fp8_e4m3fn fp9_e5m2  |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model`   | MODEL     | Retorna o modelo U-Net carregado, permitindo que ele seja utilizado para processamento adicional ou inferência dentro do sistema. |
