# LumaRay32VideoEditNode

Este nó re-renderiza um vídeo existente sob um novo prompt usando o Luma Ray 3.2, permitindo que você reformate, reilumine, adicione ou remova elementos enquanto mantém o movimento original. O vídeo de origem pode ter até 18 segundos, e o vídeo editado mantém a duração original da fonte.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `vídeo` | Vídeo de origem a ser editado. Até 18 segundos. | VIDEO | Sim | - |
| `prompt` | Descreve a edição desejada. | STRING | Sim | - |
| `resolução` | A resolução de saída para o vídeo editado. | COMBO | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `força` | O quanto preservar versus reimaginar a origem. "auto" permite que o Ray 3.2 escolha; adhere_* preserva ao máximo, flex_* é equilibrado, reimagine_* altera mais. (padrão: "auto") | COMBO | Sim | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Semente para reprodutibilidade. | INT | Sim | - |

**Nota:** O `prompt` deve ter entre 1 e 6000 caracteres. O vídeo de origem não deve exceder 18 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `VIDEO` | A saída do vídeo editado. | VIDEO |
| `generation_id` | O identificador único para a solicitação de geração. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
