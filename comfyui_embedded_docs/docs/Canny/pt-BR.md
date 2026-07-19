# Canny

Extraia todas as linhas de borda de fotos, como usar uma caneta para contornar uma foto, desenhando os contornos e limites de detalhes dos objetos.

## Princípio de Funcionamento

Imagine que você é um artista que precisa usar uma caneta para contornar uma foto. O nó Canny funciona como um assistente inteligente, ajudando você a decidir onde desenhar linhas (bordas) e onde não.

Esse processo é como um trabalho de triagem:

- **Limiar alto** é o "padrão de linha obrigatória": apenas linhas de contorno muito óbvias e nítidas serão desenhadas, como contornos faciais de pessoas e molduras de edifícios
- **Limiar baixo** é o "padrão de linha definitivamente não desenhada": bordas muito fracas serão ignoradas para evitar desenhar ruídos e linhas sem sentido
- **Área intermediária**: bordas entre os dois padrões serão desenhadas juntas se estiverem conectadas a "linhas obrigatórias", mas não serão desenhadas se estiverem isoladas

A saída final é uma imagem em preto e branco, onde as partes brancas são as linhas de borda detectadas e as partes pretas são áreas sem bordas.

## Entradas

| Nome do Parâmetro | Descrição da Função | Tipo de Dados | Tipo de Entrada | Padrão | Faixa |
| --- | --- | --- | --- | --- | --- |
| `image` | Foto original que precisa de extração de bordas | IMAGE | Entrada | - | - |
| `low_threshold` | Limiar baixo, determina quão fracas as bordas devem ser ignoradas. Valores menores preservam mais detalhes, mas podem gerar ruído | FLOAT | Widget | 0,4 | 0,01-0,99 |
| `high_threshold` | Limiar alto, determina quão fortes as bordas devem ser preservadas. Valores maiores mantêm apenas as linhas de contorno mais óbvias | FLOAT | Widget | 0,8 | 0,01-0,99 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | Imagem de borda em preto e branco, linhas brancas são bordas detectadas, áreas pretas são partes sem bordas | IMAGE |

## Comparação de Parâmetros

![Imagem Original](./asset/input.webp)

![Comparação de Parâmetros](./asset/compare.webp)

**Problemas Comuns:**

- Bordas quebradas: Tente diminuir o limiar alto
- Muito ruído: Aumente o limiar baixo
- Detalhes importantes faltando: Diminua o limiar baixo
- Bordas muito ásperas: Verifique a qualidade e resolução da imagem de entrada

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/pt-BR.md)
