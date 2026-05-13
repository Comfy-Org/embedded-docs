> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/pt-BR.md)

Gera um vídeo de transição entre duas imagens de entrada usando a API PixVerse. Você fornece uma imagem inicial e uma imagem final, e o nó cria um vídeo suave que faz a transição de uma para a outra, guiado pelo seu prompt de texto e configurações escolhidas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | Sim | - | A imagem inicial para a transição do vídeo |
| `last_frame` | IMAGE | Sim | - | A imagem final para a transição do vídeo |
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: string vazia) |
| `quality` | COMBO | Sim | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` | Configuração de qualidade do vídeo (padrão: `"540p"`) |
| `duration_seconds` | COMBO | Sim | `5`<br>`8` | Duração do vídeo em segundos |
| `motion_mode` | COMBO | Sim | `"normal"`<br>`"fast"` | Estilo de movimento para a transição (padrão: `"normal"`) |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para a geração do vídeo (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) |

**Observação sobre restrições de parâmetros:** Ao usar qualidade 1080p, o modo de movimento é automaticamente definido como `"normal"` e a duração é limitada a 5 segundos. Para qualquer duração diferente de 5 segundos, o modo de movimento também é automaticamente definido como `"normal"`.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo de transição gerado |

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
