> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen4/en.md)

O nó Runway Image to Video (Gen4 Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen4 Turbo da Runway. Ele recebe um prompt de texto e um quadro de imagem inicial e, em seguida, cria uma sequência de vídeo com base na duração fornecida e nas configurações de proporção. O nó gerencia o upload do quadro inicial para a API da Runway e retorna o vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt de texto para a geração (padrão: string vazia) |
| `quadro_inicial` | IMAGE | Sim | - | Quadro inicial a ser usado para o vídeo |
| `duração` | COMBO | Sim | `"5"`<br>`"10"` | Duração do vídeo em segundos (padrão: "5") |
| `proporção` | COMBO | Sim | `"1024:1024"`<br>`"1280:720"`<br>`"720:1280"`<br>`"1920:1080"`<br>`"1080:1920"`<br>`"2048:1080"`<br>`"1080:2048"` | Proporção de aspecto para o vídeo gerado (padrão: "1024:1024") |
| `semente` | INT | Não | 0 a 4294967295 | Semente aleatória para a geração (padrão: 0) |

**Restrições dos Parâmetros:**

- A imagem `start_frame` deve ter dimensões que não excedam 7999x7999 pixels
- A imagem `start_frame` deve ter uma proporção de aspecto entre 0,5 e 2,0
- O `prompt` deve conter pelo menos um caractere

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | VIDEO | O vídeo gerado com base no quadro de entrada e no prompt |

---
**Source fingerprint (SHA-256):** `ebb5f1cd5e6bf6e0fcfb4910c774c087980daf9a1987900ad966120608b924e7`
