# LatentOperationSharpen

O nó LatentOperationSharpen aplica um efeito de nitidez a representações latentes usando um kernel gaussiano. Ele funciona normalizando os dados latentes, aplicando uma convolução com um kernel de nitidez personalizado e, em seguida, restaurando a luminância original. Isso melhora os detalhes e as bordas na representação do espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | O raio do kernel de nitidez. O tamanho total do kernel é calculado como o dobro desse valor mais um (padrão: 9). | INT | Sim | 1-31 |
| `sigma` | O desvio padrão do kernel gaussiano (padrão: 1.0). | FLOAT | Sim | 0.1-10.0 |
| `alpha` | O fator de intensidade da nitidez que controla a força do efeito (padrão: 0.1). | FLOAT | Sim | 0.0-5.0 |

Todos os parâmetros são avançados. Este nó é marcado como experimental.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `operation` | Uma operação de nitidez que pode ser aplicada a dados latentes. Aplicá-la a um latent retorna uma versão mais nítida com a luminância original preservada. | LATENT_OPERATION |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
