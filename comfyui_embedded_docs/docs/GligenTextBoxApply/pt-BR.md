> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/pt-BR.md)

O nó `GLIGENTextBoxApply` é projetado para integrar condicionamento baseado em texto na entrada de um modelo generativo, especificamente aplicando parâmetros de caixa de texto e codificando-os usando um modelo CLIP. Este processo enriquece o condicionamento com informações espaciais e textuais, facilitando uma geração mais precisa e consciente do contexto.

## Entradas

| Parâmetro            | Tipo Comfy         | Descrição |
|----------------------|--------------------|-------------|
| `conditioning_to`     | `CONDITIONING`     | Especifica a entrada de condicionamento inicial à qual os parâmetros da caixa de texto e as informações de texto codificadas serão anexados. Desempenha um papel crucial na determinação da saída final ao integrar novos dados de condicionamento. |
| `clip`               | `CLIP`             | O modelo CLIP usado para codificar o texto fornecido em um formato que pode ser utilizado pelo modelo generativo. É essencial para converter informações textuais em um formato de condicionamento compatível. |
| `gligen_textbox_model` | `GLIGEN`         | Representa a configuração específica do modelo GLIGEN a ser usada para gerar a caixa de texto. É crucial para garantir que a caixa de texto seja gerada de acordo com as especificações desejadas. |
| `text`               | `STRING`           | O conteúdo de texto a ser codificado e integrado no condicionamento. Fornece a informação semântica que orienta o modelo generativo. |
| `width`              | `INT`              | A largura da caixa de texto em pixels. Define a dimensão espacial da caixa de texto dentro da imagem gerada. |
| `height`             | `INT`              | A altura da caixa de texto em pixels. Semelhante à largura, define a dimensão espacial da caixa de texto dentro da imagem gerada. |
| `x`                  | `INT`              | A coordenada x do canto superior esquerdo da caixa de texto dentro da imagem gerada. Especifica a posição horizontal da caixa de texto. |
| `y`                  | `INT`              | A coordenada y do canto superior esquerdo da caixa de texto dentro da imagem gerada. Especifica a posição vertical da caixa de texto. |

## Saídas

| Parâmetro            | Tipo Comfy         | Descrição |
|----------------------|--------------------|-------------|
| `conditioning`        | `CONDITIONING`     | A saída de condicionamento enriquecida, que inclui os dados de condicionamento originais juntamente com os parâmetros da caixa de texto e as informações de texto codificadas recém-anexadas. É usada para orientar o modelo generativo na produção de saídas conscientes do contexto. |
