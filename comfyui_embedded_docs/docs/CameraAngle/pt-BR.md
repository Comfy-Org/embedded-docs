# Compose Camera Angle Prompt

Este nó escolhe um ângulo de câmera ao redor de um sujeito e transforma essa escolha em duas coisas: uma estrutura `camera_info` que nós 3D podem renderizar, e uma descrição de plano em inglês simples que você pode colar em um prompt. O sujeito fica na origem da cena, onde nós 3D posteriores centralizam seus modelos, para que o ângulo escolhido aqui corresponda à pré-visualização.

Use-o para enquadrar um render antes de gerar, ou para descrever um ponto de vista como `front view eye-level shot medium shot` para um modelo de imagem ou vídeo. A pré-visualização 3D no nó mostra a posição resultante da câmera.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `horizontal_angle` | Azimute ao redor do sujeito em graus: 0 é a frente, 90 o lado direito e 180 a parte de trás. (padrão: 0) | INT | Sim | 0 a 360 |
| `vertical_angle` | Elevação em graus. Valores negativos olham de baixo para cima; valores positivos olham de cima para baixo. (padrão: 0) | INT | Sim | -30 a 60 |
| `zoom` | Zoom da lente no sujeito: 0 é um plano aberto, 10 é um close-up. O valor também é propagado para `camera_info.zoom`. (padrão: 5.0) | FLOAT | Sim | 0.0 a 10.0 (passo 0.1) |
| `image` | Imagem de referência opcional, exibida na face frontal do cubo do sujeito na pré-visualização 3D. | IMAGE | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `camera_info` | Informações da câmera para nós 3D: posição, alvo de mira, fator de zoom, tipo de câmera e campo de visão. A câmera mantém um campo de visão fixo de 35 graus e é posicionada a 6 unidades do alvo. | LOAD3DCAMERA |
| `prompt` | Descrição curta do plano construída a partir do ângulo, da elevação e da distância, por exemplo `front view eye-level shot medium shot`. | STRING |

## Termos da Descrição do Plano

A saída `prompt` combina um termo de cada grupo abaixo. Os valores são limitados primeiro aos intervalos dos widgets.

- O ângulo horizontal é dividido em oito setores de 45 graus: `front view`, `front-right quarter view`, `right side view`, `back-right quarter view`, `back view`, `back-left quarter view`, `left side view`, `front-left quarter view`.
- O ângulo vertical se torna `low-angle shot` abaixo de -15 graus, `eye-level shot` abaixo de 15, `elevated shot` abaixo de 45, e `high-angle shot` a partir de 45 graus.
- O zoom se torna `wide shot` abaixo de 2, `medium shot` abaixo de 6, e `close-up` em 6 ou mais.

O fator `camera_info.zoom` mapeia o valor do widget para o intervalo de 1.0 a 1.875, de modo que zoom 0 resulta em 1.0 e zoom 10 resulta em 1.875.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CameraAngle/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8ed2cd186bc6ca02dbc8da006b2e9156245ef691a2257f286f6e32ffa480fd5d`
