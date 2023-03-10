from .mysession import session


def get_prompt(essay):
    title = session.get("title")
    user_args = session.get("user_args")

    prompt = "" # get_article_information(article=user_args["article"])
    prompt += "Beim folgendem Text handelt es sich um einen {article} von einer Schülerin oder einem Schüler in der {year}. Klasse. "
    prompt += "Das Thema bzw. der Titel ist \"{title}\". "
    prompt += "Text: \"{essay}\" "
    prompt += "Gib Tipps zur Ausdrucksweise wie ein freundlicher Lehrer und gib konkrete Verbesserungsvorschläge."

    prompt = prompt.format(title=title, article=user_args["article"],  year=user_args["year"], essay=essay)

    print(prompt)

    return prompt


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
