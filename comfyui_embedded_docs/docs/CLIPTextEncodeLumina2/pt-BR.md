> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeLumina2/pt-BR.md)

O nó CLIP Text Encode for Lumina2 codifica um prompt de sistema e um prompt do usuário usando um modelo CLIP em um *embedding* que pode orientar o modelo de difusão para gerar imagens específicas. Ele combina um prompt de sistema predefinido com seu prompt de texto personalizado e os processa através do modelo CLIP para criar dados de condicionamento para a geração de imagens.

## Entradas

| Parâmetro | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `system_prompt` | STRING | COMBO | - | "superior", "alignment" | O Lumina2 fornece dois tipos de prompts de sistema: Superior: Você é um assistente projetado para gerar imagens superiores com o grau superior de alinhamento imagem-texto com base em prompts textuais ou prompts do usuário. Alignment: Você é um assistente projetado para gerar imagens de alta qualidade com o maior grau de alinhamento imagem-texto com base em prompts textuais. |
| `user_prompt` | STRING | STRING | - | - | O texto a ser codificado. |
| `clip` | CLIP | CLIP | - | - | O modelo CLIP usado para codificar o texto. |

**Observação:** A entrada `clip` é obrigatória e não pode ser None. Se a entrada clip for inválida, o nó gerará um erro indicando que o *checkpoint* pode não conter um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Um condicionamento contendo o texto incorporado usado para orientar o modelo de difusão. |
