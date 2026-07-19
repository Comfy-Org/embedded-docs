# Flux.1 Expandir Imagem

Expande a imagem com base no prompt. Este nó amplia uma imagem adicionando pixels aos lados superior, inferior, esquerdo e direito, enquanto gera novo conteúdo que corresponde à descrição textual fornecida.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser expandida | IMAGE | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: "") | STRING | Não | - |
| `aumento de prompt` | Se deve realizar upsampling no prompt. Se ativo, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: False) | BOOLEAN | Não | - |
| `superior` | Número de pixels a expandir na parte superior da imagem (padrão: 0) | INT | Não | 0-2048 |
| `inferior` | Número de pixels a expandir na parte inferior da imagem (padrão: 0) | INT | Não | 0-2048 |
| `esquerda` | Número de pixels a expandir no lado esquerdo da imagem (padrão: 0) | INT | Não | 0-2048 |
| `direita` | Número de pixels a expandir no lado direito da imagem (padrão: 0) | INT | Não | 0-2048 |
| `orientação` | Força de orientação para o processo de geração da imagem (padrão: 60) | FLOAT | Não | 1.5-100 |
| `passos` | Número de etapas para o processo de geração da imagem (padrão: 50) | INT | Não | 15-50 |
| `semente` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Não | 0-18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de saída expandida | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProExpandNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `15b21f1de8a98a6bcde131a61c01b062434c6a959bc563550d613972412973fe`
