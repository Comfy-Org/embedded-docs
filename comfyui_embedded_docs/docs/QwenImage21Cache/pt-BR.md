# QwenImage21Cache

O nó QwenImage21Cache configura o cache de prefixo KV do modelo Qwen-Image 2.1: onde as chaves e os valores em cache são armazenados e com qual precisão. Tokens de texto e de referência são calculados uma vez e reutilizados ao longo dos passos de amostragem, que é de onde vem a maior parte do ganho de velocidade em fluxos de trabalho de edição, e este nó permite trocar memória por velocidade ou descartar o cache completamente. Este nó está marcado como experimental.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo Qwen-Image 2.1 cujo cache de prefixo é configurado. | MODEL | Sim | - |
| `device` | Onde as chaves e os valores em cache são armazenados. `"auto"` (padrão) usa VRAM livre primeiro e depois RAM; `"gpu"` armazena o cache na VRAM; `"cpu"` armazena-o na RAM e faz prefetch em segundo plano durante a computação, o que tem pouco impacto na velocidade; `"off"` recalcula o prefixo a cada passo, o que é mais lento, mas é a única maneira de descartar o cache. | COMBO | Sim | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | Precisão de armazenamento do cache. `"default"` é sem perdas; `"int8"` reduz o cache pela metade com precisão próxima à do bf16; `"int4"` reduz a um quarto, mas aproximadamente dobra o erro por passo. | COMBO | Sim | `"default"`<br>`"int8"`<br>`"int4"` |

Quando o cache não cabe, o modelo recalcula o prefixo em vez de remover o slot do outro ramo, de modo que uma configuração superdimensionada degrada a velocidade em vez de falhar na execução.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo com o dispositivo e a precisão do cache aplicados, pronto para ser amostrado. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
