# CLIPTextEncodeKandinsky5

O nó CLIP Text Encode (Kandinsky 5) prepara prompts de texto para uso com o modelo Kandinsky 5. Ele recebe duas entradas de texto separadas, tokeniza ambas com um modelo CLIP fornecido e as combina em uma única saída de condicionamento que orienta o processo de geração de imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `clip` | O modelo CLIP usado para tokenizar e codificar os prompts de texto. | CLIP | Sim |  |
| `clip_l` | O prompt de texto primário. Esta entrada oferece suporte a texto multilinha e prompts dinâmicos. | STRING | Sim |  |
| `qwen25_7b` | O prompt de texto secundário. Esta entrada oferece suporte a texto multilinha e prompts dinâmicos. | STRING | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Os dados de condicionamento combinados gerados a partir dos dois prompts de texto, prontos para serem fornecidos a um modelo Kandinsky 5 para geração de imagem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeKandinsky5/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d988c47ab9a5f01549a3ae01b365d39e9fa2464bb69ea018ec20151939dcfc56`
