# Carregar LoRA

Este nó detecta automaticamente os modelos localizados na pasta LoRA (incluindo subpastas), com o caminho do modelo correspondente sendo `ComfyUI\models\loras`. Para mais informações, consulte Instalação de Modelos LoRA

O nó Carregador de LoRA é usado principalmente para carregar modelos LoRA. Você pode pensar nos modelos LoRA como filtros que podem dar às suas imagens estilos, conteúdos e detalhes específicos:

- Aplicar estilos artísticos específicos (como pintura a nanquim)
- Adicionar características de certos personagens (como personagens de jogos)
- Adicionar detalhes específicos à imagem
Tudo isso pode ser alcançado através do LoRA.

Se você precisar carregar vários modelos LoRA, pode simplesmente encadear vários nós diretamente, conforme mostrado abaixo:

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | Geralmente usado para conectar ao modelo base | MODEL |
| `clip` | Geralmente usado para conectar ao modelo CLIP | CLIP |
| `nome_do_lora` | Selecione o nome do modelo LoRA a ser usado | COMBO[STRING] |
| `força_modelo` | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração de imagens do dia a dia. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados | FLOAT |
| `força_clip` | Faixa de valores de -100.0 a 100.0, normalmente usado entre 0~1 para geração de imagens do dia a dia. Valores mais altos resultam em efeitos de ajuste do modelo mais pronunciados | FLOAT |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo com ajustes LoRA aplicados | MODEL |
| `clip` | A instância CLIP com ajustes LoRA aplicados | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/pt-BR.md)
