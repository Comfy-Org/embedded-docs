> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/pt-BR.md)

O nó Morphology aplica várias operações morfológicas em imagens, que são operações matemáticas usadas para processar e analisar formas em imagens. Ele pode realizar operações como erosão, dilatação, abertura, fechamento e outras, utilizando um tamanho de kernel personalizável para controlar a intensidade do efeito.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser processada |
| `operation` | STRING | Sim | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | A operação morfológica a ser aplicada (padrão: "erode") |
| `kernel_size` | INT | Sim | 3-999 | O tamanho do kernel do elemento estruturante (padrão: 3). Deve ser um número ímpar. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem processada após a aplicação da operação morfológica |

---
**Source fingerprint (SHA-256):** `7f6224a0e58fbb7263267b377394e119c6f8d65d16af4ce492ca9504654af7b4`
