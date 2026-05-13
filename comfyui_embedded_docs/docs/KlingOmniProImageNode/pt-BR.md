> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/pt-BR.md)

O nó Kling Omni Image (Pro) cria ou edita imagens usando o modelo de IA Kling mais recente. Ele gera imagens com base em uma descrição textual e pode opcionalmente usar imagens de referência para orientar o estilo ou conteúdo. O nó envia uma solicitação para uma API externa, que processa a tarefa e retorna a(s) imagem(ns) final(is).

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `model_name` | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-image-o1"` | O modelo Kling AI específico a ser usado para geração de imagens. |
| `prompt` | STRING | Sim | - | Um prompt textual descrevendo o conteúdo da imagem. Pode incluir descrições positivas e negativas. O texto deve ter entre 1 e 2500 caracteres. |
| `resolution` | COMBO | Sim | `"1K"`<br>`"2K"`<br>`"4K"` | A resolução alvo para a imagem gerada. Observação: a resolução 4K não é suportada para o modelo `kling-image-o1`. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"21:9"` | A proporção de aspecto desejada (largura para altura) para a imagem gerada. |
| `quantidade_de_séries` | COMBO | Sim | `"disabled"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"` | Gera uma série de imagens. Este recurso não é suportado para o modelo `kling-image-o1`. (padrão: "disabled") |
| `reference_images` | IMAGE | Não | - | Até 10 imagens de referência adicionais. Cada imagem deve ter pelo menos 300 pixels de largura e altura, e sua proporção de aspecto deve estar entre 1:2,5 e 2,5:1. |
| `semente` | INT | Não | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
| :--- | :--- | :--- |
| `image` | IMAGE | A(s) imagem(ns) final(is) gerada(s) ou editada(s) pelo modelo Kling AI. Se uma série foi solicitada, múltiplas imagens são retornadas como um lote. |

---
**Source fingerprint (SHA-256):** `7bbed260436bc60e284c99e091cd28b2b0cf50e98e876f94278f1ac2834e61f8`
