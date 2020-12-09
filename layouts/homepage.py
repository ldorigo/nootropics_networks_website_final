import dash_html_components as html
import dash_bootstrap_components as dbc


reddit_table = dbc.Table(
    children=[
        html.Thead(
            html.Tr(html.Th("Reddit Data", colSpan=2, style={"text-align": "center"}))
        ),
        html.Tbody(
            [
                html.Tr([html.Th("Number of Posts"), html.Td("108.588")]),
                html.Tr(
                    [
                        html.Th("Total Size of the Dataset"),
                        html.Td("~65 MB (after cleaning)"),
                    ]
                ),
                html.Tr(
                    [
                        html.Th("Recorded Variables"),
                        html.Td("Title, Author, Contents, Date"),
                    ]
                ),
                html.Tr([html.Th("Average post length"), html.Td("426 Characters")]),
                html.Tr(
                    [html.Th("Average nootropics mentions per post"), html.Td("1.95")]
                ),
                html.Tr(
                    [html.Th("Number of posts with 2+ nootropics"), html.Td("23.361")]
                ),
            ]
        ),
    ],
    borderless=True,
    striped=True,
    hover=True,
)

wiki_table = dbc.Table(
    children=[
        html.Thead(
            html.Tr(
                html.Th("Wikipedia Data", colSpan=2, style={"text-align": "center"})
            )
        ),
        html.Tbody(
            [
                html.Tr([html.Th("Number of Pages"), html.Td("1.502")]),
                html.Tr([html.Th("Total Size of the Dataset"), html.Td("~10 MB")]),
                html.Tr(
                    [
                        html.Th("Recorded Variables"),
                        html.Td(
                            "Name (title), Categories, Content, Links, Redirects (synonyms), URL"
                        ),
                    ]
                ),
                html.Tr([html.Th("Average page length"), html.Td("4.798 Characters")]),
                html.Tr(
                    [
                        html.Th("Average links to other nootropics"),
                        html.Td("2.77"),
                    ]
                ),
            ]
        ),
    ],
    borderless=True,
    striped=True,
    hover=True,
)


homepage_explainer_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Explainer Notebook", className="card-title"),
            html.P(
                "This is the notebook containing our more lengthy and technical analysis. Non-interactive, only for viewing."
            ),
            dbc.CardLink(
                children="Open on nbviewer",
                href="https://nbviewer.jupyter.org/github/wojciechdk/Social_Graphs_Final_Project/blob/master/explainer_notebook/explainer_notebook_final.ipynb",
            ),
        ]
    )
)
homepage_repo_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("GitHub Repository  (Analysis)", className="card-title"),
            html.P(
                "GitHub repository containing all our data and code. For playing around/executing on your own computer."
            ),
            dbc.CardLink(
                children="Open on GitHub",
                href="https://github.com/wojciechdk/Social_Graphs_and_Interactions_Final_Project",
            ),
        ]
    )
)
website_repo_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("GitHub Repository (Website)", className="card-title"),
            html.P("The source code of this website."),
            dbc.CardLink(
                children="Open on GitHub",
                href="https://github.com/ldorigo/nootropics_network_website_final",
            ),
        ]
    )
)

link_cards = dbc.Row(
    dbc.CardDeck(
        children=[
            homepage_explainer_card,
            homepage_repo_card,
            website_repo_card,
        ]
    )
)


