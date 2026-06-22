# TorchCompileModel

Este documento foi gerado por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/en.md)

O nó TorchCompileModel aplica a compilação PyTorch a um modelo para otimizar seu desempenho. Ele cria uma cópia do modelo de entrada e a envolve com a funcionalidade de compilação do PyTorch usando o backend especificado. Isso pode melhorar a velocidade de execução do modelo durante a inferência.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser compilado e otimizado | MODEL | Sim | - |
| `backend` | O backend de compilação PyTorch a ser usado para otimização (padrão: "inductor") | STRING | Sim | "inductor"<br>"cudagraphs" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo compilado com a compilação PyTorch aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
