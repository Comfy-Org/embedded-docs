> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/pt-BR.md)

O nó EmptyChromaRadianceLatentImage cria uma imagem latente em branco com dimensões especificadas para uso em fluxos de trabalho de radiância cromática. Ele gera um tensor preenchido com zeros que serve como ponto de partida para operações no espaço latente. O nó permite definir a largura, altura e tamanho do lote da imagem latente vazia.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `width` | INT | Sim | 16 a MAX_RESOLUTION | A largura da imagem latente em pixels (padrão: 1024, deve ser divisível por 16) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | A altura da imagem latente em pixels (padrão: 1024, deve ser divisível por 16) |
| `batch_size` | INT | Não | 1 a 4096 | O número de imagens latentes a serem geradas em um lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `samples` | LATENT | O tensor de imagem latente vazia gerado com as dimensões especificadas |

---
**Source fingerprint (SHA-256):** `f2bc90a236f91e0161142f5242647d15adc8a10c57c920d2eb97e87040ac99d4`
