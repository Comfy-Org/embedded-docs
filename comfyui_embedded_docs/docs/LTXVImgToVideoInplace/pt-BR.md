# LTXVImgToVideoInplace

O nó LTXVImgToVideoInplace condiciona uma representação latente de vídeo codificando uma imagem de entrada em seus quadros iniciais. Ele funciona usando um VAE para codificar a imagem no espaço latente e, em seguida, substituindo os primeiros quadros das amostras de vídeo latente por essa imagem codificada. Uma máscara de ruído é aplicada para que a intensidade do condicionamento controle o quanto a imagem influencia esses quadros iniciais durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem de entrada no espaço latente. | VAE | Sim | - |
| `image` | A imagem de entrada a ser codificada e usada para condicionar o latente de vídeo. | IMAGE | Sim | - |
| `latent` | A representação latente de vídeo de destino a ser modificada. | LATENT | Sim | - |
| `strength` | Controla a intensidade do condicionamento da imagem codificada nos quadros latentes iniciais. Um valor de 1.0 condiciona totalmente os quadros iniciais, enquanto valores menores aplicam um condicionamento mais fraco. (padrão: 1.0) | FLOAT | Não | 0.0 - 1.0 |
| `bypass` | Ignora o condicionamento. Quando ativado, o nó retorna o latente de entrada inalterado. (padrão: False) | BOOLEAN | Não | - |

**Nota:** A `image` será redimensionada automaticamente (interpolação bilinear) para corresponder às dimensões espaciais exigidas pelo `vae` para codificação, com base na largura e altura do latente de entrada `latent`. Apenas os 3 primeiros canais de cor (RGB) da imagem são usados; qualquer canal alfa é ignorado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A representação latente de vídeo modificada. Ela contém as amostras atualizadas e uma `noise_mask` que aplica a intensidade do condicionamento aos quadros iniciais. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
