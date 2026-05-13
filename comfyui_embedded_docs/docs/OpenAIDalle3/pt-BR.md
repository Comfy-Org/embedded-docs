> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/pt-BR.md)

Gera imagens de forma síncrona por meio do endpoint DALL·E 3 da OpenAI. Este nó recebe um prompt de texto e cria imagens correspondentes usando o modelo DALL·E 3 da OpenAI, permitindo especificar qualidade, estilo e dimensões da imagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt de texto para o DALL·E (padrão: "") |
| `seed` | INT | Não | 0 a 2147483647 | Ainda não implementado no backend (padrão: 0) |
| `quality` | COMBO | Não | "standard"<br>"hd" | Qualidade da imagem (padrão: "standard") |
| `style` | COMBO | Não | "natural"<br>"vivid" | Vívido faz o modelo tender a gerar imagens hiper-realistas e dramáticas. Natural faz o modelo produzir imagens mais naturais e menos hiper-realistas. (padrão: "natural") |
| `size` | COMBO | Não | "1024x1024"<br>"1024x1792"<br>"1792x1024" | Tamanho da imagem (padrão: "1024x1024") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `IMAGE` | IMAGE | A imagem gerada pelo DALL·E 3 |

---
**Source fingerprint (SHA-256):** `e36bfe2a6ecec050906f220de3a3edf06eff0bfd6e21f08ce90579172a07d7eb`
