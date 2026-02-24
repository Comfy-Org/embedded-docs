> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/pt-BR.md)

O SDTurboScheduler é projetado para gerar uma sequência de valores sigma para a amostragem de imagens, ajustando a sequência com base no nível de denoise e no número de etapas especificados. Ele aproveita as capacidades de amostragem de um modelo específico para produzir esses valores sigma, que são cruciais para controlar o processo de remoção de ruído durante a geração de imagens.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
| --- | --- | --- |
| `model` | `MODEL` | O parâmetro `model` especifica o modelo generativo a ser usado para a geração dos valores sigma. É crucial para determinar o comportamento e as capacidades específicas de amostragem do agendador. |
| `steps` | `INT` | O parâmetro `steps` determina o comprimento da sequência de valores sigma a ser gerada, influenciando diretamente a granularidade do processo de remoção de ruído. |
| `denoise` | `FLOAT` | O parâmetro `denoise` ajusta o ponto de partida da sequência de valores sigma, permitindo um controle mais refinado sobre o nível de remoção de ruído aplicado durante a geração da imagem. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
| --- | --- | --- |
| `sigmas` | `SIGMAS` | Uma sequência de valores sigma gerada com base no modelo, número de etapas e nível de denoise especificados. Esses valores são essenciais para controlar o processo de remoção de ruído na geração de imagens. |
