> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/pt-BR.md)

Preenche áreas de uma imagem com base em uma máscara e um prompt. Este nó utiliza o modelo Flux.1 para preencher as áreas mascaradas de uma imagem de acordo com a descrição textual fornecida, gerando novo conteúdo que combina com a imagem ao redor.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser pintada |
| `mask` | MASK | Sim | - | A máscara que define quais áreas da imagem devem ser preenchidas |
| `prompt` | STRING | Não | - | Prompt para a geração da imagem (padrão: string vazia) |
| `aumento de prompt` | BOOLEAN | Não | - | Se deve realizar upsampling no prompt. Se ativado, modifica automaticamente o prompt para uma geração mais criativa, mas os resultados são não determinísticos (a mesma semente não produzirá exatamente o mesmo resultado). (padrão: falso) |
| `orientação` | FLOAT | Não | 1,5-100 | Força de orientação para o processo de geração da imagem (padrão: 60) |
| `passos` | INT | Não | 15-50 | Número de etapas para o processo de geração da imagem (padrão: 50) |
| `semente` | INT | Não | 0-18446744073709551615 | A semente aleatória usada para criar o ruído. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output_image` | IMAGE | A imagem gerada com as áreas mascaradas preenchidas de acordo com o prompt |

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
