Preenche áreas de uma imagem com base em uma máscara e um prompt. Este nó utiliza o modelo Flux.1 para preencher as áreas mascaradas de uma imagem de acordo com a descrição textual fornecida, gerando novo conteúdo que combina com a imagem ao redor.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A imagem de entrada a ser pintada | IMAGE | Sim | - |
| `mask` | A máscara que define quais áreas da imagem devem ser preenchidas | MASK | Sim | - |
| `prompt` | Prompt para a geração da imagem (padrão: string vazia) | STRING | Não | - |
| `aumento de prompt` | Se deve realizar upsampling no prompt. Se ativado, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: falso) | BOOLEAN | Não | - |
| `orientação` | Força de orientação para o processo de geração da imagem (padrão: 60) | FLOAT | Não | 1,5-100 |
| `passos` | Número de etapas para o processo de geração da imagem (padrão: 50) | INT | Não | 15-50 |
| `semente` | A semente aleatória usada para criar o ruído. (padrão: 0) | INT | Não | 0-18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output_image` | A imagem gerada com as áreas mascaradas preenchidas de acordo com o prompt | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
