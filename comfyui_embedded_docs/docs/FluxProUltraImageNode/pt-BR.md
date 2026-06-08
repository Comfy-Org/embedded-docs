Gera imagens usando Flux Pro 1.1 Ultra via API com base no prompt e na resolução. Este nó se conecta a um serviço externo para criar imagens de acordo com sua descrição textual e dimensões especificadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Sim | - |
| `prompt_upsampling` | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: False) | BOOLEAN | Não | - |
| `seed` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Não | 0 a 18446744073709551615 |
| `aspect_ratio` | Proporção de aspecto da imagem; deve estar entre 1:4 e 4:1. (padrão: "16:9") | STRING | Não | - |
| `raw` | Quando True, gera imagens menos processadas, com aparência mais natural. (padrão: False) | BOOLEAN | Não | - |
| `image_prompt` | Imagem de referência opcional para guiar a geração | IMAGE | Não | - |
| `image_prompt_strength` | Mistura entre o prompt e o prompt de imagem. (padrão: 0.1) | FLOAT | Não | 0.0 a 1.0 |

**Nota:** O parâmetro `aspect_ratio` deve estar entre 1:4 e 4:1. Quando `image_prompt` é fornecido, `image_prompt_strength` se torna ativo e controla o quanto a imagem de referência influencia o resultado final. Se `image_prompt` não for fornecido, o parâmetro `prompt` é validado para garantir que não esteja vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output_image` | A imagem gerada pelo Flux Pro 1.1 Ultra | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8632aeb76e9007d65d7f3fd51465fe78f56ba92264ef65ce505db2fc95cfd25b`
