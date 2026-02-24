> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/pt-BR.md)

O nó Wan22ImageToVideoLatent cria representações latentes de vídeo a partir de imagens. Ele gera um espaço latente de vídeo em branco com dimensões especificadas e pode, opcionalmente, codificar uma sequência de imagem inicial nos quadros iniciais. Quando uma imagem inicial é fornecida, ela codifica a imagem no espaço latente e cria uma máscara de ruído correspondente para as regiões a serem preenchidas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Não | 32 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 1280, passo: 32) |
| `height` | INT | Não | 32 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 704, passo: 32) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | O número de quadros na sequência de vídeo (padrão: 49, passo: 4) |
| `batch_size` | INT | Não | 1 a 4096 | O número de lotes a serem gerados (padrão: 1) |
| `start_image` | IMAGE | Não | - | Sequência de imagem inicial opcional para codificar no latente do vídeo |

**Observação:** Quando `start_image` é fornecido, o nó codifica a sequência de imagem nos quadros iniciais do espaço latente e gera uma máscara de ruído correspondente. Os parâmetros de largura e altura devem ser divisíveis por 16 para as dimensões adequadas do espaço latente.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | A representação latente de vídeo gerada |
| `noise_mask` | LATENT | A máscara de ruído que indica quais regiões devem ser desruídas durante a geração |
