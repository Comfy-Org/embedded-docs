O nó WebcamCapture captura imagens de um dispositivo de webcam e as converte em um formato que pode ser utilizado nos fluxos de trabalho do ComfyUI. Ele herda do nó LoadImage e oferece opções para controlar as dimensões da captura e o momento em que ela ocorre. Quando habilitado, o nó pode capturar novas imagens a cada vez que a fila do fluxo de trabalho for processada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | A fonte de entrada da webcam para capturar imagens | WEBCAM | Sim | - |
| `largura` | A largura desejada para a imagem capturada (padrão: 0, usa a resolução nativa da webcam) | INT | Sim | 0 a MAX_RESOLUTION |
| `altura` | A altura desejada para a imagem capturada (padrão: 0, usa a resolução nativa da webcam) | INT | Sim | 0 a MAX_RESOLUTION |
| `capturar_na_fila` | Quando habilitado, captura uma nova imagem a cada vez que a fila do fluxo de trabalho for processada (padrão: True) | BOOLEAN | Sim | - |

**Observação:** Quando tanto `width` quanto `height` estiverem definidos como 0, o nó utiliza a resolução nativa da webcam. Definir qualquer uma das dimensões com um valor diferente de zero redimensionará a imagem capturada de acordo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `IMAGE` | A imagem capturada da webcam convertida para o formato de imagem do ComfyUI | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WebcamCapture/pt-BR.md)

---
**Source fingerprint (SHA-256):** `551368150fc293309f917eabaa066f223b1fa1a016ffd3643b57b80c83f812cc`
