from CovidETL import CovidBrasil, CovidMundo
from CovidETL import Writer
from CovidETL import Args
from CovidETL import MakeGraph


def main():
    args = Args.args_params()

    if args.estado:
        state = CovidBrasil()
        contain = state.requisita_estados()
        Writer.write_brstates(contain=contain)
        MakeGraph.process_state()

    elif args.pais:
        country = CovidMundo()
        contain = country.requisita_paises()
        Writer.write_allcountries(contain=contain)
        MakeGraph.process_country()


if __name__ == '__main__':
    main()
