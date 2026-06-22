# FreeU_V2

O nó FreeU_V2 melhora a qualidade da geração de imagens aplicando modificações baseadas em frequência à arquitetura U-Net de um modelo de difusão. Ele utiliza fatores de escala configuráveis para ajustar os canais de características em diferentes blocos, melhorando a saída sem exigir treinamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual aplicar o aprimoramento FreeU | MODEL | Sim | - |
| `b1` | Fator de escala das características do backbone para o primeiro bloco (padrão: 1,3) | FLOAT | Sim | 0,0 - 10,0 |
| `b2` | Fator de escala das características do backbone para o segundo bloco (padrão: 1,4) | FLOAT | Sim | 0,0 - 10,0 |
| `s1` | Fator de escala das características de skip para o primeiro bloco (padrão: 0,9) | FLOAT | Sim | 0,0 - 10,0 |
| `s2` | Fator de escala das características de skip para o segundo bloco (padrão: 0,2) | FLOAT | Sim | 0,0 - 10,0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo de difusão aprimorado com as modificações FreeU aplicadas | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `40ded64177e8e00cc5d8d5dde35c20958a77c500dada725572b64484c5ce1045`
