# FluxProImageNode

Gera imagens de forma síncrona com base no prompt e na resolução. Este nó cria imagens usando o modelo Flux 1.1 Pro ao enviar requisições para um endpoint de API e aguardar a resposta completa antes de retornar a imagem gerada.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Sim | - |
| `prompt_upsampling` | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma seed não produzirá exatamente o mesmo resultado). (padrão: False) | BOOLEAN | Sim | - |
| `width` | Largura da imagem em pixels (padrão: 1024, passo: 32) | INT | Sim | 256-1440 |
| `height` | Altura da imagem em pixels (padrão: 768, passo: 32) | INT | Sim | 256-1440 |
| `seed` | A seed aleatória usada para criar o ruído. (padrão: 0) | INT | Sim | 0-18446744073709551615 |
| `image_prompt` | Imagem de referência opcional para orientar a geração | IMAGE | Não | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `output` | A imagem gerada retornada pela API | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
