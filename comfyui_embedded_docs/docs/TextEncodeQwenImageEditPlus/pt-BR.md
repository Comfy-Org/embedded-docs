# TextEncodeQwenImageEditPlus

O nó TextEncodeQwenImageEditPlus processa prompts de texto e imagens opcionais para gerar dados de conditioning para tarefas de geração ou edição de imagens. Ele usa um template especializado para analisar as imagens de entrada e entender como as instruções de texto devem modificá-las, em seguida, codifica essas informações para uso nas etapas subsequentes de geração. O nó pode processar até três imagens de entrada e, opcionalmente, gerar latents de referência quando um VAE é fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `prompt` | Instrução de texto que descreve a modificação desejada da imagem (suporta entrada multilinha e prompts dinâmicos) | STRING | Sim | - |
| `vae` | Modelo VAE opcional para gerar latents de referência a partir das imagens de entrada | VAE | Não | - |
| `image1` | Primeira imagem de entrada opcional para análise e modificação | IMAGE | Não | - |
| `image2` | Segunda imagem de entrada opcional para análise e modificação | IMAGE | Não | - |
| `image3` | Terceira imagem de entrada opcional para análise e modificação | IMAGE | Não | - |

**Observação:** Quando um VAE é fornecido, o nó gera latents de referência a partir de todas as imagens de entrada fornecidas. Até três imagens podem ser processadas de uma vez. As imagens são redimensionadas para uma área alvo de 384x384 pixels (proporção de aspecto preservada) para processamento de visão-linguagem, e para dimensões divisíveis por 8 (com uma área alvo de 1024x1024 pixels) para codificação pelo VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Dados de conditioning codificados contendo tokens de texto e latents de referência opcionais para geração de imagens | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
