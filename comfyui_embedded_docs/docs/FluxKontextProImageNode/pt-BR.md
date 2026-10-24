# Flux.1 Kontext [pro] Image

Gera ou edita uma imagem com o Flux.1 Kontext [pro] por meio da API da BFL, com base em um prompt e em uma proporção. Com `input_image` conectado, o prompt descreve a edição; sem ele, o nó gera uma nova imagem apenas a partir do prompt.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração da imagem. Com uma imagem de entrada, especifique o que e como editar. | STRING | Sim | - |
| `proporção` | Proporção da imagem; deve estar entre 1:4 e 4:1 (padrão: `"16:9"`). | STRING | Sim | - |
| `orientação` | Força de orientação para o processo de geração da imagem (padrão: 3.0). | FLOAT | Sim | 0.1 a 99.0 (passo 0.1) |
| `etapas` | Número de etapas para o processo de geração da imagem (padrão: 50). | INT | Sim | 1 a 150 |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 1234). | INT | Sim | 0 a 18446744073709551615 |
| `amostragem_do_prompt` | Se deve realizar upsampling no prompt. Se ativado, o prompt é modificado automaticamente para uma geração mais criativa, mas os resultados são não determinísticos, então a mesma seed não produzirá exatamente o mesmo resultado (padrão: `False`). Esta é uma configuração avançada. | BOOLEAN | Sim | True / False |
| `imagem_de_entrada` | Imagem opcional para editar. Quando omitida, o prompt é validado para garantir que não esteja vazio. | IMAGE | Não | - |

**Nota:** O nó envia a solicitação à BFL e consulta repetidamente até que a imagem esteja pronta. Solicitações rejeitadas pela moderação de conteúdo da BFL falham em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada ou editada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextProImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a5be7e7859b1aca5130552345c76045ab64be3b4bee588091d147480a9ae1ac`
