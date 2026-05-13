> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/en.md)

O nó Batch Latents combina múltiplas entradas latentes em um único lote. Ele recebe um número variável de amostras latentes e as mescla ao longo da dimensão do lote, permitindo que sejam processadas juntas em nós subsequentes. Isso é útil para gerar ou processar múltiplas imagens em uma única operação.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `latents` | LATENT | Sim | 2 a 50 entradas | Um conjunto de amostras latentes a serem combinadas em um único lote. Você deve fornecer pelo menos dois latentes e pode adicionar até 50. O nó cria automaticamente slots de entrada conforme você conecta mais latentes. |

**Nota:** Você deve fornecer pelo menos duas entradas latentes para o nó funcionar. O nó criará automaticamente slots de entrada conforme você conectar mais latentes, até o máximo de 50.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | LATENT | Uma única saída latente contendo todas as entradas latentes combinadas em um lote. |

---
**Source fingerprint (SHA-256):** `215e7e2df43e902815dd87d228e8d5e09f18f6f52002cc3e861551fc207a9896`
