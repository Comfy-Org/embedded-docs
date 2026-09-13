# YuE2 Gerar ABC

Este nó gera notação ABC para uma música com base em uma descrição de estilo e letras, usando um modelo de texto e letras YuE2. A saída `abc` resultante pode ser conectada ao nó YuE2 Generate Music para produzir áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `clip` | O modelo YuE2 usado para tokenizar o estilo e as letras e gerar a notação ABC. | CLIP | Sim | - |
| `style` | Texto que descreve o estilo musical da música. Suporta entrada de várias linhas e prompts dinâmicos. | STRING | Sim | - |
| `lyrics` | Texto contendo as letras da música. Suporta entrada de várias linhas e prompts dinâmicos. | STRING | Sim | - |
| `semente` | Semente aleatória usada para a geração. Alterá-la produz resultados diferentes. Padrão: 0. | INT | Sim | 0 a 18446744073709551615 |
| `modo` | full: gera melodia e acordes; melody: gera apenas a melodia, recomendado para covers. | COMBO | Sim | "full"<br>"melody" |
| `max_abc_tokens` | Número máximo de tokens gerados para a notação ABC. Padrão: 8192. Configuração avançada. | INT | Sim | 1 a 20000 |
| `temperature` | Controla a aleatoriedade dos tokens gerados. Valores mais altos produzem saídas mais variadas. Padrão: 0.7. Configuração avançada. | FLOAT | Sim | 0.0 a 5.0 |
| `top_p` | Limiar de amostragem nucleus; apenas tokens com probabilidade acumulada dentro desse limiar são considerados. Padrão: 0.9. Configuração avançada. | FLOAT | Sim | 0.01 a 1.0 |
| `top_k` | Limita a seleção de tokens aos K mais prováveis. Padrão: 30. Configuração avançada. | INT | Sim | 1 a 32768 |
| `repetition_penalty` | Penalidade aplicada a tokens repetidos durante a geração. Padrão: 1.005. Configuração avançada. | FLOAT | Sim | 0.01 a 10.0 |
| `penalty_window` | Número de tokens ABC recentes usados para penalizar repetição. Padrão: 100. Configuração avançada. | INT | Sim | 1 a 20000 |

## Saídas

| Nome de Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `abc` | A notação ABC gerada da música, que pode ser conectada ao nó YuE2 Generate Music. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/YuE2GenerateABC/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2c1bf0841a044724ff0477f920972d70bbd97de49b56fbe6213a9ac134797130`
