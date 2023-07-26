from .mysession import session
from .io_utils import get_whole_elo
import numpy as np


def sample_prompts(num_prompts=2) -> dict:
    elo_dataset = get_whole_elo()

    # Choose two prompts based on the elo ranking they have ("better" prompts are sampled more often)
    weights = elo_dataset['weights']
    sampled_idx = np.random.choice(len(weights), p=weights, size=num_prompts, replace=False)

    print("Comparing the prompts " + elo_dataset["names"][sampled_idx[0]] +
          " and " + elo_dataset["names"][sampled_idx[1]])

    return {elo_dataset['ids'][i]: (elo_dataset['engines'][i], elo_dataset['prompts'][i]) for i in sampled_idx}


def get_prompts(essay: str, num_prompts=2) -> dict:
    title = session.get("title")
    user_args = session.get("user_args")

    prompts = sample_prompts(num_prompts)
    prompts = {k: (eng, promp.format(title=title, article=user_args["article"], year=user_args["year"], essay=essay,
                                     extra_info=get_article_information(user_args["article"])))
               for k, (eng, promp) in prompts.items()}

    return prompts


def get_article_information(article):
    match article:
        case 'Bericht':
            return ""
        case 'Erörterung':
            return "Eine Erörterung analysiert beide Seiten eines Sachverhaltes und am Ende erklärt, welche Seite " \
                   "bevorzugt wird. Wichtig ist die Trennung von Tatsachen und Hypothesen. "
        case 'Essay':
            return ""
        case 'Gedichtsanalyse':
            return "In einer Gedichtsanalyse wird ein Gedicht detailliert auf seinen Inhalt, seine Struktur und " \
                   "seine sprachliche Gestaltung analysiert. Zum Beispiel können typische Merkmale wie die Art des " \
                   "Gedichtes, die Reime, die Strophen und die Stilmittel untersucht werden. Die Gedichtsanalyse " \
                   "sollte folgendermaßen aufgebaut sein: Einleitung (wichtige Informationen über das Gedicht), " \
                   "Hauptteil (Inhalt, Form, Sprache), Schlussteil (Fazit). "
        case 'Inhaltsangabe':
            return "Eine Inhaltsangabe ist eine komprimierte Information über ein Originalwerk, die objektiv und " \
                   "unvoreingenommen ist. "
        case 'Kurzgeschichte':
            return "Eine Kurzgeschichte ist eine Erzählung, die kurz ist. Sie besteht aus einem einzigen " \
                   "Handlungsstrang und weist nur wenige Figuren auf. Es gibt keine oder nur eine sehr kurze " \
                   "Einleitung. Stattdessen erfordert die kurze Form den sofortigen Einstieg in die Handlung. Das " \
                   "chronologische Erzählen erfolgt hauptsächlich im Präteritum. Die erzählte Zeit beträgt meist nur " \
                   "wenige Minuten oder Stunden, häufig wird das Geschehen auf wenige Augenblicke, eine " \
                   "exemplarische Situation, ein Bild oder eine Momentaufnahme reduziert. Ein offener Schluss " \
                   "veranlasst den Leser dazu, über das Geschehen nachzudenken. Wertungen, Deutungen und Lösungen " \
                   "werden dagegen weitgehend vermieden."
        case 'Rezension':
            return "Eine Rezension ist sowohl eine Zusammenfassung als auch eine Bewertung. Eine vollständige " \
                   "Rezension enthält ein Einleitung, Zusammenfassung, Bewertung und Schlussfolgerung. "
        case 'Sachtextanalyse':
            return ""
        case 'Szenenanalyse':
            return "Die Szenenanalyse ist eine Art der Textanalyse, die sich besonders für Theaterstücke eignet. Sie " \
                   "bietet einen Überblick über die Szene, ordnet sie in das Gesamtwerk ein und analysiert die " \
                   "Bedeutung. Form und Inhalt werden analysiert, interpretiert und Zusammenhänge aufgezeigt. "
        case _:
            return ""
