> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/pt-BR.md)

O nó Hunyuan3Dv2Conditioning processa a saída do CLIP vision para gerar dados de condicionamento para modelos 3D. Ele extrai os embeddings do último estado oculto da saída visual e cria pares de condicionamento positivo e negativo. O condicionamento positivo utiliza os embeddings reais, enquanto o condicionamento negativo utiliza embeddings com valor zero, de mesma forma.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip_vision_output` | CLIP_VISION_OUTPUT | Sim | - | A saída de um modelo CLIP vision contendo embeddings visuais |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `positive` | CONDITIONING | Dados de condicionamento positivo contendo os embeddings do CLIP vision |
| `negative` | CONDITIONING | Dados de condicionamento negativo contendo embeddings com valor zero, correspondendo à forma dos embeddings positivos |

---
**Source fingerprint (SHA-256):** `3a32967d62a0645b0c375b17ab96e20805c2e0005e585dddf5a3a77d35994fec`
