# LatentOperationSharpen

O nó LatentOperationSharpen cria uma operação de nitidez para representações latentes usando um kernel gaussiano. Ele normaliza os dados latentes, aplica um kernel de nitidez personalizado por meio de convolução e, em seguida, restaura a luminância original. Isso melhora os detalhes e as bordas na representação do espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `raio_de_nitidez` | O raio do kernel de nitidez, que controla o tamanho da área usada para a nitidez (padrão: 9) | INT | Sim | 1-31 |
| `sigma` | O desvio padrão do kernel gaussiano usado para construir o kernel de nitidez (padrão: 1.0) | FLOAT | Sim | 0.1-10.0 |
| `alfa` | O fator de intensidade da nitidez; valores maiores produzem um efeito de nitidez mais forte (padrão: 0.1) | FLOAT | Sim | 0.0-5.0 |

Os três parâmetros são avançados e possuem valores padrão, portanto o nó pode ser usado sem alterá-los. Este nó é marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `operation` | Retorna uma operação de nitidez que pode ser aplicada a dados latentes | LATENT_OPERATION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
