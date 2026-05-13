> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TomePatchModel/pt-BR.md)

O nó TomePatchModel aplica a Fusão de Tokens (ToMe) a um modelo de difusão para reduzir os requisitos computacionais durante a inferência. Ele funciona mesclando seletivamente tokens semelhantes no mecanismo de atenção, permitindo que o modelo processe menos tokens enquanto mantém a qualidade da imagem. Essa técnica ajuda a acelerar a geração sem perda significativa de qualidade.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual aplicar a fusão de tokens |
| `ratio` | FLOAT | Não | 0.0 - 1.0 | A proporção de tokens a serem mesclados (padrão: 0.3) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com a fusão de tokens aplicada |

---
**Source fingerprint (SHA-256):** `23d63ffa1b468a8a41533cc926125f4ef566b13edd1d95a6ef1ae63096a9d878`
