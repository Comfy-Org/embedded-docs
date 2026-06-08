O nó ModelMergeFlux1 mescla dois modelos de difusão combinando seus componentes por meio de interpolação ponderada. Ele permite controle refinado sobre como diferentes partes dos modelos são combinadas, incluindo blocos de processamento de imagem, camadas de incorporação temporal, mecanismos de orientação, entradas vetoriais, codificadores de texto e vários blocos transformadores. Isso possibilita criar modelos híbridos com características personalizadas a partir de dois modelos de origem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | Primeiro modelo de origem para mesclar | MODEL | Sim | - |
| `model2` | Segundo modelo de origem para mesclar | MODEL | Sim | - |
| `img_in.` | Peso de interpolação da entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `time_in.` | Peso de interpolação da incorporação temporal (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `guidance_in` | Peso de interpolação do mecanismo de orientação (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `vector_in.` | Peso de interpolação da entrada vetorial (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `txt_in.` | Peso de interpolação do codificador de texto (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.0.` | Peso de interpolação do bloco duplo 0 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.1.` | Peso de interpolação do bloco duplo 1 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.2.` | Peso de interpolação do bloco duplo 2 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.3.` | Peso de interpolação do bloco duplo 3 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.4.` | Peso de interpolação do bloco duplo 4 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.5.` | Peso de interpolação do bloco duplo 5 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.6.` | Peso de interpolação do bloco duplo 6 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.7.` | Peso de interpolação do bloco duplo 7 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.8.` | Peso de interpolação do bloco duplo 8 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.9.` | Peso de interpolação do bloco duplo 9 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.10.` | Peso de interpolação do bloco duplo 10 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.11.` | Peso de interpolação do bloco duplo 11 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.12.` | Peso de interpolação do bloco duplo 12 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.13.` | Peso de interpolação do bloco duplo 13 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.14.` | Peso de interpolação do bloco duplo 14 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.15.` | Peso de interpolação do bloco duplo 15 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.16.` | Peso de interpolação do bloco duplo 16 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.17.` | Peso de interpolação do bloco duplo 17 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `double_blocks.18.` | Peso de interpolação do bloco duplo 18 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.0.` | Peso de interpolação do bloco simples 0 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.1.` | Peso de interpolação do bloco simples 1 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.2.` | Peso de interpolação do bloco simples 2 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.3.` | Peso de interpolação do bloco simples 3 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.4.` | Peso de interpolação do bloco simples 4 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.5.` | Peso de interpolação do bloco simples 5 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.6.` | Peso de interpolação do bloco simples 6 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.7.` | Peso de interpolação do bloco simples 7 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.8.` | Peso de interpolação do bloco simples 8 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.9.` | Peso de interpolação do bloco simples 9 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.10.` | Peso de interpolação do bloco simples 10 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.11.` | Peso de interpolação do bloco simples 11 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.12.` | Peso de interpolação do bloco simples 12 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.13.` | Peso de interpolação do bloco simples 13 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.14.` | Peso de interpolação do bloco simples 14 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.15.` | Peso de interpolação do bloco simples 15 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.16.` | Peso de interpolação do bloco simples 16 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.17.` | Peso de interpolação do bloco simples 17 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.18.` | Peso de interpolação do bloco simples 18 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.19.` | Peso de interpolação do bloco simples 19 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.20.` | Peso de interpolação do bloco simples 20 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.21.` | Peso de interpolação do bloco simples 21 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.22.` | Peso de interpolação do bloco simples 22 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.23.` | Peso de interpolação do bloco simples 23 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.24.` | Peso de interpolação do bloco simples 24 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.25.` | Peso de interpolação do bloco simples 25 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.26.` | Peso de interpolação do bloco simples 26 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.27.` | Peso de interpolação do bloco simples 27 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.28.` | Peso de interpolação do bloco simples 28 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.29.` | Peso de interpolação do bloco simples 29 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.30.` | Peso de interpolação do bloco simples 30 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.31.` | Peso de interpolação do bloco simples 31 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.32.` | Peso de interpolação do bloco simples 32 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.33.` | Peso de interpolação do bloco simples 33 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.34.` | Peso de interpolação do bloco simples 34 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.35.` | Peso de interpolação do bloco simples 35 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.36.` | Peso de interpolação do bloco simples 36 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `single_blocks.37.` | Peso de interpolação do bloco simples 37 (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `final_layer.` | Peso de interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a632133b5d4bc7c5a4e1be5f6f779e424a491fffb8ef7702346adc4acf6f23bc`
