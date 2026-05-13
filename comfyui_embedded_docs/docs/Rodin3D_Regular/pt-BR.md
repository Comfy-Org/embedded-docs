> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Regular/pt-BR.md)

O nó Rodin 3D Regular gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as processa através do serviço Rodin para criar modelos 3D. O nó gerencia todo o fluxo de trabalho, desde a criação da tarefa até o download dos arquivos finais do modelo 3D.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `Imagens` | IMAGE | Sim | - | Imagens de entrada usadas para geração do modelo 3D. Múltiplas imagens podem ser fornecidas. |
| `Semente` | INT | Sim | - | Valor de semente aleatório para resultados reproduzíveis. |
| `Tipo de Material` | STRING | Sim | - | Tipo de material a ser aplicado ao modelo 3D. |
| `Contagem de Polígonos` | STRING | Sim | - | Contagem de polígonos alvo para o modelo 3D gerado. Este parâmetro determina o modo de qualidade e a complexidade da malha. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D gerado (mantido para compatibilidade reversa). |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB. |

---
**Source fingerprint (SHA-256):** `f937be3aa579baf4407434839e741141d6bd63c09b7e0bdc49a9e92a10d7a130`
