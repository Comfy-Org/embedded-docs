Gera um vídeo de transição entre duas imagens de entrada usando a API PixVerse. Você fornece uma imagem inicial e uma imagem final, e o nó cria um vídeo suave que faz a transição de uma para a outra, guiado pelo seu prompt de texto e configurações escolhidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `first_frame` | A imagem inicial para a transição do vídeo | IMAGE | Sim | - |
| `last_frame` | A imagem final para a transição do vídeo | IMAGE | Sim | - |
| `prompt` | Prompt para a geração do vídeo (padrão: string vazia) | STRING | Sim | - |
| `quality` | Configuração de qualidade do vídeo (padrão: `"540p"`) | COMBO | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duration_seconds` | Duração do vídeo em segundos | COMBO | Sim | `5`<br>`8` |
| `motion_mode` | Estilo de movimento para a transição (padrão: `"normal"`) | COMBO | Sim | `"normal"`<br>`"fast"` |
| `seed` | Semente para a geração do vídeo (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) | STRING | Não | - |

**Observação sobre restrições de parâmetros:** Ao usar qualidade 1080p, o modo de movimento é automaticamente definido como `"normal"` e a duração é limitada a 5 segundos. Para qualquer duração diferente de 5 segundos, o modo de movimento também é automaticamente definido como `"normal"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O vídeo de transição gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
