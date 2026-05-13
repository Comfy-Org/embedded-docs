> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/pt-BR.md)

O nó AlignYourStepsScheduler gera valores sigma para o processo de remoção de ruído com base em diferentes tipos de modelo. Ele calcula níveis de ruído apropriados para cada etapa do processo de amostragem e ajusta o número total de etapas de acordo com o parâmetro de remoção de ruído. Isso ajuda a alinhar as etapas de amostragem com os requisitos específicos de diferentes modelos de difusão.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `tipo_de_modelo` | STRING | Sim | `"SD1"`<br>`"SDXL"`<br>`"SVD"` | Especifica o tipo de modelo a ser usado para o cálculo sigma (padrão: "SD1") |
| `passos` | INT | Sim | 1 a 10000 | O número total de etapas de amostragem a serem geradas (padrão: 10) |
| `reduzir_ruído` | FLOAT | Sim | 0.0 a 1.0 | Controla o quanto remover o ruído da imagem, onde 1.0 usa todas as etapas e valores menores usam menos etapas (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `sigmas` | SIGMAS | Retorna os valores sigma calculados para o processo de remoção de ruído |

---
**Source fingerprint (SHA-256):** `112535f9c100ca4e13dcd733e7a371c00c203b38d77bd10beb4355ba3512ec66`
