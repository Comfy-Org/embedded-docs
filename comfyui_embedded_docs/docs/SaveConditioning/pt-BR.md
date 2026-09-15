# Salvar Condicionamento

Este nó salva um único condicionamento na pasta de saída como um arquivo safetensors. O arquivo salvo pode ser movido para a pasta models/embeddings e carregado posteriormente com Load Conditioning, por exemplo, para pular o codificador de texto. O nó repassa o condicionamento sem alterações, para que ele ainda possa ser usado posteriormente no fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | O condicionamento a ser salvo. Apenas uma única entrada de condicionamento é suportada. | CONDITIONING | Sim | - |
| `filename_prefix` | Prefixo usado para montar o nome do arquivo de saída. O arquivo é gravado na pasta de saída com um contador numérico anexado. Padrão: `conditioning/ComfyUI` | STRING | Sim | - |

**Observações:**

- Se a entrada `conditioning` contiver mais de uma entrada (por exemplo, após combinar condicionamentos), o nó gera um erro: "O Save Conditioning oferece suporte a apenas uma entrada de condicionamento; salve-a antes de combinar."
- Opções de condicionamento que são tensores, listas/tuplas de tensores, booleanos, inteiros, floats ou strings são salvas junto com o condicionamento. Opções que são `None` são ignoradas. Qualquer outro tipo de opção gera um erro informando que a opção não pode ser salva.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `conditioning` | O mesmo condicionamento que foi passado, sem alterações. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
