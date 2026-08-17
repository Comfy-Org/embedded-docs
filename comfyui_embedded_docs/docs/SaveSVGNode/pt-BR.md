# Salvar Nó SVG

Salva arquivos SVG em disco. Este nó recebe dados SVG como entrada e os salva no seu diretório de saída com incorporação opcional de metadados. O nó lida automaticamente com a nomeação de arquivos com sufixos de contador e pode incorporar informações de prompt do fluxo de trabalho diretamente no arquivo SVG.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `svg` | Os dados SVG a serem salvos em disco | SVG | Sim | - |
| `filename_prefix` | O prefixo para o arquivo a ser salvo. Isso pode incluir informações de formatação como %date:yyyy-MM-dd% ou %Empty Latent Image.width% para incluir valores de nós. (padrão: "svg/ComfyUI") | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `svg` | Os dados SVG que foram salvos em disco | SVG |
| `ui` | Retorna informações do arquivo, incluindo nome, subpasta e tipo para exibição na interface do ComfyUI | DICT |

**Nota:** Este nó incorpora automaticamente metadados do fluxo de trabalho (prompt e informações extras de PNG) no arquivo SVG, quando disponíveis. Os metadados são inseridos como uma seção CDATA dentro do elemento de metadados do SVG.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`
