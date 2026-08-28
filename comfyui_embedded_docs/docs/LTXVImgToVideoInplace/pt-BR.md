# LTXVImgToVideoInplace

LTXVImgToVideoInplace codifica uma imagem de entrada no espaço latente e coloca esses quadros codificados no início de um vídeo latente existente. O valor `strength` controla a força com que a imagem codificada condiciona esses quadros iniciais e, quando `bypass` está habilitado, o latente de entrada é retornado inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem de entrada no espaço latente. | VAE | Sim | - |
| `image` | A imagem de entrada a ser codificada e usada para condicionar o vídeo latente. | IMAGE | Sim | - |
| `latent` | A representação de vídeo latente de destino a ser modificada. | LATENT | Sim | - |
| `strength` | Controla a força com que a imagem codificada condiciona os quadros iniciais do latente. Um valor de 1.0 condiciona totalmente os quadros iniciais com a imagem codificada, enquanto valores menores os condicionam com menos intensidade. A máscara de ruído para os quadros iniciais é definida como `1.0 - strength`. (padrão: 1.0) | FLOAT | Não | 0.0 - 1.0 |
| `bypass` | Ignora o condicionamento. Quando habilitado, o nó retorna o latente de entrada inalterado. (padrão: False) | BOOLEAN | Não | True or False |

**Nota:** A `image` será redimensionada automaticamente para corresponder às dimensões espaciais exigidas pelo `vae` para codificação, com base na largura e altura do latente de entrada `latent`. Somente os canais RGB da `image` são usados para codificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A representação de vídeo latente resultante. Quando o bypass está desabilitado, ela contém os `samples` atualizados e um `noise_mask` que aplica a força de condicionamento aos quadros iniciais. Quando o bypass está habilitado, é o latente de entrada retornado inalterado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideoInplace/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69faa4b2e7b0fedeee531dc5a8809e23a79c9ce03e9760afb865160594fef30d`
