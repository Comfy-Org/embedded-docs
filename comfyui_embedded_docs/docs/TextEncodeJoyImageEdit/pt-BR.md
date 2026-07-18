# TextEncodeJoyImageEdit

Este nó codifica um prompt de texto e imagens opcionais em dados de condicionamento para uso com modelos JoyImage. Ele combina um codificador de texto CLIP com entradas de imagem opcionais para criar um condicionamento rico que pode guiar tarefas de geração ou edição de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `clip` | O modelo CLIP usado para codificar o prompt de texto | CLIP | Sim | - |
| `prompt` | O prompt de texto a ser codificado, suportando entrada multilinha e prompts dinâmicos | STRING | Sim | - |
| `vae` | Um modelo VAE para codificar imagens no espaço latente (opcional) | VAE | Não | - |
| `images` | Uma ou mais imagens a serem incluídas no condicionamento, até o máximo de 6 imagens | IMAGE | Não | 0 a 6 imagens |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `CONDITIONING` | Os dados de condicionamento codificados combinando o prompt de texto e quaisquer imagens fornecidas | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
