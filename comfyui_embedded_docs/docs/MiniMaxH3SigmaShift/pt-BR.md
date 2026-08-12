# MiniMax H3 Sigma Shift

Define os valores de deslocamento de fluxo de vídeo e áudio para um modelo MiniMax H3. O deslocamento de vídeo controla a agenda sigma do amostrador, e ambos os valores de deslocamento são passados para o transformador interno do modelo, que os utiliza para derivar a agenda de áudio a partir da grade base compartilhada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|---------------|--------------|-------|
| `modelo` | O modelo ao qual aplicar o patch de deslocamento sigma. O nó clona o modelo, portanto o original permanece inalterado. | MODEL | Sim | - |
| `deslocamento_vídeo` | O valor de deslocamento de fluxo de vídeo. Ele conduz a agenda sigma do amostrador. Padrão: 12.0. | FLOAT | Sim | 0.01 a 100.0 |
| `deslocamento_áudio` | O valor de deslocamento de fluxo de áudio. É usado pelo modelo para derivar a agenda de áudio. Padrão: 3.0. | FLOAT | Sim | 0.01 a 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `MODEL` | O modelo clonado com as configurações de deslocamento sigma de vídeo e áudio aplicadas. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3SigmaShift/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f731585cc1a9c87a3e54341757c4cf4e490d1d4718ecf458bd2b9f4378af63f`
