# Carregador de Codificador de Texto LTXV Áudio

Este nó carrega um codificador de texto especializado para o modelo de áudio LTXV. Ele combina um arquivo de codificador de texto com um arquivo de checkpoint para criar um modelo CLIP que pode ser usado em tarefas de condicionamento de texto relacionadas a áudio. De acordo com a descrição da receita do nó, o codificador de texto de áudio LTXV deve ser um modelo Gemma 3 12B ou um modelo Gemma 4 correspondente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `text_encoder` | O nome do arquivo do modelo de codificador de texto LTXV a ser carregado. As opções disponíveis são carregadas da pasta `text_encoders`. | COMBO | Sim | Várias opções disponíveis |
| `ckpt_name` | O nome do arquivo de checkpoint a ser carregado. As opções disponíveis são carregadas da pasta `checkpoints`. | COMBO | Sim | Várias opções disponíveis |
| `device` | Especifica o dispositivo no qual o modelo será carregado. Use `"cpu"` para forçar o carregamento na CPU. O comportamento padrão (`"default"`) usa a alocação automática de dispositivo do sistema (padrão: `"default"`). | COMBO | Não | `"default"`<br>`"cpu"` |

**Nota:** Os parâmetros `text_encoder` e `ckpt_name` funcionam em conjunto. O nó carrega os dois arquivos especificados para criar um único modelo CLIP funcional. Os arquivos devem ser compatíveis com a arquitetura LTXV.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `clip` | O modelo CLIP LTXV carregado, pronto para ser usado na codificação de prompts de texto para geração de áudio. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`
