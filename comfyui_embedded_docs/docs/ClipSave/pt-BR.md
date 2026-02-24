> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/pt-BR.md)

O nó `CLIPSave` é projetado para salvar modelos de codificador de texto CLIP no formato SafeTensors. Este nó faz parte de fluxos de trabalho avançados de fusão de modelos e é tipicamente usado em conjunto com nós como `CLIPMergeSimple` e `CLIPMergeAdd`. Os arquivos salvos utilizam o formato SafeTensors para garantir segurança e compatibilidade.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Valor Padrão | Descrição |
|-----------|-----------|----------|---------------|-------------|
| `clip` | CLIP | Sim | - | O modelo CLIP a ser salvo |
| `filename_prefix` | STRING | Sim | "clip/ComfyUI" | O caminho prefixo para o arquivo salvo |
| `prompt` | PROMPT | Oculto | - | Informações do prompt do fluxo de trabalho (para metadados) |
| `extra_pnginfo` | EXTRA_PNGINFO | Oculto | - | Informações PNG adicionais (para metadados) |

## Saídas

Este nó não possui tipos de saída definidos. Ele salva os arquivos processados na pasta `ComfyUI/output/`.

### Estratégia de Salvamento Multi-arquivo

O nó salva diferentes componentes com base no tipo de modelo CLIP:

| Tipo de Prefixo | Sufixo do Arquivo | Descrição |
|------------|-------------|-------------|
| `clip_l.` | `_clip_l` | Codificador de texto CLIP-L |
| `clip_g.` | `_clip_g` | Codificador de texto CLIP-G |
| Prefixo vazio | Sem sufixo | Outros componentes CLIP |

## Notas de Uso

1. **Localização do Arquivo**: Todos os arquivos são salvos no diretório `ComfyUI/output/`
2. **Formato do Arquivo**: Os modelos são salvos no formato SafeTensors por segurança
3. **Metadados**: Inclui informações do fluxo de trabalho e metadados PNG, se disponíveis
4. **Convenção de Nomenclatura**: Utiliza o prefixo especificado mais os sufixos apropriados com base no tipo de modelo
