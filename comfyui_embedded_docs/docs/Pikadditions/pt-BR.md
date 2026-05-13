> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/pt-BR.md)

O nó Pikadditions permite adicionar qualquer objeto ou imagem ao seu vídeo. Você envia um vídeo e especifica o que deseja adicionar para criar um resultado perfeitamente integrado. Este nó utiliza a API Pika para inserir imagens em vídeos com uma integração de aparência natural.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `video` | VIDEO | Sim | - | O vídeo ao qual será adicionada uma imagem. |
| `image` | IMAGE | Sim | - | A imagem a ser adicionada ao vídeo. |
| `prompt_text` | STRING | Sim | - | Descrição textual do que adicionar ao vídeo. |
| `negative_prompt` | STRING | Sim | - | Descrição textual do que evitar no vídeo. |
| `seed` | INT | Sim | 0 a 4294967295 | Valor de semente aleatório para resultados reproduzíveis. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo processado com a imagem inserida. |

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
