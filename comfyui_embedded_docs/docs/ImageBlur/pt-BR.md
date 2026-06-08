O nó `ImageBlur` aplica um desfoque gaussiano a uma imagem, permitindo suavizar bordas e reduzir detalhes e ruídos. Ele oferece controle sobre a intensidade e a propagação do desfoque por meio de parâmetros.

## Entradas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de entrada a ser desfocada. Este é o alvo principal do efeito de desfoque. | `IMAGE` |
| `raio_de_desfoque` | Determina o raio do efeito de desfoque. Um raio maior resulta em um desfoque mais pronunciado. | `INT` |
| `sigma` | Controla a propagação do desfoque. Um valor de sigma mais alto significa que o desfoque afetará uma área mais ampla ao redor de cada pixel. | `FLOAT` |

## Saídas

| Campo | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A saída é a versão desfocada da imagem de entrada, com o grau de desfoque determinado pelos parâmetros de entrada. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlur/pt-BR.md)
