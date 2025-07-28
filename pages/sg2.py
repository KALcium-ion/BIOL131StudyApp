import dash
import dash_bootstrap_components as dbc
from dash import html

sg2_sections = [
    {
        "header":"Chapter 7: Cell Signaling and Communication",
        "questions":[
            {"question":"Know the formal definitions of the following terms: signal transduction pathway, autocrine, paracrine, and endocrine.", "path":"/studyguide/sg2/q1"},
            {"question":"Be familair with examples of the main types of cytoplasmic receptors, including ion channels, protein kinase receptors, and G protein-linked receptors. Understand the specific activation process of these receptors and how the activation leads to signal transduction. What are some of the general potential outcomes of these pathways (i.e., insulin)?", "path":"/studyguide/sg2/q2"},
            {"question":"Be able to explain the mechanisms of action associated with cytoplasmic receptors. Be familiar with the names of different ligands that act through cytoplasmic receptors.", "path":"/studyguide/sg2/q3"},
            {"question":"Be familiar with the major components of the MAPK pathway. Know how the players in this pathway become sequentially activated.", "path":"/studyguide/sg2/q4"},
            {"question":"Know what a second messenger is and be able to give some examples (i.e., NO, cAMP, IP3, cGMP). Be able to explain how acetylcholine leads to the formation of NO in endothelial cells. Know how NO initiates relaxation in smooth muscle cells to cause vasodilation in arteries.", "path":"/studyguide/sg2/q5"}
        ]
    },
    {
        "header":"Chapter 6: Cell Membranes",
        "questions":[
            {"question":"Be able to explain what the fluid mosiac model of membranes means. Know the general components of a lipid bilayer.", "path":"/studyguide/sg2/q6"},
            {"question":"Be familair with the three different types of cell junctions (tight junctions, desmosomes, and gap junctions). Know the differences in their specific functions.", "path":"/studyguide/sg2/q7"},
            {"question":"Understand the concept of diffusion/osmosis and the factors which affect their rates. Know the terms hypertonic, isotonic, and hypotonic.", "path":"/studyguide/sg2/q8"},
            {"question":"Be able to explain the difference between facilitated diffusion and primary/secondary active transport across membranes. Be prepared to give specific examples of transporters for each.", "path":"/studyguide/sg2/q9"},
            {"question":"Understand the terms phagocytosis, pinocytosis, receptor-mediated endocytosis, and exocytosis.", "path":"/studyguide/sg2/q10"}
        ]
    },
    {
        "header":"Chapter 8: Energy, Enzymes, and Metabolism",
        "questions": [
            {"question": "Be able to define the terms metabolism, anabolic reactions, and catabolic reactions. Know the Laws of Thermodynamics.", "path":"/studyguide/sg2/q11"},
            {"question":"Understand the concept of free energy (G) and its relationship to enthalpy (H) and entropy (S). Be able to explain and give examples of exergonic and endergonic reactions.", "path":"/studyguide/sg2/q12"},
            {"question":"Be familiar with the role of ATP in biochemical energetics.", "path":"/studyguide/sg2/q13"},
            {"question":"Be able to explain the three different mechanisms by which enzymes catalyze reactions.", "path":"/studyguide/sg2/q14"},
            {"question":"Know the different manners by which the activity of enzymes is regulated, including: irreversible inhibition, reversible inhibition, competitive inhibition, noncompetitive inhibition, and allosteric regulation.", "path":"/studyguide/sg2/q15"}
        ]
    },
    {
        "header":"Chapter 34: The Plant Body",
        "questions": [
            {"question":"Know the 3 types of vegetative organs of angiosperms and the organization of their 2 main systems. What is the difference between monocots and eudicots?", "path":"/studyguide/sg2/q16"},
            {"question":"Be familiar with the three structural components that make plant cells unique. What are three types of sugars that constitute the primary cell wall?", "path":"/studyguide/sg2/q17"},
            {"question":"Be able to describe the function, and example cell types, associated with dermal tissue, ground tissue, and vascular tissue systems.", "path":"/studyguide/sg2/q18"},
            {"question":"Understand how apical and lateral meristems lead to primary and secondary growth, respectively.", "path":"/studyguide/sg2/q19"},
            {"question":"Be familiar with the three major zones of development in the plant root.", "path":"/studyguide/sg2/q20"}
        ]
    },
    {
        "header":"Chapter 35: Transport in Plants",
        "questions": [
            {"question":"Understand the concept of water potential and how it relates to solute and pressure potential. If given a diffusion scenario with megapascal units, be able to predict in which direction water will move.", "path":"/studyguide/sg2/q21"},
            {"question":"Be able to explain how the apoplast and symplast contribute to the uptake of water in plant roots. Know how to identify these structures on a diagram.", "path":"/studyguide/sg2/q22"},
            {"question":"Know the details of how the transpiration-cohesion-tension mechanism promotes water transport in the xylem of plants.", "path":"/studyguide/sg2/q23"},
            {"question":"Be able to describe the mechanisms by which blue light, K+, and the proton pump contribute to stomata opening and CO2 uptake.", "path":"/studyguide/sg2/q24"},
            {"question":"Understand the concepts of loading and unloading and how they releate to substance transport in the phloem.", "path":"/studyguide/sg2/q25"}
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
    html.H2("Study Guide 2", style={"textAlign": "center", "marginTop": "20px", "fontFamily":"Arial"}),
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
        ]) for section in sg2_sections
    ], style={"marginTop": "30px", 'fontFamily':'Arial'}),
    html.Div(style = {'height':'100px'})
])


