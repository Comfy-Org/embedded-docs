# EmptyARVideoLatent

## Visão Geral

O nó EmptyARVideoLatent cria uma representação latente de vídeo vazia, em branco, para geração de vídeos. Ele é usado para inicializar um processo de geração de vídeo fornecendo um tensor de zeros com as dimensões, a proporção de aspecto e o comprimento especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `width` | A largura dos quadros de vídeo em pixels (padrão: 832) | INT | Sim | 16 a 8192 (passo: 16) |
| `height` | A altura dos quadros de vídeo em pixels (padrão: 480) | INT | Sim | 16 a 8192 (passo: 16) |
| `length` | O número de quadros do vídeo (padrão: 81) | INT | Sim | 1 a 1024 (passo: 4) |
| `batch_size` | O número de vídeos a serem gerados em um único lote (padrão: 1) | INT | Sim | 1 a 64 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | Um tensor latente preenchido com zeros, representando um espaço latente de vídeo vazio com as dimensões, o comprimento e o tamanho do lote especificados. A forma do tensor é [batch_size, 16, lat_t, height/8, width/8], em que lat_t = ((length - 1) // 4) + 1 é o número de etapas de tempo latentes derivado do comprimento solicitado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
