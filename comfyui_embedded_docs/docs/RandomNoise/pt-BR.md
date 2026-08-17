# Ruído Aleatório

O nó RandomNoise gera padrões de ruído aleatório com base em um valor de seed. Ele cria ruído reproduzível que pode ser usado para diversas tarefas de processamento e geração de imagens. A mesma seed sempre produzirá o mesmo padrão de ruído, permitindo resultados consistentes em várias execuções.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `noise_seed` | O valor de seed usado para gerar o padrão de ruído aleatório (padrão: 0). A mesma seed sempre produzirá a mesma saída de ruído. O controle após a geração está habilitado, permitindo que o valor de seed seja randomizado, fixado, incrementado ou decrementado após cada geração. | INT | Sim | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `noise` | O padrão de ruído aleatório gerado com base no valor de seed fornecido. | NOISE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
