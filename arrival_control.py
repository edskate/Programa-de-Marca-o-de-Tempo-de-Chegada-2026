<<<<<<< HEAD
import csv
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

DATE_FORMAT = "%Y-%m-%d %H:%M"

@dataclass
class Chegada:
    colaborador: str
    horario_agendado: datetime
    horario_chegada: datetime
    tolerancia_minutos: int = 5

    @property
    def atraso_minutos(self) -> int:
        delta = self.horario_chegada - self.horario_agendado
        return max(0, int(delta.total_seconds() // 60))

    @property
    def esta_pontual(self) -> bool:
        return self.horario_chegada <= self.horario_agendado + timedelta(minutes=self.tolerancia_minutos)


def carregar_registros_csv(caminho: str) -> List[Chegada]:
    registros: List[Chegada] = []
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            registros.append(
                Chegada(
                    colaborador=linha["colaborador"].strip(),
                    horario_agendado=datetime.strptime(linha["horario_agendado"].strip(), DATE_FORMAT),
                    horario_chegada=datetime.strptime(linha["horario_chegada"].strip(), DATE_FORMAT),
                    tolerancia_minutos=int(linha.get("tolerancia_minutos", 5) or 5),
                )
            )
    return registros


def calcular_pontualidade(chegadas: List[Chegada]) -> float:
    if not chegadas:
        return 0.0
    pontuais = sum(1 for chegada in chegadas if chegada.esta_pontual)
    return round((pontuais / len(chegadas)) * 100, 2)


def calcular_aprimoramento(anteriores: List[Chegada], atuais: List[Chegada]) -> float:
    pontualidade_anterior = calcular_pontualidade(anteriores)
    pontualidade_atual = calcular_pontualidade(atuais)
    return round(pontualidade_atual - pontualidade_anterior, 2)


def imprimir_relatorio(atuais: List[Chegada], anteriores: List[Chegada]) -> None:
    pontualidade_atual = calcular_pontualidade(atuais)
    pontualidade_anterior = calcular_pontualidade(anteriores)
    aprimoramento = calcular_aprimoramento(anteriores, atuais)

    print("=== Relatório de Controle de Chegada ===")
    print(f"Registros atuais: {len(atuais)}")
    print(f"Pontualidade atual: {pontualidade_atual}%")
    print(f"Pontualidade anterior: {pontualidade_anterior}%")

    if aprimoramento > 0:
        print(f"Aprimoramento: +{aprimoramento}%")
    elif aprimoramento < 0:
        print(f"Deterioração: {aprimoramento}%")
    else:
        print("Nenhuma mudança na pontualidade.")

    print("\nDetalhes por colaborador:")
    for chegada in atuais:
        status = "PONTUAL" if chegada.esta_pontual else f"ATRASO {chegada.atraso_minutos} min"
        print(f"- {chegada.colaborador}: {status}")


def criar_arquivo_exemplo(caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        arquivo.write(
            "colaborador,horario_agendado,horario_chegada,tolerancia_minutos\n"
            "Ana,2026-06-07 08:00,2026-06-07 07:58,5\n"
            "Bruno,2026-06-07 08:00,2026-06-07 08:03,5\n"
            "Carla,2026-06-07 08:00,2026-06-07 08:12,5\n"
        )


def main() -> None:
    caminho_atual = Path("dados_atual.csv")
    caminho_anterior = Path("dados_anterior.csv")

    if not caminho_atual.exists():
        print("Criando arquivo de exemplo 'dados_atual.csv'...")
        criar_arquivo_exemplo(caminho_atual)

    if not caminho_anterior.exists():
        print("Criando arquivo de exemplo 'dados_anterior.csv'...")
        criar_arquivo_exemplo(caminho_anterior)

    atuais = carregar_registros_csv(str(caminho_atual))
    anteriores = carregar_registros_csv(str(caminho_anterior))
    imprimir_relatorio(atuais, anteriores)


if __name__ == "__main__":
    main()
=======
import csv
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import List

DATE_FORMAT = "%Y-%m-%d %H:%M"

@dataclass
class Chegada:
    colaborador: str
    horario_agendado: datetime
    horario_chegada: datetime
    tolerancia_minutos: int = 5

    @property
    def atraso_minutos(self) -> int:
        delta = self.horario_chegada - self.horario_agendado
        return max(0, int(delta.total_seconds() // 60))

    @property
    def esta_pontual(self) -> bool:
        return self.horario_chegada <= self.horario_agendado + timedelta(minutes=self.tolerancia_minutos)


def carregar_registros_csv(caminho: str) -> List[Chegada]:
    registros: List[Chegada] = []
    with open(caminho, encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            registros.append(
                Chegada(
                    colaborador=linha["colaborador"].strip(),
                    horario_agendado=datetime.strptime(linha["horario_agendado"].strip(), DATE_FORMAT),
                    horario_chegada=datetime.strptime(linha["horario_chegada"].strip(), DATE_FORMAT),
                    tolerancia_minutos=int(linha.get("tolerancia_minutos", 5) or 5),
                )
            )
    return registros


def calcular_pontualidade(chegadas: List[Chegada]) -> float:
    if not chegadas:
        return 0.0
    pontuais = sum(1 for chegada in chegadas if chegada.esta_pontual)
    return round((pontuais / len(chegadas)) * 100, 2)


def calcular_aprimoramento(anteriores: List[Chegada], atuais: List[Chegada]) -> float:
    pontualidade_anterior = calcular_pontualidade(anteriores)
    pontualidade_atual = calcular_pontualidade(atuais)
    return round(pontualidade_atual - pontualidade_anterior, 2)


def imprimir_relatorio(atuais: List[Chegada], anteriores: List[Chegada]) -> None:
    pontualidade_atual = calcular_pontualidade(atuais)
    pontualidade_anterior = calcular_pontualidade(anteriores)
    aprimoramento = calcular_aprimoramento(anteriores, atuais)

    print("=== Relatório de Controle de Chegada ===")
    print(f"Registros atuais: {len(atuais)}")
    print(f"Pontualidade atual: {pontualidade_atual}%")
    print(f"Pontualidade anterior: {pontualidade_anterior}%")

    if aprimoramento > 0:
        print(f"Aprimoramento: +{aprimoramento}%")
    elif aprimoramento < 0:
        print(f"Deterioração: {aprimoramento}%")
    else:
        print("Nenhuma mudança na pontualidade.")

    print("\nDetalhes por colaborador:")
    for chegada in atuais:
        status = "PONTUAL" if chegada.esta_pontual else f"ATRASO {chegada.atraso_minutos} min"
        print(f"- {chegada.colaborador}: {status}")


def criar_arquivo_exemplo(caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="") as arquivo:
        arquivo.write(
            "colaborador,horario_agendado,horario_chegada,tolerancia_minutos\n"
            "Ana,2026-06-07 08:00,2026-06-07 07:58,5\n"
            "Bruno,2026-06-07 08:00,2026-06-07 08:03,5\n"
            "Carla,2026-06-07 08:00,2026-06-07 08:12,5\n"
        )


def main() -> None:
    caminho_atual = Path("dados_atual.csv")
    caminho_anterior = Path("dados_anterior.csv")

    if not caminho_atual.exists():
        print("Criando arquivo de exemplo 'dados_atual.csv'...")
        criar_arquivo_exemplo(caminho_atual)

    if not caminho_anterior.exists():
        print("Criando arquivo de exemplo 'dados_anterior.csv'...")
        criar_arquivo_exemplo(caminho_anterior)

    atuais = carregar_registros_csv(str(caminho_atual))
    anteriores = carregar_registros_csv(str(caminho_anterior))
    imprimir_relatorio(atuais, anteriores)


if __name__ == "__main__":
    main()
>>>>>>> 5b249e3f3e6eb4de122d9818e2e46e127f1e1a50
