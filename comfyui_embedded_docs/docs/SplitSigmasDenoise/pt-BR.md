# SplitSigmasDenoise

O nó SplitSigmasDenoise divide uma sequência de valores sigma em duas partes com base em um parâmetro de força de denoising. Ele divide os sigmas de entrada em sequências de sigma altos e baixos, onde o ponto de divisão é determinado multiplicando-se o total de etapas pelo fator de denoise. Isso permite separar o agendamento de ruído em diferentes faixas de intensidade para processamento especializado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `sigmas` | A sequência de entrada de valores sigma que representa o agendamento de ruído | SIGMAS | Sim | - |
| `redução_de_ruído` | O fator de força de denoising que determina onde dividir a sequência de sigmas (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sigmas_altos` | A primeira parte da sequência de sigmas contendo os valores de sigma mais altos | SIGMAS |
| `sigmas_baixos` | A segunda parte da sequência de sigmas contendo os valores de sigma mais baixos | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6198cdbc07b5c9aacf1137a5d6350e090ffd14050abbcc37ff79ff5e975a8c20`
