> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/pt-BR.md)

Este nó gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D por meio de um serviço externo. O nó gerencia todo o processo, desde a criação da tarefa até o download dos arquivos finais do modelo 3D.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `Imagens` | IMAGE | Sim | - | Imagens de entrada a serem convertidas em modelos 3D. Várias imagens podem ser fornecidas. |
| `Semente` | INT | Não | 0-65535 | Valor de semente aleatória para geração (padrão: 0). Defina como 0 para semente aleatória. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `3D Model Path` | STRING | Caminho do arquivo para o modelo 3D gerado (apenas para compatibilidade com versões anteriores) |
| `GLB` | FILE3DGLB | O modelo 3D gerado no formato GLB |

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
