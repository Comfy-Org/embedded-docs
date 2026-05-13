> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/pt-BR.md)

# Visão Geral

O nó EmptyARVideoLatent cria uma representação latente vazia e em branco para geração de vídeos. Ele é utilizado para inicializar um processo de geração de vídeo fornecendo um tensor de zeros com as dimensões, proporção de aspecto e comprimento especificados.

# Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `width` | INT | Sim | 16 a 8192 (passo: 16) | A largura dos quadros do vídeo em pixels (padrão: 832) |
| `height` | INT | Sim | 16 a 8192 (passo: 16) | A altura dos quadros do vídeo em pixels (padrão: 480) |
| `length` | INT | Sim | 1 a 1024 (passo: 4) | O número de quadros no vídeo (padrão: 81) |
| `batch_size` | INT | Sim | 1 a 64 | O número de vídeos a serem gerados em um único lote (padrão: 1) |

# Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `LATENT` | LATENT | Um tensor latente preenchido com zeros, representando um espaço latente de vídeo vazio com as dimensões, comprimento e tamanho de lote especificados. A forma do tensor é [batch_size, 16, lat_t, altura/8, largura/8], onde lat_t é calculado a partir do comprimento. |

---
**Source fingerprint (SHA-256):** `5ae25e2ccb24e627eae583d14c5bcba8b576a227b7a489f3cd4bc56738928513`
