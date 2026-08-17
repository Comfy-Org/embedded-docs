# ModelMergeFlux1

O nó **ModelMergeFlux1** mescla dois modelos de difusão combinando seus componentes por meio de interpolação ponderada. Ele oferece controle detalhado sobre como diferentes partes dos modelos são combinadas, incluindo blocos de processamento de imagem, camadas de incorporação temporal, mecanismos de orientação, entradas vetoriais, codificadores de texto e blocos de transformadores. Isso permite criar modelos híbridos com características personalizadas a partir de dois modelos de origem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | Primeiro modelo de origem para mesclar | MODEL | Sim | - |
| `model2` | Segundo modelo de origem para mesclar | MODEL | Sim | - |
| `img_in.` | Peso da interpolação da entrada de imagem (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `time_in.` | Peso da interpolação da incorporação temporal (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `guidance_in` | Peso da interpolação do mecanismo de orientação (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `vector_in.` | Peso da interpolação da entrada vetorial (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `txt_in.` | Peso da interpolação do codificador de texto (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.0.` | Peso da interpolação do bloco duplo 0 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.1.` | Peso da interpolação do bloco duplo 1 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.2.` | Peso da interpolação do bloco duplo 2 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.3.` | Peso da interpolação do bloco duplo 3 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.4.` | Peso da interpolação do bloco duplo 4 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.5.` | Peso da interpolação do bloco duplo 5 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.6.` | Peso da interpolação do bloco duplo 6 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.7.` | Peso da interpolação do bloco duplo 7 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.8.` | Peso da interpolação do bloco duplo 8 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.9.` | Peso da interpolação do bloco duplo 9 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.10.` | Peso da interpolação do bloco duplo 10 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.11.` | Peso da interpolação do bloco duplo 11 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.12.` | Peso da interpolação do bloco duplo 12 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.13.` | Peso da interpolação do bloco duplo 13 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.14.` | Peso da interpolação do bloco duplo 14 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.15.` | Peso da interpolação do bloco duplo 15 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.16.` | Peso da interpolação do bloco duplo 16 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.17.` | Peso da interpolação do bloco duplo 17 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `double_blocks.18.` | Peso da interpolação do bloco duplo 18 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.0.` | Peso da interpolação do bloco único 0 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.1.` | Peso da interpolação do bloco único 1 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.2.` | Peso da interpolação do bloco único 2 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.3.` | Peso da interpolação do bloco único 3 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.4.` | Peso da interpolação do bloco único 4 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.5.` | Peso da interpolação do bloco único 5 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.6.` | Peso da interpolação do bloco único 6 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.7.` | Peso da interpolação do bloco único 7 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.8.` | Peso da interpolação do bloco único 8 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.9.` | Peso da interpolação do bloco único 9 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.10.` | Peso da interpolação do bloco único 10 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.11.` | Peso da interpolação do bloco único 11 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.12.` | Peso da interpolação do bloco único 12 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.13.` | Peso da interpolação do bloco único 13 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.14.` | Peso da interpolação do bloco único 14 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.15.` | Peso da interpolação do bloco único 15 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.16.` | Peso da interpolação do bloco único 16 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.17.` | Peso da interpolação do bloco único 17 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.18.` | Peso da interpolação do bloco único 18 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.19.` | Peso da interpolação do bloco único 19 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.20.` | Peso da interpolação do bloco único 20 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.21.` | Peso da interpolação do bloco único 21 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.22.` | Peso da interpolação do bloco único 22 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.23.` | Peso da interpolação do bloco único 23 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.24.` | Peso da interpolação do bloco único 24 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.25.` | Peso da interpolação do bloco único 25 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.26.` | Peso da interpolação do bloco único 26 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.27.` | Peso da interpolação do bloco único 27 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.28.` | Peso da interpolação do bloco único 28 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.29.` | Peso da interpolação do bloco único 29 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.30.` | Peso da interpolação do bloco único 30 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.31.` | Peso da interpolação do bloco único 31 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.32.` | Peso da interpolação do bloco único 32 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.33.` | Peso da interpolação do bloco único 33 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.34.` | Peso da interpolação do bloco único 34 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.35.` | Peso da interpolação do bloco único 35 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.36.` | Peso da interpolação do bloco único 36 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `single_blocks.37.` | Peso da interpolação do bloco único 37 (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `final_layer.` | Peso da interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |

Todos os pesos de interpolação de entrada compartilham o mesmo intervalo (0.0 to 1.0), padrão (1.0) e passo (0.01).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a1cc4dd2c253bbeb94144969e921af40a7f12a1ec23ed7c23da89107767dc26`
