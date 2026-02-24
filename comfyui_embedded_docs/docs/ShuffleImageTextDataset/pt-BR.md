> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/pt-BR.md)

Este nó embaralha uma lista de imagens e uma lista de textos em conjunto, mantendo seus pares intactos. Ele usa uma semente aleatória para determinar a ordem do embaralhamento, garantindo que as mesmas listas de entrada sejam embaralhadas da mesma forma sempre que a semente for reutilizada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Lista de imagens a serem embaralhadas. |
| `texts` | STRING | Sim | - | Lista de textos a serem embaralhados. |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente aleatória. A ordem do embaralhamento é determinada por este valor (padrão: 0). |

**Observação:** As entradas `images` e `texts` devem ser listas de mesmo comprimento. O nó irá parear a primeira imagem com o primeiro texto, a segunda imagem com o segundo texto, e assim por diante, antes de embaralhar esses pares juntos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | A lista embaralhada de imagens. |
| `texts` | STRING | A lista embaralhada de textos, mantendo seus pares originais com as imagens. |
