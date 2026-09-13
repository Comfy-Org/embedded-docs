# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent cria representações latentes de vídeo a partir de imagens. Ele gera um espaço latente de vídeo em branco com a largura, altura, comprimento de quadros e tamanho de lote especificados e, opcionalmente, pode codificar uma sequência de imagens inicial nos primeiros quadros. Quando uma imagem inicial é fornecida, o nó a codifica no espaço latente e cria uma máscara de ruído correspondente que marca quais regiões devem ter o ruído removido durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente | VAE | Sim | - |
| `width` | A largura do vídeo de saída em pixels (padrão: 1280, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `height` | A altura do vídeo de saída em pixels (padrão: 704, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `length` | O número de quadros na sequência de vídeo (padrão: 49, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `batch_size` | O número de latentes de vídeo a gerar (padrão: 1) | INT | Sim | 1 a 4096 |
| `start_image` | Sequência de imagens inicial opcional a ser codificada nos primeiros quadros do latente de vídeo (usa os primeiros `length` quadros) | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, a sequência de imagens é ampliada para a `width` e a `height` de destino, codificada com o VAE e colocada nos primeiros quadros do latente. A máscara de ruído para esses quadros é definida como 0 (preservados), enquanto os quadros restantes têm um valor de máscara 1 (para ter o ruído removido). O latente sempre tem 48 canais, dimensões espaciais de `height / 16` por `width / 16` e uma dimensão temporal de `((length - 1) // 4) + 1`. `width` e `height` devem ser divisíveis por 16 (garantido pelo passo de 32), e `length` aumenta a dimensão temporal em passos de 4.

Quando `start_image` não é fornecido, um latente totalmente em branco é retornado sem máscara de ruído, e a entrada `batch_size` não é aplicada a esse latente em branco.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | A representação latente de vídeo gerada, repetida para cada item do lote | LATENT |
| `noise_mask` | A máscara de ruído que indica quais regiões devem ter o ruído removido (valor 1) e quais mantêm a imagem inicial codificada (valor 0) | LATENT |

Ambos os campos são retornados juntos dentro de uma única saída LATENT.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
