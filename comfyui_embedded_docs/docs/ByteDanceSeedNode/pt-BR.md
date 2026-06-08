# Visão Geral

Gere respostas de texto usando os modelos Seed 2.0 da ByteDance. Forneça um prompt de texto e, opcionalmente, inclua imagens ou vídeos para contexto multimodal.

# Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Entrada de texto para o modelo. | STRING | Sim | N/A |
| `modelo` | O modelo Seed usado para gerar a resposta. | COMBO | Sim | `"Seed 2.0 Pro"`<br>`"Seed 2.0 Lite"`<br>`"Seed 2.0 Mini"` |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `prompt do sistema` | Instruções fundamentais que determinam o comportamento do modelo. (padrão: "") | STRING | Não | N/A |

**Observação sobre o parâmetro `model`:** O parâmetro `model` é uma combinação dinâmica que também aceita imagens e vídeos. Você pode conectar entradas de imagem e vídeo a este parâmetro para fornecer contexto multimodal. São suportados no máximo 20 imagens e 4 vídeos por requisição.

# Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | A resposta de texto gerada pelo modelo Seed. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d1ef73cf72e88216d40c0cf727f90c40cf783cecabe3be0e7530fe72dba6c172`
