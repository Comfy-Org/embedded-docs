> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/pt-BR.md)

O nó CLIPTextEncodeSD3 processa entradas de texto para modelos Stable Diffusion 3, codificando múltiplos prompts de texto usando diferentes modelos CLIP. Ele gerencia três entradas de texto separadas (`clip_g`, `clip_l` e `t5xxl`) e oferece opções para gerenciar o preenchimento de texto vazio. O nó garante o alinhamento adequado de tokens entre diferentes entradas de texto e retorna dados de condicionamento adequados para pipelines de geração SD3.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `clip` | CLIP | Sim | - | O modelo CLIP usado para codificação de texto |
| `clip_l` | STRING | Sim | - | Entrada de texto para o modelo CLIP local. Suporta texto multilinha e prompts dinâmicos. |
| `clip_g` | STRING | Sim | - | Entrada de texto para o modelo CLIP global. Suporta texto multilinha e prompts dinâmicos. |
| `t5xxl` | STRING | Sim | - | Entrada de texto para o modelo T5-XXL. Suporta texto multilinha e prompts dinâmicos. |
| `empty_padding` | COMBO | Sim | `"none"`<br>`"empty_prompt"` | Controla como entradas de texto vazias são tratadas. Quando definido como "none", entradas de texto vazias para `clip_g`, `clip_l` ou `t5xxl` resultarão em listas de tokens vazias em vez de preenchimento. Este é um parâmetro avançado (padrão: "none"). |

**Restrições dos Parâmetros:**

- Quando `empty_padding` está definido como "none", entradas de texto vazias para `clip_g`, `clip_l` ou `t5xxl` resultarão em listas de tokens vazias em vez de preenchimento
- O nó equilibra automaticamente os comprimentos de token entre as entradas `clip_l` e `clip_g`, preenchendo a mais curta com tokens vazios quando os comprimentos diferem
- Todas as entradas de texto suportam prompts dinâmicos e entrada de texto multilinha

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento de texto codificados, prontos para uso em pipelines de geração SD3 |

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`
