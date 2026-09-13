# LTXVScheduler

O nó LTXVScheduler gera valores sigma para um processo de amostragem personalizado. Ele calcula o cronograma de ruído a partir do número de tokens no latente fornecido, ou usa um padrão de 4096 tokens quando nenhum latente está conectado, e pode opcionalmente esticar os valores sigma para que o valor final corresponda ao valor `terminal` especificado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `steps` | Número de etapas de amostragem (padrão: 20) | INT | Sim | 1-10000 |
| `max_shift` | Valor máximo de deslocamento usado no cálculo de sigma (padrão: 2.05) | FLOAT | Sim | 0.0-100.0 (passo: 0.01) |
| `base_shift` | Valor base de deslocamento usado no cálculo de sigma (padrão: 0.95) | FLOAT | Sim | 0.0-100.0 (passo: 0.01) |
| `stretch` | Estica os sigmas para que fiquem no intervalo [terminal, 1] (padrão: True) | BOOLEAN | Sim | True/False |
| `terminal` | O valor terminal dos sigmas após o esticamento (padrão: 0.1). Usado apenas quando `stretch` está habilitado. | FLOAT | Sim | 0.0-0.99 (passo: 0.01) |
| `latent` | Entrada latente opcional usada para calcular a contagem de tokens para ajuste dos sigmas. Quando não fornecida, usa-se uma contagem padrão de 4096 tokens. | LATENT | Não | - |

**Nota:** Quando `stretch` está habilitado, os valores sigma diferentes de zero são reescalados para que o último sigma diferente de zero seja igual ao valor `terminal`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sigmas` | Valores sigma gerados para o processo de amostragem | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
