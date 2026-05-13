> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/pt-BR.md)

O nó Vidu Start End To Video Generation cria um vídeo gerando quadros entre um quadro inicial e um quadro final. Ele usa um prompt de texto para orientar o processo de geração de vídeo e suporta vários modelos de vídeo com diferentes configurações de resolução e movimento. O nó valida se os quadros inicial e final têm proporções de aspecto compatíveis antes do processamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | `"viduq1"` | Nome do modelo |
| `quadro inicial` | IMAGE | Sim | - | Quadro inicial |
| `quadro final` | IMAGE | Sim | - | Quadro final |
| `prompt` | STRING | Não | - | Uma descrição textual para a geração do vídeo |
| `duração` | INT | Não | 5-5 | Duração do vídeo de saída em segundos (padrão: 5, fixado em 5 segundos) |
| `semente` | INT | Não | 0-2147483647 | Semente para a geração do vídeo (0 para aleatório) (padrão: 0) |
| `resolução` | COMBO | Não | `"1080p"` | Os valores suportados podem variar conforme o modelo e a duração (padrão: "1080p") |
| `amplitude de movimento` | COMBO | Não | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` | A amplitude de movimento dos objetos no quadro (padrão: "auto") |

**Observação:** Os quadros inicial e final devem ter proporções de aspecto compatíveis (validadas com tolerância de proporção min_rel=0,8, max_rel=1,25).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado |

---
**Source fingerprint (SHA-256):** `d859d67b3ff73977b95e3903b461509f933f9652fedc016e1cd362f6bef1b8dc`
