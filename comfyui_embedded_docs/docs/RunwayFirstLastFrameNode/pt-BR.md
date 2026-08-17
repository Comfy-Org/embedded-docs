# Runway Quadro Inicial-Final para Vídeo

O nó Runway First-Last-Frame to Video gera vídeos ao enviar o primeiro e o último quadro-chave, juntamente com um prompt de texto. Ele cria transições suaves entre os quadros inicial e final fornecidos usando o modelo Gen-3 da Runway. Isso é particularmente útil para transições complexas em que o quadro final difere significativamente do quadro inicial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|-------------|-------|
| `prompt` | Prompt de texto para a geração (padrão: string vazia) | STRING | Sim | N/A |
| `start_frame` | Quadro inicial a ser usado no vídeo | IMAGE | Sim | N/A |
| `end_frame` | Quadro final a ser usado no vídeo. Suportado apenas para gen3a_turbo. | IMAGE | Sim | N/A |
| `duration` | Duração do vídeo em segundos (padrão: "5") | COMBO | Sim | `"5"`<br>`"10"` |
| `ratio` | Proporção de aspecto para o vídeo gerado (padrão: "768:1280") | COMBO | Sim | `"768:1280"`<br>`"1280:768"` |
| `seed` | Semente aleatória para geração. Defina como 0 para uma semente aleatória (padrão: 0). | INT | Não | 0 a 4294967295 |

**Restrições dos Parâmetros:**

- O `prompt` deve conter pelo menos 1 caractere
- Tanto `start_frame` quanto `end_frame` devem ter dimensões máximas de 7999x7999 pixels
- Tanto `start_frame` quanto `end_frame` devem ter proporções de aspecto entre 0,5 e 2,0
- O parâmetro `end_frame` só é suportado ao usar o modelo gen3a_turbo

**Nota:** Este nó está marcado como obsoleto. Revise as práticas recomendadas da Runway para criação com quadros-chave no Gen-3 antes do uso: https://help.runwayml.com/hc/en-us/articles/34170748696595-Creating-with-Keyframes-on-Gen-3

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `output` | O vídeo gerado que faz a transição entre os quadros inicial e final | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
