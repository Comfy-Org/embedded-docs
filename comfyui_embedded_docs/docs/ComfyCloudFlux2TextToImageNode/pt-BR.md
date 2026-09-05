# ComfyCloudFlux2TextToImageNode

Executa o modelo de texto para imagem Flux 2 dev em uma GPU do Comfy Cloud e retorna a imagem gerada. A opção `turbo` aplica o Turbo LoRA com um cronograma curto para uma execução muito mais rápida, ao custo de um pouco de fidelidade; desativá-la executa a passagem completa do modelo dev sem o LoRA. Este é um conjunto de nós beta, cobrado pelo tempo de execução em créditos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | O prompt de texto que descreve a imagem a ser gerada. Espaços em branco no início e no fim são removidos antes do envio. | STRING | Sim | 1 a 4096 caracteres |
| `seed` | Semente aleatória que controla o resultado gerado para reprodutibilidade (padrão: 42). | INT | Sim | 0 a 18446744073709551615 |
| `aspect_ratio` | Proporção de aspecto da imagem de saída (padrão: "1:1"). | COMBO | Sim | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Orçamento total de pixels. 1.0 equivale a cerca de 1024x1024 em proporção quadrada (padrão: 1.0). | FLOAT | Sim | 0.1 a 16.0 (passo 0.1) |
| `turbo` | Executa o Turbo LoRA em um cronograma curto, trocando um pouco de fidelidade por uma execução muito mais rápida. Desativado executa a passagem completa do dev sem o LoRA (padrão: True). | BOOLEAN | Sim | True / False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem gerada a partir do prompt de texto, retornada como um tensor de imagem do ComfyUI que pode ser passado para outros nós. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`
