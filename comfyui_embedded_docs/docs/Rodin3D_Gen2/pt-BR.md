O nó Rodin3D_Gen2 gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D com vários tipos de material e contagens de polígonos. O nó gerencia automaticamente todo o processo de geração, incluindo criação de tarefas, verificação de status e download de arquivos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `Imagens` | Imagens de entrada para gerar o modelo 3D | IMAGE | Sim | - |
| `Semente` | Valor de semente aleatória para geração (padrão: 0) | INT | Não | 0-65535 |
| `Tipo de Material` | Tipo de material a ser aplicado ao modelo 3D (padrão: "PBR") | COMBO | Não | "PBR"<br>"Shaded" |
| `Contagem de Polígonos` | Contagem de polígonos alvo para o modelo 3D gerado (padrão: "500K-Triangle") | COMBO | Não | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" |
| `TAPose` | Se deve aplicar o processamento TAPose (padrão: False) | BOOLEAN | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `Caminho do Modelo 3D` | Caminho do arquivo para o modelo 3D gerado (para compatibilidade reversa) | STRING |
| `GLB` | O modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
