import dash
import dash_bootstrap_components as dbc
from dash import html

# Define your sections and questions here (example format)
sg3_sections = [
    {
        "header":"Chapter 42: Animal Fertilization",
        "questions": [
            {"question":"Be familiar with the process of spermatogenesis and oogenesis. Know what the beginning components are compared to the end components.", "path":"/sg3/q1"},
            {"question":"Know the major steps involved in fertilization (the union of sperm and egg to produce a zygote). Be prepared to discuss the details of the acrosome reaction and the process of sperm adhesion and fusion with the egg. What is the role of G-actin in these processes?", "path":"/sg3/q2"},
            {"question":"Understand the mechanisms involved in the blocks to polyspermy. Be familiar with the difference between the fast and slow block.", "path":"/sg3/q3"},
            {"question":"Know the role that Ernest Everett played in improving our understanding of fertilization.", "path":"/sg3/q4"},
            {"question":"Be able to explain the contributions of Ca2+ and of cortical granules in the process of fertilization.", "path":"/sg3/q5"}
        ]
    },
    {
        "header":"Chapter 43: Animal Development (Cleavage)",
        "questions": [
            {"question":"Be able to define the term Homunculus. Be able to describe the difference between the theories of Preformation and Epigenesis.", "path":"/sg3/q6"},
            {"question":"Understand the following terms: cleavage, blastocoel, blastomeres, blastocyst, micromere, macromere, and mesomere. Be prepared to describe the process of cleavage.", "path":"/sg3/q7"},
            {"question":"Regarding the initial stages of development, be able to describe the series of events that lead to the formation of the grey crescent. This includes: sperm entry, animal pole and vegetal pole movement, and cortical cytoplasm movement.", "path":"/sg3/q8"}
        ]
    },
    {
        "header":"Chapter 43: Animal Development (Blastula Formation)",
        "questions":[
            {"question":"Know the difference between differentiation and polarity. How are plasma membrane-associated proteins involved in establishing cell adhesion and differentiation?", "path":"/sg3/q9"},
            {"question":"Be able to define the term blastula. Be familiar with the processes involved in the formation of the sea urchin, frog, and chick blastula.", "path":"/sg3/q10"},
            {"question":"In the formation of the chick blastula, know the roles of the following structures: area pellucida, area opaca, epiblast, hypoblast, and marginal zone.", "path":"/sg3/q11"},
            {"question":"In particular, how does blastula formation in the chick differ from the frog?", "path":"/sg3/q12"}
        ]
    },
    {
        "header":"Chapter 43: Animal Development (Gastrulation)",
        "questions":[
            {"question":"Define the term gastrulation. Be able to name the three germ layers formed during gastrulation. Know the final main tissues or organs that each layer eventually becomes.", "path":"/sg3/q13"},
            {"question":"Be familiar with the process of gastrulation in the sea urchin. Know the major structures, including mesenchyme cells, blastopore, archenteron, skeletal rods, and stomodeum. Be able to distinguish these structures in a cartoon or microscope-generated image.", "path":"/sg3/q14"},
            {"question":"Know how to describe the process of gastrulation in the frog. How do the bottle cells contribute to this process? What structure contributes to the formation of the ventral lip?", "path":"/sg3/q15"},
            {"question":"Be familiar with the process of gastrulation in the chick embryo. Know the contributions of the primitive streak, Henson's node, and th primitive groove. How do the three main layers arise from the epiblast? What does the hypoblast contribute?", "path":"/sg3/q16"}
        ]
    },
    {
        "header":"Chapter 43: Animal Development (Neural Development)",
        "questions":[
            {"question":"Be able to explain the major steps involved in neurulation. Include the role of the neural plate, neural tube, notochord, neural crest cells, and somites.", "path":"/sg3/q17"},
            {"question":"Understand the term primary induction.", "path":"/sg3/q18"},
            {"question":"Know how the notochord contributes to the formation of the neural tube. How are the molecules Shh, TGF, and BMP involved in the process? What type of protein is Shh? What are the major types of neurons that initially develop from the neural tube?", "path":"/sg3/q19"},
            {"question":"Be able to convey how the neural tube results in the formation of the brain.", "path":"/sg3/q20"}
        ]
    },
    {
        "header":"Chapter 44: Neurons and Nervous Systems (Generation of Action Potentials)",
        "questions": [
            {"question":"Be able to define the following terms: neurons, nerve, glia, afferent neurons, efferent neurons, ganglia, central nervous system, peripheral nervous system, neurite, and motor neuron.", "path":"/sg3/q21"},
            {"question":"Know the major regions of a neuron and their associated function, including the axon, dendrite, hillock, and synapse.", "path":"/sg3/q22"},
            {"question":"Be familiar with the contributions of Hodgkin and Huxley towards our understanding of the generation of action potentials in neurons. Be able to describe experimental procedures they employed, the major results, and the significance of the results.", "path":"/sg3/q23"}
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
    html.H2("Study Guide 3", style={"textAlign": "center", "marginTop": "20px", "fontFamily":"Arial"}),
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
        ]) for section in sg3_sections
    ], style={"marginTop": "30px", 'fontFamily':'Arial'}),
    html.Div(style = {'height':'100px'})
])
