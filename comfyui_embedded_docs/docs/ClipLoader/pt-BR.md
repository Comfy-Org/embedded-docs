> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPLoader/pt-BR.md)

Este nó é usado principalmente para carregar modelos de codificador de texto CLIP de forma independente.
Os arquivos de modelo podem ser detectados nos seguintes caminhos:

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> Se você salvar um modelo após o ComfyUI ter iniciado, será necessário atualizar a interface do ComfyUI para obter a lista mais recente de caminhos de arquivos de modelo.

Formatos de modelo suportados:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

Para mais detalhes sobre o carregamento mais recente de arquivos de modelo, consulte [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## Entradas

| Parâmetro     | Tipo de Dados | Descrição |
|---------------|---------------|-------------|
| `clip_name`   | COMBO[STRING] | Especifica o nome do modelo CLIP a ser carregado. Este nome é usado para localizar o arquivo do modelo dentro de uma estrutura de diretórios predefinida. |
| `type`        | COMBO[STRING] | Determina o tipo de modelo CLIP a ser carregado. Conforme o ComfyUI suporta mais modelos, novos tipos serão adicionados aqui. Por favor, verifique a definição da classe `CLIPLoader` em [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) para obter detalhes. |
| `device`      | COMBO[STRING] | Escolha o dispositivo para carregar o modelo CLIP. `default` executará o modelo na GPU, enquanto selecionar `CPU` forçará o carregamento na CPU. |

### Explicação das Opções de Dispositivo

**Quando escolher "default":**

- Ter memória de GPU suficiente
- Desejar o melhor desempenho
- Permitir que o sistema otimize o uso de memória automaticamente

**Quando escolher "cpu":**

- Memória de GPU insuficiente
- Necessidade de reservar memória de GPU para outros modelos (como UNet)
- Execução em um ambiente com VRAM limitada
- Necessidades de depuração ou propósitos especiais

**Impacto no Desempenho**

Executar na CPU será muito mais lento do que na GPU, mas pode economizar valiosa memória de GPU para outros componentes de modelo mais importantes. Em ambientes com restrições de memória, colocar o modelo CLIP na CPU é uma estratégia de otimização comum.

### Combinações Suportadas

| Tipo de Modelo | Codificador Correspondente |
|------------|---------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

Conforme o ComfyUI é atualizado, essas combinações podem se expandir. Para detalhes, consulte a definição da classe `CLIPLoader` em [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `clip`    | CLIP      | O modelo CLIP carregado, pronto para uso em tarefas subsequentes ou processamento adicional. |

## Notas Adicionais

Os modelos CLIP desempenham um papel central como codificadores de texto no ComfyUI, responsáveis por converter prompts de texto em representações numéricas que os modelos de difusão podem entender. Você pode pensar neles como tradutores, responsáveis por traduzir seu texto para uma linguagem que os modelos grandes possam compreender. É claro que diferentes modelos têm seus próprios "dialetos", portanto, diferentes codificadores CLIP são necessários entre diferentes arquiteturas para completar o processo de codificação de texto.
