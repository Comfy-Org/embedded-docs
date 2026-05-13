> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/pt-BR.md)

O nó Runway Image to Video (Gen3a Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen3a Turbo da Runway. Ele recebe um prompt de texto e uma imagem de quadro inicial, depois cria uma sequência de vídeo com base na duração e proporção especificadas. Este nó se conecta à API da Runway para processar a geração remotamente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a geração (padrão: "") |
| `start_frame` | IMAGE | Sim | N/A | Quadro inicial a ser usado para o vídeo |
| `duration` | COMBO | Sim | `"5"`<br>`"10"` | Duração do vídeo em segundos (padrão: "5") |
| `ratio` | COMBO | Sim | `"1280x720"`<br>`"720x1280"`<br>`"1920x1080"`<br>`"1080x1920"`<br>`"1080x1080"` | Proporção de aspecto do vídeo gerado (padrão: "1280x720") |
| `seed` | INT | Não | 0 a 4294967295 | Semente aleatória para a geração (padrão: 0) |

**Restrições dos Parâmetros:**

- O `start_frame` deve ter dimensões que não excedam 7999x7999 pixels.
- O `start_frame` deve ter uma proporção de aspecto entre 0,5 e 2,0.
- O `prompt` deve conter pelo menos um caractere (não pode estar vazio).

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | A sequência de vídeo gerada |

---
**Source fingerprint (SHA-256):** `4f3270ce070ce50580699292e21c5f9e3b1a56dd8ac981f67a9026ef6fc8ed76`
