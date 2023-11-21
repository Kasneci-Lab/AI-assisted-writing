from .mysession import session
from .io_utils import sample_prompts


def get_prompts(essay: str, task: str, num_prompts=2) -> dict:
    title = session.get("title")
    user_args = session.get("user_args")

    prompts = sample_prompts(num_prompts)
    prompts = {k: (eng, promp.format(title=title, article=user_args["article"], year=user_args["year"], essay=essay,
                                     task=task,
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
        case "Geschichte":
            return "Folgende Kriterien sind für eine Geschichte relevant: " \
                    "- Klarere Ausdrucksweise und Strukturierung der Sätze. " \
                    "- Verbesserung der Beschreibungen, um die Szene lebendiger zu gestalten. " \
                    "- Bessere Nutzung von Adjektiven und Adverbien zur Verstärkung der Beschreibungen. " \
                    "- Präzisere Verwendung von Verben, um die Handlung genauer zu beschreiben. " \
                    "- Einheitliche und präzisere Ausdrucksweise. " \
                    "- Vermeidung von Wiederholungen und redundanten Phrasen. " \
                    "- Verbesserte Verknüpfung von Sätzen und Absätzen, um den Text flüssiger zu gestalten"
        case _:
            return ""
