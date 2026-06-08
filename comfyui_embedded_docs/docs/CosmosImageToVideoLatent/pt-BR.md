O nó CosmosImageToVideoLatent cria representações latentes de vídeo a partir de imagens de entrada. Ele gera um latente de vídeo em branco e, opcionalmente, codifica imagens de início e/ou fim nos quadros iniciais e/ou finais da sequência de vídeo. Quando imagens são fornecidas, ele também cria máscaras de ruído correspondentes para indicar quais partes do latente devem ser preservadas durante a geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `vae` | O modelo VAE usado para codificar imagens no espaço latente | VAE | Sim | - |
| `largura` | A largura do vídeo de saída em pixels (padrão: 1280) | INT | Sim | 16 a MAX_RESOLUTION |
| `altura` | A altura do vídeo de saída em pixels (padrão: 704) | INT | Sim | 16 a MAX_RESOLUTION |
| `comprimento` | O número de quadros na sequência de vídeo (padrão: 121) | INT | Sim | 1 a MAX_RESOLUTION |
| `tamanho_do_lote` | O número de lotes latentes a serem gerados (padrão: 1) | INT | Sim | 1 a 4096 |
| `imagem_inicial` | Imagem opcional para codificar no início da sequência de vídeo | IMAGE | Não | - |
| `imagem_final` | Imagem opcional para codificar no final da sequência de vídeo | IMAGE | Não | - |

**Observação:** Quando nem `start_image` nem `end_image` são fornecidos, o nó retorna um latente em branco sem nenhuma máscara de ruído. Quando qualquer imagem é fornecida, as seções correspondentes do latente são codificadas e mascaradas adequadamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latent` | A representação latente de vídeo gerada, com imagens codificadas opcionais e máscaras de ruído correspondentes | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `31ce4dc577c672e0b3dc0bfb6644b2ef7ab737f6c4ee5e0677973b6a4efdd66d`
