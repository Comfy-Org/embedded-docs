> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen2/pt-BR.md)

O nó Rodin3D_Gen2 gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D com vários tipos de material e contagens de polígonos. O nó gerencia automaticamente todo o processo de geração, incluindo criação de tarefas, verificação de status e download de arquivos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `Imagens` | IMAGE | Sim | - | Imagens de entrada para gerar o modelo 3D |
| `Semente` | INT | Não | 0-65535 | Valor de semente aleatória para geração (padrão: 0) |
| `Tipo de Material` | COMBO | Não | "PBR"<br>"Shaded" | Tipo de material a ser aplicado ao modelo 3D (padrão: "PBR") |
| `Contagem de Polígonos` | COMBO | Não | "4K-Quad"<br>"8K-Quad"<br>"18K-Quad"<br>"50K-Quad"<br>"2K-Triangle"<br>"20K-Triangle"<br>"150K-Triangle"<br>"500K-Triangle" | Contagem de polígonos alvo para o modelo 3D gerado (padrão: "500K-Triangle") |
| `TAPose` | BOOLEAN | Não | - | Se deve aplicar o processamento TAPose (padrão: False) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `Caminho do Modelo 3D` | STRING | Caminho do arquivo para o modelo 3D gerado (para compatibilidade reversa) |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `940712a9a40f4cb07050f3ed7ac502469b30bd364f86bb42b9dd8bf63eb912a2`
