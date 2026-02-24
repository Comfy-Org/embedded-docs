> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/pt-BR.md)

O nó `BasicScheduler` é projetado para calcular uma sequência de valores sigma para modelos de difusão com base no agendador, modelo e parâmetros de remoção de ruído fornecidos. Ele ajusta dinamicamente o número total de etapas com base no fator de denoise para refinar o processo de difusão, fornecendo "receitas" precisas para diferentes estágios em processos de amostragem avançados que exigem controle fino (como amostragem multiestágio).

## Entradas

| Parâmetro   | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo     | Descrição Metafórica           | Propósito Técnico            |
| ----------- | ------------- | --------------- | ------ | ------------- | ------------------------------ | ---------------------------- |
| `model`     | MODEL         | Input           | -      | -             | **Tipo de Tela**: Diferentes materiais de tela precisam de fórmulas de tinta diferentes | Objeto do modelo de difusão, determina a base de cálculo do sigma |
| `scheduler` | COMBO[STRING] | Widget          | -      | 9 opções      | **Técnica de Mistura**: Escolha como a concentração da tinta muda | Algoritmo de agendamento, controla o modo de decaimento do ruído |
| `steps`     | INT           | Widget          | 20     | 1-10000       | **Contagem de Misturas**: Diferença de precisão entre 20 e 50 misturas | Etapas de amostragem, afeta a qualidade e velocidade da geração |
| `denoise`   | FLOAT         | Widget          | 1.0    | 0.0-1.0       | **Intensidade da Criação**: Nível de controle do ajuste fino à repintura | Força de remoção de ruído, suporta cenários de repintura parcial |

### Tipos de Agendador

Com base no código-fonte `comfy.samplers.SCHEDULER_NAMES`, suporta os seguintes 9 agendadores:

| Nome do Agendador   | Características      | Casos de Uso                 | Padrão de Decaimento do Ruído |
| ------------------- | -------------------- | ---------------------------- | ----------------------------- |
| **normal**          | Linear padrão        | Cenários gerais, equilibrado | Decaimento uniforme           |
| **karras**          | Transição suave      | Alta qualidade, rico em detalhes | Decaimento não-linear suave   |
| **exponential**     | Decaimento exponencial | Geração rápida, eficiência   | Decaimento exponencial rápido |
| **sgm_uniform**     | Uniforme SGM         | Otimização de modelo específico | Decaimento otimizado SGM      |
| **simple**          | Agendamento simples  | Testes rápidos, uso básico   | Decaimento simplificado       |
| **ddim_uniform**    | Uniforme DDIM        | Otimização de amostragem DDIM | Decaimento específico DDIM    |
| **beta**            | Distribuição Beta    | Necessidades de distribuição especial | Decaimento por função Beta    |
| **linear_quadratic**| Quadrático linear    | Otimização de cenário complexo | Decaimento por função quadrática |
| **kl_optimal**      | KL ótimo             | Otimização teórica           | Decaimento otimizado por divergência KL |

## Saídas

| Parâmetro | Tipo de Dados | Tipo de Saída | Descrição Metafórica   | Significado Técnico                |
| --------- | ------------- | ------------- | ---------------------- | ---------------------------------- |
| `sigmas`  | SIGMAS        | Output        | **Gráfico de Receita de Tinta**: Lista detalhada de concentrações de tinta para uso passo a passo | Sequência de níveis de ruído, guia o processo de remoção de ruído do modelo de difusão |

## Papel do Nó: Assistente de Mistura de Cores do Artista

Imagine que você é um artista criando uma imagem clara a partir de uma mistura caótica de tinta (ruído). O `BasicScheduler` atua como seu **assistente profissional de mistura de cores**, cujo trabalho é preparar uma série de receitas precisas de concentração de tinta:

### Fluxo de Trabalho

- **Etapa 1**: Use tinta com 90% de concentração (alto nível de ruído)
- **Etapa 2**: Use tinta com 80% de concentração
- **Etapa 3**: Use tinta com 70% de concentração
- **...**
- **Etapa Final**: Use 0% de concentração (tela limpa, sem ruído)

### Habilidades Especiais do Assistente de Cores

**Diferentes métodos de mistura (scheduler)**:

- **Método de mistura "karras"**: A concentração da tinta muda de forma muito suave, como a técnica de gradiente de um artista profissional
- **Método de mistura "exponential"**: A concentração da tinta diminui rapidamente, adequado para criação rápida
- **Método de mistura "linear"**: A concentração da tinta diminui uniformemente, estável e controlável

**Controle fino (steps)**:

- **20 misturas**: Pintura rápida, prioridade para eficiência
- **50 misturas**: Pintura refinada, prioridade para qualidade

**Intensidade da criação (denoise)**:

- **1.0 = Criação completamente nova**: Comece completamente do zero, tela em branco
- **0.5 = Meia transformação**: Mantenha metade da pintura original, transforme metade
- **0.2 = Ajuste fino**: Apenas faça ajustes sutis na pintura original

### Colaboração com Outros Nós

`BasicScheduler` (Assistente de Cores) → Prepara a Receita → `SamplerCustom` (Artista) → Pintura Real → Trabalho Concluído
