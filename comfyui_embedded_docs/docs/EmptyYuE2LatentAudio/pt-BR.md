# Áudio latent YuE2 Vazio

Este nó cria um latente de áudio vazio para YuE2, dimensionado para uma duração e uma quantidade de lote escolhidas. Ele produz dados de áudio silenciosos provisórios que nós posteriores podem preencher durante a geração de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Comprimento do latente de áudio a criar, em segundos (padrão: 120.0). O número de frames latentes é calculado a partir deste valor, com um mínimo de 1 frame. | FLOAT | Sim | 0.04 a 1000.0 (passo 0.04) |
| `batch_size` | Número de latentes de áudio a criar em um lote (padrão: 1). | INT | Sim | 1 a 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `LATENT` | Um latente de áudio vazio contendo um tensor de zeros, dimensionado por `batch_size` e pela contagem de frames derivada de `seconds`. Ele é marcado como tipo áudio com uma proporção de redução temporal de 1920. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
