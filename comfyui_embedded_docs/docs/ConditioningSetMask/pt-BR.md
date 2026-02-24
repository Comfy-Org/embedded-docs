> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/pt-BR.md)

Este nó foi projetado para modificar o condicionamento de um modelo generativo aplicando uma máscara com uma força especificada a determinadas áreas. Ele permite ajustes direcionados dentro do condicionamento, possibilitando um controle mais preciso sobre o processo de geração.

## Entradas

### Obrigatórias

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento a serem modificados. Servem como base para aplicar os ajustes de máscara e força. |
| `mask`        | `MASK`       | Um tensor de máscara que especifica as áreas dentro do condicionamento a serem modificadas. |
| `strength`    | `FLOAT`      | A força do efeito da máscara sobre o condicionamento, permitindo o ajuste fino das modificações aplicadas. |
| `set_cond_area` | COMBO[STRING] | Determina se o efeito da máscara é aplicado à área padrão ou delimitado pela própria máscara, oferecendo flexibilidade para direcionar regiões específicas. |

## Saídas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento modificados, com os ajustes de máscara e força aplicados. |
