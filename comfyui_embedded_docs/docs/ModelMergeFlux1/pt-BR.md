> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/pt-BR.md)

O nó ModelMergeFlux1 mescla dois modelos de difusão combinando seus componentes por meio de interpolação ponderada. Ele permite controle refinado sobre como diferentes partes dos modelos são combinadas, incluindo blocos de processamento de imagem, camadas de incorporação temporal, mecanismos de orientação, entradas vetoriais, codificadores de texto e vários blocos transformadores. Isso possibilita criar modelos híbridos com características personalizadas a partir de dois modelos de origem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model1` | MODEL | Sim | - | Primeiro modelo de origem para mesclar |
| `model2` | MODEL | Sim | - | Segundo modelo de origem para mesclar |
| `img_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação da entrada de imagem (padrão: 1.0) |
| `time_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação da incorporação temporal (padrão: 1.0) |
| `guidance_in` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do mecanismo de orientação (padrão: 1.0) |
| `vector_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação da entrada vetorial (padrão: 1.0) |
| `txt_in.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do codificador de texto (padrão: 1.0) |
| `double_blocks.0.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 0 (padrão: 1.0) |
| `double_blocks.1.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 1 (padrão: 1.0) |
| `double_blocks.2.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 2 (padrão: 1.0) |
| `double_blocks.3.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 3 (padrão: 1.0) |
| `double_blocks.4.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 4 (padrão: 1.0) |
| `double_blocks.5.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 5 (padrão: 1.0) |
| `double_blocks.6.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 6 (padrão: 1.0) |
| `double_blocks.7.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 7 (padrão: 1.0) |
| `double_blocks.8.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 8 (padrão: 1.0) |
| `double_blocks.9.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 9 (padrão: 1.0) |
| `double_blocks.10.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 10 (padrão: 1.0) |
| `double_blocks.11.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 11 (padrão: 1.0) |
| `double_blocks.12.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 12 (padrão: 1.0) |
| `double_blocks.13.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 13 (padrão: 1.0) |
| `double_blocks.14.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 14 (padrão: 1.0) |
| `double_blocks.15.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 15 (padrão: 1.0) |
| `double_blocks.16.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 16 (padrão: 1.0) |
| `double_blocks.17.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 17 (padrão: 1.0) |
| `double_blocks.18.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco duplo 18 (padrão: 1.0) |
| `single_blocks.0.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 0 (padrão: 1.0) |
| `single_blocks.1.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 1 (padrão: 1.0) |
| `single_blocks.2.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 2 (padrão: 1.0) |
| `single_blocks.3.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 3 (padrão: 1.0) |
| `single_blocks.4.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 4 (padrão: 1.0) |
| `single_blocks.5.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 5 (padrão: 1.0) |
| `single_blocks.6.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 6 (padrão: 1.0) |
| `single_blocks.7.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 7 (padrão: 1.0) |
| `single_blocks.8.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 8 (padrão: 1.0) |
| `single_blocks.9.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 9 (padrão: 1.0) |
| `single_blocks.10.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 10 (padrão: 1.0) |
| `single_blocks.11.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 11 (padrão: 1.0) |
| `single_blocks.12.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 12 (padrão: 1.0) |
| `single_blocks.13.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 13 (padrão: 1.0) |
| `single_blocks.14.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 14 (padrão: 1.0) |
| `single_blocks.15.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 15 (padrão: 1.0) |
| `single_blocks.16.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 16 (padrão: 1.0) |
| `single_blocks.17.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 17 (padrão: 1.0) |
| `single_blocks.18.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 18 (padrão: 1.0) |
| `single_blocks.19.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 19 (padrão: 1.0) |
| `single_blocks.20.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 20 (padrão: 1.0) |
| `single_blocks.21.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 21 (padrão: 1.0) |
| `single_blocks.22.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 22 (padrão: 1.0) |
| `single_blocks.23.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 23 (padrão: 1.0) |
| `single_blocks.24.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 24 (padrão: 1.0) |
| `single_blocks.25.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 25 (padrão: 1.0) |
| `single_blocks.26.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 26 (padrão: 1.0) |
| `single_blocks.27.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 27 (padrão: 1.0) |
| `single_blocks.28.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 28 (padrão: 1.0) |
| `single_blocks.29.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 29 (padrão: 1.0) |
| `single_blocks.30.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 30 (padrão: 1.0) |
| `single_blocks.31.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 31 (padrão: 1.0) |
| `single_blocks.32.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 32 (padrão: 1.0) |
| `single_blocks.33.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 33 (padrão: 1.0) |
| `single_blocks.34.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 34 (padrão: 1.0) |
| `single_blocks.35.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 35 (padrão: 1.0) |
| `single_blocks.36.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 36 (padrão: 1.0) |
| `single_blocks.37.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação do bloco simples 37 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 a 1.0 | Peso de interpolação da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo mesclado combinando características de ambos os modelos de entrada |

---
**Source fingerprint (SHA-256):** `a632133b5d4bc7c5a4e1be5f6f779e424a491fffb8ef7702346adc4acf6f23bc`
