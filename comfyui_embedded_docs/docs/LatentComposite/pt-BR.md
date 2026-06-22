# Latent Composite

O nó LatentComposite foi projetado para mesclar ou combinar duas representações latentes em uma única saída. Esse processo é essencial para criar imagens compostas ou características combinando as propriedades das entradas latentes de forma controlada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `amostras_destino` | A representação latente 'samples_to' onde o 'samples_from' será sobreposto. Serve como base para a operação de composição. | `LATENT` |
| `amostras_origem` | A representação latente 'samples_from' a ser sobreposta no 'samples_to'. Contribui com suas características ou propriedades para a saída composta final. | `LATENT` |
| `x` | A coordenada x (posição horizontal) onde o latente 'samples_from' será posicionado sobre o 'samples_to'. Determina o alinhamento horizontal da composição. | `INT` |
| `y` | A coordenada y (posição vertical) onde o latente 'samples_from' será posicionado sobre o 'samples_to'. Determina o alinhamento vertical da composição. | `INT` |
| `suavização` | Um valor booleano que indica se o latente 'samples_from' deve ser redimensionado para corresponder ao 'samples_to' antes da composição. Isso pode afetar a escala e a proporção do resultado composto. | `INT` |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A saída é uma representação latente composta, mesclando as características de ambos os latentes 'samples_to' e 'samples_from' com base nas coordenadas especificadas e na opção de redimensionamento. | `LATENT` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/pt-BR.md)
