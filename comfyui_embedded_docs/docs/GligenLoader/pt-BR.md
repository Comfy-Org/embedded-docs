> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENLoader/pt-BR.md)

Este nó detecta modelos localizados na pasta `ComfyUI/models/gligen` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para que ele leia os arquivos de modelo da pasta correspondente.

O nó `GLIGENLoader` foi projetado para carregar modelos GLIGEN, que são modelos generativos especializados. Ele facilita o processo de recuperação e inicialização desses modelos a partir de caminhos especificados, deixando-os prontos para tarefas generativas posteriores.

## Entradas

| Campo         | Tipo Comfy        | Descrição                                                                                     |
|---------------|-------------------|-----------------------------------------------------------------------------------------------|
| `gligen_name` | `COMBO[STRING]`   | O nome do modelo GLIGEN a ser carregado, especificando qual arquivo de modelo recuperar e carregar, crucial para a inicialização do modelo GLIGEN. |

## Saídas

| Campo     | Tipo de Dados | Descrição                                                                                         |
|-----------|---------------|---------------------------------------------------------------------------------------------------|
| `gligen`  | `GLIGEN`      | O modelo GLIGEN carregado, pronto para uso em tarefas generativas, representando o modelo totalmente inicializado carregado do caminho especificado. |