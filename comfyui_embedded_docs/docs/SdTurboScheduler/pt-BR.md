SDTurboScheduler foi projetado para gerar uma sequência de valores sigma para amostragem de imagens, ajustando a sequência com base no nível de redução de ruído e no número de etapas especificadas. Ele utiliza as capacidades de amostragem de um modelo específico para produzir esses valores sigma, que são cruciais para controlar o processo de redução de ruído durante a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo` | O parâmetro model especifica o modelo generativo a ser usado para a geração dos valores sigma. É crucial para determinar o comportamento de amostragem específico e as capacidades do agendador. | `MODEL` |
| `passos` | O parâmetro steps determina o comprimento da sequência sigma a ser gerada, influenciando diretamente a granularidade do processo de redução de ruído. | `INT` |
| `redução_de_ruído` | O parâmetro denoise ajusta o ponto inicial da sequência sigma, permitindo um controle mais preciso sobre o nível de redução de ruído aplicado durante a geração da imagem. | `FLOAT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Uma sequência de valores sigma gerada com base no modelo, nas etapas e no nível de redução de ruído especificados. Esses valores são essenciais para controlar o processo de redução de ruído na geração de imagens. | `SIGMAS` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDTurboScheduler/pt-BR.md)
