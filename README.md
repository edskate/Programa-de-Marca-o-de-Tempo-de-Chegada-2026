# Automação de Controle de Chegada

Este projeto fornece uma automação simples para controlar chegadas de colaboradores, calcular a porcentagem de pontualidade e avaliar o aprimoramento entre dois períodos.

## Arquivos
- `arrival_control.py`: script principal de automação.
- `dados_atual.csv`: exemplo de registros do período atual.
- `dados_anterior.csv`: exemplo de registros do período anterior.
- `diagrama.mmd`: diagrama em Mermaid mostrando o fluxo da automação.

## Como usar

1. Abra um terminal no diretório do projeto.
2. Execute:

```bash
python arrival_control.py
```

3. O script criará arquivos de exemplo caso ainda não existam e exibirá:
- porcentagem de pontualidade do período atual
- porcentagem de pontualidade do período anterior
- porcentagem de aprimoramento
- detalhes de cada colaborador

## Métodos e métricas

- `Pontualidade (%)`: percentual de chegadas dentro da tolerância permitida.
- `Aprimoramento (%)`: diferença entre a pontualidade do período atual e a pontualidade do período anterior.

## Exemplo de dados CSV

```csv
colaborador,horario_agendado,horario_chegada,tolerancia_minutos
Ana,2026-06-07 08:00,2026-06-07 07:58,5
Bruno,2026-06-07 08:00,2026-06-07 08:03,5
Carla,2026-06-07 08:00,2026-06-07 08:12,5
```

## Diagrama

O diagrama `diagrama.mmd` mostra o fluxo de:
- carregar dados
- comparar períodos
- calcular pontualidade
- gerar relatório

> Você pode visualizar o diagrama com um renderizador Mermaid ou usar a pré-visualização de Mermaid se suportada pelo editor.
