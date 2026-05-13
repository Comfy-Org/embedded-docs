> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/pt-BR.md)

O nó CosmosImageToVideoLatent cria representações latentes de vídeo a partir de imagens de entrada. Ele gera um latente de vídeo em branco e, opcionalmente, codifica imagens de início e/ou fim nos quadros iniciais e/ou finais da sequência de vídeo. Quando imagens são fornecidas, ele também cria máscaras de ruído correspondentes para indicar quais partes do latente devem ser preservadas durante a geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `vae` | VAE | Sim | - | O modelo VAE usado para codificar imagens no espaço latente |
| `largura` | INT | Sim | 16 a MAX_RESOLUTION | A largura do vídeo de saída em pixels (padrão: 1280) |
| `altura` | INT | Sim | 16 a MAX_RESOLUTION | A altura do vídeo de saída em pixels (padrão: 704) |
| `comprimento` | INT | Sim | 1 a MAX_RESOLUTION | O número de quadros na sequência de vídeo (padrão: 121) |
| `tamanho_do_lote` | INT | Sim | 1 a 4096 | O número de lotes latentes a serem gerados (padrão: 1) |
| `imagem_inicial` | IMAGE | Não | - | Imagem opcional para codificar no início da sequência de vídeo |
| `imagem_final` | IMAGE | Não | - | Imagem opcional para codificar no final da sequência de vídeo |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó retorna um latente em branco sem nenhuma máscara de ruído. Quando qualquer imagem é fornecida, as seções correspondentes do latente são codificadas e mascaradas adequadamente.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `latent` | LATENT | A representação latente de vídeo gerada, com imagens codificadas opcionais e máscaras de ruído correspondentes |

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
