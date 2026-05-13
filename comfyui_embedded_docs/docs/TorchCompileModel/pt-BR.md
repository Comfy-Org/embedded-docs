> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/pt-BR.md)

Este documento foi gerado por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/en.md)

O nó TorchCompileModel aplica a compilação PyTorch a um modelo para otimizar seu desempenho. Ele cria uma cópia do modelo de entrada e a envolve com a funcionalidade de compilação do PyTorch usando o backend especificado. Isso pode melhorar a velocidade de execução do modelo durante a inferência.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | MODEL | Sim | - | O modelo a ser compilado e otimizado |
| `backend` | STRING | Sim | "inductor"<br>"cudagraphs" | O backend de compilação PyTorch a ser usado para otimização (padrão: "inductor") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `modelo` | MODEL | O modelo compilado com a compilação PyTorch aplicada |

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
