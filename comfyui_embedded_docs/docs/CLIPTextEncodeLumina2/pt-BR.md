# Codificação de Texto CLIP para Lumina2

Este nó codifica um prompt de sistema e um prompt de usuário usando um modelo CLIP em um embedding que pode ser usado para guiar o modelo de difusão na geração de imagens específicas. Ele combina um prompt de sistema Lumina 2 pré-definido com seu prompt de texto personalizado e os processa por meio do modelo CLIP para criar dados de condicionamento para a geração de imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt_do_sistema` | A Lumina2 fornece dois tipos de prompts de sistema: Superior: Você é um assistente projetado para gerar imagens superiores com o mais alto grau de alinhamento imagem-texto com base em prompts textuais ou prompts de usuário. Alinhamento: Você é um assistente projetado para gerar imagens de alta qualidade com o mais alto grau de alinhamento imagem-texto com base em prompts textuais. | COMBO | Sim | `"superior"`<br>`"alignment"` |
| `prompt_do_usuário` | O texto a ser codificado. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | N/A |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | N/A |

**Nota:** A entrada `clip` é obrigatória e não pode ser None. Se a entrada clip for inválida, o nó gerará um erro indicando que o checkpoint pode não conter um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c7540e6232c93b0f76c4903f5646e00a639ccb0b7720f70b5ac727513358a02`
