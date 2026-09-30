# ModelPatchLoader

O nó ModelPatchLoader carrega um arquivo de patch de modelo da pasta `model_patches` e o prepara para uso em um fluxo de trabalho. Ele detecta automaticamente o tipo de patch contido no arquivo, constrói a arquitetura correspondente, carrega os pesos salvos e envolve tudo em um model patcher para que possa ser aplicado a outros modelos. Ele oferece suporte a muitos formatos especializados de patch, incluindo ramificações adicionais de ControlNet, modelos de incorporação de recursos, adaptadores, módulos de orientação de animação/LLLite e módulos semelhantes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome` | O nome do arquivo do patch de modelo a ser carregado da pasta `model_patches`. Selecione um dos arquivos de patch disponíveis na lista. | COMBO | Sim | Lista gerada dinamicamente de todos os arquivos de patch de modelo encontrados na pasta `model_patches` |

Observação: este nó está marcado como experimental. O tipo de patch é detectado automaticamente a partir do conteúdo do arquivo, portanto, nenhuma seleção manual de tipo é necessária. O nó lê os metadados do checkpoint e inspeciona as chaves de peso para decidir qual arquitetura construir (por exemplo, Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, projeção de características SigLIP, cabeça de duração Lightricks, Anima LLLite, MultiTalk ou SUPIR). Os pesos são carregados com o carregamento seguro habilitado, e o modelo é colocado no dispositivo de offload dentro de um `CoreModelPatcher` para que possa ser aplicado posteriormente a outro modelo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL_PATCH` | O patch de modelo carregado envolvido em um model patcher, pronto para ser aplicado a um modelo no fluxo de trabalho | MODEL_PATCH |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`
