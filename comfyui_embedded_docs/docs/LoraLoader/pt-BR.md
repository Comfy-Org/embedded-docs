> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/pt-BR.md)

Este nó detecta automaticamente modelos localizados na pasta LoRA (incluindo subpastas), sendo o caminho correspondente `ComfyUI\models\loras`. Para mais informações, consulte Instalando Modelos LoRA.

O nó LoRA Loader é usado principalmente para carregar modelos LoRA. Você pode pensar em modelos LoRA como filtros que podem dar às suas imagens estilos, conteúdos e detalhes específicos:

- Aplicar estilos artísticos específicos (como pintura em tinta)
- Adicionar características de certos personagens (como personagens de jogos)
- Adicionar detalhes específicos à imagem
Todos esses efeitos podem ser alcançados através do LoRA.

Se você precisar carregar vários modelos LoRA, pode conectar vários nós diretamente em sequência, como mostrado abaixo:

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
| --- | --- | --- |
| `model` | MODEL | Normalmente usado para conectar ao modelo base |
| `clip` | CLIP | Normalmente usado para conectar ao modelo CLIP |
| `lora_name` | COMBO[STRING] | Selecione o nome do modelo LoRA a ser usado |
| `strength_model` | FLOAT | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração diária de imagens. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados |
| `strength_clip` | FLOAT | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração diária de imagens. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
| --- | --- | --- |
| `model` | MODEL | O modelo com os ajustes LoRA aplicados |
| `clip` | CLIP | A instância CLIP com os ajustes LoRA aplicados |
