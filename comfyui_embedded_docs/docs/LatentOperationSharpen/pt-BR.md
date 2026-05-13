> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/pt-BR.md)

O nó **LatentOperationSharpen** aplica um efeito de nitidez a representações latentes usando um kernel Gaussiano. Ele funciona normalizando os dados latentes, aplicando uma convolução com um kernel de nitidez personalizado e, em seguida, restaurando a luminância original. Isso realça os detalhes e bordas na representação do espaço latente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `sharpen_radius` | INT | Não | 1-31 | O raio do kernel de nitidez (padrão: 9) |
| `sigma` | FLOAT | Não | 0.1-10.0 | O desvio padrão para o kernel Gaussiano (padrão: 1.0) |
| `alpha` | FLOAT | Não | 0.0-5.0 | O fator de intensidade da nitidez (padrão: 0.1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `operation` | LATENT_OPERATION | Retorna uma operação de nitidez que pode ser aplicada a dados latentes |

---
**Source fingerprint (SHA-256):** `542754746ab462eb27229ab9b949bb66054ab4c87c77cc59d405b35a2cc27bce`
