O nó LTXVScheduler gera valores sigma para processos de amostragem personalizados. Ele calcula os parâmetros do cronograma de ruído com base no número de tokens no latent de entrada e aplica uma transformação sigmoide para criar o cronograma de amostragem. O nó pode opcionalmente esticar os sigmas resultantes para corresponder a um valor terminal especificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `steps` | Número de etapas de amostragem (padrão: 20) | INT | Sim | 1-10000 |
| `max_shift` | Valor máximo de deslocamento para cálculo do sigma (padrão: 2.05) | FLOAT | Sim | 0.0-100.0 |
| `base_shift` | Valor base de deslocamento para cálculo do sigma (padrão: 0.95) | FLOAT | Sim | 0.0-100.0 |
| `stretch` | Estica os sigmas para ficarem no intervalo [terminal, 1] (padrão: Verdadeiro) | BOOLEAN | Sim | Verdadeiro/Falso |
| `terminal` | O valor terminal dos sigmas após o esticamento (padrão: 0.1) | FLOAT | Sim | 0.0-0.99 |
| `latent` | Entrada latent opcional usada para calcular a contagem de tokens para ajuste do sigma | LATENT | Não | - |

**Nota:** O parâmetro `latent` é opcional. Quando não fornecido, o nó usa uma contagem de tokens padrão de 4096 para os cálculos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas` | Valores sigma gerados para o processo de amostragem | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3c7e8721fd75bfb0a253c38cd29e2ee1905bfe08193aa97dbaa959550aba34bc`
