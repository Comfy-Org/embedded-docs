# Carregador de Codificador de Texto LTXV Áudio

Este nó carrega um codificador de texto especializado para o modelo de áudio LTXV. Ele combina um arquivo de codificador de texto específico com um arquivo de checkpoint para criar um modelo CLIP que pode ser usado para tarefas de condicionamento de texto relacionadas a áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `text_encoder` | O nome do arquivo do modelo de codificador de texto LTXV a ser carregado. As opções disponíveis são carregadas da pasta `text_encoders`. | STRING | Sim | Múltiplas opções disponíveis |
| `ckpt_name` | O nome do arquivo do checkpoint a ser carregado. As opções disponíveis são carregadas da pasta `checkpoints`. | STRING | Sim | Múltiplas opções disponíveis |
| `device` | Especifica o dispositivo para carregar o modelo. Use `"cpu"` para forçar o carregamento na CPU. O comportamento padrão (`"default"`) usa a alocação automática de dispositivo do sistema. | STRING | Não | `"default"`<br>`"cpu"` |

**Observação:** Os parâmetros `text_encoder` e `ckpt_name` funcionam em conjunto. O nó carrega ambos os arquivos especificados para criar um único modelo CLIP funcional. Os arquivos devem ser compatíveis com a arquitetura LTXV.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip` | O modelo CLIP LTXV carregado, pronto para ser usado na codificação de prompts de texto para geração de áudio. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c072a0b3393aa44333bb15ae42179c50868a4e9d7ca706d6c7da5922625373e6`
