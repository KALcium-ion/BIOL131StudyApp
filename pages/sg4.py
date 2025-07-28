import dash
import dash_bootstrap_components as dbc
from dash import html

# Define your sections and questions here (example format)
sg4_sections = [
    {
        "header":"Chapter 44: Molecular Basis of Action Potentials",
        "questions": [
            {"question":"Be particularly familiar with the structure and function of Schwann cells. Know what the term saltatory conduction means.", "path":"/sg4/q1"},
            {"question":"Be able to explain, in detail, how Na+ and K+ channels contribute to membrane depolarization, action potentials, and hyperpolarization. Understand how to interpret graphs that a part of Figure 45.10 in your text, which displays changes in membrane potential associated with ion channel activity.", "path":"/sg4/q2"},
            {"question":"Understand the concepts of spatial and temporal summation, and be able to give an example of each.", "path":"/sg4/q3"},
            {"question":"Be able to explain why action potentials, once initiated, can only travel in one direction.", "path":"/sg4/q4"},
            {"question":"Be familiar with the types of ion channels that are stimulated by excitatory presynaptic axons and the inhibitory presynaptic axons. Understand how these two types of axons cause different changes in the membrane potential and how these signals are integrated at the axon hillock.", "path":"/sg4/q5"}
        ]
    },
    {
        "header":"Chapter 47: Muscle Contraction", 
        "questions": [
            {"question":"Know the mechanisms by which an action potential promotes neurotransmitter release at the neuromuscular junction and subsequently stimulate action potentials in the muscle cell (this process involves the acetylcholine receptor).", "path":"/sg4/q6"},
            {"question":"Be familiar with the following trems: sarcomeres, muscle fibers, myofibrils, sarcolemma, sarcoplasm, T tubules, and sarcoplasmic reticulum.", "path":"/sg4/q7"},
            {"question":"Be able to identify the following myofibril structures on a diagram: Z line, myosin filament, actin filament, M band, A band, I band, titin, tropomyosin, troponin, and the globular head.", "path":"/sg4/q8"},
            {"question":"Be able to explain how a stimulated motor neuron transfers an action potential, via the T-tubule, to the sarcoplasmic reticulum, to cause changes in Ca+ levels of the sarcoplasm.", "path":"/sg4/q9"},
            {"question":"Know the detailed mechanism by which Ca+ promotes muscle contraction. Be able to describe the interactions among actin, myosin, tropomyosin, troponin, and ATP.", "path":"/sg4/q10"},
            {"question":"Be able to detail the function of the following proteins in excitation-contracting coupling: DHP receptor, Ry receptor, and SERCA.", "path":"/sg4/q11"}
        ]
    },
    {
        "header":"Chapter 45: Visions Systems Part 1 (Microanatomy)",
        "questions": [
            {"question":"Be able to explain how the sensation of pain in your finger leads to the stimulation of inhibitory and excitatory neurons that causes you to pull your arm back.", "path":"/sg4/q12"},
            {"question":"Know the anatomy of the human eye. Be able to detail how the ganglion, bipolar, rod, and cone cells of the retina work together to deliver action potentials to the optic nerve.", "path":"/sg4/q13"},
            {"question":"Be able to describe the contributions of Santiaga Ramon y Cajal to our understanding of visual perception.", "path":"/sg4/q14"},
            {"question":"Know the anatomy of the rod cell (the major structures).", "path":"/sg4/q15"}
        ]
    },
    {
        "header":"Chapter 45: Vision Systems Part 2 (Mechanisms of Vision)",
        "questions": [
            {"question":"Understand the process by which photoreceptor cells transform light into action potentials. Be able to describe the contributions of rhodopsin, 11-cis-retinal, all-trans-retinal, and transducin to light sensitivity. Know the signaling mechanisms that are associated with the dark response and the light response in rod cells (i.e., guanylyl cyclase, cGMP, PDE, GMP, Na+ channel).", "path":"/sg4/q16"},
            {"question":"Be able to explain how rod cells transmit signals to bipolar cells and then on to ganglion cells. What is the neurotransmitter released by rod cells.", "path":"/sg4/q17"},
            {"question":"Know the difference in functionality between ON-bipolar cells and OFF-bipolar cells.", "path":"/sg4/q18"},
            {"question":"Be familiar with the term receptive field. Know the difference in cellular organization between the On-center receptive field and an Off-center receptive field.", "path":"/sg4/q19"},
            {"question":"Be able to predict the action potential responses when light is directed at the central vs. peripheral region of an On-center receptive field and of an Off-center receptive field.", "path":"/sg4/q20"}
        ]
    },
    {
        "header":"Chapter 46: The Mammalian Nervous System",
        "questions": [
            {"question":"Be familiar with the development changes associated with the formation of the spinal cord, hindbrain, midbrain, and forebrain from the initial neural tube.", "path":"/sg4/q21"},
            {"question":"Know the functions of the major parts of the brain (cerebrum, cerebellum, Pons, Medulla, diencephalon).", "path":"/sg4/q22"},
            {"question":"Be prepared to desribe the anatomy of a spinal nerve (gray matter, white matter, dorsal horn, ventral horn, dorsal root, and ventral root). In this context, know the specific sequence of events that comprise a knee-jerk reflex.", "path":"/sg4/q23"},
            {"question":"Be able to explain the anatomy and functions of the reticular system. Also, be familiar with the components of the limbic system and their roles in regulating basic physiological drives.", "path":"/sg4/q24"},
            {"question":"Know how the parasympathetic and sympathetic nervous systems are related and how they differ. Be able to list the numerous activities they regulate throughout the body. Be familiar with the differences in anatomy between these systems, regarding the use of different neurotransmitters.", "path":"/sg4/q25"},
            {"question":"Be able to name the areas of the brain that contribute to language (Wernicke’s area, Broca’s area, primary motor cortex). Know the sequence of activity of these areas that lead to the repeating of a word that is heard. Along these lines, contrast the activation of language areas that lead to speaking a word that is written (this process involves the visual area and Angular gyrus).", "path":"/sg4/q26"}
        ]
    }
]

layout = html.Div([
    html.Div(
        dbc.Button("Back to Home", href="/", style={
            "backgroundColor": "#3a5a40",
            "color": "white",
            "border": "none",
            'fontWeight':'bold'
        }),
        style={
            "position": "fixed",
            "top": "10px",
            "left": "10px",
            "zIndex": "1000",
        }
    ),
    html.Div(style = {'height':'25px'}),
    html.H2("Study Guide 4", style={"textAlign": "center", "marginTop": "20px"}),
    dbc.Container([
        html.Div([
            html.H4(section["header"], style={"marginTop": "30px", "fontSize": "22px", "fontWeight": "bold"}),
            dbc.ListGroup([
                dbc.ListGroupItem(q["question"], action=True, href=q["path"], style={"fontSize": "18px"})
                for q in section["questions"]
            ])
        ]) for section in sg4_sections
    ], style={"marginTop": "30px"}),
    html.Div(style = {'height':'100px'})
])