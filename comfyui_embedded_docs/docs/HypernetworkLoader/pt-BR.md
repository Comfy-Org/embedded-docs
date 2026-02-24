> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/pt-BR.md)

Este nó detectará modelos localizados na pasta `ComfyUI/models/hypernetworks`, e também lerá modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, pode ser necessário **atualizar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo da pasta correspondente.

O nó HypernetworkLoader é projetado para aprimorar ou modificar as capacidades de um determinado modelo aplicando uma hiper-rede. Ele carrega uma hiper-rede especificada e a aplica ao modelo, potencialmente alterando seu comportamento ou desempenho com base no parâmetro de força. Este processo permite ajustes dinâmicos na arquitetura ou nos parâmetros do modelo, possibilitando sistemas de IA mais flexíveis e adaptativos.

## Entradas

| Campo                 | Tipo Comfy       | Descrição                                                                                  |
|-----------------------|-------------------|----------------------------------------------------------------------------------------------|
| `model`               | `MODEL`           | O modelo base ao qual a hiper-rede será aplicada, determinando a arquitetura a ser aprimorada ou modificada. |
| `hypernetwork_name`  | `COMBO[STRING]`   | O nome da hiper-rede a ser carregada e aplicada ao modelo, impactando o comportamento ou desempenho modificado do modelo. |
| `strength`            | `FLOAT`           | Um escalar que ajusta a intensidade do efeito da hiper-rede no modelo, permitindo o ajuste fino das alterações. |

## Saídas

| Campo   | Tipo de Dados | Descrição                                                              |
|---------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL`     | O modelo modificado após a aplicação da hiper-rede, demonstrando o impacto da hiper-rede no modelo original. |
