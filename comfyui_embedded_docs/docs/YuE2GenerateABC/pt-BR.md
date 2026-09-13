# YuE2 Gerar ABC

Este nó gera notação ABC para uma música com base em uma descrição de estilo e letras, usando um modelo de texto e letras YuE2. A saída `abc` resultante pode ser conectada ao nó YuE2 Generate Music para produzir áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | O modelo YuE2 usado para tokenizar o estilo e as letras e gerar a notação ABC. | CLIP | Sim | - |
| `style` | Texto que descreve o estilo musical da música. | STRING | Sim | - |
| `lyrics` | Texto contendo as letras da música. | STRING | Sim | - |
| `seed` | Semente aleatória usada para a geração. Alterá-la produz resultados diferentes. Padrão: 0. | INT | Sim | 0 a 18446744073709551615 |
| `mode` | full: gera melodia e acordes; melody: gera apenas a melodia, recomendado para covers. | COMBO | Sim | "full"<br>"melody" |
| `max_abc_tokens` | Número máximo de tokens gerados para a notação ABC. Padrão: 8192. | INT | Sim | 1 a 20000 |

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `abc` | A notação ABC gerada da música, que pode ser conectada ao nó YuE2 Generate Music. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e06f980a53e90b750f4190a95199e0e5ed1bd8c54d4dbf8485602ff1af00102`
