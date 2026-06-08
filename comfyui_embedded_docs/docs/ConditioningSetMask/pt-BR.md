Este nó foi projetado para modificar o condicionamento de um modelo generativo aplicando uma máscara com uma intensidade específica em determinadas áreas. Ele permite ajustes direcionados dentro do condicionamento, possibilitando um controle mais preciso sobre o processo de geração.

## Entradas

### Obrigatórias

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento a serem modificados. Servem como base para aplicar a máscara e os ajustes de intensidade. | CONDITIONING |
| `mask` | Um tensor de máscara que especifica as áreas dentro do condicionamento a serem modificadas. | `MASK` |
| `força` | A intensidade do efeito da máscara sobre o condicionamento, permitindo o ajuste fino das modificações aplicadas. | `FLOAT` |
| `definir_área_cond` | Determina se o efeito da máscara é aplicado à área padrão ou limitado pela própria máscara, oferecendo flexibilidade na segmentação de regiões específicas. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento modificados, com os ajustes de máscara e intensidade aplicados. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/pt-BR.md)
