O nó Empty Qwen Image Layered Latent cria uma representação latente em branco e multicamadas para uso com modelos de imagem Qwen. Ele gera um tensor preenchido com zeros, estruturado com um número específico de camadas, tamanho de lote e dimensões espaciais. Essa latente vazia serve como ponto de partida para fluxos de trabalho subsequentes de geração ou manipulação de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `largura` | A largura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) | INT | Sim | 16 a MAX_RESOLUTION |
| `camadas` | O número de camadas adicionais a serem adicionadas à estrutura latente. Isso define a profundidade da representação latente. (padrão: 3) | INT | Sim | 0 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de amostras latentes a serem geradas em um lote. (padrão: 1) | INT | Não | 1 a 4096 |

**Observação:** Os parâmetros `width` e `height` são internamente divididos por 8 para determinar as dimensões espaciais do tensor latente de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `samples` | Um tensor latente preenchido com zeros. Sua forma é `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `99497e3e4a67bf7b3f650573e7b8eb2d7fad6be5819b7ebbbb8736291dc44e0c`
