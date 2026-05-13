> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/pt-BR.md)

Salva arquivos SVG no disco. Este nó recebe dados SVG como entrada e os salva no diretório de saída, com incorporação opcional de metadados. O nó gerencia automaticamente a nomeação de arquivos com sufixos numéricos e pode incorporar informações do fluxo de trabalho diretamente no arquivo SVG.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `svg` | SVG | Sim | - | Os dados SVG a serem salvos no disco |
| `prefixo_do_arquivo` | STRING | Sim | - | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de nós. (padrão: "svg/ComfyUI") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | DICT | Retorna informações do arquivo, incluindo nome, subpasta e tipo para exibição na interface do ComfyUI |

**Nota:** Este nó incorpora automaticamente metadados do fluxo de trabalho (informações do prompt e dados extras PNG) no arquivo SVG quando disponíveis. Os metadados são inseridos como uma seção CDATA dentro do elemento de metadados do SVG.

---
**Source fingerprint (SHA-256):** `a294103d8d2306ce6765912a98c5572323bb5394909ee384591534b0b404ea70`
