# Carregar Modelo MoGe

Carrega um modelo MoGe (Monocular Geometry) de um arquivo e o prepara para uso em tarefas de estimativa de geometria. Este nó lê um arquivo de modelo da pasta `geometry_estimation` e inicializa o modelo MoGe com seus pesos treinados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model_name` | O nome do arquivo de modelo MoGe a carregar. Selecione entre os arquivos de modelo disponíveis na sua instalação do ComfyUI. | COMBO | Sim | Lista de arquivos de modelo disponíveis na pasta `geometry_estimation` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MOGE_MODEL` | A instância do modelo MoGe carregada, pronta para uso em fluxos de trabalho de estimativa de geometria. | MOGE_MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`
