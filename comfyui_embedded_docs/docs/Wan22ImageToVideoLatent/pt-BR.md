# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent cria representações latentes de vídeo a partir de imagens. Ele gera um espaço latente de vídeo em branco com a largura, altura, comprimento de quadro e tamanho de lote especificados, e pode opcionalmente codificar uma sequência de imagens inicial nos quadros iniciais. Quando uma imagem inicial é fornecida, o nó a codifica no espaço latente e cria uma máscara de ruído correspondente que indica quais regiões devem ter o ruído removido durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar a imagem inicial no espaço latente | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 1280, passo: 32) | INT | Sim | 32 to MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 704, passo: 32) | INT | Sim | 32 to MAX_RESOLUTION |
| `duração` | O número de quadros na sequência de vídeo (padrão: 49, passo: 4) | INT | Sim | 1 to MAX_RESOLUTION |
| `tamanho_do_lote` | O número de latentes de vídeo a serem gerados (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Sequência de imagens inicial opcional para codificar nos quadros iniciais do latente de vídeo (usa os primeiros `length` quadros) | IMAGE | Não | - |

**Nota:** Quando `start_image` é fornecido, a sequência de imagens é redimensionada para a `width` e `height` alvo, codificada com o VAE e colocada nos primeiros quadros do latente. A máscara de ruído desses quadros é definida como 0 (preservado), enquanto os quadros restantes têm valor de máscara 1 (para terem o ruído removido). O latente sempre tem 48 canais, dimensões espaciais de `height / 16` por `width / 16` e uma dimensão temporal de `((length - 1) // 4) + 1`. `width` e `height` devem ser divisíveis por 16 (garantido pelo passo de 32), e `length` aumenta a dimensão temporal em passos de 4.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | A representação latente de vídeo gerada, repetida para cada item do lote | LATENT |
| `noise_mask` | A máscara de ruído que indica quais regiões devem ter o ruído removido (valor 1) e quais preservam a imagem inicial codificada (valor 0) | LATENT |

Ambos os campos são retornados juntos em uma única saída LATENT.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
