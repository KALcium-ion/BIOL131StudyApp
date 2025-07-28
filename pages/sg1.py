import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, page_container, page_registry
from dash import Input, Output

# Define your sections and questions here (example format)
sg1_sections = [
    {
        "header": "Chapters 1-2: Studying Life and the Chemistry of Life",
        "questions": [
            {"question": "Be familiar with the process of the Scientific Method and what a hypothesis is.", "path": "/studyguide/sg1/q1"},
            {"question":"Know the various types of chemical bonds discussed and the basis of their interactions (i.e., covalent, hydrogen, double covalent).","path":"/studyguide/sg1/q2"},
            {"question":"Be able to describe the various important properties of water.", "path":"/studyguide/sg1/q3"},
            {"question":"Understand what pH is and why it is important biologically.", "path":"/studyguide/sg1/q4"}
        ]
    },
    {
        "header": "Chapter 3: Proteins, Carbohydrates, and Lipids",
        "questions": [
            {"question": "Be familiar with the general molecular structure of amino acids, carbohydrates, and lipids. Know a representative example of a protein, sugar, and fat.", "path":"/studyguide/sg1/q5"},
            {"question":"Be able to name the types of chemical bonds responsible for constructing each macromolecule from its monomers (peptide, phosphodiester, glycosidic).","path":"/studyguide/sg1/q6"},
            {"question":"Be able to define the 4 different levels of protein structure. Understand how different types of bonds can contribute to different levels of protein structure.","path":"/studyguide/sg1/q7"},
            {"question":"Be familiar with the major classifications of amino acids.","path":"/studyguide/sg1/q8"},
            {"question":"Understand how phospholipids organize to generate biological membranes.","path":"/studyguide/sg1/q9"}
        ]
    },
    {
        "header": "Chapter 4: Nucleic Acids and the Origin of Life",
        "questions": [
            {"question": "Know the definition of DNA, RNA, and the 3 major structural components of nucleotides.", "path": "/studyguide/sg1/q10"},
            {"question": "Be familiar with the structural features of DNA and RNA.", "path": "/studyguide/sg1/q11"},
            {"question":"Be able to name the bases present in DNA and RNA, and which bases form complementary pairs.","path":"/studyguide/sg1/q12"},
            {"question":"Understand the difference between the terms anabolism and catabolism, and how these processes relate to the formation or breakdown of each of the three groups of macromolecules.","path":"/studyguide/sg1/q13"},
            {"question":"Be able to name each of the four scientists that were involved in the discovery of the structure of DNA. Be familiar with the contribution of each scientist to this discovery.","path":"/studyguide/sg1/q14"},
            {"question":"Explain how two critical pieces of data led scientists to construct the DNA double helix model.", "path":"/studyguide/sg1/q15"}
        ]
    },
    {
        "header":"Chapter 14: From DNA to Protein (Gene Expression)",
        "questions": [
            {"question":"Be able to discuss what the central dogma of molecular biology means.","path":"/studyguide/sg1/q16"},
            {"question":"Know the three major classes of RNA and what the central role is for each type.","path":"/studyguide/sg1/q17"},
            {"question":"Be familiar with the necessary components of transcription and be able to explain each of the main transcriptional phases (initiation, elongation, and termination).","path":"/studyguide/sg1/q18"},
            {"question":"Be prepared to define the terms: genetic code, codons, introns, and exons. Know how to use a genetic code table to identify amino acids associated with specific codons.","path":"/studyguide/sg1/q19"},
            {"question":"Understand how ribosomes contribute to the three major steps of the translation process.","path":"/studyguide/sg1/q20"},
            {"question":"Be able to describe the three main types of protein modifications and where they occur.","path":"/studyguide/sg1/q21"}
        ]
    }
]

layout = html.Div([
    html.Div(
        dbc.Button("Back to Home", href="/", style={
            "backgroundColor": "#3a5a40",
            "color": "white",
            "border": "none",
            'fontWeight':'bold',
            'borderRadius':'20px',
            'padding':'10px 20px',
            'fontSize':'18px',
            'textDecoration':'none',
            'fontFamily':'Arial'
        }),
        style={
            "position": "fixed",
            "top": "30px",
            "left": "10px",
            "zIndex": "1000",
        }
    ),

    html.Div(style = {'height':'25px'}),
    html.H2("Study Guide 1", style={"textAlign": "center", "marginTop": "20px", "fontFamily":"Arial"}),
    dbc.Container([
        html.Div([
            html.H4(section["header"], style={"marginTop": "30px", "fontSize": "22px", "fontWeight": "bold"}),
            dbc.ListGroup([
                dbc.ListGroupItem(q["question"], 
                                  action=True, 
                                  href=q["path"], 
                                  style={"fontSize": "18px",
                                         "display":"block",
                                         "marginBottom":"10px",
                                         "border":"2px solid black",
                                         "padding":"5px",
                                         "borderRadius":"8px",
                                         "textDecoration":"none",
                                         "color":"black"
                                        }
                                )
                for q in section["questions"]
            ])
        ]) for section in sg1_sections
    ], style={"marginTop": "30px", 'fontFamily':'Arial'}),
    html.Div(style = {'height':'100px'})
])


