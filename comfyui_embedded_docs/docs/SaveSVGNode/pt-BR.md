> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/pt-BR.md)

Salva arquivos SVG no disco. Este nó recebe dados SVG como entrada e os salva no seu diretório de saída com opção de incorporar metadados. O nó gerencia automaticamente a nomenclatura dos arquivos com sufixos numéricos e pode incorporar informações do fluxo de trabalho (prompt) diretamente no arquivo SVG.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `svg` | SVG | Sim | - | Os dados SVG a serem salvos no disco |
| `filename_prefix` | STRING | Sim | - | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como %date:yyyy-MM-dd% ou %Empty Latent Image.width% para incluir valores de outros nós. (padrão: "svg/ComfyUI") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `ui` | DICT | Retorna informações do arquivo, incluindo nome do arquivo, subpasta e tipo, para exibição na interface do ComfyUI |

**Observação:** Este nó incorpora automaticamente metadados do fluxo de trabalho (prompt e informações extras do tipo PNG) no arquivo SVG quando disponíveis. Os metadados são inseridos como uma seção CDATA dentro do elemento de metadados do SVG.
