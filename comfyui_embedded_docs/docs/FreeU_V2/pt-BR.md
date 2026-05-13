> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU_V2/pt-BR.md)

O nó FreeU_V2 melhora a qualidade da geração de imagens aplicando modificações baseadas em frequência à arquitetura U-Net de um modelo de difusão. Ele utiliza fatores de escala configuráveis para ajustar os canais de características em diferentes blocos, melhorando a saída sem exigir treinamento adicional.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar o aprimoramento FreeU |
| `b1` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala das características do backbone para o primeiro bloco (padrão: 1,3) |
| `b2` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala das características do backbone para o segundo bloco (padrão: 1,4) |
| `s1` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala das características de skip para o primeiro bloco (padrão: 0,9) |
| `s2` | FLOAT | Sim | 0,0 - 10,0 | Fator de escala das características de skip para o segundo bloco (padrão: 0,2) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo de difusão aprimorado com as modificações FreeU aplicadas |

---
**Source fingerprint (SHA-256):** `40ded64177e8e00cc5d8d5dde35c20958a77c500dada725572b64484c5ce1045`
