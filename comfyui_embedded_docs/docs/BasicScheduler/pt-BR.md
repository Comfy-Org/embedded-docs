# Agendador Básico

O nó `BasicScheduler` é projetado para calcular uma sequência de valores sigma para modelos de difusão com base no agendador, modelo e parâmetros de remoção de ruído fornecidos. Ele ajusta dinamicamente o número total de etapas com base no fator de remoção de ruído para ajustar finamente o processo de difusão, fornecendo "receitas" precisas para diferentes estágios em processos avançados de amostragem que exigem controle fino (como amostragem multiestágio).

## Entradas

| Parâmetro | Descrição metafórica | Tipo de dados | Tipo de entrada | Padrão | Intervalo | Propósito técnico |
| --- | --- | --- | --- | --- | --- | --- |
| `modelo` | **Tipo de tela**: Diferentes materiais de tela precisam de diferentes fórmulas de tinta | MODEL | Entrada | - | - | Objeto de modelo de difusão, determina a base de cálculo de sigma |
| `agendador` | **Técnica de mistura**: Escolha como a concentração da tinta muda | COMBO[STRING] | Widget | - | 9 opções | Algoritmo de agendamento, controla o modo de decaimento do ruído |
| `etapas` | **Número de misturas**: diferença de precisão entre 20 misturas e 50 misturas | INT | Widget | 20 | 1-10000 | Etapas de amostragem, afeta a qualidade e a velocidade da geração |
| `reduzir_ruído` | **Intensidade de criação**: nível de controle de ajuste fino até repintura | FLOAT | Widget | 1.0 | 0.0-1.0 | Força de remoção de ruído, suporta cenários de repintura parcial |

### Tipos de agendador

Com base no código-fonte `comfy.samplers.SCHEDULER_NAMES`, oferece suporte aos seguintes 9 agendadores:

| Nome do agendador   | Características      | Casos de uso                 | Padrão de decaimento de ruído |
| -------------------- | -------------------- | ---------------------------- | ---------------------------- |
| **normal**           | Linear padrão        | Cenários gerais, equilibrado | Decaimento uniforme          |
| **karras**           | Transição suave      | Alta qualidade, rico em detalhes | Decaimento não linear suave |
| **exponential**      | Decaimento exponencial | Geração rápida, eficiência | Decaimento exponencial rápido |
| **sgm_uniform**      | SGM uniforme         | Otimização de modelo específico | Decaimento otimizado SGM |
| **simple**           | Agendamento simples  | Testes rápidos, uso básico   | Decaimento simplificado      |
| **ddim_uniform**     | DDIM uniforme        | Otimização de amostragem DDIM | Decaimento específico DDIM |
| **beta**             | Distribuição beta    | Necessidades de distribuição especiais | Decaimento da função beta |
| **linear_quadratic** | Linear quadrático    | Otimização de cenários complexos | Decaimento de função quadrática |
| **kl_optimal**       | KL ótimo             | Otimização teórica           | Decaimento otimizado por divergência KL |

## Saídas

| Parâmetro | Descrição metafórica | Tipo de dados | Tipo de saída | Significado técnico |
| --- | --- | --- | --- | --- |
| `sigmas` | **Gráfico de receita de tinta**: Lista detalhada de concentração de tinta para uso passo a passo | SIGMAS | Saída | Sequência de níveis de ruído, orienta o processo de remoção de ruído do modelo de difusão |

## Papel do nó: Assistente de mistura de cores do artista

Imagine que você é um artista criando uma imagem nítida a partir de uma mistura caótica de tinta (ruído). O `BasicScheduler` atua como seu **assistente profissional de mistura de cores**, cujo trabalho é preparar uma série de receitas precisas de concentração de tinta:

### Fluxo de trabalho

- **Etapa 1**: Use tinta com 90% de concentração (alto nível de ruído)
- **Etapa 2**: Use tinta com 80% de concentração
- **Etapa 3**: Use tinta com 70% de concentração
- **...**
- **Etapa final**: Use 0% de concentração (tela limpa, sem ruído)

### Habilidades especiais do assistente de cores

**Diferentes métodos de mistura (agendador)**:

- **Método de mistura "karras"**: A concentração da tinta muda suavemente, como a técnica de gradiente de um artista profissional
- **Método de mistura "exponential"**: A concentração da tinta diminui rapidamente, adequado para criação rápida
- **Método de mistura "linear"**: A concentração da tinta diminui uniformemente, estável e controlável

**Controle fino (`steps`)**:

- **20 misturas**: Pintura rápida, prioridade na eficiência
- **50 misturas**: Pintura refinada, prioridade na qualidade

**Intensidade de criação (`denoise`)**:

- **1.0 = Criação totalmente nova**: Comece completamente do zero na tela em branco
- **0.5 = Meia transformação**: Mantenha metade da pintura original, transforme metade
- **0.2 = Ajuste fino**: Faça apenas ajustes sutis na pintura original

### Colaboração com outros nós

`BasicScheduler` (Assistente de cores) → Preparar receita → `SamplerCustom` (Artista) → Pintura real → Obra concluída

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/pt-BR.md)
