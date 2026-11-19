# Video Deflicker

Remove a cintilação temporal de um vídeo processado, de modo que cada quadro mantenha seus próprios detalhes enquanto segue o movimento de seus vizinhos. Destina-se a filmagens que pulsam após serem ampliadas ou processadas quadro a quadro: conecte o modelo de fluxo óptico e os quadros com cintilação e, opcionalmente, uma cópia estável da fonte como guia.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `optical_flow` | Modelo de fluxo óptico do nó Load Optical Flow Model (torchvision RAFT-large). | OPTICAL_FLOW | Sim | - |
| `images` | Quadros com cintilação a estabilizar, por exemplo, um vídeo que foi ampliado ou processado quadro a quadro. | IMAGE | Sim | - |
| `guide` | Quadros de origem estáveis cujo movimento deve ser seguido, em qualquer resolução. O padrão é `images`, o que remove menos cintilação. As diferenças entre quadros consecutivos do guia, após a compensação de movimento, também ponderam a suavização: se o guia muda de formas que o fluxo não explica, a suavização diminui mesmo quando a estimativa de movimento está correta. | IMAGE | Não | - |
| `strength` | Quão fortemente cada quadro segue seus vizinhos (padrão: 1.0). Valores mais altos removem mais cintilação e suavizam mais os detalhes finos; 0 retorna os quadros inalterados. | FLOAT | Sim | 0.0 a 100.0 (passo: 0.1) |
| `direction` | Direção da passada. `bidirectional` faz a média de uma passada para frente e uma para trás, o que evita atraso em relação ao movimento; `forward` executa uma única passada. (padrão: `bidirectional`) | COMBO | Sim | `"bidirectional"`<br>`"forward"` |
| `threshold` | Mudanças maiores que este limiar entre um quadro e seu vizinho compensado por movimento são tratadas como reais e suavizadas menos (padrão: 0.1). 0 suaviza todas as mudanças da mesma forma. | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

**Notas:**

- O fluxo óptico é calculado sobre uma cópia reduzida do guia, então ele não precisa ter o tamanho de `images`; os pixels do guia não são misturados à saída.
- Quadros além do mais curto entre `images` e `guide` não são processados. Se `guide` for mais curto, os quadros restantes voltam inalterados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | Quadros sem cintilação, com o mesmo tamanho e a mesma contagem de quadros que `images`. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`
