# Wan22ImageToVideoLatent

O nó Wan22ImageToVideoLatent cria representações latentes de vídeo a partir de imagens. Ele gera um espaço latente de vídeo em branco com dimensões especificadas e pode, opcionalmente, codificar uma sequência de imagem inicial nos primeiros quadros. Quando uma imagem inicial é fornecida, o nó codifica a imagem no espaço latente e cria uma máscara de ruído correspondente para as regiões com inpainting.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 1280, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 704, passo: 32) | INT | Sim | 32 a MAX_RESOLUTION |
| `duração` | O número de quadros na sequência de vídeo (padrão: 49, passo: 4) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de lotes a serem gerados (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Sequência de imagem inicial opcional para codificar no vídeo latente | IMAGE | Não | - |

**Observação:** Quando `start_image` é fornecido, o nó codifica a sequência de imagem nos primeiros quadros do espaço latente e gera uma máscara de ruído correspondente. Os parâmetros de largura e altura devem ser divisíveis por 16 para dimensões adequadas do espaço latente. O parâmetro `length` determina o número de quadros no vídeo latente; a dimensão temporal do espaço latente é calculada como `((length - 1) // 4) + 1`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | A representação latente do vídeo gerado | LATENT |
| `noise_mask` | A máscara de ruído que indica quais regiões devem ser removidas de ruído durante a geração | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
