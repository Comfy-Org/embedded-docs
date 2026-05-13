> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/pt-BR.md)

Este nó detecta automaticamente os modelos localizados na pasta LoRA (incluindo subpastas), com o caminho do modelo correspondente sendo `ComfyUI\models\loras`. Para mais informações, consulte Instalação de Modelos LoRA

O nó Carregador de LoRA é usado principalmente para carregar modelos LoRA. Você pode pensar nos modelos LoRA como filtros que podem dar às suas imagens estilos, conteúdos e detalhes específicos:

- Aplicar estilos artísticos específicos (como pintura a nanquim)
- Adicionar características de certos personagens (como personagens de jogos)
- Adicionar detalhes específicos à imagem
Tudo isso pode ser alcançado através do LoRA.

Se você precisar carregar vários modelos LoRA, pode simplesmente encadear vários nós diretamente, conforme mostrado abaixo:

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
| --- | --- | --- |
| `modelo` | MODEL | Geralmente usado para conectar ao modelo base |
| `clip` | CLIP | Geralmente usado para conectar ao modelo CLIP |
| `nome_do_lora` | COMBO[STRING] | Selecione o nome do modelo LoRA a ser usado |
| `força_modelo` | FLOAT | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração de imagens do dia a dia. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados |
| `força_clip` | FLOAT | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração de imagens do dia a dia. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
| --- | --- | --- |
| `modelo` | MODEL | O modelo com ajustes LoRA aplicados |
| `clip` | CLIP | A instância CLIP com ajustes LoRA aplicados |