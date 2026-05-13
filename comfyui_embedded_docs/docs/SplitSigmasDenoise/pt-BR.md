> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/pt-BR.md)

O nó SplitSigmasDenoise divide uma sequência de valores sigma em duas partes com base em um parâmetro de intensidade de redução de ruído. Ele separa os sigmas de entrada em sequências de sigma alto e baixo, onde o ponto de divisão é determinado multiplicando o total de etapas pelo fator de redução de ruído. Isso permite separar o agendamento de ruído em diferentes faixas de intensidade para processamento especializado.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `sigmas` | SIGMAS | Sim | - | A sequência de entrada de valores sigma que representa o agendamento de ruído |
| `redução_de_ruído` | FLOAT | Sim | 0.0 - 1.0 | O fator de intensidade de redução de ruído que determina onde dividir a sequência sigma (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `high_sigmas` | SIGMAS | A primeira parte da sequência sigma contendo valores sigma mais altos |
| `low_sigmas` | SIGMAS | A segunda parte da sequência sigma contendo valores sigma mais baixos |

---
**Source fingerprint (SHA-256):** `fda53efe2fcaed9244376b7360d8b0b76ce7395d594de4c2ecc48a8f243d7ca6`