ref_table = dbc.Row(
    dbc.Col(
        dbc.Table(
            children=[
                # html.Caption("References and used software"),
                # html.Thead(
                #     html.Tr(
                #         html.Th(
                #             "References and used software",
                #             colSpan=2,
                #             style={"text-align": "center"},
                #         )
                #     )
                # ),
                html.Tbody(
                    [
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "MediaWiki Python Library",
                                        href="https://github.com/barrust/mediawiki",
                                    )
                                ),
                                html.Td("Scraping and parsing of Wikipedia content"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "PushShift Python Library",
                                        href="https://github.com/pushshift/api",
                                    )
                                ),
                                html.Td("Finding and downloading Reddit Posts"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "Spacy NLP",
                                        href="https://spacy.io/",
                                    )
                                ),
                                html.Td(
                                    "Processing Reddit Posts to find nootropics and other NLP tasks"
                                ),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "Plotly",
                                        href="https://plotly.com/",
                                    )
                                ),
                                html.Td("Interactive plots"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "Cytoscape.js",
                                        href="https://js.cytoscape.org/",
                                    )
                                ),
                                html.Td("Interactive network visualizations"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "TextBlob",
                                        href="https://textblob.readthedocs.io/en/dev/",
                                    )
                                ),
                                html.Td("Sentiment and Subjectivity Analysis"),
                            ]
                        ),
                        html.Tr(
                            [
                                html.Th(
                                    html.A(
                                        "Networkx",
                                        href="https://networkx.org",
                                    )
                                ),
                                html.Td("Network manipulation and analysis"),
                            ]
                        ),
                    ]
                ),
            ],
            borderless=True,
            striped=True,
            hover=True,
            # dark=True,
        ),
        width={"size": 8, "offset": 2},
    ),
    className="my-5",
)

linkref_container = dbc.Container(
    [
        link_cards,
        html.Hr(className="my-5"),
        html.H3("Used software and libraries"),
        html.P(
            "The following table contains contains the main libraries, frameworks, and utilities we have used in this project."
        ),
        ref_table,
    ]
)
homepage_layout = html.Div(
    [
        html.H1(
            "Nootropic Networks: What can Wikipedia and Reddit teach us about smart drugs?".title(),
            className="mb-5",
        ),
        html.Blockquote(
            [
                html.Dfn("Nootropic, n. :"),
                " A drug that enhances learning and memory and lacks the usual pharmacology of other \
            psychotropic drugs (e.g. sedation, motor stimulation) and possesses very few side \
            effects and extremely low toxicity.",
                html.Footer("WikiTionary", className="blockquote-footer"),
            ],
            className="blockquote text-center text-muted mb-3",
        ),
        html.P(
            [
                "Nootropics, often called ",
                html.Em("smart drugs"),
                ", have seen a huge increase in popularity worldwide - with ",
                html.A(
                    "some studies",
                    href="https://www.scientificamerican.com/article/use-of-ldquo-smart-drugs-rdquo-on-the-rise/",
                ),
                " finding that up to 14% of the population uses them in one form or another. Despite their popularity, these\
                substances are often much less studied and understood than typical (medical) drugs: \
                because they aim at improving performance of healthy people, rather than curing disease, there is little funding for large-scale studies or clinical trials.\
                With this project, we want to explore some of the ways that network science and text analysis can help infer information on the uses and effects of nootropics.\
                We apply the same network and text analysis tools to an encyclopedic source of knowledge - Wikipedia - and to a vast amount of posts on a community in the social network Reddit, ",
                html.A("r/Nootropics", href="https://www.reddit.com/r/nootropics"),
                " - to see what, if anything, can be learned.",
            ]
        ),
        html.P(
            [
                "At the same time, from a sligthly more theoretical and network-science point-of-view, we are interested in investigating the ",
                html.Em("networks "),
                'that can be extracted from these two sources: In both cases, the nodes of the network are nootropics. In the case of Wikipedia, we build the network by \
                considering "links" to be a link between two pages about two nootropics. In the case of Reddit, a "link" arises whenever two substances are mentioned together within a post. \
                    How do the resulting networks compare to each other, and why?',
            ]
        ),
        html.Hr(className="my-5"),
        html.H2("Our Data"),
        html.P(
            [
                "Here's a quick overview of the data we are analyzing. \
                For more info, refer to the Jupyter notebook linked below. \
            All of our datasets can be downloaded from our ",
                html.A(
                    html.Em("GitHub repository, in the data directory."),
                    href="https://github.com/wojciechdk/Social_Graphs_and_Interactions_Final_Project/tree/master/data",
                ),
            ]
        ),
        dbc.Container(dbc.Row([dbc.Col(reddit_table), dbc.Col(wiki_table)])),
        html.Hr(className="my-5"),
        html.H2("Links and References", className="mb-5"),
        linkref_container,
    ]
)
