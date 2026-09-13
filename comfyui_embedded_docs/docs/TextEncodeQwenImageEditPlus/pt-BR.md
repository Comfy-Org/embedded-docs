# TextEncodeQwenImageEditPlus

O nó TextEncodeQwenImageEditPlus processa um prompt de texto e até três imagens opcionais para produzir dados de condicionamento para tarefas de geração ou edição de imagens. Ele usa um template especializado que primeiro solicita ao modelo que descreva as principais características das imagens de entrada e, em seguida, explique como a instrução de texto do usuário deve alterá-las, para que o resultado codificado compreenda tanto as imagens quanto a modificação solicitada. Quando um VAE é fornecido, o nó também cria latents de referência a partir das imagens de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `prompt` | Instrução de texto descrevendo a modificação de imagem desejada (suporta entrada multilinha e prompts dinâmicos) | STRING | Sim | - |
| `vae` | Modelo VAE opcional para gerar latents de referência a partir das imagens de entrada | VAE | Não | - |
| `image1` | Primeira imagem de entrada opcional para análise e modificação | IMAGE | Não | - |
| `image2` | Segunda imagem de entrada opcional para análise e modificação | IMAGE | Não | - |
| `image3` | Terceira imagem de entrada opcional para análise e modificação | IMAGE | Não | - |

**Nota:** Quando um VAE é fornecido, o nó gera latents de referência a partir de todas as imagens de entrada fornecidas. Até três imagens podem ser processadas de uma vez. As imagens são redimensionadas para uma área alvo de 384x384 pixels (proporção preservada) para processamento de visão-linguagem, e para dimensões divisíveis por 8 (com uma área alvo de 1024x1024 pixels) para codificação VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento codificados contendo tokens de texto e latents de referência opcionais para geração de imagens | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
