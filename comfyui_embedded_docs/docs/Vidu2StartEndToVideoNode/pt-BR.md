Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/en.md)

Este nó gera um vídeo interpolando entre um quadro inicial e um quadro final fornecidos, guiado por um prompt de texto. Ele usa um modelo Vidu especificado para criar uma transição suave entre as duas imagens ao longo de uma duração definida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo Vidu a ser usado para geração de vídeo. | COMBO | Sim | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` |
| `quadro_inicial` | A imagem inicial para a sequência de vídeo. Apenas uma única imagem é permitida. | IMAGE | Sim | - |
| `quadro_final` | A imagem final para a sequência de vídeo. Apenas uma única imagem é permitida. | IMAGE | Sim | - |
| `prompt` | Uma descrição textual que guia a geração do vídeo (máximo de 2000 caracteres). | STRING | Sim | - |
| `duração` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Não | 2 a 8 |
| `semente` | Um número usado para inicializar a geração aleatória para resultados reproduzíveis (padrão: 1). | INT | Não | 0 a 2147483647 |
| `resolução` | A resolução de saída do vídeo gerado. | COMBO | Não | `"720p"`<br>`"1080p"` |
| `amplitude_de_movimento` | A amplitude de movimento dos objetos no quadro. | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**Nota:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes. O nó validará se suas proporções estão dentro de uma faixa relativa de 0,8 a 1,25.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
