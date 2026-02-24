> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/controlnet` e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó ControlNetLoader é projetado para carregar um modelo ControlNet de um caminho especificado. Ele desempenha um papel crucial na inicialização de modelos ControlNet, que são essenciais para aplicar mecanismos de controle sobre o conteúdo gerado ou modificar o conteúdo existente com base em sinais de controle.

## Entradas

| Campo                | Tipo Comfy        | Descrição                                                                       |
|----------------------|-------------------|---------------------------------------------------------------------------------|
| `control_net_name`   | `COMBO[STRING]`   | Especifica o nome do modelo ControlNet a ser carregado, usado para localizar o arquivo do modelo dentro de uma estrutura de diretórios predefinida. |

## Saídas

| Campo          | Tipo Comfy     | Descrição                                                                       |
|----------------|----------------|---------------------------------------------------------------------------------|
| `control_net`  | `CONTROL_NET`  | Retorna o modelo ControlNet carregado, pronto para ser usado no controle ou na modificação dos processos de geração de conteúdo. |
