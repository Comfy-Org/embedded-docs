> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/pt-BR.md)

O nó CosmosImageToVideoLatent cria representações latentes de vídeo a partir de imagens de entrada. Ele gera um latente de vídeo em branco e, opcionalmente, codifica imagens de início e/ou fim nos quadros iniciais e/ou finais da sequência de vídeo. Quando as imagens são fornecidas, ele também cria máscaras de ruído correspondentes para indicar quais partes do latente devem ser preservadas durante a geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Range | Descrição |
|-----------|-----------|----------|-------|-------------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens no espaço latente |
| `width` | INT | Não | 16 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 1280) |
| `height` | INT | Não | 16 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 704) |
| `length` | INT | Não | 1 a MAX_RESOLUTION | O número de quadros na sequência de vídeo (padrão: 121) |
| `batch_size` | INT | Não | 1 a 4096 | O número de lotes latentes a serem gerados (padrão: 1) |
| `start_image` | IMAGE | Não | - | Imagem opcional para codificar no início da sequência de vídeo |
| `end_image` | IMAGE | Não | - | Imagem opcional para codificar no final da sequência de vídeo |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó retorna um latente em branco sem qualquer máscara de ruído. Quando qualquer uma das imagens é fornecida, as seções correspondentes do latente são codificadas e mascaradas de acordo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `latent` | LATENT | A representação latente de vídeo gerada, com imagens codificadas opcionais e máscaras de ruído correspondentes |
