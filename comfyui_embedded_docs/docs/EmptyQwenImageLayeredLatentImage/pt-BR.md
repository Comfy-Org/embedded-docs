> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/pt-BR.md)

O nó **Empty Qwen Image Layered Latent** cria uma representação latente em branco e multicamadas para uso com modelos de imagem Qwen. Ele gera um tensor preenchido com zeros, estruturado com um número especificado de camadas, tamanho do lote e dimensões espaciais. Este latente vazio serve como ponto de partida para fluxos de trabalho subsequentes de geração ou manipulação de imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | Sim | 16 a MAX_RESOLUTION | A largura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) |
| `height` | INT | Sim | 16 a MAX_RESOLUTION | A altura da imagem latente a ser criada. O valor deve ser divisível por 16. (padrão: 640) |
| `layers` | INT | Sim | 0 a MAX_RESOLUTION | O número de camadas adicionais a serem adicionadas à estrutura latente. Isso define a profundidade da representação latente. (padrão: 3) |
| `batch_size` | INT | Não | 1 a 4096 | O número de amostras latentes a serem geradas em um lote. (padrão: 1) |

**Observação:** Os parâmetros `width` e `height` são internamente divididos por 8 para determinar as dimensões espaciais do tensor latente de saída.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | Um tensor latente preenchido com zeros. Sua forma é `[batch_size, 16, layers + 1, height // 8, width // 8]`. |
