> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/pt-BR.md)

O nó Reve Image Remix utiliza a API Reve para gerar uma nova imagem. Ele combina uma ou mais imagens de referência com um prompt de texto para criar uma nova imagem remixada com base na descrição fornecida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `reference_images` | IMAGE | Sim | 1 a 6 imagens | Uma ou mais imagens de referência para usar como base para o remix. Você pode adicionar entre 1 e 6 imagens. |
| `prompt` | STRING | Sim | 1 a 2560 caracteres | Uma descrição textual da imagem desejada. Você pode incluir tags XML `<img>` para referenciar imagens específicas pelo seu índice (ex.: `<img>0</img>`, `<img>1</img>`). (padrão: vazio) |
| `model` | COMBO | Sim | `reve-remix@20250915`<br>`reve-remix-fast@20251030` | A versão do modelo a ser usada para o remix. Cada opção de modelo inclui proporções de aspecto configuráveis e escalonamento em tempo de teste. |
| `upscale` | COMBO | Não | `"disabled"`<br>`"enabled"` | Controla se a imagem gerada será ampliada. Quando ativado, você pode selecionar um fator de ampliação. |
| `remove_background` | BOOLEAN | Não | `true`<br>`false` | Quando ativado, tenta remover o fundo da imagem gerada. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente. Alterar este valor fará com que o nó seja executado novamente, mas os resultados são não determinísticos independentemente da semente. (padrão: 0) |

**Nota:** O parâmetro `model` é uma combinação dinâmica que inclui configurações aninhadas para `aspect_ratio` (opções: "auto", "16:9", "9:16", "3:2", "2:3", "4:3", "3:4", "1:1") e `test_time_scaling`. O parâmetro `upscale`, quando definido como "enabled", revela uma configuração aninhada `upscale_factor`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A nova imagem gerada pelo processo de remix do Reve. |

---
**Source fingerprint (SHA-256):** `e64dccddfd55ebaa7e28bf17c2a5ff1a0c130db1475e307940b75106c788f687`
