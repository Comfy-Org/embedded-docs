# TextEncodeQwenImageEditPlus

O nó TextEncodeQwenImageEditPlus processa prompts de texto e imagens opcionais para gerar dados de condicionamento para tarefas de geração ou edição de imagens. Ele utiliza um template especializado para analisar imagens de entrada e entender como as instruções de texto devem modificá-las, em seguida, codifica essas informações para uso em etapas subsequentes de geração. O nó pode processar até três imagens de entrada e, opcionalmente, gerar latentes de referência quando um VAE é fornecido.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenização e codificação | CLIP | Sim | - |
| `prompt` | Instrução de texto descrevendo a modificação desejada na imagem (suporta entrada multilinha e prompts dinâmicos) | STRING | Sim | - |
| `vae` | Modelo VAE opcional para gerar latentes de referência a partir das imagens de entrada | VAE | Não | - |
| `image1` | Primeira imagem opcional de entrada para análise e modificação | IMAGE | Não | - |
| `image2` | Segunda imagem opcional de entrada para análise e modificação | IMAGE | Não | - |
| `image3` | Terceira imagem opcional de entrada para análise e modificação | IMAGE | Não | - |

**Nota:** Quando um VAE é fornecido, o nó gera latentes de referência a partir de todas as imagens de entrada. O nó pode processar até três imagens simultaneamente. As imagens são redimensionadas automaticamente para 384x384 pixels para processamento visão-linguagem e para dimensões divisíveis por 8 (com uma área alvo de 1024x1024 pixels) para codificação VAE.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Dados de condicionamento codificados contendo tokens de texto e latentes de referência opcionais para geração de imagem | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54889d9a3b70e41d623020f3fd5e3c798c72799492c67a9efd99f543c88bb968`
