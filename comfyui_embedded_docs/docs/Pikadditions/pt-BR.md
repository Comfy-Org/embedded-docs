O nó Pikadditions permite adicionar qualquer objeto ou imagem ao seu vídeo. Você envia um vídeo e especifica o que deseja adicionar para criar um resultado perfeitamente integrado. Este nó utiliza a API Pika para inserir imagens em vídeos com uma integração de aparência natural.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `video` | O vídeo ao qual será adicionada uma imagem. | VIDEO | Sim | - |
| `image` | A imagem a ser adicionada ao vídeo. | IMAGE | Sim | - |
| `prompt_text` | Descrição textual do que adicionar ao vídeo. | STRING | Sim | - |
| `negative_prompt` | Descrição textual do que evitar no vídeo. | STRING | Sim | - |
| `seed` | Valor de semente aleatório para resultados reproduzíveis. | INT | Sim | 0 a 4294967295 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo processado com a imagem inserida. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cf7bb4ee0a672e20c0ffc128fa95df43e05356aea03b2070f928a0263aff6234`
