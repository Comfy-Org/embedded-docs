O nó **Rodin 3D Detail** gera ativos 3D detalhados usando a API Rodin. Ele recebe imagens de entrada e as processa através do serviço Rodin para criar modelos 3D de alta qualidade com geometria e materiais detalhados. O nó gerencia todo o fluxo de trabalho, desde a criação da tarefa até o download do arquivo final do modelo 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `Imagens` | Imagens de entrada usadas para a geração do modelo 3D. Múltiplas imagens podem ser fornecidas. | IMAGE | Sim | - |
| `Semente` | Valor de semente aleatório para resultados reproduzíveis | INT | Sim | - |
| `Tipo de Material` | Tipo de material a ser aplicado ao modelo 3D | STRING | Sim | - |
| `Contagem de Polígonos` | Contagem de polígonos alvo para o modelo 3D gerado. Determina o nível de qualidade da malha. | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `3D Model Path` | Caminho do arquivo para o modelo 3D gerado (apenas para compatibilidade reversa) | STRING |
| `GLB` | O modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Detail/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ed9ed2c8a55ca80d18da88ee2703c66057a09beeac7163fc270d81a492417b0a`
