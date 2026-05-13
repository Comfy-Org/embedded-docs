> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2StartEndToVideoNode/en.md)

Este nó gera um vídeo interpolando entre um quadro inicial e um quadro final fornecidos, guiado por um prompt de texto. Ele usa um modelo Vidu especificado para criar uma transição suave entre as duas imagens ao longo de uma duração definida.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"viduq2-pro-fast"`<br>`"viduq2-pro"`<br>`"viduq2-turbo"` | O modelo Vidu a ser usado para geração de vídeo. |
| `quadro_inicial` | IMAGE | Sim | - | A imagem inicial para a sequência de vídeo. Apenas uma única imagem é permitida. |
| `quadro_final` | IMAGE | Sim | - | A imagem final para a sequência de vídeo. Apenas uma única imagem é permitida. |
| `prompt` | STRING | Sim | - | Uma descrição textual que guia a geração do vídeo (máximo de 2000 caracteres). |
| `duração` | INT | Não | 2 a 8 | A duração do vídeo gerado em segundos (padrão: 5). |
| `semente` | INT | Não | 0 a 2147483647 | Um número usado para inicializar a geração aleatória para resultados reproduzíveis (padrão: 1). |
| `resolução` | COMBO | Não | `"720p"`<br>`"1080p"` | A resolução de saída do vídeo gerado. |
| `amplitude_de_movimento` | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | A amplitude de movimento dos objetos no quadro. |

**Nota:** As imagens `first_frame` e `end_frame` devem ter proporções de aspecto semelhantes. O nó validará se suas proporções estão dentro de uma faixa relativa de 0,8 a 1,25.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `0a2a125fcb0a519e3aa98ed846f0c7bdc14644a27aaaab3953d55945f787de2a`
