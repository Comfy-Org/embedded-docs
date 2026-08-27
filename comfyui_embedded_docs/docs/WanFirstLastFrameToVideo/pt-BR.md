# WanFirstLastFrameToVideo

O nó WanFirstLastFrameToVideo prepara o condicionamento para geração de vídeo combinando um quadro inicial e um quadro final com prompts de texto. Ele codifica as imagens dos quadros no espaço latente, cria uma máscara que informa ao modelo de vídeo quais quadros já são conhecidos e anexa características de CLIP vision quando estas são fornecidas. O nó gera condicionamentos positivo e negativo atualizados, além de um latent vazio que define o tamanho e o comprimento do vídeo a ser gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | Condicionamento de texto positivo usado para guiar a geração de vídeo. | CONDITIONING | Sim | - |
| `negativo` | Condicionamento de texto negativo usado para guiar a geração de vídeo. | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar as imagens combinadas dos quadros no espaço latente. | VAE | Sim | - |
| `largura` | Largura do vídeo gerado em pixels (padrão: 832, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | Altura do vídeo gerado em pixels (padrão: 480, passo: 16). | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | Número de quadros na sequência de vídeo (padrão: 81, passo: 4). | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | Número de vídeos a serem gerados de uma vez (padrão: 1). | INT | Sim | 1 a 4096 |
| `clip_vision_start_image` | Características de CLIP vision extraídas da imagem inicial. Se tanto as entradas de CLIP vision inicial quanto final forem fornecidas, suas características são combinadas. | CLIP_VISION_OUTPUT | Não | - |
| `clip_vision_end_image` | Características de CLIP vision extraídas da imagem final. Se tanto as entradas de CLIP vision inicial quanto final forem fornecidas, suas características são combinadas. | CLIP_VISION_OUTPUT | Não | - |
| `imagem_inicial` | Imagem do quadro inicial para a sequência de vídeo. Seus primeiros `length` quadros são usados e redimensionados para `width` × `height`. | IMAGE | Não | - |
| `imagem_final` | Imagem do quadro final para a sequência de vídeo. Seus últimos `length` quadros são usados e redimensionados para `width` × `height`. | IMAGE | Não | - |

**Nota:** Quando pelo menos uma das imagens `start_image` ou `end_image` é fornecida, o nó constrói uma sequência combinada de quadros em que os quadros inicial e final são preenchidos e os quadros restantes usam um espaço reservado de cinza neutro (0.5). Uma máscara marca as regiões preenchidas como conhecidas e as regiões de espaço reservado como desconhecidas, permitindo que o modelo de vídeo gere os quadros intermediários. Quando uma imagem inicial é fornecida, a região conhecida também se estende por 3 quadros extras além da imagem. A mesma imagem de quadro codificada e a máscara são anexadas tanto ao condicionamento `positive` quanto ao `negative`. Se ambas as entradas de CLIP vision forem fornecidas, seus estados ocultos são concatenados; se apenas uma for fornecida, ela é usada isoladamente. O comprimento do vídeo latente é derivado de `length` após a compressão temporal: `((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positivo` | Condicionamento positivo com a imagem do quadro codificada, a máscara e (se fornecidas) as características de CLIP vision anexadas. | CONDITIONING |
| `negativo` | Condicionamento negativo com a imagem do quadro codificada, a máscara e (se fornecidas) as características de CLIP vision anexadas. | CONDITIONING |
| `latente` | Tensor latent vazio (todos os zeros) formatado para o tamanho do lote, o comprimento do vídeo e a resolução fornecidos. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
