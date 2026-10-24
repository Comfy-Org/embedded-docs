# Flux.1 Kontext [max] Image

Gera ou edita uma imagem com o Flux.1 Kontext [max] por meio da BFL API, com base em um prompt e uma proporção de aspecto. Com `input_image` conectado, o prompt descreve a edição; sem ele, o nó gera uma nova imagem apenas a partir do prompt. Ele expõe as mesmas entradas que o Flux.1 Kontext [pro] Image.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração da imagem. Com uma imagem de entrada, especifique o que e como editar. | STRING | Sim | - |
| `proporção` | Proporção de aspecto da imagem; deve estar entre 1:4 e 4:1 (padrão: `"16:9"`). | STRING | Sim | - |
| `orientação` | Força de orientação para o processo de geração da imagem (padrão: 3.0). | FLOAT | Sim | 0.1 a 99.0 (passo 0.1) |
| `etapas` | Número de etapas para o processo de geração da imagem (padrão: 50). | INT | Sim | 1 a 150 |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 1234). | INT | Sim | 0 a 18446744073709551615 |
| `amostragem_do_prompt` | Se deve realizar upsampling no prompt. Se ativado, o prompt é modificado automaticamente para uma geração mais criativa, mas os resultados são não determinísticos, então a mesma seed não produzirá exatamente o mesmo resultado (padrão: `False`). Esta é uma configuração avançada. | BOOLEAN | Sim | True / False |
| `imagem_de_entrada` | Imagem opcional a ser editada. Quando omitida, o prompt é validado para garantir que não esteja vazio. | IMAGE | Não | - |

**Observação:** O nó envia a solicitação para a BFL e consulta repetidamente até que a imagem esteja pronta. Solicitações rejeitadas pela moderação de conteúdo da BFL falham em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada ou editada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMaxImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `557f9e69de37ee89e161dffdaef7458ed026b884298594f2046454b6b8d3c415`
