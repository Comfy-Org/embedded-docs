Este nó embaralha uma lista de imagens e uma lista de textos juntas, mantendo seus pares intactos. Ele usa uma semente aleatória para determinar a ordem do embaralhamento, garantindo que as mesmas listas de entrada sejam embaralhadas da mesma forma sempre que a semente for reutilizada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | Lista de imagens para embaralhar. | IMAGE | Sim | - |
| `textos` | Lista de textos para embaralhar. | STRING | Sim | - |
| `semente` | Semente aleatória. A ordem do embaralhamento é determinada por este valor (padrão: 0). | INT | Não | 0 a 18446744073709551615 |

**Observação:** As entradas `images` e `texts` devem ser listas do mesmo comprimento. O nó pareará a primeira imagem com o primeiro texto, a segunda imagem com o segundo texto e assim por diante, antes de embaralhar esses pares juntos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagens` | A lista embaralhada de imagens. | IMAGE |
| `textos` | A lista embaralhada de textos, mantendo seus pares originais com as imagens. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleImageTextDataset/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c87cef780c98b1cf2a58a7d5faf4399c85edd647a9fdba693d008152e43d9c99`
