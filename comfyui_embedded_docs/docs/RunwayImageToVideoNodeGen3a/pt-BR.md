# Runway Imagem para Vídeo (Gen3a Turbo)

O nó Runway Image to Video (Gen3a Turbo) gera um vídeo a partir de um único quadro inicial usando o modelo Gen3a Turbo da Runway. Ele recebe um prompt de texto e um quadro de imagem inicial e, em seguida, cria uma sequência de vídeo com base na duração e na proporção de aspecto especificadas. A geração é processada remotamente por meio da API da Runway. Este nó está marcado como obsoleto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração (padrão: "") | STRING | Sim | N/A |
| `quadro_inicial` | Quadro inicial a ser usado para o vídeo | IMAGE | Sim | N/A |
| `duração` | Duração do vídeo gerado, em segundos (padrão: "5") | COMBO | Sim | `"5"`<br>`"10"` |
| `proporção` | Proporção de aspecto do vídeo gerado (padrão: "768:1280") | COMBO | Sim | `"768:1280"`<br>`"1280:768"` |
| `semente` | Semente aleatória para geração (padrão: 0) | INT | Sim | 0 a 4294967295 |

**Restrições dos parâmetros:**

- O `prompt` deve conter pelo menos um caractere (não pode estar vazio).
- O `start_frame` aceita uma única imagem (máximo de 1).
- O `start_frame` não deve exceder 7999 x 7999 pixels em dimensões.
- O `start_frame` deve ter uma proporção de aspecto entre 1:2 e 2:1 (0,5 a 2,0).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | A sequência de vídeo gerada | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayImageToVideoNodeGen3a/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ff66cbdfa80aabeaf96d43e7822dd0c700ee027d13fb430a9dc2079e1a23f38e`
