# Runway Quadro Inicial-Final para Vídeo

O nó Runway First-Last-Frame to Video gera um vídeo usando um quadro inicial, um quadro final e um prompt de texto. Ele cria uma transição suave entre os dois quadros-chave fornecidos usando o modelo gen3a_turbo da Runway. É especialmente útil para transições complexas em que o quadro final é completamente diferente do quadro inicial.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt de texto para a geração (padrão: string vazia) | STRING | Sim | N/A |
| `quadro_inicial` | Quadro inicial a ser usado no vídeo | IMAGE | Sim | N/A |
| `quadro_final` | Quadro final a ser usado no vídeo. Suportado apenas para gen3a_turbo. | IMAGE | Sim | N/A |
| `duração` | Duração do vídeo gerado em segundos. A duração mais longa, de 10s, dá mais tempo para a geração transicionar suavemente entre os quadros inicial e final (padrão: "5"). | COMBO | Sim | `"5"`<br>`"10"` |
| `proporção` | Proporção de aspecto do vídeo gerado (padrão: "768:1280") | COMBO | Sim | `"768:1280"`<br>`"1280:768"` |
| `semente` | Semente aleatória para a geração. Defina como 0 para usar uma semente aleatória (padrão: 0). | INT | Não | 0 a 4294967295 |

**Restrições de parâmetros:**

- O `prompt` deve conter pelo menos 1 caractere
- Tanto `start_frame` quanto `end_frame` devem ter dimensões máximas de 7999x7999 pixels
- Tanto `start_frame` quanto `end_frame` devem ter proporções de aspecto entre 0,5 e 2,0
- O parâmetro `end_frame` só é suportado ao usar o modelo gen3a_turbo

**Observações:**

- O custo de geração é baseado na duração selecionada: USD 0,0715 por segundo (USD 0,3575 para 5 segundos, USD 0,715 para 10 segundos)
- Este nó está marcado como obsoleto

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado com a transição entre os quadros inicial e final | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d8720aba833348583d2aa37e13a1ad43d9055b0201c9cb6ad9c95dada7e5056`
