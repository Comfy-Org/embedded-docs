# Hunyuan3Dv2Conditioning

O nó Hunyuan3Dv2Conditioning processa a saída do CLIP vision para gerar dados de condicionamento para modelos 3D. Ele extrai os embeddings do último estado oculto da saída de visão e cria pares de condicionamento positivo e negativo. O condicionamento positivo usa os embeddings reais, enquanto o condicionamento negativo usa embeddings de valor zero com a mesma forma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip_vision_output` | A saída de um modelo de visão CLIP contendo embeddings visuais | CLIP_VISION_OUTPUT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Dados de condicionamento positivo contendo os embeddings de visão do CLIP | CONDITIONING |
| `negative` | Dados de condicionamento negativo contendo embeddings de valor zero que correspondem à forma dos embeddings positivos | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`
