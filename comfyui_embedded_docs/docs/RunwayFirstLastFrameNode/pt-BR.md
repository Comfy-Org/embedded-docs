> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayFirstLastFrameNode/pt-BR.md)

O nó "Primeiro-Último Quadro para Vídeo" do Runway gera vídeos a partir do upload do primeiro e último quadro-chave, juntamente com um prompt de texto. Ele cria transições suaves entre os quadros inicial e final fornecidos, utilizando o modelo Gen-3 do Runway. Isso é particularmente útil para transições complexas onde o quadro final difere significativamente do quadro inicial.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para a geração (padrão: string vazia) |
| `start_frame` | IMAGE | Sim | N/A | Quadro inicial a ser usado para o vídeo |
| `end_frame` | IMAGE | Sim | N/A | Quadro final a ser usado para o vídeo. Suportado apenas para gen3a_turbo. |
| `duration` | COMBO | Sim | `"5"`<br>`"10"` | Duração do vídeo em segundos (padrão: "5") |
| `ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | Proporção de aspecto para o vídeo gerado (padrão: "16:9") |
| `seed` | INT | Não | 0 a 4294967295 | Semente aleatória para geração. Defina como 0 para semente aleatória (padrão: 0). |

**Restrições dos Parâmetros:**

- O `prompt` deve conter pelo menos 1 caractere
- Tanto `start_frame` quanto `end_frame` devem ter dimensões máximas de 7999x7999 pixels
- Tanto `start_frame` quanto `end_frame` devem ter proporções de aspecto entre 0,5 e 2,0
- O parâmetro `end_frame` é suportado apenas ao usar o modelo gen3a_turbo

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo gerado fazendo a transição entre os quadros inicial e final |

---
**Source fingerprint (SHA-256):** `57b72c1143b7053272107403279e1f84919cbfe71c57ca4f4e21b4324f7a5346`
