# SplitSigmasDenoise

O nó SplitSigmasDenoise divide uma sequência de valores sigma em duas partes com base em um parâmetro de força de denoising. Ele divide os sigmas de entrada em sequências de sigma altos e baixos, onde o ponto de divisão é determinado multiplicando o número total de etapas (um a menos que o número de valores sigma) pelo fator de denoise. Isso permite separar o cronograma de ruído em diferentes faixas de intensidade para processamento especializado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de entrada de valores sigma que representa o cronograma de ruído | SIGMAS | Sim | - |
| `denoise` | O fator de força de denoising que determina onde dividir a sequência de sigma (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `high_sigmas` | A primeira porção da sequência de sigma, contendo os valores sigma mais altos até o ponto de divisão | SIGMAS |
| `low_sigmas` | A segunda porção da sequência de sigma, contendo os valores sigma mais baixos a partir do ponto de divisão | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
