# Ruído Aleatório

O nó RandomNoise cria um gerador de ruído baseado em um valor de semente (seed) para uso durante o processo de amostragem. A mesma semente sempre produz o mesmo padrão de ruído, permitindo resultados consistentes e reproduzíveis em várias execuções. Os amostradores usam o ruído gerado ao processar imagens latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `semente do ruído` | O valor de semente usado para gerar o padrão de ruído aleatório (padrão: 0). A mesma semente sempre produz a mesma saída de ruído. Esta entrada inclui uma opção de controle após a geração para atualizar automaticamente a semente após cada geração. | INT | Sim | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `noise` | Um objeto de ruído que gera ruído aleatório para amostras latentes com base no valor de semente fornecido. Usado pelos amostradores durante o processo de amostragem. | NOISE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b55ff98c636c55f064ede82c6848ffa163d1fd9b0cf6195f4a35603cfbe2bc1e`
