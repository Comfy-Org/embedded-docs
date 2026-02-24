> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/pt-BR.md)

O nó WebcamCapture captura imagens de um dispositivo de webcam e as converte em um formato que pode ser usado nos fluxos de trabalho do ComfyUI. Ele herda do nó LoadImage e fornece opções para controlar as dimensões e o momento da captura. Quando habilitado, o nó pode capturar novas imagens sempre que a fila de processamento do fluxo de trabalho é executada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | WEBCAM | Sim | - | A fonte de entrada da webcam para capturar imagens |
| `width` | INT | Não | 0 a MAX_RESOLUTION | A largura desejada para a imagem capturada (padrão: 0, usa a resolução nativa da webcam) |
| `height` | INT | Não | 0 a MAX_RESOLUTION | A altura desejada para a imagem capturada (padrão: 0, usa a resolução nativa da webcam) |
| `capture_on_queue` | BOOLEAN | Não | - | Quando habilitado, captura uma nova imagem cada vez que a fila de processamento do fluxo de trabalho é executada (padrão: True) |

**Observação:** Quando tanto `width` quanto `height` estão definidos como 0, o nó usa a resolução nativa da webcam. Definir qualquer dimensão para um valor diferente de zero redimensionará a imagem capturada de acordo.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | A imagem da webcam capturada, convertida para o formato de imagem do ComfyUI |
