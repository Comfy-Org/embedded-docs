# Amostrar Quadro de Vídeo

O nó `VideoFrameSample` extrai um número fixo de quadros de um vídeo usando uma de quatro estratégias. Para as estratégias contíguas "head" e "tail", a saída é uma referência de vídeo lazy (os quadros não são decodificados); para as estratégias não contíguas "uniform" e "random", apenas os quadros selecionados são decodificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-----------|--------------|-------------|-----------|
| `vídeo` | Vídeo de entrada. | VIDEO | Sim | – |
| `número_de_quadros` | Número de quadros a serem amostrados (padrão: 16). | INT | Sim | 1 – 9999 |
| `estratégia` | uniform: espaçados uniformemente, head: primeiros N, tail: últimos N, random: ordem aleatória (padrão: "uniform"). | COMBO | Sim | "uniform"<br>"head"<br>"tail"<br>"random" |
| `semente` | Semente aleatória, usada apenas com a estratégia "random" (padrão: 0). | INT | Sim | 0 – 18446744073709551615 |

- O valor de `num_frames` é automaticamente limitado ao número total de quadros do vídeo de entrada.
- O parâmetro `seed` não tem efeito a menos que `strategy` esteja definido como `"random"`.
- Quando `strategy` é `"uniform"` e `num_frames` é 1, o quadro central do vídeo é selecionado.
- Um valor de `strategy` não reconhecido gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `vídeo` | Vídeo amostrado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/pt-BR.md)

---
**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`
