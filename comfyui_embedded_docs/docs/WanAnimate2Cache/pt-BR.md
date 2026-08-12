# WanAnimate2Cache

Armazena em cache as ativações por bloco do vídeo de pose uma única vez, para que não precisem ser recalculadas a cada etapa de amostragem, o que reduz aproximadamente pela metade o tempo de geração. A compensação é o uso extra de memória: cerca de 12,5 GB de RAM do sistema na resolução 480x832 com 81 quadros em bf16, escalando com a resolução e o comprimento do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo Wan Animate2 ao qual anexar o cache. | MODEL | Sim | |
| `device` | Onde manter o cache. cpu (RAM) é a opção segura; o cache não cabe na VRAM junto com o modelo em tamanhos típicos. gpu (VRAM) pode ser mais rápido se couber. (padrão: "cpu") | STRING | Sim | "cpu"<br>"gpu" |
| `dtype` | Precisão de armazenamento. default armazena as ativações no dtype de cálculo do modelo. int8 reduz o cache pela metade, int4 o reduz a um quarto, convrot é usado para manter a precisão. (padrão: "default") | STRING | Sim | "default"<br>"int8"<br>"int4" |

Nota: quando janelas de contexto são usadas, cada janela é armazenada em cache separadamente, então o uso de memória aumenta de acordo com o número de janelas. O agendamento static_standard deve ser usado, pois agendamentos uniformes deslocam as janelas a cada etapa e o cache nunca é reutilizado.

## Saídas

| Nome de Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `model` | O modelo clonado com o cache de ativações do vídeo de pose anexado. O cache é liberado automaticamente quando a geração termina. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2Cache/pt-BR.md)

---
**Source fingerprint (SHA-256):** `06305432601afd7c797ef29ef4be3f2bb1aa660e05edde270499e94ccdd54f84`
