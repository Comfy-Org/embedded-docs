# SplitSigmasDenoise

O nó SplitSigmasDenoise divide uma sequência de valores sigma em duas partes com base em um parâmetro de força de remoção de ruído. Ele divide os sigmas de entrada em sequências de sigma altos e baixos, onde o ponto de divisão é determinado multiplicando o total de passos pelo fator de denoise. Isso permite separar a programação de ruído em diferentes faixas de intensidade para processamento especializado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de entrada de valores sigma que representa a programação de ruído | SIGMAS | Sim | - |
| `denoise` | O fator de força de remoção de ruído que determina onde dividir a sequência de sigma (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

Nota: O número total de passos é o número de valores sigma menos 1. As duas sequências de saída compartilham um valor sigma no ponto de divisão. Em `denoise` = 0.0, `high_sigmas` está vazio; em `denoise` = 1.0, `high_sigmas` contém apenas o primeiro valor sigma e `low_sigmas` contém a sequência completa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `high_sigmas` | A primeira parte da sequência de sigma contendo os valores sigma mais altos | SIGMAS |
| `low_sigmas` | A segunda parte da sequência de sigma contendo os valores sigma mais baixos | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
