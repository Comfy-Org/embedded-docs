# Codificação de Texto CLIP para Lumina2

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/en.md)

O nó CLIP Text Encode for Lumina2 codifica um prompt de sistema e um prompt de usuário usando um modelo CLIP em uma incorporação que pode guiar o modelo de difusão para gerar imagens específicas. Ele combina um prompt de sistema predefinido com seu prompt de texto personalizado e os processa através do modelo CLIP para criar dados de condicionamento para a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt_do_sistema` | O Lumina2 oferece dois tipos de prompts de sistema: "superior" gera imagens com alinhamento superior entre imagem e texto; "alignment" gera imagens de alta qualidade com o mais alto grau de alinhamento entre imagem e texto. | STRING | Sim | `"superior"`<br>`"alignment"` |
| `prompt_do_usuário` | O texto a ser codificado. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | N/A |

**Nota:** A entrada `clip` é obrigatória e não pode ser Nula. Se a entrada clip for inválida, o nó gerará um erro indicando que o checkpoint pode não conter um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fcc0802180ffc2c0757b395850d54632da011473da0c6b1c5268b42da3747024`
