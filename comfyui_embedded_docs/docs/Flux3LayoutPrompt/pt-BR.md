# FLUX 3 Image Layout Prompt

Constrói a tabela de layout que o FLUX 3 Image lê a partir de um prompt. Ela pega os elementos desenhados no nó Create Bounding Boxes e os anexa ao seu prompt como uma lista de caixas, cada uma com um id, suas coordenadas e sua descrição. Cite uma caixa no prompt como `<obj_N>` para vincular palavras àquela região e, em seguida, conecte a saída à entrada de prompt do nó FLUX 3 Image. Sem elementos conectados, o prompt é retornado inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | O texto do prompt. Cite a caixa N como `<obj_N>` para vincular palavras a ela. | STRING | Sim | - |
| `element` | Os elementos a serem posicionados no layout, obtidos do nó Create Bounding Boxes. Paletas de cores não são usadas, então descreva as cores na descrição. | ARRAY | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `prompt` | O prompt com a tabela de layout de caixas anexada, pronto para ser enviado ao nó FLUX 3 Image. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`
