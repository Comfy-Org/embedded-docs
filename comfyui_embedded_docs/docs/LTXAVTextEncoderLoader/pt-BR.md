> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/pt-BR.md)

Este nó carrega um codificador de texto especializado para o modelo de áudio LTXV. Ele combina um arquivo específico de codificador de texto com um arquivo de checkpoint para criar um modelo CLIP que pode ser usado para tarefas de condicionamento de texto relacionadas a áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `text_encoder` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo do modelo codificador de texto LTXV a ser carregado. As opções disponíveis são carregadas da pasta `text_encoders`. |
| `ckpt_name` | STRING | Sim | Múltiplas opções disponíveis | O nome do arquivo do checkpoint a ser carregado. As opções disponíveis são carregadas da pasta `checkpoints`. |
| `device` | STRING | Não | `"default"`<br>`"cpu"` | Especifica o dispositivo no qual carregar o modelo. Use `"cpu"` para forçar o carregamento na CPU. O comportamento padrão (`"default"`) usa o posicionamento automático de dispositivo do sistema. |

**Observação:** Os parâmetros `text_encoder` e `ckpt_name` funcionam em conjunto. O nó carrega ambos os arquivos especificados para criar um único modelo CLIP funcional. Os arquivos devem ser compatíveis com a arquitetura LTXV.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `clip` | CLIP | O modelo CLIP LTXV carregado, pronto para ser usado na codificação de prompts de texto para geração de áudio. |
