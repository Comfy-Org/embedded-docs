> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/style_models` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó StyleModelLoader é projetado para carregar um modelo de estilo a partir de um caminho especificado. Ele se concentra em recuperar e inicializar modelos de estilo que podem ser usados para aplicar estilos artísticos específicos a imagens, permitindo assim a personalização de saídas visuais com base no modelo de estilo carregado.

## Entradas

| Nome do Parâmetro   | Tipo Comfy     | Tipo Python | Descrição                                                                                       |
|---------------------|----------------|-------------|---------------------------------------------------------------------------------------------------|
| `style_model_name`  | COMBO[STRING] | `str`        | Especifica o nome do modelo de estilo a ser carregado. Este nome é usado para localizar o arquivo do modelo dentro de uma estrutura de diretórios predefinida, permitindo o carregamento dinâmico de diferentes modelos de estilo com base na entrada do usuário ou nas necessidades da aplicação. |

## Saídas

| Nome do Parâmetro | Tipo Comfy   | Tipo Python | Descrição                                                                                       |
|-------------------|--------------|-------------|---------------------------------------------------------------------------------------------------|
| `style_model`     | `STYLE_MODEL` | `StyleModel` | Retorna o modelo de estilo carregado, pronto para ser usado na aplicação de estilos a imagens. Isso permite a personalização dinâmica de saídas visuais através da aplicação de diferentes estilos artísticos. |
