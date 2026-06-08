Este nó gera ativos 3D usando a API Rodin. Ele recebe imagens de entrada e as converte em modelos 3D por meio de um serviço externo. O nó gerencia todo o processo, desde a criação da tarefa até o download dos arquivos finais do modelo 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `Imagens` | Imagens de entrada a serem convertidas em modelos 3D. Várias imagens podem ser fornecidas. | IMAGE | Sim | - |
| `Semente` | Valor de semente aleatória para geração (padrão: 0). Defina como 0 para semente aleatória. | INT | Não | 0-65535 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `3D Model Path` | Caminho do arquivo para o modelo 3D gerado (apenas para compatibilidade com versões anteriores) | STRING |
| `GLB` | O modelo 3D gerado no formato GLB | FILE3DGLB |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d3bc71e6a44c11cbeff25351d561e99a7f09ed8ce3544d2968a873b6796512da`
