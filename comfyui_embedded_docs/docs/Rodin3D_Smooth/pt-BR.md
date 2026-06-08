O nó Rodin 3D Smooth gera ativos 3D usando a API Rodin, processando imagens de entrada e convertendo-as em modelos 3D suaves. Ele recebe múltiplas imagens como entrada e produz um arquivo de modelo 3D para download. O nó gerencia todo o processo de geração, incluindo criação de tarefas, monitoramento de status e download automático de arquivos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `Imagens` | Imagens de entrada para usar na geração do modelo 3D. Várias imagens podem ser fornecidas. | IMAGE | Sim | - |
| `Semente` | Valor de semente aleatório para consistência na geração. | INT | Sim | - |
| `Tipo de Material` | Tipo de material a ser aplicado ao modelo 3D. | STRING | Sim | - |
| `Contagem de Polígonos` | Contagem de polígonos alvo para o modelo 3D gerado. Determina a qualidade da malha e o nível de detalhe. | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `3D Model Path` | Caminho do arquivo para o modelo 3D baixado (apenas para compatibilidade reversa). | STRING |
| `GLB` | O modelo 3D gerado no formato GLB. | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/pt-BR.md)

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
