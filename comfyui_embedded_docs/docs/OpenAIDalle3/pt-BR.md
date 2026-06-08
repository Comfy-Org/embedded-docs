Gera imagens de forma síncrona por meio do endpoint DALL·E 3 da OpenAI. Este nó recebe um prompt de texto e cria imagens correspondentes usando o modelo DALL·E 3 da OpenAI, permitindo especificar qualidade, estilo e dimensões da imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para o DALL·E (padrão: "") | STRING | Sim | - |
| `seed` | Ainda não implementado no backend (padrão: 0) | INT | Não | 0 a 2147483647 |
| `qualidade` | Qualidade da imagem (padrão: "standard") | COMBO | Não | "standard"<br>"hd" |
| `estilo` | Vívido faz o modelo tender a gerar imagens hiper-realistas e dramáticas. Natural faz o modelo produzir imagens mais naturais e menos hiper-realistas. (padrão: "natural") | COMBO | Não | "natural"<br>"vivid" |
| `tamanho` | Tamanho da imagem (padrão: "1024x1024") | COMBO | Não | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem gerada pelo DALL·E 3 | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
