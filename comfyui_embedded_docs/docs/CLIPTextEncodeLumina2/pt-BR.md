# Codificação de Texto CLIP para Lumina2

O nó CLIP Text Encode for Lumina2 codifica um prompt de sistema e um prompt de usuário usando um modelo CLIP em um embedding que pode guiar o modelo de difusão para gerar imagens específicas. Ele combina um prompt de sistema predefinido com seu prompt de texto personalizado e os processa por meio do modelo CLIP para criar dados de condicionamento para geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `system_prompt` | O Lumina2 fornece dois tipos de prompts de sistema: "superior" gera imagens com alinhamento imagem-texto superior; "alignment" gera imagens de alta qualidade com o maior grau de alinhamento imagem-texto. | COMBO | Sim | `"superior"`<br>`"alignment"` |
| `user_prompt` | O texto a ser codificado. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | N/A |

**Nota:** A entrada `clip` é obrigatória e não pode ser None. Se a entrada clip for inválida, o nó gerará um erro indicando que o checkpoint pode não conter um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
