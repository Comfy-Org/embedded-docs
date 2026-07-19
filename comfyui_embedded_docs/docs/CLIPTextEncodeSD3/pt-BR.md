# CLIPTextEncodeSD3

O nó CLIPTextEncodeSD3 processa entradas de texto para modelos Stable Diffusion 3, codificando múltiplos prompts de texto usando diferentes modelos CLIP. Ele gerencia três entradas de texto separadas (`clip_g`, `clip_l` e `t5xxl`) e oferece opções para gerenciar o preenchimento de texto vazio. O nó garante o alinhamento adequado de tokens entre diferentes entradas de texto e retorna dados de condicionamento adequados para pipelines de geração SD3.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para codificação de texto | CLIP | Sim | - |
| `clip_l` | Entrada de texto para o modelo CLIP local. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `clip_g` | Entrada de texto para o modelo CLIP global. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `t5xxl` | Entrada de texto para o modelo T5-XXL. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | - |
| `preenchimento_vazio` | Controla como entradas de texto vazias são tratadas. Quando definido como "none", entradas de texto vazias para `clip_g`, `clip_l` ou `t5xxl` resultarão em listas de tokens vazias em vez de preenchimento. Este é um parâmetro avançado (padrão: "none"). | COMBO | Sim | `"none"`<br>`"empty_prompt"` |

**Restrições dos Parâmetros:**

- Quando `empty_padding` está definido como "none", entradas de texto vazias para `clip_g`, `clip_l` ou `t5xxl` resultarão em listas de tokens vazias em vez de preenchimento
- O nó equilibra automaticamente os comprimentos de token entre as entradas `clip_l` e `clip_g`, preenchendo a mais curta com tokens vazios quando os comprimentos diferem
- Todas as entradas de texto suportam prompts dinâmicos e entrada de texto multilinha

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento de texto codificados, prontos para uso em pipelines de geração SD3 | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `38f7538d05fe48e74f41f265550b83906b2f0c5d31f0783f6859f4df7b5cb9d3`
