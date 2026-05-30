> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/en.md)

## Visão Geral

O nó Selecionar Dispositivo CLIP permite que você escolha em qual dispositivo (CPU ou uma GPU específica) o codificador de texto CLIP será executado. Por padrão, o dispositivo é atribuído pelo carregador de modelo, mas você pode substituí-lo para usar a CPU ou uma GPU específica. Se o dispositivo solicitado não existir em sua máquina, o nó simplesmente passa o CLIP adiante sem alterações e registra uma mensagem em vez de causar um erro.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | | O codificador de texto CLIP a ser atribuído a um dispositivo específico. |
| `device` | COMBO | Sim | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` | O dispositivo no qual colocar o codificador de texto CLIP. `"default"` restaura o dispositivo atribuído pelo carregador. `"cpu"` fixa tanto o dispositivo de carregamento quanto o de descarregamento na CPU. `"gpu:N"` fixa o dispositivo de carregamento na N-ésima GPU disponível (padrão: `"default"`). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `clip` | CLIP | O codificador de texto CLIP atribuído ao dispositivo selecionado, ou o CLIP original passado adiante sem alterações se o dispositivo solicitado não estiver disponível. |

---
**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`
