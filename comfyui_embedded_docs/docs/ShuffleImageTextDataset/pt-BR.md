> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/pt-BR.md)

Este nó embaralha uma lista de imagens e uma lista de textos juntas, mantendo seus pares intactos. Ele usa uma semente aleatória para determinar a ordem do embaralhamento, garantindo que as mesmas listas de entrada sejam embaralhadas da mesma forma sempre que a semente for reutilizada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `images` | IMAGE | Sim | - | Lista de imagens para embaralhar. |
| `texts` | STRING | Sim | - | Lista de textos para embaralhar. |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente aleatória. A ordem do embaralhamento é determinada por este valor (padrão: 0). |

**Observação:** As entradas `images` e `texts` devem ser listas do mesmo comprimento. O nó pareará a primeira imagem com o primeiro texto, a segunda imagem com o segundo texto e assim por diante, antes de embaralhar esses pares juntos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `images` | IMAGE | A lista embaralhada de imagens. |
| `texts` | STRING | A lista embaralhada de textos, mantendo seus pares originais com as imagens. |

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
