# Runway Imagem para Vídeo (Gen3a Turbo)

O nó Runway Image to Video (Gen3a Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen3a Turbo da Runway. Ele recebe um prompt de texto e um quadro de imagem inicial e, em seguida, cria uma sequência de vídeo com base na duração e na proporção especificadas. Este nó se conecta à API da Runway para processar a geração remotamente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração (padrão: "") | STRING | Sim | N/A |
| `start_frame` | Quadro inicial a ser usado no vídeo | IMAGE | Sim | N/A |
| `duration` | Duração do vídeo em segundos (padrão: "5") | COMBO | Sim | `"5"`<br>`"10"` |
| `ratio` | Proporção de aspecto do vídeo gerado (padrão: "768:1280") | COMBO | Sim | `"768:1280"`<br>`"1280:768"` |
| `seed` | Semente aleatória para geração (padrão: 0) | INT | Não | 0 a 4294967295 |

**Restrições dos Parâmetros:**

- O `start_frame` deve ter dimensões não superiores a 7999x7999 pixels.
- O `start_frame` deve ter uma proporção de aspecto entre 0,5 e 2,0.
- O `prompt` deve conter pelo menos um caractere (não pode estar vazio).

**Notas:**

- Este nó está obsoleto.
- Antes de gerar, a Runway recomenda revisar o guia de boas práticas: https://help.runwayml.com/hc/en-us/articles/33927968552339-Creating-with-Act-One-on-Gen-3-Alpha-and-Turbo

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A sequência de vídeo gerada | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
