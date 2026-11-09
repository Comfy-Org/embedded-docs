# WeVisOne-VL Detect

WeVisOne-VL Detect encontra objetos em uma imagem a partir de um prompt de texto e retorna caixas, máscaras alfa, pontos ou a própria resposta do modelo, dependendo da tarefa escolhida. Ele abrange detecção e segmentação de vocabulário aberto, expressões referenciais, apontamento, contagem e ancoragem OCR, e executa um prompt por imagem no lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O codificador de texto WeVisOne-VL que carrega o checkpoint. | CLIP | Sim | - |
| `image` | A imagem ou o lote de imagens a pesquisar. | IMAGE | Sim | - |
| `task` | O que o nó deve retornar. A segmentação retorna caixas mais máscaras alfa; detection, referring, ocr e ocr_grounding retornam caixas; point e count_point retornam pontos; count_box conta usando caixas; visual_prompt encontra objetos semelhantes às caixas de referência em `bboxes`; freeform envia a consulta sem alterações e retorna apenas texto (padrão: "segmentation"). | COMBO | Sim | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | O que encontrar, em linguagem natural (por exemplo, "a caneca vermelha"). `detection` e `point` leem um rótulo por linha, `count_box` e `count_point` contam o sujeito que você nomear, `ocr_grounding` procura por este texto exato, `visual_prompt` usa `bboxes` em vez disso, e `freeform` o envia como o prompt completo. `ocr` o ignora. | STRING | Sim | - |
| `bboxes` | Caixas de referência que `visual_prompt` usa como exemplos do objeto a ser encontrado. | BOUNDING_BOX | Não | - |
| `individual_masks` | Retorna uma máscara por caixa detectada na saída `bboxes`, quadro a quadro, em vez de uma máscara combinada por quadro (padrão: false). | BOOLEAN | Não | true<br>false |
| `max_length` | Número máximo de tokens que o modelo pode gerar para sua resposta (padrão: 4096). | INT | Sim | 1 a 32768 |

**Observação:** As máscaras só são preenchidas quando o modelo responde com referências de objeto, que é o que a tarefa de segmentação solicita. Outras tarefas retornam caixas, pontos ou texto com uma máscara vazia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `masks` | Máscaras alfa dos objetos encontrados, uma por quadro por padrão ou uma por caixa com `individual_masks`. | MASK |
| `bboxes` | Caixas encontradas em cada imagem, armazenadas como `x`, `y`, `width`, `height` e `label`. | BOUNDING_BOX |
| `points` | Pontos como JSON em pixels, no formato `[{"x", "y", "label", "frame"}]`, preenchidos pelas tarefas `point` e `count_point`. | STRING |
| `text` | A resposta bruta do modelo, uma linha por imagem. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
