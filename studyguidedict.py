'''
            "q2": {
                "question": html.P(""),
                "overview": html.Div([]), 
                "deep_dive": html.Div([]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [],
                "blurting": [],
                "feynman": []
            }, #end of study guide #1, question 2 material
'''

from dash import html

study_guides = {
    "sg1": {
        "questions": {
            "q1": {
                "question":html.P("Be familiar with the process of the Scientific Method and what a hypothesis is."),
                "overview": html.Div([
                    html.P("The scientific method is a systematic approach to understanding natural phenomena. It involves several key steps:"),
                    html.Ul([
                        html.Li("Observation"), 
                        html.Li("Question"), 
                        html.Li("Hypothesis"),
                        html.Li("Experiment"),
                        html.Li("Data Collection"),
                        html.Li("Analysis"),
                        html.Li("Conclusion"),
                        html.Li("Communication"),
                        html.Li("Repetition") 
                        ]),
                    html.P("A hypothesis is an educated guess or a tentative explanation that answers the question posed. It is a prediction that can be tested through experiments.")
                ]),
                "deep_dive": html.Div([
                    html.P(["Let's take a look at each step of the ", html.Strong("scientific method.")]),
                    html.Ul([
                        html.Li([html.Strong("Observation"),": the process of observing a natural phenomenon"]), 
                        html.Li([html.Strong("Question"),": based on the observation, a specific question is formed and asked to try to understand the how (the mechanism) through which the phenomena is occuring."]),
                        html.Li([html.Strong("Hypothesis"), ": the educated guess or tentative explanation which answers the question and serves as the basis of experimentation"]),
                        html.Li([html.Strong("Experiment"), ": the process of designing and conducting an experiment to prove or disprove the hypothesis"]),
                        html.Li([html.Strong("Data Collection"), ": during the experiment, data is gathered in order to analyze the result. Data can be quantitative or qualitative"]),
                        html.Li([html.Strong("Analysis"), ": the process of examining the data for an answer to the hypothesis"]),
                        html.Li([html.Strong("Conclusion"), ": based on the analysis, a conclusion (proving or disproving the hypothesis) is drawn"]),
                        html.Li([html.Strong("Communication"), ": the findings of the experiment are shared with the broader community"]),
                        html.Li([html.Strong("Repetition"), ": the experiment must be able to be replicated in order for the hypothesis to be proven correct and to allow for further exploration of the hypothesis"]) 
                    ]),
                    html.P(["A ", html.Strong("hypothesis"), " is an educated guess or a proposed explanation for a specific observation or question, which is based on prior knowledge and logical reasoning. It is a testable statement that predicts a possible outcome of an experiment."]),
                    html.P("A good hypothesis is:"),
                    html.Ul([
                        html.Li([html.Strong("Specific"), ": the variables and the relationship being tested are clearly defined"]),
                        html.Li([html.Strong("Testable"), ": the hypothesis can be supported or refuted through experimentation"]),
                        html.Li([html.Strong("Falsifiable"), ": there must be a possible outcome that would show the hypothesis is incorrect"])
                    ]),
                    html.P(["A hypothesis is often written as an ", html.Strong("'if/then' statement"), ". If A occurs, then B occurs."]),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li(html.A("Crash Course Biology: The Scientific Method", href = "https://www.youtube.com/watch?v=xOLcZMw0hd4&pp=ygUVdGhlIHNjaWVudGlmaWMgbWV0aG9k", target = "_blank")),
                        html.Li(html.A("Sprouts: The Scientific Method (Examples, Tips, and Exercise)", href = "https://www.youtube.com/watch?v=yi0hwFDQTSQ", target = "_blank")),
                        html.Li(html.A("Khan Academy: The Scientific Method", href = "https://www.youtube.com/watch?v=N6IAzlugWw0&pp=ygUVdGhlIHNjaWVudGlmaWMgbWV0aG9k0gcJCcEJAYcqIYzv", target = "_blank"))
                    ])
                ]),
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter1/Slide10.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className="text-center"),
                    html.Img(
                        src="/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]),
                "practice_questions": [
                    {
                        "question": "What is the first step in the Scientific Method?",
                        "options": ["Forming a hypothesis", "Making an observation", "Conducting an experiment", "Analyzing data", "Drawing a conclusion"],
                        "answer": "Making an observation"
                    },
                    {
                        "question": "A hypothesis in the Scientific Method is best described as:",
                        "options": ["A conclusion based on experimental results", "A testable explanation for an observed phenomenon", "A fact that does not require testing", "A final answer to a research question", "The collection of data from experiments"],
                        "answer": "A testable explanation for an observed phenomenon"
                    },
                    {
                        "question": "Which of the following is true about a good hypothesis?",
                        "options": ["It cannot be tested", "It is based on personal beliefs", "It must be testable and falsifiable", "It provides a final answer", "It can only be proven true"],
                        "answer": "It must be testable and falsifiable"
                    },
                    {
                        "question": "What is typically done after forming a hypothesis in the Scientific Method?",
                        "options": ["Analyze data", "Make an observation", "Form a conclusion", "Design and conduct an experiment", "Report results"],
                        "answer": "Design and conduct an experiment"
                    },
                    {
                        "question": "In the Scientific Method, the experiment is used to:",
                        "options": ["Test the hypothesis", "Form a new hypothesis", "Make observations", "Develop conclusions", "Gather data without a hypothesis"],
                        "answer": "Test the hypothesis"
                    },
                    {
                        "question": "Which of the following is an essential characteristic of scientific inquiry?",
                        "options": ["Personal opinions and beliefs", "Controlled experiments", "Superstition", "Ignoring evidence that contradicts a theory", "Results that are not repeatable"],
                        "answer": "Controlled experiments"
                    },
                    {
                        "question": "What happens if a hypothesis is not supported by experimental data?",
                        "options": ["The hypothesis is proven false", "The hypothesis is discarded and never tested again", "The hypothesis is supported by the data", "The hypothesis is revised or rejected", "The experiment is repeated with the same result"],
                        "answer": "The hypothesis is revised or rejected"
                    },
                    {
                        "question": "What is the purpose of a control group in an experiment?",
                        "options": ["To introduce variables that may affect the outcome", "To ensure the experiment is more complex", "To provide a comparison against the experimental group", "To change the results of the experiment", "To confuse the data analysis"],
                        "answer": "To provide a comparison against the experimental group"
                    },
                    {
                        "question": "In the Scientific Method, after analyzing data, what is the next step?",
                        "options": ["Form a hypothesis", "Make a conclusion", "Reformulate the experiment", "Ask a new question", "Publish the findings"],
                        "answer": "Make a conclusion"
                    },
                    {
                        "question": "A scientific theory is:",
                        "options": ["A guess or prediction", "A tested and well-supported explanation of phenomena", "The first step in the Scientific Method", "A hypothesis that has been proven true", "Always subject to personal opinions"],
                        "answer": "A tested and well-supported explanation of phenomena"
                    },
                    {
                        "question": "What is a key difference between a scientific theory and a scientific law?",
                        "options": ["A law is a broad explanation, while a theory is a specific observation", "A theory is a broad explanation, while a law describes a specific observation", "A law is testable, while a theory is not", "A law explains how phenomena occur, while a theory explains why they occur", "A theory is more reliable than a law"],
                        "answer": "A law describes a specific observation, while a theory explains why they occur"
                    },
                    {
                        "question": "What role does peer review play in the scientific method?",
                        "options": ["It confirms the hypothesis is correct", "It helps to ensure the quality and validity of the experiment and conclusions", "It guarantees the experiment's success", "It provides funding for the research", "It ensures the hypothesis is falsifiable"],
                        "answer": "It helps to ensure the quality and validity of the experiment and conclusions"
                    },
                    {
                        "question": "Which of the following is a hypothesis that can be tested through an experiment?",
                        "options": ["All living things are made of cells", "Plants will grow faster in soil with more nitrogen", "Evolution is true", "The Earth is round", "The sun rises in the east"],
                        "answer": "Plants will grow faster in soil with more nitrogen"
                    },
                    {
                        "question": "Which of the following is an example of a controlled experiment?",
                        "options": ["Measuring the speed of light", "Testing the effect of different amounts of fertilizer on plant growth while keeping all other factors constant", "Observing stars through a telescope", "Studying the population of a species in the wild", "Examining historical events"],
                        "answer": "Testing the effect of different amounts of fertilizer on plant growth while keeping all other factors constant"
                    },
                    {
                        "question": "What is the purpose of the observation phase in the Scientific Method?",
                        "options": ["To test the hypothesis", "To form a conclusion", "To make sense of existing knowledge", "To gather data and identify patterns or problems", "To publish the findings"],
                        "answer": "To gather data and identify patterns or problems"
                    },
                    {
                        "question": "What does it mean when a hypothesis is falsifiable?",
                        "options": ["It can be proven true", "It can be tested and potentially shown to be false", "It is universally accepted", "It cannot be tested", "It is based on facts only"],
                        "answer": "It can be tested and potentially shown to be false"
                    },
                    {
                        "question": "After an experiment, why is it important to share your results with others?",
                        "options": ["To get recognition", "To allow others to replicate the study and verify results", "To persuade others to agree with your hypothesis", "To demonstrate the experiment's limitations", "To ensure the results are kept confidential"],
                        "answer": "To allow others to replicate the study and verify results"
                    },
                    {
                        "question": "Which of the following statements about a theory in science is true?",
                        "options": ["It is always proven true", "It is a tested and well-supported explanation that can be modified over time", "It can never change once established", "It is the same as a hypothesis", "It is a guess made before experimentation"],
                        "answer": "It is a tested and well-supported explanation that can be modified over time"
                    },
                    {
                        "question": "Why is it important for experiments to have a control group?",
                        "options": ["To eliminate all variables from the experiment", "To make the experiment more complex", "To measure the impact of the independent variable", "To compare the effects of different variables", "To manipulate the experiment's outcome"],
                        "answer": "To measure the impact of the independent variable"
                    },
                    {
                        "question": "In the Scientific Method, what step involves interpreting the results and determining if the hypothesis is supported?",
                        "options": ["Making observations", "Forming a hypothesis", "Drawing a conclusion", "Designing an experiment", "Communicating results"],
                        "answer": "Drawing a conclusion"
                    }
                ],
                "blurting": [
                        html.Div([
                            html.P(["Let's take a look at each step of the ", html.Strong("scientific method.")]),
                            html.Ul([
                                html.Li([html.Strong("Observation"),": the process of observing a natural phenomenon"]), 
                                html.Li([html.Strong("Question"),": based on the observation, a specific question is formed and asked to try to understand the how (the mechanism) through which the phenomena is occuring."]),
                                html.Li([html.Strong("Hypothesis"), ": the educated guess or tentative explanation which answers the question and serves as the basis of experimentation"]),
                                html.Li([html.Strong("Experiment"), ": the process of designing and conducting an experiment to prove or disprove the hypothesis"]),
                                html.Li([html.Strong("Data Collection"), ": during the experiment, data is gathered in order to analyze the result. Data can be quantitative or qualitative"]),
                                html.Li([html.Strong("Analysis"), ": the process of examining the data for an answer to the hypothesis"]),
                                html.Li([html.Strong("Conclusion"), ": based on the analysis, a conclusion (proving or disproving the hypothesis) is drawn"]),
                                html.Li([html.Strong("Communication"), ": the findings of the experiment are shared with the broader community"]),
                                html.Li([html.Strong("Repetition"), ": the experiment must be able to be replicated in order for the hypothesis to be proven correct and to allow for further exploration of the hypothesis"]) 
                            ]),
                        html.P(["A ", html.Strong("hypothesis"), " is an educated guess or a proposed explanation for a specific observation or question, which is based on prior knowledge and logical reasoning. It is a testable statement that predicts a possible outcome of an experiment."]),
                        html.P("A good hypothesis is:"),
                        html.Ul([
                            html.Li([html.Strong("Specific"), ": the variables and the relationship being tested are clearly defined"]),
                            html.Li([html.Strong("Testable"), ": the hypothesis can be supported or refuted through experimentation"]),
                            html.Li([html.Strong("Falsifiable"), ": there must be a possible outcome that would show the hypothesis is incorrect"])
                        ]),
                        html.P(["A hypothesis is often written as an", html.Strong("'if/then' statement"), ". If A occurs, then B occurs."])
                        ], style = {'textAlign':'left'})
                ],
                "feynman":[
                    html.Div([
                        html.Div(
                            html.P(["The ", html.Strong("Scientific Method "), "is a way of thinking about how or why something you saw happens the way it does. It involves a lot of steps, such as looking at whatever is happening, making a guess about why it happens that way, and testing that guess. The guess on how or why something happens is called a hypothesis."]),
                        )
                    ], style = {'textAlign':'left'}),
                ]
            }, #end of study guide #1, question 1 material
            "q2": {
                "question": html.P("Know the various types of chemical bonds discussed and the basis of their interactions (such as covalent, hydrogen, and double covalent.)"),
                "overview": html.Div([
                    html.P("The types of bonds to know are as follows: "),
                    html.Ul([
                        html.Li([html.Strong("Covalent bond")]),
                        html.Li([html.Strong("Polar covalent bond")]),
                        html.Li([html.Strong("Hydrogen bond")])
                    ]),
                    html.Div([html.P(["The other important concept to understand is that of" , html.Strong(" electronegativity.")])]),
                    html.P("In short:"),
                    html.Ul([
                        html.Li([html.Strong("Covalent bond: "), "atoms share electrons equally"]),
                        html.Li([html.Strong("Polar covalent bond: "), "atoms share electrons unequally"]),
                        html.Li([html.Strong("Hydrogen bond: "), "forms only between particular types of atoms"])
                    ]),
                    html.P([html.Strong("Electronegativity "), "is how attracted electrons are to the nucleus of an atom"])
                ]), 
                "deep_dive": html.Div([
                    html.Ul([html.Li([html.Strong("Covalent bond: "), "A chemical bond that is formed when two atoms are sharing one or more pairs of electrons. It forms because atoms are then able to achieve a more stable electron configuration, typically through filling their outer valence electron shell. The bond strengths very high as covalent bonds are among the strongest chemical bonds."])]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/covalent bond.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.chemistrylearner.com/chemical-bonds/covalent-bond", target = "_blank")])
                        ]
                    ),
                    html.Ul([html.Li([html.Strong("Polar covalent bond: "), "A chemical bond that is formed when two atoms are sharing one or more pairs of electrons unequally. This occurs because one atom pulls the electrons closer than the other atom. This creates partial charges, where the more electronegative atom will get a partial negative charge and the less electronegative atom will get a partial positive charge. The reason that polar covalent bonds can form is due to the difference in electronegativity between the two atoms."])]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/polar covalent bond.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.chemistrylearner.com/chemical-bonds/covalent-bond/polar-covalent-bond", target = "_blank")])
                        ]
                    ),
                    html.Ul([html.Li([html.Strong("Hydrogen bond: "), "A weak attraction between a hydrogen atom attached to an electronegative atom such as F, O, or N (remember that hydrogen bonds are 'FON' ('fun')) and another electronegative atom with a lone pair of electrons. Hydrogen bonds are weaker than covalent bonds, but biologically important. It is not a 'true' bond, but rather an intermolecular force (meaning that it occurs between molecules, not within molecules)."])]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/hydrogen bond.jpg", style = {'width':'400px', 'marginRight':'40px'}),
                            html.Img(src = "/assets/hydrogen bond examples.jpg", style = {'width':'400px','marginRight':'40px'}),
                            html.Div(["Images from ", html.A("here", href = "https://www.chemistrylearner.com/chemical-bonds/hydrogen-bond", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Electronegativity "), "is the ability of an atom to attract electrons towards itself. You can imagine it as the 'electron hunger' of atoms. On the period table, electronegativity increases from left to right and decreases from top to bottom. Differences in electronegativity contribute to the type of bond that is formed."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/Electronegativity-polar-covalent-bond.jpg", style = {'marginRight':'40px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://www.chemistrylearner.com/the-periodic-table/electronegativity", target = "_blank")])
                        ]
                    ),
                    html.P("If you imagine electrons like a tug-of-war rope, nonpolar covalent bonds occur when both 'teams' (atoms) pull equally on the rope. Polar covalent bonds occur when one 'team' (atom) is stronger than the other and can pull more of the rope towards itself. Ionic bonds occur when one team (atom) lets go completely, so the other team (atom) has the entire rope all to itself."),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li(html.A("Crash Course: Types of Chemical Bonds", href = "https://www.youtube.com/watch?v=QXT4OVM4vXI&t=198s&pp=ygUsY292YWxlbnQsIHBvbGFyIGNvdmFsZW50LCBhbmQgaHlkcm9nZW4gYm9uZHPSBwkJwQkBhyohjO8%3D", target = "_blank")), 
                        html.Li(html.A("Professor Dave Explains: Covalent vs. Ionic and Polar vs. Nonpolar", href = "https://www.youtube.com/watch?v=PoQjsnQmxok&pp=ygUsY292YWxlbnQsIHBvbGFyIGNvdmFsZW50LCBhbmQgaHlkcm9nZW4gYm9uZHM%3D", target = "_blank")), 
                        html.Li(html.A("The Organic Chemistry Tutor: Ionic Bonds, Polar Covalent Bonds, and Nonpolar Covalent Bonds", href = "https://www.youtube.com/watch?v=8NQzcpWvq4g&pp=ygUsY292YWxlbnQsIHBvbGFyIGNvdmFsZW50LCBhbmQgaHlkcm9nZW4gYm9uZHPSBwkJwQkBhyohjO8%3D", target = "_blank")), 
                        html.Li(html.A("Whats Up Dude: Hydrogen Bonds (What Are Hydrogen Bonds, How Do Hydrogen Bonds Form)", href = "https://www.youtube.com/watch?v=RSRiywp9v9w&pp=ygUOaHlkcm9nZW4gYm9uZHM%3D", target = "_blank"))
                    ])
                ]), 
                "lecture" : html.Div([
                    html.Img(src = "/assets/Chapter1/Slide14.jpg"),
                    html.Img(src = "/assets/Chapter1/Slide15.jpg"),
                    html.Img(src = "/assets/Chapter1/Slide19.jpg"),
                    html.Img(src = "/assets/Chapter1/Slide20.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide21.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide22.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question2.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Which of the following best describes a covalent bond?",
                        "options": ["Electrons are transferred from one atom to another", "Electrons are shared equally between atoms", "Electrons are shared between atoms", "Electrons are completely absent", "One atom pulls all electrons away from the other"],
                        "answer": "Electrons are shared between atoms"
                    },
                    {
                        "question": "What is the key characteristic of a polar covalent bond?",
                        "options": ["Electrons are shared equally", "One atom has a greater electronegativity, leading to unequal sharing of electrons", "Electrons are completely transferred from one atom to another", "Atoms share electrons with no charge difference", "Both atoms in the bond are equally electronegative"],
                        "answer": "One atom has a greater electronegativity, leading to unequal sharing of electrons"
                    },
                    {
                        "question": "What does electronegativity refer to?",
                        "options": ["The ability of an atom to attract protons", "The ability of an atomic nucleus to attract electrons", "The number of electrons in an atom", "The number of neutrons in an atom", "The distance between an atom's nucleus and electrons"],
                        "answer": "The ability of an atomic nucleus to attract electrons"
                    },
                    {
                        "question": "Which of the following is a characteristic of hydrogen bonds?",
                        "options": ["They are weaker than covalent bonds", "They only form between atoms of the same element", "They provide the primary structural support for covalent bonds", "They form only in gases", "They are stronger than ionic bonds"],
                        "answer": "They are weaker than covalent bonds"
                    },
                    {
                        "question": "How do hydrogen bonds contribute to the properties of water?",
                        "options": ["They allow water to form strong covalent bonds", "They make water molecules non-polar", "They help water resist changes in temperature and provide cohesion", "They prevent water from evaporating", "They make water a good solvent for ionic compounds"],
                        "answer": "They help water resist changes in temperature and provide cohesion"
                    },
                    {
                        "question": "What is the role of hydrogen bonds in protein structure?",
                        "options": ["They hold the covalent bonds together", "They determine the sequence of amino acids in a protein", "They help to stabilize the 3D shape of proteins", "They are responsible for the peptide bonds between amino acids", "They form the primary structure of the protein"],
                        "answer": "They help to stabilize the 3D shape of proteins"
                    },
                    {
                        "question": "What kind of bond is formed between water molecules?",
                        "options": ["Covalent bond", "Polar covalent bond", "Hydrogen bond", "Ionic bond", "Metallic bond"],
                        "answer": "Hydrogen bond"
                    },
                    {
                        "question": "Which of the following best explains why oxygen in a water molecule is more electronegative than hydrogen?",
                        "options": ["Oxygen has more protons, which attract electrons more strongly", "Oxygen is less reactive than hydrogen", "Hydrogen is larger than oxygen", "Hydrogen has more electrons than oxygen", "Oxygen has a more stable electron shell"],
                        "answer": "Oxygen has more protons, which attract electrons more strongly"
                    },
                    {
                        "question": "Which of the following is an example of a polar covalent bond?",
                        "options": ["The bond between two oxygen atoms in O2", "The bond between hydrogen and oxygen in water", "The bond between sodium and chlorine in NaCl", "The bond between two hydrogen atoms in H2", "The bond between carbon and hydrogen in methane"],
                        "answer": "The bond between hydrogen and oxygen in water"
                    },
                    {
                        "question": "Why do hydrogen bonds play an important role in the double helix structure of DNA?",
                        "options": ["They hold the sugar-phosphate backbone together", "They provide energy for DNA replication", "They form the bonds between complementary base pairs", "They help to organize the DNA inside the nucleus", "They make the DNA molecule soluble in water"],
                        "answer": "They form the bonds between complementary base pairs"
                    },
                    {
                        "question": "Which of the following is the best example of a covalent bond?",
                        "options": ["The bond between sodium and chloride in NaCl", "The bond between hydrogen and oxygen in water", "The bond between calcium and chloride in CaCl2", "The bond between magnesium and oxygen in MgO", "The bond between nitrogen and oxygen in NO2"],
                        "answer": "The bond between hydrogen and oxygen in water"
                    },
                    {
                        "question": "What is the result of unequal sharing of electrons in a covalent bond?",
                        "options": ["A non-polar covalent bond", "An ionic bond", "A polar covalent bond", "A metallic bond", "A hydrogen bond"],
                        "answer": "A polar covalent bond"
                    },
                    {
                        "question": "What does it mean when a molecule is described as polar?",
                        "options": ["The molecule has equal distribution of charge", "The molecule has a net charge", "The electrons are shared equally", "The molecule has an unequal distribution of charge", "The molecule contains only covalent bonds"],
                        "answer": "The molecule has an unequal distribution of charge"
                    },
                    {
                        "question": "What role do hydrogen bonds play in the structure of DNA?",
                        "options": ["They hold the sugar-phosphate backbone together", "They form the covalent bonds between the nucleotides", "They connect complementary base pairs of nucleotides", "They stabilize the helical structure of the DNA", "They prevent the strands from separating"],
                        "answer": "They connect complementary base pairs of nucleotides"
                    },
                    {
                        "question": "Which of the following bonds results from the attraction between two oppositely charged ions?",
                        "options": ["Covalent bond", "Polar covalent bond", "Ionic bond", "Hydrogen bond", "Metallic bond"],
                        "answer": "Ionic bond"
                    },
                    {
                        "question": "Why do covalent bonds form between atoms?",
                        "options": ["To transfer electrons and create oppositely charged ions", "To fill the atoms' outer electron shells by sharing electrons", "To create a strong electrical charge between atoms", "To form stable molecules with high electronegativity", "To enable atoms to repel each other"],
                        "answer": "To fill the atoms' outer electron shells by sharing electrons"
                    },
                    {
                        "question": "How does electronegativity affect the formation of a polar covalent bond?",
                        "options": ["The atom with lower electronegativity attracts electrons more", "Electrons are shared equally between atoms", "The atom with higher electronegativity attracts more electrons", "Electrons are transferred from one atom to the other", "The two atoms are equally electronegative"],
                        "answer": "The atom with higher electronegativity attracts more electrons"
                    },
                    {
                        "question": "What is the primary reason why water molecules form hydrogen bonds?",
                        "options": ["Water has a polar covalent bond", "Water molecules are non-polar", "Water molecules have a negative charge", "Water molecules have an even distribution of charge", "Water molecules form ionic bonds"],
                        "answer": "Water has a polar covalent bond"
                    },
                    {
                        "question": "What type of bond is formed between two atoms of the same element, such as two oxygen atoms in O2?",
                        "options": ["Covalent bond", "Polar covalent bond", "Hydrogen bond", "Ionic bond", "Metallic bond"],
                        "answer": "Covalent bond"
                    },
                    {
                        "question": "Which of the following statements about electronegativity is true?",
                        "options": ["Electronegativity increases with the number of protons", "Electronegativity decreases with the number of protons", "Electronegativity depends only on the size of the atom", "Electronegativity is irrelevant to bond formation", "Electronegativity is constant across all elements"],
                        "answer": "Electronegativity increases with the number of protons"
                    },
                    {
                        "question": "Which type of bond is formed when one atom donates an electron to another atom?",
                        "options": ["Covalent bond", "Polar covalent bond", "Ionic bond", "Hydrogen bond", "Metallic bond"],
                        "answer": "Ionic bond"
                    },
                    {
                        "question": "What is the main difference between a non-polar covalent bond and a polar covalent bond?",
                        "options": ["Non-polar covalent bonds involve equal sharing of electrons, while polar covalent bonds involve unequal sharing of electrons", "Non-polar covalent bonds are stronger than polar covalent bonds", "Non-polar covalent bonds form only between similar atoms", "Non-polar covalent bonds result in a net charge", "Polar covalent bonds are found only in water"],
                        "answer": "Non-polar covalent bonds involve equal sharing of electrons, while polar covalent bonds involve unequal sharing of electrons"
                    },
                    {
                        "question": "What property of water is primarily due to hydrogen bonding?",
                        "options": ["Low boiling point", "High heat capacity", "Low surface tension", "High viscosity", "Non-polarity"],
                        "answer": "High heat capacity"
                    },
                    {
                        "question": "What does the term 'electronegativity' describe in relation to covalent bonds?",
                        "options": ["The ability of an atom to form bonds with metals", "The tendency of an atom to attract and hold onto electrons in a bond", "The force that causes an atom to repel electrons", "The strength of a covalent bond", "The energy required to break a bond"],
                        "answer": "The tendency of an atom to attract and hold onto electrons in a bond"
                    },
                    {
                        "question": "Which of the following statements is true about hydrogen bonds?",
                        "options": ["Hydrogen bonds are stronger than covalent bonds", "Hydrogen bonds occur between positively charged hydrogen atoms and negatively charged atoms", "Hydrogen bonds form only in organic molecules", "Hydrogen bonds involve the sharing of electrons", "Hydrogen bonds occur between atoms of the same element"],
                        "answer": "Hydrogen bonds occur between positively charged hydrogen atoms and negatively charged atoms"
                    },
                    {
                        "question": "Which type of bond holds the two strands of a DNA molecule together?",
                        "options": ["Covalent bonds", "Hydrogen bonds", "Ionic bonds", "Peptide bonds", "Van der Waals forces"],
                        "answer": "Hydrogen bonds"
                    },
                    {
                        "question": "Which element typically forms polar covalent bonds due to its high electronegativity?",
                        "options": ["Oxygen", "Sodium", "Calcium", "Carbon", "Nitrogen"],
                        "answer": "Oxygen"
                    },
                    {
                        "question": "What is the relationship between electronegativity differences and bond polarity?",
                        "options": ["A small electronegativity difference results in a non-polar bond", "A large electronegativity difference results in a non-polar bond", "A large electronegativity difference results in a polar bond", "Electronegativity differences have no effect on bond polarity", "A small electronegativity difference results in a polar bond"],
                        "answer": "A large electronegativity difference results in a polar bond"
                    },
                    {
                        "question": "In what way do hydrogen bonds affect the structure of proteins?",
                        "options": ["They stabilize the 3D structure by holding together the protein's primary structure", "They are responsible for the peptide bonds in proteins", "They help fold the protein into its functional shape by stabilizing the tertiary structure", "They are the main force that holds the protein's primary sequence", "They disrupt protein folding by causing denaturation"],
                        "answer": "They help fold the protein into its functional shape by stabilizing the tertiary structure"
                    },
                    {
                        "question": "Which of the following molecules contains both covalent and hydrogen bonds?",
                        "options": ["NaCl", "H2O", "O2", "CO2", "CaCl2"],
                        "answer": "H2O"
                    },
                    {
                        "question": "What type of bond is formed when two atoms share a pair of electrons?",
                        "options": ["Covalent bond", "Ionic bond", "Hydrogen bond", "Metallic bond", "Van der Waals forces"],
                        "answer": "Covalent bond"
                    },
                    {
                        "question": "What type of covalent bond occurs when electrons are shared equally between two atoms?",
                        "options": ["Polar covalent bond", "Ionic bond", "Non-polar covalent bond", "Hydrogen bond", "Metallic bond"],
                        "answer": "Non-polar covalent bond"
                    },
                    {
                        "question": "Which of the following is an example of a molecule that contains a polar covalent bond?",
                        "options": ["O2", "H2O", "N2", "CH4", "Cl2"],
                        "answer": "H2O"
                    },
                    {
                        "question": "Which of the following types of bonds is responsible for the high boiling point of water?",
                        "options": ["Covalent bonds", "Hydrogen bonds", "Ionic bonds", "Peptide bonds", "Van der Waals forces"],
                        "answer": "Hydrogen bonds"
                    },
                    {
                        "question": "What determines whether a covalent bond is polar or non-polar?",
                        "options": ["The type of atoms involved", "The electronegativity difference between the atoms", "The size of the atoms involved", "The number of bonds formed", "The presence of hydrogen atoms"],
                        "answer": "The electronegativity difference between the atoms"
                    },
                    {
                        "question": "How does the electronegativity of an atom influence its ability to form bonds?",
                        "options": ["A higher electronegativity makes an atom less likely to form bonds", "A higher electronegativity makes an atom more likely to attract electrons in a bond", "Electronegativity has no effect on bond formation", "A higher electronegativity makes an atom more likely to donate electrons", "Electronegativity determines the color of the atom in a molecule"],
                        "answer": "A higher electronegativity makes an atom more likely to attract electrons in a bond"
                    },
                    {
                        "question": "Which of the following bonds is typically weaker than ionic and covalent bonds?",
                        "options": ["Covalent bonds", "Ionic bonds", "Hydrogen bonds", "Metallic bonds", "Peptide bonds"],
                        "answer": "Hydrogen bonds"
                    },
                    {
                        "question": "Which property of water is most directly associated with its hydrogen bonding?",
                        "options": ["Its high surface tension", "Its low freezing point", "Its lack of polarity", "Its low boiling point", "Its ability to dissolve non-polar molecules"],
                        "answer": "Its high surface tension"
                    },
                    {
                        "question": "Which type of bond occurs between a hydrogen atom and an electronegative atom like oxygen or nitrogen?",
                        "options": ["Ionic bond", "Covalent bond", "Hydrogen bond", "Metallic bond", "Peptide bond"],
                        "answer": "Hydrogen bond"
                    },
                    {
                        "question": "What is the result of a hydrogen bond between two molecules?",
                        "options": ["A strong covalent bond is formed", "Electrons are transferred between the molecules", "A temporary bond between molecules is formed due to attraction between partial charges", "A new molecule is synthesized", "The molecules become chemically inert"],
                        "answer": "A temporary bond between molecules is formed due to attraction between partial charges"
                    }
                ],
                "blurting": [html.Div([
                                html.Ul([
                                    html.Li([html.Strong("Covalent bond: "), "atoms share electrons equally"]),
                                    html.Li([html.Strong("Polar covalent bond: "), "atoms share electrons unequally"]),
                                    html.Li([html.Strong("Hydrogen bond: "), "forms only between particular types of atoms"])
                                ]),
                                html.P([html.Strong("Electronegativity "), "is how attracted electrons are to the nucleus of an atom"])
                            ])],
                "feynman": [html.Div([
                    html.P(["Atoms are tiny building blocks that make up everything. They like to connect with other atoms so that they can become more stable and they do this by sharing little pieces called ", html.Strong("electrons")]),
                    html.Ul([
                        html.Li(["When atoms are sharing electrons equally, it is called a", html.Strong(" covalent bond")]),
                        html.Li(["If one atom pulls harder on the electrons, then it is called a", html.Strong(" polar covalent bond")]),
                        html.Li(["This happens because some atoms are able to pull better than others. This pulling power is called", html.Strong(" electronegativity")]), 
                        html.Li(html.P(["Another type of connection is called a", html.Strong(" hydrogen bond "), "which is not a 'strong hold' like the others, but rather more like stickiness. It happens when parts of molecules are a little bit positive or a little bit negative, causing them to attract like tiny magnets."])),
                    ]), 
                    html.P("Hydrogen bonds are important because they help water stay together, help proteins fold into their special shapes, and help DNA twist into its spiral shape, among other things."),
                    html.P("An analogy for this could be kids at recess. A covalent bond is when two kids are playing with a jump rope and sharing it, nicely and evenly. A polar covalent bond is when one kid is pulling on the jump rope harder than the other. A hydrogen bond is like the two kids giving each other a high-five. It is not a tight grip, but it still connects them a little. Electronegativity is like how some kids are stronger than other kids and can therefore pull the rope more easily.")
                ])]
            }, #end of study guide #1, question 2 material
            "q3": {
                "question": html.P("Be able to describe the various important properties of water."),
                "overview": html.Div([
                    html.P("There are four primary important properties of water:"),
                    html.Ul([
                        html.Li([html.Strong("High cohesive strength: "), "Water is sticky"]),
                        html.Li([html.Strong("High specific heat: "), "It takes a lot of energy to heat up water"]),
                        html.Li([html.Strong("High surface tension: "), "Because water is sticky, the surface of water is hard to puncture."]),
                        html.Li([html.Strong("Universal solvent: "), "Water can act as a weak acid"])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.P("A water molecule is composed of two hydrogen atoms covalently bonded to an oxygen atom. Oxygen is more electronegative, so a polar covalent bond is formed."),
                    html.P("This causes the oxygen to have a partial negative charge and the hydrogens to have a partial positive charge."), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/water molecule.jpg", style = {'width':'500px','marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://courses.lumenlearning.com/suny-monroe-environmentalbiology/chapter/2-1-matter/", target = "_blank")])
                        ]
                    ),
                    html.P(["Because of the charge difference between oxygen and hydrogen, ", html.Strong("hydrogen bonds "), "form between water molecules. Hydrogen bonds are the basis of nearly all of water's important properties."]),
                    html.P("Let's take a look at each of the properties in more detail."), 
                    html.P(""),
                    html.P([html.Strong("High cohesive strength: Cohesion "), "is the attraction between molecules. Water has high cohesion because each molecule can form up to four hydrogen bonds with neighboring water molecules, creating a very strong, structured network. This network is what makes water so 'sticky' in comparison to other liquids."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/water cohesion.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://theory.labster.com/adhesion-cohesion/", target = "_blank")])
                        ]
                    ), 
                    html.P([html.Strong("High specific heat: Specific heat "), "is the amount of energy required to raise the temperature of 1 gram of a substance by 1 degree Celsius. Water has high speciic heat because it takes a lot of energy to break the hydrogen bonds in the 'water network.'"]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/specific heat.jpg", style = {'marginRight':'40px', 'width':'500px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.sciencefacts.net/specific-heat.html", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("High surface tension: Surface tension "), "is the force that acts on the surface of a liquid. In water, surface water molecules are attracted more strongly inward (toward the rest of the liquid) because at the surface, there are fewer water molecules nearby to hydrogen bond with. The inward pull creates a very tight and cohesive surface. Fun fact: water has the highest surface tension of any liquid except for mercury!"]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/surface tension.jpg", style = {'marginRight':'40px', 'width':'500px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.sciencefacts.net/surface-tension.html", target = "_blank:")])
                        ]
                    ),
                    html.P([html.Strong("Universal solvent: "), "Water is considered the universal solvent because it can dissolve more substances than any other liquid, particularly ionic compounds and polar molecules. It is such a good solvent because of its polar nature (remember that the oxygen has a partial negative charge, which attracts positive ions, and the hydrogens have partial positive charges, which attract negative ions). These interactions allow water to surround solute particles, separating them and dissolving them. Fun fact: that process is known as hydration or solvation!"]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/universal solvent.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://en.khanacademy.org/science/biology/water-acids-and-bases/hydrogen-bonding-in-water/a/water-as-a-solvent", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources")]), 
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Properties of Water", href = "https://www.youtube.com/watch?v=3jwAGWky98c&t=69s", target = "_blank")]),
                        html.Li([html.A("Crash Course: Water - Liquid Awesome", href = "https://www.youtube.com/watch?v=HVT3Y3_gHGg&t=2s&pp=ygUVcHJvcGVydGllcyBvZiB0d2F0ZXIg", target = "_blank")]),
                        html.Li([html.A("Crash Course: The Unexpected Truth About Water", href = "https://www.youtube.com/watch?v=zheKWEkW94o&t=310s&pp=ygUVcHJvcGVydGllcyBvZiB0d2F0ZXIg", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Physical Properties of Water", href = "https://www.youtube.com/watch?v=ltFNs994mGI&pp=ygUVcHJvcGVydGllcyBvZiB0d2F0ZXIg", target = "_blank")])
                    ])
                ]), 
                "lecture" : html.Div([
                    html.Img(src = "/assets/Chapter1/Slide15.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide16.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide17.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide18.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide21.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide23.jpg"), 
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question3.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Why does water have a high specific heat?",
                        "options": ["It has a low molecular weight", "Its molecules form ionic bonds with each other", "Its hydrogen bonds absorb a lot of energy before breaking", "It has a high density at all temperatures"],
                        "answer": "Its hydrogen bonds absorb a lot of energy before breaking"
                    },
                    {
                        "question": "Which of the following is a result of water’s high specific heat?",
                        "options": ["Water molecules are more likely to evaporate quickly", "Organisms easily overheat", "Large bodies of water experience rapid temperature changes", "Bodies of water maintain stable temperatures throughout the year"],
                        "answer": "Bodies of water maintain stable temperatures throughout the year"
                    },
                    {
                        "question": "What property of water makes it difficult to puncture the surface?",
                        "options": ["Its high density at cold temperatures", "The tight packing of oxygen atoms", "The hydrogen bonding between surface molecules and those below", "The covalent bonding of all surface molecules"],
                        "answer": "The hydrogen bonding between surface molecules and those below"
                    },
                    {
                        "question": "What does it mean that water is the 'universal solvent'?",
                        "options": ["Water dissolves only nonpolar substances", "Water dissolves more substances than any other liquid", "Water cannot dissolve ionic compounds", "Water is always acidic in nature"],
                        "answer": "Water dissolves more substances than any other liquid"
                    },
                    {
                        "question": "Why is water able to dissolve many substances?",
                        "options": ["Because water has a high boiling point", "Because it can form hydrogen bonds with nonpolar molecules", "Because it is a polar molecule that interacts with charged or polar substances", "Because its molecules repel one another"],
                        "answer": "Because it is a polar molecule that interacts with charged or polar substances"
                    },
                    {
                        "question": "What happens when water captures a hydrogen ion?",
                        "options": ["It forms a salt", "It becomes more neutral in pH", "It forms a hydroxide ion and a hydronium ion", "It loses all hydrogen atoms"],
                        "answer": "It forms a hydroxide ion and a hydronium ion"
                    },
                    {
                        "question": "At what temperature is water’s density greatest?",
                        "options": ["0°C", "4°C", "100°C", "Room temperature"],
                        "answer": "4°C"
                    },
                    {
                        "question": "Which of the following is true about water’s density as it cools?",
                        "options": ["It continues to increase indefinitely", "It increases until 4°C, then decreases as it approaches 0°C", "It decreases steadily from 100°C to 0°C", "It does not change at all"],
                        "answer": "It increases until 4°C, then decreases as it approaches 0°C"
                    },
                    {
                        "question": "How does water act like a weak acid?",
                        "options": ["It donates hydrogen atoms to form NaCl", "It dissolves only in acidic environments", "It dissociates to form hydronium and hydroxide ions", "It neutralizes all other acids in solution"],
                        "answer": "It dissociates to form hydronium and hydroxide ions"
                    },
                    {
                        "question": "Which of the following best explains why water exhibits surface tension?",
                        "options": ["Water molecules are repelled by air", "Water molecules at the surface experience stronger hydrogen bonding with molecules below", "Covalent bonds hold surface molecules tightly", "Water molecules lose energy at the surface"],
                        "answer": "Water molecules at the surface experience stronger hydrogen bonding with molecules below"
                    },
                    {
                        "question": "Why does ice float on liquid water?",
                        "options": ["Ice is composed of nonpolar molecules", "Ice is denser due to molecular compression", "The hydrogen bonds in ice create a crystalline structure with lower density", "The oxygen atoms in ice weigh less than in water"],
                        "answer": "The hydrogen bonds in ice create a crystalline structure with lower density"
                    },
                    {
                        "question": "Why does ice float on liquid water?",
                        "options": ["Ice is composed of nonpolar molecules", "Ice is denser due to molecular compression", "The hydrogen bonds in ice create a crystalline structure with lower density", "The oxygen atoms in ice weigh less than in water"],
                        "answer": "The hydrogen bonds in ice create a crystalline structure with lower density"
                    },
                    {
                        "question": "Which statement about water’s density is true?",
                        "options": ["Water is most dense at 0°C", "Water’s density increases continuously as temperature decreases", "Water is least dense at 4°C", "Water is most dense at 4°C"],
                        "answer": "Water is most dense at 4°C"
                    },
                    {
                        "question": "Which of the following contributes most to water’s role in temperature regulation?",
                        "options": ["Its polarity", "Its low molecular weight", "Its high specific heat", "Its high freezing point"],
                        "answer": "Its high specific heat"
                    },
                    {
                        "question": "What allows water to move upward through narrow plant vessels against gravity?",
                        "options": ["High specific heat", "High surface tension and cohesive forces", "Low density of water", "Water’s neutral pH"],
                        "answer": "High surface tension and cohesive forces"
                    },
                    {
                        "question": "How does water interact with ionic compounds like NaCl?",
                        "options": ["Water molecules align randomly and repel ions", "Water breaks the covalent bonds in NaCl", "Water surrounds the ions and dissolves them due to polarity", "Water removes electrons from the ions"],
                        "answer": "Water surrounds the ions and dissolves them due to polarity"
                    },
                    {
                        "question": "Why can water dissolve polar substances?",
                        "options": ["Because it contains ionic bonds", "Because its molecules are nonpolar", "Because it forms hydrogen bonds with other polar molecules", "Because it has a low boiling point"],
                        "answer": "Because it forms hydrogen bonds with other polar molecules"
                    },
                    {
                        "question": "Which property of water is most responsible for moderating Earth's climate?",
                        "options": ["Its high surface tension", "Its universal solvent ability", "Its high cohesive strength", "Its high specific heat"],
                        "answer": "Its high specific heat"
                    },
                    {
                        "question": "Which of the following explains why sweating helps cool the body?",
                        "options": ["Water molecules evaporate easily at low temperatures", "Heat is absorbed when hydrogen bonds form", "Evaporation removes heat as hydrogen bonds break", "Covalent bonds release heat when broken"],
                        "answer": "Evaporation removes heat as hydrogen bonds break"
                    },
                    {
                        "question": "Why do polar molecules dissolve more readily in water than nonpolar molecules?",
                        "options": ["Polar molecules repel water, breaking it into ions", "Polar molecules can form hydrogen bonds with water", "Nonpolar molecules have stronger bonds with water", "Nonpolar molecules are heavier and sink"],
                        "answer": "Polar molecules can form hydrogen bonds with water"
                    },
                    {
                        "question": "What role do hydrogen bonds play in water’s high surface tension?",
                        "options": ["They prevent molecules from separating at high temperatures", "They allow water molecules to evaporate more quickly", "They tightly hold surface molecules together", "They create ionic interactions at the surface"],
                        "answer": "They tightly hold surface molecules together"
                    },
                    {
                        "question": "Which of the following would most likely dissolve in water?",
                        "options": ["Nonpolar oil molecules", "Large hydrophobic proteins", "Polar sugar molecules", "Inert gases like helium"],
                        "answer": "Polar sugar molecules"
                    },
                    {
                        "question": "How does water help regulate the temperature inside living organisms?",
                        "options": ["By dissolving all organic molecules", "By resisting temperature changes due to high specific heat", "By lowering the boiling point of bodily fluids", "By increasing the rate of cellular respiration"],
                        "answer": "By resisting temperature changes due to high specific heat"
                    },
                    {
                        "question": "Which property of water allows aquatic life to survive under ice during winter?",
                        "options": ["Water’s high vapor pressure", "Ice being less dense than liquid water", "Water’s ability to dissolve gases", "Water’s low boiling point"],
                        "answer": "Ice being less dense than liquid water"
                    },
                    {
                        "question": "What causes water to have a high boiling point compared to similar-sized molecules?",
                        "options": ["Its low molecular weight", "The presence of ionic bonds", "Strong hydrogen bonding between water molecules", "Its ability to expand when frozen"],
                        "answer": "Strong hydrogen bonding between water molecules"
                    },
                    {
                        "question": "Which of the following best explains water’s ability to act as both an acid and a base?",
                        "options": ["It breaks down into oxygen and hydrogen", "It forms hydroxide and hydronium ions", "It has a pH of exactly 7", "It only dissolves basic substances"],
                        "answer": "It forms hydroxide and hydronium ions"
                    },
                    {
                        "question": "Which biological process relies heavily on the cohesion and adhesion of water?",
                        "options": ["Photosynthesis", "Protein folding", "Transpiration in plants", "Fermentation"],
                        "answer": "Transpiration in plants"
                    },
                    {
                        "question": "Why is water less dense as a solid than as a liquid?",
                        "options": ["The molecules lose mass when frozen", "The hydrogen bonds lock water molecules into a spacious crystalline structure", "The atoms shrink in size", "The covalent bonds weaken during freezing"],
                        "answer": "The hydrogen bonds lock water molecules into a spacious crystalline structure"
                    },
                    {
                        "question": "What would happen if water had a low specific heat?",
                        "options": ["Large bodies of water would resist temperature change", "Water would retain heat for long periods", "Organisms would experience drastic temperature swings", "Ice would be denser than liquid water"],
                        "answer": "Organisms would experience drastic temperature swings"
                    },
                    {
                        "question": "What happens to water molecules when heat is added during boiling?",
                        "options": ["Hydrogen bonds form more tightly", "Molecules move slower and condense", "Hydrogen bonds break, allowing molecules to escape as gas", "Water becomes more dense"],
                        "answer": "Hydrogen bonds break, allowing molecules to escape as gas"
                    },
                    {
                        "question": "What allows water to resist rapid changes in temperature?",
                        "options": ["Its low freezing point", "Its hydrogen bonds which absorb heat", "Its strong ionic bonds", "Its ability to act as a base"],
                        "answer": "Its hydrogen bonds which absorb heat"
                    },
                    {
                        "question": "Which of the following is NOT a property of water?",
                        "options": ["High specific heat", "High surface tension", "High compressibility", "High cohesive strength"],
                        "answer": "High compressibility"
                    },
                    {
                        "question": "How does water's cohesive strength benefit living organisms?",
                        "options": ["It causes water to evaporate faster", "It helps transport water through plant vessels", "It prevents water from mixing with solutes", "It keeps water from freezing"],
                        "answer": "It helps transport water through plant vessels"
                    },
                    {
                        "question": "What is one biological consequence of water's high surface tension?",
                        "options": ["It allows for rapid cooling in organisms", "It enables some insects to walk on water", "It reduces water’s ability to dissolve solutes", "It increases evaporation rate"],
                        "answer": "It enables some insects to walk on water"
                    },
                    {
                        "question": "How does water act as a weak acid?",
                        "options": ["It donates oxygen atoms to other molecules", "It breaks apart covalent bonds in solutes", "It occasionally dissociates into H3O+ and OH− ions", "It forms ionic compounds with nonpolar substances"],
                        "answer": "It occasionally dissociates into H3O+ and OH− ions"
                    },
                    {
                        "question": "What happens to water molecules when heat is added?",
                        "options": ["Hydrogen bonds form more rapidly", "Molecular motion increases and hydrogen bonds break", "Water becomes more dense", "Electrons are transferred between molecules"],
                        "answer": "Molecular motion increases and hydrogen bonds break"
                    },
                    {
                        "question": "Why does water expand as it freezes?",
                        "options": ["Hydrogen bonds force molecules into a lattice with more space", "Ionic repulsion increases at low temperatures", "Covalent bonds loosen at freezing point", "Water becomes nonpolar at low temperatures"],
                        "answer": "Hydrogen bonds force molecules into a lattice with more space"
                    },
                    {
                        "question": "What role do hydrogen bonds play in the high specific heat of water?",
                        "options": ["They prevent molecules from moving", "They store heat energy before breaking", "They cause water to boil at a lower temperature", "They block the absorption of light"],
                        "answer": "They store heat energy before breaking"
                    },
                    {
                        "question": "Which of the following contributes to capillary action in plants?",
                        "options": ["Hydrogen bonding and adhesion to vessel walls", "Low surface tension of water", "Water’s nonpolarity", "High density of frozen water"],
                        "answer": "Hydrogen bonding and adhesion to vessel walls"
                    },
                    {
                        "question": "How does water's polarity affect its ability to dissolve substances?",
                        "options": ["It prevents water from interacting with other molecules", "It causes water molecules to cluster and exclude solutes", "It allows water to surround and interact with polar and ionic substances", "It makes water act more like a gas at room temperature"],
                        "answer": "It allows water to surround and interact with polar and ionic substances"
                    }
                ],
                "blurting": [html.Div([
                                html.P("A water molecule is composed of two hydrogen atoms covalently bonded to an oxygen atom. Oxygen is more electronegative, so a polar covalent bond is formed."),
                                html.P("This causes the oxygen to have a partial negative charge and the hydrogens to have a partial positive charge."), 
                                html.P(["Because of the charge difference between oxygen and hydrogen, ", html.Strong("hydrogen bonds "), "form between water molecules. Hydrogen bons are the basis of nearly all of water's important properties."]),
                                html.P("Let's take a look at each of the properties in more detail."), 
                                html.P(""),
                                html.P([html.Strong("High cohesive strength: Cohesion "), "is the attraction between molecules. Water has high cohesion because each molecule can form up to four hydrogen bonds with neighboring water molecules, creating a very strong, structured network. This network is what makes water so 'sticky' in comparison to other liquids."]),
                                html.P(""), 
                                html.P([html.Strong("High specific heat: Specific heat "), "is the amount of energy required to raise the temperature of 1 gram of a substance by 1 degree Celsius. Water has high speciic heat because it takes a lot of energy to break the hydrogen bonds in the 'water network.'"]),
                                html.P(""),
                                html.P([html.Strong("High surface tension: Surface tension "), "is the force that acts on the surface of a liquid. In water, surface water molecules are attracted more strongly inward (toward the rest of the liquid) because at the surface, there are fewer water molecules nearby to hydrogen bond with. The inward pull creates a very tight and cohesive surface. Fun fact: water has the highest surface tension of any liquid except for mercury!"]),
                                html.P(""),
                                html.P([html.Strong("Universal solvent: "), "Water is considered the universal solvent because it can dissolve more substances than any other liquid, particularly ionic compounds and polar molecules. It is such a good solvent because of its polar nature (remember that the oxygen has a partial negative charge, which attracts positive ions, and the hydrogens have partial positive charges, which attract negative ions). These interactions allow water to surround solute particles, separating them and dissolving them. Fun fact: that process is known as hydration or solvation!"]) 
                            ])],
                "feynman": [html.Div([
                    html.P(["Water molecules stick together because of", html.Strong(" hydrogen bonds, "), "which give water many unique traits."]),
                    html.Ul([
                        html.Li([html.Strong("Cohesion: "), "water molecules stick to each other, making water 'sticky'"]),
                        html.Li([html.Strong("High Specific Heat: "), "it takes a lot of energy to heat water up, so large bodies of water have a relatively stable temperature"]),
                        html.Li([html.Strong("Surface Tension: "), "the surface of water is hard to break because molecules at the top are bonded tightly to molecules below"]),
                        html.Li([html.Strong("Density: "), "ice floats because water is less dense at 0 degrees C than at 4 degrees C, which is a unique property of water"]),
                        html.Li([html.Strong("Universal Solvent: "), "water can dissolve many things and can act as a weak acid"])
                    ])
                ])]
            }, #end of study guide #1, question 3 material
            "q4": {
                "question": html.P("Understand what pH is and why it is important biologically."),
                "overview": html.Div([
                    html.P([html.Strong("pH "), "is a measure of how acidic or basic a solution is based on its H+ (hydrogen ion) concentration where pH = -log[H+]."]), 
                    html.P([html.Strong("Acids "), "donate H+ and ", html.Strong("bases "), "accept H+. Each change in pH unit equals a ten-fold difference in the H+ ion concentration."]),
                    html.P("pH is important biologically because certain molecules only work within a specific pH range.")
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("pH "), "stands for 'Potential of Hydrogen' or 'Power of Hydrogen.' It is a measure of the concentration of hydrogen ions (H+) in a solution and tells you how acidic or how basic that solution is."]),
                    html.P("The pH scale ranges from 0 to 14 where pH 7 is neutral (pure water), pH < 7 means the solution is acidic (more H+ ions), and pH > 7 means the solution is basic (more OH- ions)."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/pH scale.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://blog.jencoi.com/what-is-ph-in-water-testing", target = "_blank")])
                        ]
                    ),
                    html.Br(),
                    html.P("The pH scale is logmarithmic. This means that each unit change in pH is equal to a 10x change in the hydrogen ion (H+) concentration."),
                    html.Div([
                        html.P("For example: a solution with pH 5 has 10x more H+ ions than a solution with pH 6. A solution with pH 4 has 1000x more H+ ions than a solution with pH 6.")
                    ], style = {'border':'1 px solid #ccc',
                                'padding':'15px',
                                'borderRadius':'5px',
                                'backgroundColor':'#ccd5ae',
                                'margin':'10px 0'}),
                    html.P(["The ", html.Strong("biological importance "), "of pH is that certain molecules only work within a specific pH range."]),
                    html.Div([
                        html.P(["For example: normal human blood is pH 7.35 - 7.45. ", html.Strong("Acidosis "), "occurs when the blood is too acidic."]),
                        html.P(["This can occur because of ", html.Strong("respiratory failure "), "where the lungs cannot exhale CO2 from the blood, so carbonic acid builds up, or due to ", html.Strong("untreated diabetes "), "where fat is broken down for energy into acetone and carboxylic acid."]),
                        html.P("A blood pH of 6.8 - 6.9 could be fatal.")
                    ], style = {'border':'1 px solid #ccc',
                                'padding':'15px',
                                'borderRadius':'5px',
                                'backgroundColor':'#ccd5ae',
                                'margin':'10px 0'}),
                    html.Br(), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/acidosis.png", style = {'marginRight':'40px', 'width':'400px'}),
                            html.Div(["Image from ", html.A("here", href = "https://drsushrutfuladi.com/Acid-Base-Disorder.php", target = "_blank")])
                        ]
                    ),
                    html.P("You can think of pH like a scale. Adding more H+ causes the scale to tip acidic. Removing H+ or adding more OH- causes the scale to tip to basic. Buffers are like hands which hold the scale steady when something tries to tip it."),
                    html.Br(), 
                    html.P([html.Strong("Helpful Outside Resources: pH")]),
                    html.Ul([
                        html.Li([html.A("MooMooMath and Science: pH Scale in Simple Terms", href = "https://www.youtube.com/watch?v=KfWvdSyW6Io&pp=ygUCcEg%3D", target = "_blank")]),
                        html.Li([html.A("Crash Course: pH and pOH", href = "https://www.youtube.com/watch?v=LS67vS10O5Y&t=14s&pp=ygUCcEg%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Introduction to pH", href = "https://www.youtube.com/watch?v=oda2K4IFBaE&pp=ygUQa2hhbiBhY2FkZW15IHBIIA%3D%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Definition of pH", href = "https://www.youtube.com/watch?v=J7-GewgqWUQ&pp=ygUQa2hhbiBhY2FkZW15IHBIIA%3D%3D", target = "_blank")])
                    ]),
                    html.P(html.Strong("Helpful Outside Resources: Acidosis and Alkalosis")),
                    html.Ul([
                        html.Li([html.A("Alila Medical Media: Acidosis, Respiratory and Metabolic", href = "https://www.youtube.com/watch?v=C_gpG7HjdDc&t=78s&pp=ygUWYWNpZG9zaXMgYW5kIGFsa2Fsb3Npcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Medicosis Perfectionalis: Acid-Base Disturbances (Acidosis and Alkalosis - Introduction)", href = "https://www.youtube.com/watch?v=VT5Mn9gM7Ww&pp=ygUWYWNpZG9zaXMgYW5kIGFsa2Fsb3Npcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Medicosis Perfectionalis: Respiratory Acidosis & Alkalosis", href = "https://www.youtube.com/watch?v=6XyLSm3vJDQ&pp=ygUWYWNpZG9zaXMgYW5kIGFsa2Fsb3Npcw%3D%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter1/Slide23.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide24.jpg"), 
                    html.Img(src = "/assets/Chapter1/Slide25.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question4.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does pH directly measure?",
                        "options": ["The concentration of oxygen", "The concentration of hydrogen ions", "The number of water molecules", "The amount of carbon dioxide"],
                        "answer": "The concentration of hydrogen ions"
                    },
                    {
                        "question": "Which of the following correctly describes how acids and bases behave?",
                        "options": ["Acids accept H⁺ and bases donate H⁺", "Acids donate H⁺ and bases accept H⁺", "Both acids and bases donate H⁺", "Neither acids nor bases interact with H⁺"],
                        "answer": "Acids donate H⁺ and bases accept H⁺"
                    },
                    {
                        "question": "What happens to H⁺ concentration when pH increases by 1 unit?",
                        "options": ["It increases 10-fold", "It doubles", "It decreases 10-fold", "It remains unchanged"],
                        "answer": "It decreases 10-fold"
                    },
                    {
                        "question": "Why is pH important in biological systems?",
                        "options": ["It controls the shape of DNA", "It prevents oxygen from binding to cells", "It determines whether cells will divide", "Certain molecules function only within a specific pH range"],
                        "answer": "Certain molecules function only within a specific pH range"
                    },
                    {
                        "question": "What is the normal pH range of human blood?",
                        "options": ["6.5 to 6.9", "7.35 to 7.45", "7.9 to 8.4", "8.5 to 9.0"],
                        "answer": "7.35 to 7.45"
                    },
                    {
                        "question": "What condition occurs when blood becomes too acidic?",
                        "options": ["Alkalosis", "Photosynthesis", "Acidosis", "Neutralization"],
                        "answer": "Acidosis"
                    },
                    {
                        "question": "Why can respiratory failure lead to acidosis?",
                        "options": ["It increases water retention", "It causes the kidneys to excrete more acid", "It prevents CO₂ from being exhaled, increasing carbonic acid", "It reduces oxygen delivery to tissues"],
                        "answer": "It prevents CO₂ from being exhaled, increasing carbonic acid"
                    },
                    {
                        "question": "How can untreated diabetes lead to blood acidosis?",
                        "options": ["The body stores excess sugar as acid", "Fat breakdown produces acidic molecules like acetone", "The pancreas secretes too much H⁺", "Insulin lowers blood pH directly"],
                        "answer": "Fat breakdown produces acidic molecules like acetone"
                    },
                    {
                        "question": "What blood pH value may be fatal to humans?",
                        "options": ["7.5", "7.0", "6.8 to 6.9", "None are correct"],
                        "answer": "6.8 to 6.9"
                    },
                    {
                        "question": "What mathematical formula defines pH?",
                        "options": ["pH = H⁺ (x) 10", "pH = log[H⁺]", "pH = -log[H⁺]", "pH = -[H⁺]/10"],
                        "answer": "pH = -log[H⁺]"
                    },
                    {
                        "question": "What effect does a low pH have on hydrogen ion concentration?",
                        "options": ["It indicates fewer hydrogen ions", "It means the solution is neutral", "It indicates more hydrogen ions", "It has no effect on hydrogen ions"],
                        "answer": "It indicates more hydrogen ions"
                    },
                    {
                        "question": "Which of the following pH values represents a basic solution?",
                        "options": ["3.5", "6.0", "7.0", "8.5"],
                        "answer": "8.5"
                    },
                    {
                        "question": "Why is maintaining a stable blood pH critical in humans?",
                        "options": ["To support cellular respiration", "To prevent blood clotting", "To ensure enzymes function properly", "To allow rapid heartbeat"],
                        "answer": "To ensure enzymes function properly"
                    },
                    {
                        "question": "What happens when a person’s blood pH drops below 7.35?",
                        "options": ["They become more basic", "They experience alkalosis", "They are at risk of acidosis", "They lose carbon dioxide rapidly"],
                        "answer": "They are at risk of acidosis"
                    },
                    {
                        "question": "Which of the following is a weak acid produced when CO₂ dissolves in blood?",
                        "options": ["Hydrochloric acid", "Carbonic acid", "Acetic acid", "Sulfuric acid"],
                        "answer": "Carbonic acid"
                    },
                    {
                        "question": "What role do the lungs play in regulating blood pH?",
                        "options": ["They absorb hydrogen ions directly", "They exhale CO₂ to prevent acid buildup", "They release insulin", "They produce ketone bodies"],
                        "answer": "They exhale CO₂ to prevent acid buildup"
                    },
                    {
                        "question": "In untreated diabetes, why are fats used for energy instead of glucose?",
                        "options": ["Glucose levels are too low in the blood", "Insulin allows glucose to leave the cell", "Insulin is lacking, so cells can’t take in glucose", "Glucose is converted into oxygen"],
                        "answer": "Insulin is lacking, so cells can’t take in glucose"
                    },
                    {
                        "question": "What chemical property makes ketones dangerous when they accumulate?",
                        "options": ["They raise blood pressure", "They are highly basic", "They are acidic and lower blood pH", "They increase oxygen flow to tissues"],
                        "answer": "They are acidic and lower blood pH"
                    },
                    {
                        "question": "Which of the following best describes a buffer system?",
                        "options": ["A molecule that only works in acids", "A substance that maintains pH by neutralizing small amounts of acids or bases", "A solution that causes rapid pH changes", "A gas that lowers blood pH"],
                        "answer": "A substance that maintains pH by neutralizing small amounts of acids or bases"
                    },
                    {
                        "question": "What does a pH of 7 indicate?",
                        "options": ["The solution is acidic", "The solution is basic", "The solution is neutral", "The solution contains no H⁺"],
                        "answer": "The solution is neutral"
                    }
                ],
                "blurting": [html.Div([
                                html.P([html.Strong("pH "), "is a measure of how acidic or basic a solution is based on its H+ (hydrogen ion) concentration where pH = -log[H+]."]), 
                                html.P([html.Strong("Acids "), "donate H+ and ", html.Strong("bases "), "accept H+. Each change in pH unit equals a ten-fold difference in the H+ ion concentration."]),
                                html.P("pH is important biologically because certain molecules, such as enzymes, only work within a specific pH range.")
                            ])],
                "feynman": [html.Div([
                    html.P([html.Strong("pH "), "is a way to tell how acidic or basic something is. It is a scale from 0 to 14 where:"]),
                    html.Ul([
                        html.Li("Low numbers = more acidic (lots of H+ ions)"), 
                        html.Li("High numbers = more basic (fewer H+ ions)"),
                        html.Li("7 is neutral (like pure water)")
                    ]),
                    html.P("Every time the pH changes by 1, it means that the H+ ion concentration changes by 10 times."),
                    html.P([html.Strong("Acids "), "are molecules that give away H+ and ", html.Strong("bases "), "are molecules that take them in."]),
                    html.P([html.Strong("So why is this biologically important?")]), 
                    html.P("Our bodies need the pH to stay within a safe range. If the pH of our blood becomes too low or too high, it can be very dangerous or even cause death. Even small pH changes can stop proteins from working or cause damage to cells.")
                ])]
            }, #end of study guide #1, question 4 material
            "q5": {
                "question": html.P("Be familiar with the general molecular structure of amino acids, carbohydrates, and lipids. Know a representative example of a protein, sugar, and fat."),
                "overview": html.Div([
                    html.P(["Biological molecules like ",html.Strong("proteins, carbohydrates, "), "and ", html.Strong("lipids "), "are essential for life."]),
                    html.Ul([
                        html.Li([html.Strong("Proteins "), "are made of amino acids and have diverse roles, such as catalysis (enzymes), structure, and communication."]),
                        html.Li([html.Strong("Carbohydrates "), "like glucose, store energy and provide structural support. Their structure (linear or branched) affects their function."]),
                        html.Li([html.Strong("Lipids "), "like triglycerides, are hydrophobic molecules for energy storage, insulation, and membrane structure. Their function and properties depend on the saturation of fatty acid chains."])
                    ]),
                    html.P(["In this context, ", html.Strong("saturation "), "refers to the presence or absence of double bonds between the carbon atoms in the hydrocarbon chain of a fatty acid."])
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Proteins:")]),
                    html.P("Proteins are polymers made from 20 different amino acids. Each amino acid contains:"), 
                    html.Ul([
                        html.Li("A central (alpha) carbon"),
                        html.Li("An amino group (H3N+)"),
                        html.Li("A carboxyl group (COO-)"),
                        html.Li("A hydrogen atom"), 
                        html.Li("A variable side chain (the R-group)")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/amino acid.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://chemistrytalk.org/amino-acid-chart/", target = "_blank")])
                        ]
                    ),
                    html.P(["These building blocks link via ", html.Strong("peptide bonds "), "and fold into complex 3D shapes that determine their roles and functions, which can include catalysis (enzymes), transport, defense (antibodies), regulation (hormones), structural support, and movement."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/peptide bond.jpg", style = {'marginRight':'40px', 'width':'400px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://mothergoosehealth.storymd.com/journal/wz38qozslm-amino-acids/page/an5dr613qrl6-amino-acids-and-peptide-bonds", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Carbohydrates:")]),
                    html.P("Carbohydrates follow the general formula of (H-C-OH)x and are crucial for: energy storage (glycogen and starch), transport, and structural integrity (cellulose)."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/carbohydrate structure.jpg", style = {'marginRight':'40px', 'width':'800px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.merckmanuals.com/home/multimedia/video/overview-of-carbohydrates-and-sugars", target = "_blank")])
                        ]
                    ),
                    html.P(["A representative example of a carbohydrate would be ", html.Strong("glucose.")]),
                    html.P("Glucose is a 6-carbon sugar and considered to be the most common monosaccharide. It exists in both linear and ring forms, where the ring form is more stable. Glucose can have two orientations:"),
                    html.Ul([
                        html.Li([html.Strong("Alpha-glucose: "), "easier to digest, forms starch and glycogen"]),
                        html.Li([html.Strong("Beta-glucose: "), "forms cellulose, which is more resistant to breakdown due to different bond orientation"])
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/alpha and beta glucose.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://mysciencesquad.weebly.com/ib-hl-23a1--s1-cellulose--starch-v-glycogen.html", target = "_blank")])
                        ]
                    ),
                    html.P("Cellulose is linear and used for structure. Starch is branched and is the primary source of plant energy storage. Glycogen is highly branched and is the primary source of animal energy storage."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/cellulose starch glycogen.png", style = {'marginRight':'40px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://pressbooks.bccampus.ca/humanbiology053/chapter/3-4-carbohydrates/", target = "_blank")])
                        ]
                    ), 
                    html.P([html.Strong("Lipids:")]),
                    html.P("Lipids are hydrophobic (water-fearing, water-insoluble) molecules made mostly of hydrocarbons (meaning they are composed primarily of hydrogens and carbons). They serve multiple roles, such as energy storage, insulation, cell membrane structure, and signaling."),
                    html.P(["A common type of lipid is a ", html.Strong("triglyceride"), " , which is composed of 1 glycerol (a 3-carbon alcohol) and 3 fatty acid chains (hydrocarbon chains with a carboxyl group at the end)"]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/triglyceride.png", style = {'marginRight':'40px', 'width':'500px'}),
                            html.Div(["Image from ", html.A("here", href = "https://en.wikipedia.org/wiki/Triglyceride", target = "_blank")])
                        ]
                    ),
                    html.P(["Fatty acids can be:"]),
                    html.Ul([
                        html.Li([html.Strong("Saturated: "), "no double bonds, solid at room temperature"]),
                        html.Li([html.Strong("Unsaturated: "), "one or more double bonds; liquid at room temperature. Can be ", html.Strong("monounsaturated"), " or ", html.Strong("polyunsaturated"), " which refers to how many double bonds the fatty acid chain contains."])
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/unsaturated versus saturated.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://observatoireprevention.org/en/2020/02/05/choosing-dietary-sources-of-unsaturated-fats-has-many-health-benefits/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources: Proteins")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Protein Structure and Folding", href = "https://www.youtube.com/watch?v=hok2hyED9go&t=25s&pp=ygUIcHJvdGVpbnM%3D", target = "_blank")]),
                        html.Li([html.A("Dirty Medicine: Amino Acids", href = "https://www.youtube.com/watch?v=shM19vvmhWE&pp=ygUIcHJvdGVpbnM%3D", target = "_blank")]),
                        html.Li([html.A("Amoeba Sisters: Biomolecules", href = "https://www.youtube.com/watch?v=1Dx7LDwINLU&pp=ygUVcHJvdGVpbnMgY3Jhc2ggY291cnNl", target = "_blank")]),
                        html.Li([html.A("Osmosis from Elsevier: Proteins", href = "https://www.youtube.com/watch?v=HSCUAjZQhXI&pp=ygUVcHJvdGVpbnMgY3Jhc2ggY291cnNl", target = "_blank")])
                    ]),
                    html.P([html.Strong("Helpful Outside Resources: Carbohydrates")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Biomolecules", href = "https://www.youtube.com/watch?v=1Dx7LDwINLU&pp=ygUVcHJvdGVpbnMgY3Jhc2ggY291cnNl", target = "_blank")]),
                        html.Li([html.A("Nucleus Biology: Carbohydrates", href = "https://www.youtube.com/watch?v=rQyWJIn1HYE&pp=ygUNY2FyYm9oeWRyYXRlcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Osmosis from Elsevier: Carbohydrates & Sugars", href = "https://www.youtube.com/watch?v=jQi84TnstI4&pp=ygUWd2hhdCBhcmUgY2FyYm9oeWRyYXRlcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Cognito: Carbohydrates (Monosaccharides and Disaccharides)", href = "https://www.youtube.com/watch?v=2xDhjHxP688&pp=ygUed2hhdCBhcmUgY2FyYm9oeWRyYXRlcyBiaW9sb2d5", target = "_blank")]),
                        html.Li([html.A("Free Animated Education: What are Carbohydrates? What Are Its Different Types?", href = "https://www.youtube.com/watch?v=IJUwdIups9o&pp=ygUed2hhdCBhcmUgY2FyYm9oeWRyYXRlcyBiaW9sb2d5", target = "_blank")])
                    ]),
                    html.P([html.Strong("Helpful Outside Resources: Lipids")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Biomolecules", href = "https://www.youtube.com/watch?v=1Dx7LDwINLU&pp=ygUVcHJvdGVpbnMgY3Jhc2ggY291cnNl", target = "_blank")]),
                        html.Li([html.A("2 Minute Classroom: Lipids (Fats, Steroids, Phospholipids)", href = "https://www.youtube.com/watch?v=69-eGO7XDfU&t=26s&pp=ygUXd2hhdCBhcmUgbGlwaWRzIGJpb2xvZ3k%3D", target = "_blank")]),
                        html.Li([html.A("Osmosis from Elsevier: Fats", href = "https://www.youtube.com/watch?v=BVxeeiR7JB0&pp=ygUXd2hhdCBhcmUgbGlwaWRzIGJpb2xvZ3k%3D", target = "_blank")]),
                        html.Li([html.A("Nucleus Biology: Lipids", href = "https://www.youtube.com/watch?v=ebScOnAJdu0&pp=ygUXd2hhdCBhcmUgbGlwaWRzIGJpb2xvZ3k%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter3/Slide4.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide6.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide11.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide16.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide19.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide20.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide21.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide22.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide23.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide25.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter3question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the basic structure of an amino acid?",
                        "options": [
                            "A sugar ring, a phosphate group, and a nitrogenous base",
                            "A glycerol and three fatty acids",
                            "An alpha carbon, amino group, carboxyl group, hydrogen, and a side chain",
                            "A glucose molecule and a protein backbone"
                        ],
                        "answer": "An alpha carbon, amino group, carboxyl group, hydrogen, and a side chain"
                    },
                    {
                        "question": "Which of the following best describes a function of proteins?",
                        "options": [
                            "Energy storage only",
                            "Waterproofing surfaces",
                            "Catalyzing chemical reactions",
                            "Insulating the body"
                        ],
                        "answer": "Catalyzing chemical reactions"
                    },
                    {
                        "question": "What molecule do all cells primarily use as an energy source?",
                        "options": [
                            "Triglyceride",
                            "Amino acid",
                            "Glucose",
                            "Cellulose"
                        ],
                        "answer": "Glucose"
                    },
                    {
                        "question": "How do alpha and beta glucose differ structurally?",
                        "options": [
                            "They differ in the length of their carbon chains",
                            "They differ in the orientation of their hydroxyl groups",
                            "One contains nitrogen while the other does not",
                            "Alpha glucose has double bonds while beta does not"
                        ],
                        "answer": "They differ in the orientation of their hydroxyl groups"
                    },
                    {
                        "question": "Which type of carbohydrate is most difficult for humans to digest?",
                        "options": [
                            "Glycogen",
                            "Starch",
                            "Cellulose",
                            "Sucrose"
                        ],
                        "answer": "Cellulose"
                    },
                    {
                        "question": "What is a triglyceride made of?",
                        "options": [
                            "One fatty acid and three glycerols",
                            "One glycerol and three fatty acids",
                            "Three amino acids and one glycerol",
                            "Three glucose molecules"
                        ],
                        "answer": "One glycerol and three fatty acids"
                    },
                    {
                        "question": "What feature makes unsaturated fats different from saturated fats?",
                        "options": [
                            "Unsaturated fats contain nitrogen",
                            "Unsaturated fats have double bonds in the carbon chain",
                            "Unsaturated fats are solid at room temperature",
                            "Unsaturated fats contain amino groups"
                        ],
                        "answer": "Unsaturated fats have double bonds in the carbon chain"
                    },
                    {
                        "question": "Which of the following is a representative example of a protein?",
                        "options": [
                            "Cellulose",
                            "Enzyme",
                            "Glucose",
                            "Triglyceride"
                        ],
                        "answer": "Enzyme"
                    },
                    {
                        "question": "Which level of structure is responsible for a protein's specific function?",
                        "options": [
                            "Simple chain of amino acids",
                            "Random shape",
                            "Its 3D folded structure",
                            "Its glucose content"
                        ],
                        "answer": "Its 3D folded structure"
                    },
                    {
                        "question": "Why are lipids generally insoluble in water?",
                        "options": [
                            "They contain only polar covalent bonds",
                            "They are composed mainly of nonpolar hydrocarbon chains",
                            "They lack any molecular structure",
                            "They have a high pH"
                        ],
                        "answer": "They are composed mainly of nonpolar hydrocarbon chains"
                    },
                    {
                        "question": "Which part of the amino acid determines its unique properties?",
                        "options": [
                            "The alpha carbon",
                            "The carboxyl group",
                            "The side chain (R group)",
                            "The hydrogen atom"
                        ],
                        "answer": "The side chain (R group)"
                    },
                    {
                        "question": "What type of bond links amino acids together to form proteins?",
                        "options": [
                            "Ionic bond",
                            "Hydrogen bond",
                            "Peptide bond",
                            "Glycosidic bond"
                        ],
                        "answer": "Peptide bond"
                    },
                    {
                        "question": "Which of the following is NOT a function of proteins?",
                        "options": [
                            "Catalyzing chemical reactions",
                            "Storing genetic information",
                            "Providing structural support",
                            "Transporting molecules"
                        ],
                        "answer": "Storing genetic information"
                    },
                    {
                        "question": "What type of carbohydrate linkage is found in cellulose?",
                        "options": [
                            "Alpha linkage",
                            "Beta linkage",
                            "Gamma linkage",
                            "Delta linkage"
                        ],
                        "answer": "Beta linkage"
                    },
                    {
                        "question": "Which carbohydrate is highly branched and found in animals?",
                        "options": [
                            "Cellulose",
                            "Starch",
                            "Glycogen",
                            "Fructose"
                        ],
                        "answer": "Glycogen"
                    },
                    {
                        "question": "What makes cellulose difficult for humans to digest?",
                        "options": [
                            "It contains no glucose",
                            "It has beta linkages",
                            "It is highly branched",
                            "It contains nitrogen"
                        ],
                        "answer": "It has beta linkages"
                    },
                    {
                        "question": "Which part of a fatty acid is polar?",
                        "options": [
                            "The hydrocarbon chain",
                            "The carboxyl group",
                            "The double bond",
                            "The entire molecule is nonpolar"
                        ],
                        "answer": "The carboxyl group"
                    },
                    {
                        "question": "What is a common feature of all lipids?",
                        "options": [
                            "They contain amino acids",
                            "They are made of sugars",
                            "They are insoluble in water",
                            "They form peptide bonds"
                        ],
                        "answer": "They are insoluble in water"
                    },
                    {
                        "question": "Which of the following correctly pairs a macromolecule with a representative example?",
                        "options": [
                            "Protein – Glucose",
                            "Lipid – Glycogen",
                            "Carbohydrate – Starch",
                            "Carbohydrate – Enzyme"
                        ],
                        "answer": "Carbohydrate – Starch"
                    },
                    {
                        "question": "What does the presence of double bonds in fatty acid chains cause?",
                        "options": [
                            "The chain to remain straight and rigid",
                            "The chain to become longer",
                            "A bend or kink in the chain",
                            "The loss of all hydrogen atoms"
                        ],
                        "answer": "A bend or kink in the chain"
                    }
                ],
                "blurting": [html.Div([
                                html.P(["Biological molecules like ",html.Strong("proteins, carbohydrates, "), "and ", html.Strong("lipids "), "are essential for life."]),
                                html.Ul([
                                    html.Li([html.Strong("Proteins "), "are made of amino acids and have diverse roles, such as catalysis (enzymes), structure, and communication."]),
                                    html.Li([html.Strong("Carbohydrates "), "like glucose, store energy and provide structural support. Their structure (linear or branched) affects their function."]),
                                    html.Li([html.Strong("Lipids "), "like triglycerides, are hydrophobic molecules for energy storage, insulation, and membrane structure. Their function and properties depend on the saturation of fatty acid chains."])
                                ]),
                                html.P(["In this context, ", html.Strong("saturation "), "refers to the presence or absence of double bonds between the carbon atoms in the hydrocarbon chain of a fatty acid."])
                            ]),],
                "feynman": [html.Div([
                    html.P("Your body runs on three major types of big molecules: proteins, carbohydrates, and lipids."),
                    html.P([html.Strong("Proteins "), "are the doers. They do most of the work, helping with structure, movement, defense, and speeding up chemical reactions. They are made of amino acids."]),
                    html.P(""),
                    html.P([html.Strong("Carbohydrates "), "are the fuel. They give quick energy and help to build structures. The main building block of carbohydrates is glucose, a sugar that can form straight chains or rings."]),
                    html.P(""), 
                    html.P([html.Strong("Lipids "), "are the storage. They store energy and make up cell membranes. Remember that saturated fats have no double bonds and are solid at room temperature, whereas unsaturated fats have double bonds and are liquid at room temperature."])
                ])]
            },
            "q6": {
                "question": html.P("Be able to name the types of chemical bonds responsible for constructing each macromolecule from its monomers (peptide, phosphodiester, glycosidic)."),
                "overview": html.Div([
                    html.P(["Different ", html.Strong("macromolecules "), "are made by linking ", html.Strong("monomers "), "together using specific types of chemical bonds."]),
                    html.Ul([
                        html.Li(["Proteins: amino acids join via ", html.Strong("peptide bonds")]),
                        html.Li(["Carbohydrates: sugars join via ", html.Strong("glycosidic linkages")]),
                        html.Li(["Lipids: fatty acids and glycerol form ", html.Strong("ester linkages "), "in triglycerides. ", html.Strong("van der Waals forces "), "also help to hold lipids together"]),
                        html.Li(["Nucleic acids: nucleotides link via ", html.Strong("phosphodiester bonds")])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.P("Macromolecules are large biological molecules which are formed by joining together smaller units called monomers. The way that these monomers are linked defines both the structure and the function of the resulting polymer. Here is how different macromolecules are built:"),
                    html.P([html.Strong("Proteins:")]),
                    html.Ul([
                        html.Li("Monomers: amino acids"),
                        html.Li("Bond: peptide bond (a type of covalent bond)"),
                        html.Li("How it forms: the carboxyl group (-COO-) of one amino acid reacts with the amino group (-NH3+) of another, releasing water in a dehydration reaction"),
                        html.Li("This linkage forms a polypeptide, which will then fold into a functional protein")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/peptide bond formation.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.mun.ca/biology/scarr/iGen3_06-03.html", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Carbohydrates:")]),
                    html.Ul([
                        html.Li("Monomer: simple sugars (monosaccharides, like glucose)"),
                        html.Li("Bond: glycosidic linkage"),
                        html.Li("How it forms: two hydroxyl groups (-OH) from different sugars bond together through a dehydration reaction"),
                        html.Li("The position and orientation of the bond (alpha or beta) determins the properties of the carbohydrate, such as how easy it is to digest")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/glycosidic bond formation.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://theory.labster.com/glycosidic-bonds/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Lipids:")]),
                    html.Ul([
                        html.Li("Monomer: has monomer-like units of gkycerol and fatty acid"),
                        html.Li("Bond: ester linkage"), 
                        html.Li("How it forms: the carboxyl group of a fatty acid reacts with the hydroxyl group of a glycerol"),
                        html.Li("Lipids also join together through van der Waals forces. These forces are weak individually, but collectively help to hold chains of fatty acids close together in membranes and stores of fat.")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/lipid bond formation.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://alevelbiology.co.uk/notes/lipid-structures-and-functions/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Nucleic acids:")]),
                    html.Ul([
                        html.Li("Monomer: nucleotides (sugar + phosphate + nitrogenous base)"),
                        html.Li("Bond: phosphodiester linkage"),
                        html.Li("How it forms: the phosphate group of one nucleotide bonds with the 3' hydroxyl group of another nucleotide's sugar"),
                        html.Li("This forms the sugar-phosphate backbone of DNA or RNA, which provides stability and directionality")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/phosphodiester bond formation.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.researchgate.net/figure/Formation-of-the-phosphodiester-bond-through-the-condensation-reaction_fig2_317401681", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources: Proteins")]),
                    html.Ul([
                        html.Li([html.A("Medicosis Perfectionalis: Peptides and Peptide Bonds", href = "https://www.youtube.com/watch?v=dltRr8w8oCo&pp=ygUNcGVwdGlkZSBib25kcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy Medicine: Peptide Bonds (Formation and Cleavage)", href = "https://www.youtube.com/watch?v=pmQuNRHJMw4&pp=ygUNcGVwdGlkZSBib25kcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Study Force: Peptide Bond Formation Animation", href = "https://www.youtube.com/watch?v=S6aIS2aoy9Q&pp=ygUNcGVwdGlkZSBib25kcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Peptide Bond Formation", href = "https://www.youtube.com/watch?v=nv2kfBFkv4s&pp=ygUNcGVwdGlkZSBib25kcw%3D%3D", target = "_blank")])
                    ]),
                    html.P([html.Strong("Helpful Outside Resources: Carbohydrates")]),
                    html.Ul([
                        html.Li([html.A("biologyexams4u: What is a Glycosidic Bond?", href = "https://www.youtube.com/watch?v=XwBE47fwPoM&pp=ygUQZ2x5Y29zaWRpYyBib25kcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Study Force: Glycosidic Bonds in Disaccharides Explained", href = "https://www.youtube.com/watch?v=Ddjvp8wUTC8&pp=ygUQZ2x5Y29zaWRpYyBib25kcw%3D%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy Medicine: Glycosidic Formation Hydrolysis", href = "https://www.youtube.com/watch?v=g9qJ19vmGQA&pp=ygUQZ2x5Y29zaWRpYyBib25kcw%3D%3D", target = "_blank")])
                    ]),
                    html.P([html.Strong("Helpful Outside Resources: Lipids")]),
                    html.Ul([
                        html.Li([html.A("biologyexams4u: What are Fats? How Are Ester Bonds Formed in Fats?", href = "https://www.youtube.com/watch?v=4JZOtWM20dI&pp=ygULZXN0ZXIgYm9uZHM%3D", target = "_blank")]),
                        html.Li([html.A("ChemProfJH: Hydrolysis Reactions for Esters, Amides, and Glycosidic Bonds", href = "https://www.youtube.com/watch?v=Jh7x7uaGHGw&pp=ygULZXN0ZXIgYm9uZHPSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Lipid Overview", href = "https://www.youtube.com/watch?v=Ezp8F7XJHWE&pp=ygULbGlwaWQgYm9uZCA%3D", target = "_blank")])
                    ]),
                    html.P([html.Strong("Helpful Outside Resources: Nucleotides")]),
                    html.Ul([
                        html.Li([html.A("Learnbiologynet: How Do Nucleotides Join Together?", href = "https://www.youtube.com/watch?v=lAUlH3rX80U&pp=ygUUcGhvc3Bob2RpZXN0ZXIgYm9uZHM%3D", target = "_blank")]),
                        html.Li([html.A("biologyexams4u: How is Phosphodiester Bond Formed in DNA?", href = "https://www.youtube.com/watch?v=HSTIVBFewkI&pp=ygUUcGhvc3Bob2RpZXN0ZXIgYm9uZHPSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("JoVE for Middle and High Schools: Phosphodiester Linkages", href = "https://www.youtube.com/watch?v=s2e12CQrhXc&pp=ygUPbnVjbGVvdGlkZSBib25k", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter3/Slide6.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide12.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide14.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide20.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter3question6.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of bond links amino acids together in a protein?",
                        "options": [
                            "Glycosidic bond",
                            "Phosphodiester bond",
                            "Peptide bond",
                            "Ester bond"
                        ],
                        "answer": "Peptide bond"
                    },
                    {
                        "question": "Which monomers are joined by glycosidic linkages?",
                        "options": [
                            "Amino acids",
                            "Fatty acids",
                            "Monosaccharides (sugars)",
                            "Nucleotides"
                        ],
                        "answer": "Monosaccharides (sugars)"
                    },
                    {
                        "question": "What type of bond forms between glycerol and fatty acids in triglycerides?",
                        "options": [
                            "Peptide bond",
                            "Ester linkage",
                            "Glycosidic linkage",
                            "Phosphodiester bond"
                        ],
                        "answer": "Ester linkage"
                    },
                    {
                        "question": "What kind of interaction helps hold lipid molecules together in membranes?",
                        "options": [
                            "Peptide bonds",
                            "Glycosidic linkages",
                            "Van der Waals forces",
                            "Hydrogen bonds"
                        ],
                        "answer": "Van der Waals forces"
                    },
                    {
                        "question": "Which type of bond forms the backbone of DNA and RNA?",
                        "options": [
                            "Ester bond",
                            "Peptide bond",
                            "Glycosidic bond",
                            "Phosphodiester bond"
                        ],
                        "answer": "Phosphodiester bond"
                    },
                    {
                        "question": "Which groups of a nucleotide are involved in forming a phosphodiester bond?",
                        "options": [
                            "Amino and carboxyl",
                            "Hydroxyl and carboxyl",
                            "Phosphate and sugar",
                            "Sugar and base"
                        ],
                        "answer": "Phosphate and sugar"
                    },
                    {
                        "question": "How do peptide bonds form between amino acids?",
                        "options": [
                            "By linking two hydroxyl groups",
                            "By removing water between an amino and carboxyl group",
                            "By connecting two phosphate groups",
                            "By joining two fatty acids"
                        ],
                        "answer": "By removing water between an amino and carboxyl group"
                    },
                    {
                        "question": "What must be removed for glycosidic bonds to form between sugars?",
                        "options": [
                            "Carbon dioxide",
                            "Oxygen",
                            "Water",
                            "Nitrogen"
                        ],
                        "answer": "Water"
                    },
                    {
                        "question": "Which type of bond is specific to carbohydrate polymers like starch and cellulose?",
                        "options": [
                            "Glycosidic linkage",
                            "Peptide bond",
                            "Phosphodiester bond",
                            "Hydrogen bond"
                        ],
                        "answer": "Glycosidic linkage"
                    },
                    {
                        "question": "What property makes van der Waals forces important in lipid structure?",
                        "options": [
                            "They are covalent and permanent",
                            "They are strong enough to form solid fat crystals",
                            "They are weak but add up when molecules are close",
                            "They form between sugar and phosphate groups"
                        ],
                        "answer": "They are weak but add up when molecules are close"
                    },
                    {
                        "question": "Which bond type is formed during protein synthesis?",
                        "options": [
                            "Glycosidic linkage",
                            "Ester linkage",
                            "Phosphodiester bond",
                            "Peptide bond"
                        ],
                        "answer": "Peptide bond"
                    },
                    {
                        "question": "Which macromolecule is assembled using phosphodiester bonds?",
                        "options": [
                            "Proteins",
                            "Lipids",
                            "Carbohydrates",
                            "Nucleic acids"
                        ],
                        "answer": "Nucleic acids"
                    },
                    {
                        "question": "What two functional groups form a peptide bond?",
                        "options": [
                            "Hydroxyl and phosphate",
                            "Carboxyl and amino",
                            "Carbonyl and methyl",
                            "Hydroxyl and carbonyl"
                        ],
                        "answer": "Carboxyl and amino"
                    },
                    {
                        "question": "What type of bond connects monosaccharides in disaccharides and polysaccharides?",
                        "options": [
                            "Ester bond",
                            "Peptide bond",
                            "Glycosidic linkage",
                            "Hydrogen bond"
                        ],
                        "answer": "Glycosidic linkage"
                    },
                    {
                        "question": "Which bond is found specifically in triglycerides?",
                        "options": [
                            "Phosphodiester bond",
                            "Glycosidic bond",
                            "Ester linkage",
                            "Peptide bond"
                        ],
                        "answer": "Ester linkage"
                    },
                    {
                        "question": "Which of the following correctly matches the bond with its macromolecule?",
                        "options": [
                            "Peptide bond – DNA",
                            "Glycosidic linkage – protein",
                            "Phosphodiester bond – nucleic acid",
                            "Ester linkage – carbohydrate"
                        ],
                        "answer": "Phosphodiester bond – nucleic acid"
                    },
                    {
                        "question": "Which type of bond results from a dehydration reaction between hydroxyl groups in sugars?",
                        "options": [
                            "Peptide bond",
                            "Hydrogen bond",
                            "Ester linkage",
                            "Glycosidic linkage"
                        ],
                        "answer": "Glycosidic linkage"
                    },
                    {
                        "question": "What is the function of van der Waals forces in lipid structure?",
                        "options": [
                            "To create covalent bonds between monomers",
                            "To help fatty acid chains stick together",
                            "To bind phosphate to sugar",
                            "To form glycosidic linkages"
                        ],
                        "answer": "To help fatty acid chains stick together"
                    },
                    {
                        "question": "In nucleic acids, which part of one nucleotide bonds to the sugar of the next?",
                        "options": [
                            "Its amino group",
                            "Its nitrogenous base",
                            "Its phosphate group",
                            "Its hydroxyl group"
                        ],
                        "answer": "Its phosphate group"
                    },
                    {
                        "question": "Which macromolecule does NOT use covalent bonds to link identical repeating monomers?",
                        "options": [
                            "Proteins",
                            "Carbohydrates",
                            "Lipids",
                            "Nucleic acids"
                        ],
                        "answer": "Lipids"
                    }
                ],
                "blurting": [html.Div([
                                html.P(["Different ", html.Strong("macromolecules "), "are made by linking ", html.Strong("monomers "), "together using specific types of chemical bonds."]),
                                html.Ul([
                                    html.Li(["Proteins: amino acids join via ", html.Strong("peptide bonds")]),
                                    html.Li(["Carbohydrates: sugars join via ", html.Strong("glycosidic linkages")]),
                                    html.Li(["Lipids: fatty acids and glycerol form ", html.Strong("ester linkages "), "in triglycerides. ", html.Strong("van der Waals forces "), "also help to hold lipids together"]),
                                    html.Li(["Nucleic acids: nucleotides link via ", html.Strong("phosphodiester bonds")])
                                ])
                            ]),],
                "feynman": [html.Div([
                    html.P("To build big molecules in the body, we stick together smaller pieces (monomers) using specific types of bonds, which are like glue for monomers."), 
                    html.P([html.Strong("Proteins "), "are made of amino acids. Amino acids link when one gives up an -OH and one gives up an H, so they form a peptide bond and stick together."]),
                    html.P([html.Strong("Carbohydrates "), "are made of sugars, which link by removing water and forming a glycosidic bond between their -OH groups. The angle of the bond (alpha or beta) changes how easy it is for the body to break them down."]),
                    html.P([html.Strong("Lipids "), "are made of glycerol and fatty acids. They form ester bonds when fatty acid carboxyl groups attach to glycerol hydroxyl groups. Fatty tails stick together by van der Waals forces, like clingy plastic wrap."]),
                    html.P([html.Strong("Nucleic acids "), "are made of nucleotides. One nucleotide's phosphate bonds to the next nucleotide's sugar, forming a phosphodiester bond that holds the chain together. This is the 'backbone' of DNA and RNA."])
                ])]
            },
            "q7": {
                "question": html.P("Be able to define the 4 different levels of protein structure. Understand how different types of bonds can contribute to different levels of protein structure."),
                "overview": html.Div([
                    html.P("Proteins have four levels of structure, which are formed sequentially."),
                    html.Ul([
                        html.Li([html.Strong("Primary structure: "), "the sequence of amino acids"]),
                        html.Li([html.Strong("Secondary structure: "), "the folding of alpha-helices and beta-sheets, which are held together by hydrogen bonds between parts of the backbone"]),
                        html.Li([html.Strong("Tertiary structure: "), "the three-dimensional (3D) shape of a single peptide, which is stabilized by side-chain interactions (such as hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions). Another way to think about it is the different folded alpha-helices and beta-sheets interacting with each other."]),
                        html.Li([html.Strong("Quaternary structure: "), "how multiple peptide chains fit together to form one functional protein. Not every protein will have a quaternary structure. Another way to think about it is multiple units in the tertiary structure interacting with each other to form one unit."])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.P("Proteins are complex molecules whose function depends entirely on how they are folded and organized. This protein folding is organized into four levels:"), 
                    html.P([html.Strong("Primary structure")]),
                    html.Ul([
                        html.Li("The order of amino acids in a linear chain (like beads on a string)"), 
                        html.Li("Determined by DNA and built during translation"), 
                        html.Li("Peptide bonds link each amino acid to the next"), 
                        html.Li("The sequence will ultimately determine how the protein will fold and function")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/primary structure.png", style = {'marginRight':'40px'})
                        ]
                    ),
                    html.P([html.Strong("Secondary structure")]),
                    html.Ul([
                        html.Li("Local, repeating shapes formed by the backbone of the chain (NOT the side chains)"), 
                        html.Li("Two main types: alpha-helix (spiral shape, like a spring), and beta-sheet (flat, sheet-like structure from parallel strands)"),
                        html.Li("Stabilized by hydrogen bonds between parts of the backbone"),
                        html.Li("Can form motifs, which are recurring structural patterns within proteins")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/secondary structure.png", style = {'marginRight':'40px'}),
                            html.Img(src = "/assets/alpha helices and beta sheets.jpeg", style = {'marginRight':'40px', 'width':'400px'}),
                            html.Div(["Image from ", html.A("here", href = "https://mysciencesquad.weebly.com/ib-hl-24u6.html", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Tertiary structure")]),
                    html.Ul([
                        html.Li("The overall 3D shape of a single polypeptide"),
                        html.Li("Formed by folding the secondary structures into a functional shape"),
                        html.Li("Stabilized by interactions between the R-groups (side-chains) such as hydrogen bonds, ionic bonds, disulfide bridges (strong covalent bonds between cysteines), and hydrophobic interactions (where nonpolar side chains are tucked inside of the structure)")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/tertiary structure.jpeg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://old-ib.bioninja.com.au/higher-level/topic-7-nucleic-acids/73-translation/protein-structure.html", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Quaternary structure")]),
                    html.Ul([
                        html.Li("Only found in proteins that are made up of more than 1 polypeptide chain"),
                        html.Li("Refers to how different subunits (peptides) fit and work together"),
                        html.Li("Stabilized by the same forces as the tertiary structure (hydrogen bonds, ionic bonds, hydrophobic interactions, etc.)"),
                        html.Li(["A primary example would be ", html.Strong("hemoglobin, "), "which has 4 subunits working as 1 protein"])
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/hemoglobin.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://chemistrytalk.org/hemoglobin-in-biochemistry/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Protein Folding", href = "https://www.youtube.com/watch?v=hok2hyED9go&t=25s&pp=ygUPcHJvdGVpbiBmb2xkaW5n", target = "_blank")]),
                        html.Li([html.A("The Organic Chemistry Tutor: Protein Structure (Primary, Secondary, Tertiary, & Quarternary)", href = "https://www.youtube.com/watch?v=Bsk9hvXDJp8&t=18s&pp=ygUccHJvdGVpbiBmb2xkaW5nIGNyYXNoIGNvdXJzZQ%3D%3D", target = "_blank")]),
                        html.Li([html.A("Neural Academy: Protein Folding", href = "https://www.youtube.com/watch?v=1peFJ_-N7V8&pp=ygUccHJvdGVpbiBmb2xkaW5nIGNyYXNoIGNvdXJzZQ%3D%3D", target = "_blank")]),
                        html.Li([html.A("Osmosis from Elsevier: Amino Acids and Protein Folding", href = "https://www.youtube.com/watch?v=KnMj64z6B3s&t=1s&pp=ygUccHJvdGVpbiBmb2xkaW5nIGNyYXNoIGNvdXJzZdIHCQnBCQGHKiGM7w%3D%3D", target = "_blank")]),
                        html.Li([html.A("Hussain Biology: Protein Folding Mechanism", href = "https://www.youtube.com/watch?v=z6OTR0oX3_E&t=31s&pp=ygUccHJvdGVpbiBmb2xkaW5nIGNyYXNoIGNvdXJzZQ%3D%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter3/Slide7.jpg"), 
                    html.Img(src = "/assets/Chapter3/Slide8.jpg"), 
                    html.Img(src = "/assets/Chapter3/Slide9.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide10.jpg") 
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter3question7.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What defines the primary structure of a protein?",
                        "options": [
                            "The 3D shape of the folded protein",
                            "The sequence of amino acids",
                            "The arrangement of multiple peptide chains",
                            "The folding into alpha-helices and beta-sheets"
                        ],
                        "answer": "The sequence of amino acids"
                    },
                    {
                        "question": "Which bond holds amino acids together in the primary structure?",
                        "options": [
                            "Peptide bond",
                            "Hydrogen bond",
                            "Ionic bond",
                            "Disulfide bridge"
                        ],
                        "answer": "Peptide bond"
                    },
                    {
                        "question": "What type of structure involves alpha-helices and beta-sheets?",
                        "options": [
                            "Primary structure",
                            "Secondary structure",
                            "Tertiary structure",
                            "Quaternary structure"
                        ],
                        "answer": "Secondary structure"
                    },
                    {
                        "question": "Which of the following stabilizes secondary structures?",
                        "options": [
                            "Peptide bonds",
                            "Hydrogen bonds between backbone atoms",
                            "Disulfide bridges",
                            "Hydrophobic interactions"
                        ],
                        "answer": "Hydrogen bonds between backbone atoms"
                    },
                    {
                        "question": "What shape is an alpha-helix?",
                        "options": [
                            "Flat sheet",
                            "Coiled spiral",
                            "Random loop",
                            "Multiple chains bonded together"
                        ],
                        "answer": "Coiled spiral"
                    },
                    {
                        "question": "Beta-sheets are formed by:",
                        "options": [
                            "Parallel arrays of the peptide backbone",
                            "Side-chain interactions",
                            "Covalent disulfide bonds",
                            "Ionic bonds between peptides"
                        ],
                        "answer": "Parallel arrays of the peptide backbone"
                    },
                    {
                        "question": "What defines the tertiary structure of a protein?",
                        "options": [
                            "The amino acid sequence",
                            "The 3D shape of a single peptide",
                            "The arrangement of multiple peptides",
                            "The hydrogen bonding of the backbone"
                        ],
                        "answer": "The 3D shape of a single peptide"
                    },
                    {
                        "question": "Which of these bonds can stabilize tertiary structure?",
                        "options": [
                            "Peptide bonds only",
                            "Hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions",
                            "Only ionic bonds",
                            "Only van der Waals forces"
                        ],
                        "answer": "Hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions"
                    },
                    {
                        "question": "Disulfide bridges form between which amino acid side chains?",
                        "options": [
                            "Lysine",
                            "Cysteine",
                            "Serine",
                            "Glycine"
                        ],
                        "answer": "Cysteine"
                    },
                    {
                        "question": "What is the quaternary structure of a protein?",
                        "options": [
                            "Sequence of amino acids",
                            "Folding of a single peptide",
                            "Arrangement of multiple peptides in space",
                            "Hydrogen bonding in beta-sheets"
                        ],
                        "answer": "Arrangement of multiple peptides in space"
                    },
                    {
                        "question": "Hemoglobin is an example of a protein with which level of structure?",
                        "options": [
                            "Primary only",
                            "Secondary only",
                            "Tertiary only",
                            "Quaternary"
                        ],
                        "answer": "Quaternary"
                    },
                    {
                        "question": "Which bonds contribute to quaternary structure?",
                        "options": [
                            "Only peptide bonds",
                            "Hydrogen bonds, ionic bonds, hydrophobic interactions, and disulfide bridges",
                            "Only glycosidic bonds",
                            "Only phosphodiester bonds"
                        ],
                        "answer": "Hydrogen bonds, ionic bonds, hydrophobic interactions, and disulfide bridges"
                    },
                    {
                        "question": "Which part of the amino acid is involved in peptide bond formation?",
                        "options": [
                            "Side chain (R group)",
                            "Carboxyl and amino groups",
                            "Hydrogen atom only",
                            "Phosphate group"
                        ],
                        "answer": "Carboxyl and amino groups"
                    },
                    {
                        "question": "Hydrogen bonds in secondary structures occur between which atoms?",
                        "options": [
                            "Side chains only",
                            "Backbone carbonyl oxygen and amide hydrogen",
                            "Phosphate and sugar",
                            "Carboxyl groups of side chains"
                        ],
                        "answer": "Backbone carbonyl oxygen and amide hydrogen"
                    },
                    {
                        "question": "Hydrophobic interactions in tertiary structure occur because:",
                        "options": [
                            "Nonpolar side chains avoid water and cluster together inside the protein",
                            "Water molecules bind tightly to side chains",
                            "Ionic side chains attract each other",
                            "Disulfide bonds form"
                        ],
                        "answer": "Nonpolar side chains avoid water and cluster together inside the protein"
                    },
                    {
                        "question": "Which of these is NOT a level of protein structure?",
                        "options": [
                            "Primary",
                            "Secondary",
                            "Tertiary",
                            "Quintary"
                        ],
                        "answer": "Quintary"
                    },
                    {
                        "question": "Motifs in proteins are:",
                        "options": [
                            "Specific sequences of amino acids",
                            "Repeated secondary structural elements",
                            "Types of disulfide bridges",
                            "Types of peptide bonds"
                        ],
                        "answer": "Repeated secondary structural elements"
                    },
                    {
                        "question": "The folding of alpha-helices and beta-sheets arises from interactions involving:",
                        "options": [
                            "Side chains only",
                            "The peptide backbone",
                            "Phosphodiester bonds",
                            "Lipid bilayers"
                        ],
                        "answer": "The peptide backbone"
                    },
                    {
                        "question": "Which type of bond is strongest in stabilizing protein tertiary structure?",
                        "options": [
                            "Hydrogen bond",
                            "Ionic bond",
                            "Van der Waals forces",
                            "Disulfide bridge"
                        ],
                        "answer": "Disulfide bridge"
                    },
                    {
                        "question": "Protein function depends mainly on its:",
                        "options": [
                            "Primary sequence only",
                            "Secondary structure only",
                            "Overall 3D shape",
                            "Number of amino acids"
                        ],
                        "answer": "Overall 3D shape"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Proteins have four levels of structure, which are formed sequentially."),
                                html.Ul([
                                    html.Li([html.Strong("Primary structure: "), "the sequence of amino acids"]),
                                    html.Li([html.Strong("Secondary structure: "), "the folding of alpha-helices and beta-sheets, which are held together by hydrogen bonds between parts of the backbone"]),
                                    html.Li([html.Strong("Tertiary structure: "), "the three-dimensional (3D) shape of a single peptide, which is stabilized by side-chain interactions (such as hydrogen bonds, ionic bonds, disulfide bridges, and hydrophobic interactions). Another way to think about it is the different folded alpha-helices and beta-sheets interacting with each other."]),
                                    html.Li([html.Strong("Quaternary structure: "), "how multiple peptide chains fit together to form one functional protein. Not every protein will have a quaternary structure. Another way to think about it is multiple units in the tertiary structure interacting with each other to form one unit."])
                                ])
                            ])],
                "feynman": [html.Div([
                    html.P("Imagine building a house step-by-step. This is similar to how proteins fold and organize themselves."), 
                    html.P(["The ", html.Strong("primary structure "), "is like the blueprint. It is the exact order of building blocks (amino acids) that tells you how to build the house."]),
                    html.P(["The ", html.Strong ("secondary structure "), "is like the walls and roof frames. Walls and the roof frames go up in simple shapes: an alpha-helix (like a spiral staircase or a curved wall) and beta-sheets (like flat walls or floors made from panels). These parts hold together because the beams (the backbone) connect firmly with strong nails (hydrogen bonds)."]),
                    html.P(["The ", html.Strong("tertiary structure "), "is like the complete house. The shape depends on how the materials (side chains) interact. Some pieces stick together, some repel, and some form strong connections"]),
                    html.P(["The ", html.Strong("quaternary structure "), "is like a neighborhood. It is a series of complete houses joining together to form a community."]),
                    html.P("So just like building a house, proteins start with a plan and gradually form and connect to make a functional structure. If the plan or the construction is off, the house will fall down, just like how a protein will not work if it is not folded correctly.")
                ])]
            },
            "q8": {
                "question": html.P("Be familiar with the major classifications of amino acids."),
                "overview": html.Div([
                    html.P("Amino acids are classified based on the chemical nature of their side chains (R-groups), which affects how they interact in proteins."), 
                    html.Ul([
                        html.Li([html.Strong("Electrically charged, hydrophilic side chains: "), "these can be positive or negative and often interact with water and other charged molecules"]),
                        html.Li([html.Strong("Polar, uncharged, hydrophilic side chains: "), "these attract water, but do not carry a charge"]),
                        html.Li([html.Strong("Special case amino acids: "), "these are unique amino acids with distinct roles, such as cysteine (can form disulfide bonds) or glycine (very small and flexible)"]),
                        html.Li([html.Strong("Nonpolar, hydrophobic side chains: "), "these avoid water and tend to cluster inside of proteins to stabilize the structure"])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.P("The properties of amino acids determine how proteins will fold, interact, and function. There are four main groups."),
                    html.P(html.Strong("Amino acids with electrically charged, hydrophobic side chains")),
                    html.Ul([
                        html.Li("Side chains carry a full positive or negative charge at physiological (natural) pH"),
                        html.Li("Examples of positively charged (basic): lysine, arginine, histidine"),
                        html.Li("Examples of negatively charged (acidic): aspartate, glutamate"), 
                        html.Li("These amino acids are water loving (hydrophilic) and are often found on the protein surface or active site, where they interact with other charged molecules or ions")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/electrically charged sidechain.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://www.technologynetworks.com/applied-sciences/articles/essential-amino-acids-chart-abbreviations-and-structure-324357", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Amino aicds with polar but uncharged, hydrophilic side chains")]),
                    html.Ul([
                        html.Li("Side chains have polar groups that can form hydrogen bonds, but do not carry a full charge"), 
                        html.Li("Examples include: serine, threonine, asparagine, glutamine, tyrosine"),
                        html.Li("These help proteins interact with water and other polar molecules"),
                        html.Li("Can be involved in catalysis or binding")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/polar uncharged sidechain.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://www.technologynetworks.com/applied-sciences/articles/essential-amino-acids-chart-abbreviations-and-structure-324357", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Special case amino acids")]),
                    html.Ul([
                        html.Li("These are amino acids that do not fit well into other categories because of unique properties"),
                        html.Li([html.Strong("Cysteine "), "contains a thiol (-SH) group that can form disulfide bonds, which are important for stabilizing tertiary and quaternary structures of proteins"]),
                        html.Li([html.Strong("Glycine "), "is the smallest amino acid. It is very flexible and can often be found in tight turns within the protein or in flexible regions"]),
                        html.Li([html.Strong("Proline "), "has a cyclic (circle) structure that introduces kinks in the polypeptide chain, which affects folding"])
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/special case.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://www.technologynetworks.com/applied-sciences/articles/essential-amino-acids-chart-abbreviations-and-structure-324357", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Amino acids with nonpolar, hydrophobic side chains")]),
                    html.Ul([
                        html.Li("Side chains are mostly hydrocarbons"),
                        html.Li("Do not interact well with water"),
                        html.Li("Examples include: alanine, valine, leucine, isoleucine, methionine, phenylalanine, tryptophan"), 
                        html.Li("Typically found buried in the protein core, away from water, helping to maintain the protein's 3D shape")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/hydrophobic sidechain.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://www.technologynetworks.com/applied-sciences/articles/essential-amino-acids-chart-abbreviations-and-structure-324357", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("N'JOY Biochemistry: Amino Acids (General Structure, Classification, Significance)", href = "https://www.youtube.com/watch?v=rUlt8Xws_3Q&t=15s&pp=ygUaYW1pbm8gYWNpZCBjbGFzc2lmaWNhdGlvbnM%3D", target = "_blank")]),
                        html.Li([html.A("Medicosis Perfectionalis: Amino Acids (Classification)", href = "https://www.youtube.com/watch?v=9I-lvdQGLA4&t=8s&pp=ygUaYW1pbm8gYWNpZCBjbGFzc2lmaWNhdGlvbnM%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Classification of Amino Acids", href = "https://www.youtube.com/watch?v=OPAvXQsPCqQ&pp=ygUaYW1pbm8gYWNpZCBjbGFzc2lmaWNhdGlvbnM%3D", target = "_blank")]),
                        html.Li([html.A("Henrik's Lab: Classification of Amino Acids", href = "https://www.youtube.com/watch?v=AYW8qO6wXv8&pp=ygUaYW1pbm8gYWNpZCBjbGFzc2lmaWNhdGlvbnM%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter3/Slide4.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide5.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter3question8.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What part of an amino acid determines its classification?",
                        "options": [
                            "Amino group",
                            "Carboxyl group",
                            "Alpha carbon",
                            "Side chain (R group)"
                        ],
                        "answer": "Side chain (R group)"
                    },
                    {
                        "question": "Amino acids with side chains that carry a full charge are generally:",
                        "options": [
                            "Hydrophobic",
                            "Nonpolar",
                            "Hydrophilic",
                            "Unreactive"
                        ],
                        "answer": "Hydrophilic"
                    },
                    {
                        "question": "Amino acids with polar but uncharged side chains tend to:",
                        "options": [
                            "Avoid water",
                            "Form hydrogen bonds",
                            "Be electrically neutral and nonpolar",
                            "Be found only in the protein core"
                        ],
                        "answer": "Form hydrogen bonds"
                    },
                    {
                        "question": "Hydrophobic amino acids typically have side chains that are:",
                        "options": [
                            "Ionic",
                            "Polar",
                            "Nonpolar hydrocarbon chains or rings",
                            "Highly reactive with water"
                        ],
                        "answer": "Nonpolar hydrocarbon chains or rings"
                    },
                    {
                        "question": "Where in a folded protein are hydrophobic amino acids most likely to be found?",
                        "options": [
                            "On the protein surface",
                            "Interacting with water",
                            "In the protein's interior",
                            "Attached to DNA"
                        ],
                        "answer": "In the protein's interior"
                    },
                    {
                        "question": "Which type of amino acid side chain is most likely to form ionic bonds?",
                        "options": [
                            "Hydrophobic",
                            "Nonpolar",
                            "Electrically charged",
                            "Uncharged polar"
                        ],
                        "answer": "Electrically charged"
                    },
                    {
                        "question": "Polar but uncharged amino acids are different from charged amino acids because they:",
                        "options": [
                            "Can form ionic bonds",
                            "Have side chains that repel water",
                            "Have uneven charge distribution but no full charge",
                            "Only occur in non-functional proteins"
                        ],
                        "answer": "Have uneven charge distribution but no full charge"
                    },
                    {
                        "question": "Which group of amino acids is most likely to form hydrogen bonds with water?",
                        "options": [
                            "Nonpolar",
                            "Hydrophobic",
                            "Polar (charged or uncharged)",
                            "Special cases only"
                        ],
                        "answer": "Polar (charged or uncharged)"
                    },
                    {
                        "question": "What term best describes amino acids with side chains that avoid water?",
                        "options": [
                            "Hydrophilic",
                            "Reactive",
                            "Hydrophobic",
                            "Polar"
                        ],
                        "answer": "Hydrophobic"
                    },
                    {
                        "question": "Amino acids with electrically charged side chains at pH 7 can be:",
                        "options": [
                            "Only positive",
                            "Only negative",
                            "Either positive or negative",
                            "Never charged"
                        ],
                        "answer": "Either positive or negative"
                    },
                    {
                        "question": "Special-case amino acids are unique because they:",
                        "options": [
                            "Can bond with nucleotides",
                            "Have unique side chain structures that affect folding",
                            "Only appear in enzymes",
                            "Are not found in living organisms"
                        ],
                        "answer": "Have unique side chain structures that affect folding"
                    },
                    {
                        "question": "Which amino acid group most directly contributes to protein solubility in water?",
                        "options": [
                            "Nonpolar side chains",
                            "Polar and charged side chains",
                            "Methyl groups",
                            "Hydrocarbon backbones"
                        ],
                        "answer": "Polar and charged side chains"
                    },
                    {
                        "question": "Hydrophobic interactions between amino acids help stabilize:",
                        "options": [
                            "The protein's surface",
                            "The peptide bond",
                            "The protein's internal structure",
                            "The RNA backbone"
                        ],
                        "answer": "The protein's internal structure"
                    },
                    {
                        "question": "What kind of amino acid side chain would most likely be found in a membrane-spanning region of a protein?",
                        "options": [
                            "Polar uncharged",
                            "Positively charged",
                            "Nonpolar",
                            "Negatively charged"
                        ],
                        "answer": "Nonpolar"
                    },
                    {
                        "question": "Which amino acid classification allows interactions with both water and other polar molecules?",
                        "options": [
                            "Nonpolar",
                            "Hydrophobic",
                            "Polar (charged or uncharged)",
                            "Aromatic"
                        ],
                        "answer": "Polar (charged or uncharged)"
                    },
                    {
                        "question": "What distinguishes polar uncharged amino acids from nonpolar amino acids?",
                        "options": [
                            "They have longer carbon chains",
                            "They have electronegative atoms in the side chains",
                            "They are more common in proteins",
                            "They repel water"
                        ],
                        "answer": "They have electronegative atoms in the side chains"
                    },
                    {
                        "question": "Amino acids with nonpolar side chains are most likely to interact via:",
                        "options": [
                            "Hydrogen bonds",
                            "Ionic interactions",
                            "Hydrophobic interactions",
                            "Disulfide bridges"
                        ],
                        "answer": "Hydrophobic interactions"
                    },
                    {
                        "question": "Charged side chains are important in proteins because they can:",
                        "options": [
                            "Pass through membranes easily",
                            "Form covalent bonds with sugars",
                            "Participate in ionic and electrostatic interactions",
                            "Act as water barriers"
                        ],
                        "answer": "Participate in ionic and electrostatic interactions"
                    },
                    {
                        "question": "The ability of a protein to dissolve in water is largely due to:",
                        "options": [
                            "The number of amino acids",
                            "The presence of hydrophobic side chains",
                            "The presence of hydrophilic side chains",
                            "Its molecular weight"
                        ],
                        "answer": "The presence of hydrophilic side chains"
                    },
                    {
                        "question": "What overall factor determines how an amino acid will behave in water?",
                        "options": [
                            "Its peptide bond",
                            "Its backbone atoms",
                            "Its side chain properties",
                            "Its position in the gene sequence"
                        ],
                        "answer": "Its side chain properties"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Amino acids are classified based on the chemical nature of their side chains (R-groups), which affects how they interact in proteins."), 
                                html.Ul([
                                    html.Li([html.Strong("Electrically charged, hydrophilic side chains: "), "these can be positive or negative and often interact with water and other charged molecules"]),
                                    html.Li([html.Strong("Polar, uncharged, hydrophilic side chains: "), "these attract water, but do not carry a charge"]),
                                    html.Li([html.Strong("Special case amino acids: "), "these are unique amino acids with distinct roles, such as cysteine (can form disulfide bonds) or glycine (very small and flexible)"]),
                                    html.Li([html.Strong("Nonpolar, hydrophobic side chains: "), "these avoid water and tend to cluster inside of proteins to stabilize the structure"])
                                ])
                            ])],
                "feynman": [html.Div([
                    html.P("Amino acids are like different puzzle pieces and they get sorted based on their side parts (side chains) behave with water and charges."), 
                    html.P([html.Strong("Charged and friendly with water: "), "some amino acids have side chains that are positively or negatively charged. These amino acids love water and other charged things."]),
                    html.P([html.Strong("Polar, but not charged: "), "some amino acids ahve side chains that aren't charged but still like water, because they can make hydrogen bonds"]),
                    html.P([html.Strong("Special ones: "), "some amino acids are unique and are considered to be special cases."]), 
                    html.P([html.Strong("Water haters: "), "some amino acids have side chains made of mostly fats and oils, so they hate water and hide inside of the protein to stay away from it"]),
                    html.P("In summary, amino acids sort themselves based on how their side parts feel about water and charges. This influences how the protein folds and works.")
                ])]
            },   
            "q9": {
                "question": html.P("Understand how phospholipids organize to generate biological membranes."),
                "overview": html.Div([
                    html.P("Phospholipids are a unique molecule due to their water-loving (hydrophilic) heads and water-hating (hydrophobic) tails. Because of this they arrange themselves into a bilayer in water where the heads face out, towards the water, and the tails face in, away from the water."), 
                    html.P("This phospholipid bilayer forms the basic structure of biological membranes, such as the plasma membrane of cells."),
                    html.P("Because phospholipids contain both hydrophobic and hydrophilic parts, they are considered to be amphipathic.")
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Phospholipid Structure: "), "Phospholipids are composed of glycerol, two fatty acid tails, and one phosphate group. The phosphate group is hydrophilic (likes water) and the fatty acid tails are hydrophobic (dislikes water). Therefore, phospholipids are amphipathic (contains both polar (water-loving) and nonpolar (water-hating) regions)."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/phospholipid structure.jpg", style = {'marginRight':'40px', 'width':'600px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://www.youtube.com/watch?v=n2FRS-8hhOo", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Behavior in Water: "), "When placed in water, hydrophilic heads will turn towards the water and the hydrophobic tails will turn away from the water, spontaneously forming a phospholipid bilayer."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/phospholipid bilayer.jpg", style = {'marginRight':'40px', 'width':'600px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://commons.wikimedia.org/wiki/File:0302_Phospholipid_Bilayer.jpg", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("The Biological Membrane: "), "This bilayer is the foundation of cell membranes. It is flexible, semi-permeable, and self-healing, allowing certain molecules to pass through while keeping other molecules out. Oftentimes proteins and other molecules are embedded in or attached to the bilayer for some function, such as transport or communication."]), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/cell membrane.jpg", style = {'marginRight':'40px', 'width':'600px'}), 
                            html.Div(["Image from ", html.A("here", href = "https://courses.lumenlearning.com/hccs-waymakerbiology1/chapter/reading-structure-of-the-cell-membrane/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Why it Matters: "), "This bilayer is important for separating internal and external environments, creating compartments within a cell, and controlling what enters and what leaves a cell."]),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Inside the Cell Membrane", href = "https://www.youtube.com/watch?v=qBCVVszQQNs&t=272s&pp=ygUUcGhvc3Bob2xpcGlkIGJpbGF5ZXI%3D", target = "_blank")]),
                        html.Li([html.A("The Organic Chemistry Tutor: Fluid Mosaic Model of the Plasma Membrane (Phospholipid Bilayer)", href = "https://www.youtube.com/watch?v=xQjzPZZ4olE&t=4s&pp=ygUUcGhvc3Bob2xpcGlkIGJpbGF5ZXI%3D", target = "_blank")]),
                        html.Li([html.A("Dr. Matt & Dr. Mike: Cell Membrane (Phospholipid Bilayer)", href = "https://www.youtube.com/watch?v=0329WCV3Zzo&pp=ygUUcGhvc3Bob2xpcGlkIGJpbGF5ZXLSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("Crash Course: How Does Stuff Get Into Your Cells?", href = "https://www.youtube.com/watch?v=9Ia8zH-qMZw&pp=ygUUcGhvc3Bob2xpcGlkIGJpbGF5ZXI%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy Medicine", href = "https://www.youtube.com/watch?v=CBEys2CTkgE&pp=ygUUcGhvc3Bob2xpcGlkIGJpbGF5ZXI%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter3/Slide24.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide25.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide26.jpg"),
                    html.Img(src = "/assets/Chapter3/Slide27.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter3question9.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What makes a phospholipid an amphipathic molecule?",
                        "options": [
                            "It has two phosphate groups",
                            "It contains both hydrophilic and hydrophobic regions",
                            "It contains only nonpolar regions",
                            "It is entirely hydrophilic"
                        ],
                        "answer": "It contains both hydrophilic and hydrophobic regions"
                    },
                    {
                        "question": "Which part of the phospholipid is hydrophilic?",
                        "options": [
                            "The fatty acid tails",
                            "The glycerol backbone",
                            "The phosphate head",
                            "The entire molecule"
                        ],
                        "answer": "The phosphate head"
                    },
                    {
                        "question": "Which part of the phospholipid avoids water?",
                        "options": [
                            "The phosphate group",
                            "The glycerol backbone",
                            "The fatty acid tails",
                            "The head group"
                        ],
                        "answer": "The fatty acid tails"
                    },
                    {
                        "question": "What happens when phospholipids are placed in water?",
                        "options": [
                            "They dissolve completely",
                            "They form a random structure",
                            "They form a bilayer with tails inward",
                            "They clump into solid crystals"
                        ],
                        "answer": "They form a bilayer with tails inward"
                    },
                    {
                        "question": "The main structural framework of a cell membrane is the:",
                        "options": [
                            "Protein network",
                            "Phospholipid bilayer",
                            "Cholesterol matrix",
                            "Carbohydrate coating"
                        ],
                        "answer": "Phospholipid bilayer"
                    },
                    {
                        "question": "In a phospholipid bilayer, the hydrophobic tails point:",
                        "options": [
                            "Toward water",
                            "Toward the outside of the membrane",
                            "Away from each other",
                            "Toward each other"
                        ],
                        "answer": "Toward each other"
                    },
                    {
                        "question": "What allows biological membranes to form spontaneously in water?",
                        "options": [
                            "Hydrogen bonding of lipids",
                            "The amphipathic nature of phospholipids",
                            "Enzyme activity",
                            "High temperature"
                        ],
                        "answer": "The amphipathic nature of phospholipids"
                    },
                    {
                        "question": "The hydrophobic region of a phospholipid consists of:",
                        "options": [
                            "Phosphate and glycerol",
                            "Amino acids",
                            "Fatty acid chains",
                            "Nucleotides"
                        ],
                        "answer": "Fatty acid chains"
                    },
                    {
                        "question": "Which feature of phospholipids helps explain selective permeability in membranes?",
                        "options": [
                            "The glycerol group",
                            "The presence of cholesterol",
                            "The hydrophobic interior of the bilayer",
                            "The rigid protein layer"
                        ],
                        "answer": "The hydrophobic interior of the bilayer"
                    },
                    {
                        "question": "Why do phospholipid heads face outward in a bilayer?",
                        "options": [
                            "They are hydrophobic",
                            "They contain nonpolar bonds",
                            "They are attracted to water",
                            "They are repelled by each other"
                        ],
                        "answer": "They are attracted to water"
                    },
                    {
                        "question": "Phospholipid bilayers are important because they:",
                        "options": [
                            "Store energy",
                            "Speed up chemical reactions",
                            "Form a barrier between cell environments",
                            "Replicate genetic material"
                        ],
                        "answer": "Form a barrier between cell environments"
                    },
                    {
                        "question": "Which of the following best describes the orientation of phospholipids in a biological membrane?",
                        "options": [
                            "Heads face in, tails face out",
                            "Tails point away from each other",
                            "Heads face water, tails face each other",
                            "Random distribution in water"
                        ],
                        "answer": "Heads face water, tails face each other"
                    },
                    {
                        "question": "The flexibility of a membrane is largely due to:",
                        "options": [
                            "The solid structure of phospholipids",
                            "The rigid protein skeleton",
                            "The fluid nature of the phospholipid bilayer",
                            "The sugar chains on the membrane"
                        ],
                        "answer": "The fluid nature of the phospholipid bilayer"
                    },
                    {
                        "question": "Which of the following is NOT a characteristic of phospholipids?",
                        "options": [
                            "They are amphipathic",
                            "They contain a phosphate group",
                            "They are proteins",
                            "They have hydrophobic tails"
                        ],
                        "answer": "They are proteins"
                    },
                    {
                        "question": "The term 'amphipathic' refers to molecules that:",
                        "options": [
                            "Are either fully polar or fully nonpolar",
                            "Have both hydrophilic and hydrophobic regions",
                            "Can dissolve any substance",
                            "Are always water-insoluble"
                        ],
                        "answer": "Have both hydrophilic and hydrophobic regions"
                    },
                    {
                        "question": "What property of phospholipid tails helps create a membrane barrier?",
                        "options": [
                            "They are hydrophilic",
                            "They are nonpolar and repel water",
                            "They form peptide bonds",
                            "They attract charged particles"
                        ],
                        "answer": "They are nonpolar and repel water"
                    },
                    {
                        "question": "Which structural component is replaced by a phosphate group in phospholipids compared to triglycerides?",
                        "options": [
                            "One of the fatty acid tails",
                            "The glycerol backbone",
                            "All fatty acid tails",
                            "The hydroxyl groups"
                        ],
                        "answer": "One of the fatty acid tails"
                    },
                    {
                        "question": "Why do phospholipids form a bilayer rather than a single layer in water?",
                        "options": [
                            "To trap ions inside",
                            "To protect proteins",
                            "So that both sides of the bilayer can interact with water",
                            "Because tails are attracted to water"
                        ],
                        "answer": "So that both sides of the bilayer can interact with water"
                    },
                    {
                        "question": "In addition to phospholipids, which other type of molecule is commonly found embedded in the membrane?",
                        "options": [
                            "DNA",
                            "RNA",
                            "Proteins",
                            "Starch"
                        ],
                        "answer": "Proteins"
                    },
                    {
                        "question": "What function does the phospholipid bilayer primarily serve?",
                        "options": [
                            "Energy storage",
                            "Protein synthesis",
                            "Genetic replication",
                            "Selective barrier for the cell"
                        ],
                        "answer": "Selective barrier for the cell"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Phospholipids are a unique molecule due to their water-loving (hydrophilic) heads and water-hating (hydrophobic) tails. Because of this they arrange themselves into a bilayer in water where the heads face out, towards the water, and the tails face in, away from the water."), 
                                html.P("This phospholipid bilayer forms the basic structure of biological membranes, such as the plasma membrane of cells."),
                                html.P("Because phospholipids contain both hydrophobic and hydrophilic parts, they are considered to be amphipathic.")
                            ])],
                "feynman": [html.Div([
                    html.P("Imagine a molecule that's part water-lover, part water-hater. That's a phospholipid."), 
                    html.P("The head loves water and wants to be near it."), 
                    html.P("The tail hates water and wants to try to hide from it."),
                    html.P("Because of this, when you put phospholipids in water, they line up in a special way where the heads face the water and the tails try to hide together, away from the water."), 
                    html.P("This forms a double layer, or a bilayer, and that is how membranes are made!"), 
                    html.P("So being amphipathic means that the molecule has a 'split personality,' where one side loves water and the other avoids it. That makes phospholipids perfect for building membranes.")
                ])]
            },
            "q10": {
                "question": html.P("Know the definition of DNA, RNA, and the 3 major structural components of nucleotides."),
                "overview": html.Div([
                    html.P([html.Strong("DNA "), "and ", html.Strong("RNA "), "are types of nucleic acids, big molecules that store and pass on genetic information."]), 
                    html.P("They are composed of smaller units called nucleotides. Each nucleotide has three parts:"),
                    html.Ul([
                        html.Li("A sugar (DNA = deoxyribose, RNA = ribose)"),
                        html.Li("A phosphate group"), 
                        html.Li("A nitrogenous base (like adenine, thymine, cytosine, guanine, or uracil)")
                    ]),
                    html.P("DNA is a long-term storage system for genetic information. RNA helps to build proteins and can act as a messenger.")
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("What are nucleic acids? "), "Nucleic acids are polymers made of repeating nucleotide units. There are two major types:"]),
                    html.Ul([
                        html.Li([html.Strong("DNA (deoxyribonucleic acid): "), "stores hereditary information in most living organisms"]),
                        html.Li([html.Strong("RNA (ribonucleic acid): "), "helps carry out the instructions in DNA (such as making proteins)"])
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/dna v rna.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.thoughtco.com/dna-versus-rna-608191", target = "_blank")])
                        ]
                    ), 
                    html.P([html.Strong("What is a nucleotide? "), "A nucleotide has three components:"]),
                    html.Ul([
                        html.Li("A pentose sugar, which is a five carbon sugar (deoxyribose in DNA and ribose in RNA)"), 
                        html.Li("A phosphate group, which links nucleotides together in a chain via phosphodiester bonds"), 
                        html.Li("A nitrogenous base, of which there are five common: adenine (A), thymine (T), uracil (U), cytosine (C), and guanine (G)")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/nucleotide structure.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://pmgbiology.com/tag/nucleotide/", target = "_blank")])
                        ]
                    ), 
                    html.P("DNA is double-stranded and forms a helix structure whereas RNA is single stranded."), 
                    html.P("DNA can contain adenine, thymine, cytosine, or guanine. RNA can contain adenine, uracil, cytosine, or guanine."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/bases.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.bocsci.com/resources/nucleotide-bases-from-structure-to-modifications.html?srsltid=AfmBOoq26TfNj9u8H7awXok4BDEMUpr4x_1CRFGbU11ADBL5vw8UXkGz", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: DNA vs RNA", href = "https://www.youtube.com/watch?v=JQByjprj_mA&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Stated Clearly: DNA vs RNA (Differences in Form and Function)", href = "https://www.youtube.com/watch?v=FNynz6Q12Bw&pp=ygULRG5hIGFuZCBSTkHSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("Nucleus Biology: Overview of DNA and RNA", href = "https://www.youtube.com/watch?v=GhABWQC3YDs&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Medicosis Perfectionalis: DNA & RNA (Introduction to Molecular Biology)", href = "https://www.youtube.com/watch?v=g_FQdmP5d5Q&pp=ygULRG5hIGFuZCBSTkHSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("2 Minute Classroom: 5 Differences Between DNA and RNA", href = "https://www.youtube.com/watch?v=ruUf7ntRCk8&t=8s&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Whats Up Dude: Structure of Nucleic Acids", href = "https://www.youtube.com/watch?v=apaP9a079po&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter4/Slide3.jpg"),
                    html.Img(src = "/assets/Chapter4/Slide4.jpg"),
                    html.Img(src = "/assets/Chapter4/Slide6.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                     {
                        "question": "What are the three structural components of a nucleotide?",
                        "options": [
                            "Phosphate, sugar, lipid",
                            "Sugar, nitrogenous base, amino acid",
                            "Phosphate group, pentose sugar, nitrogenous base",
                            "Carbohydrate, protein, lipid"
                        ],
                        "answer": "Phosphate group, pentose sugar, nitrogenous base"
                    },
                    {
                        "question": "Which sugar is found in DNA?",
                        "options": [
                            "Ribose",
                            "Deoxyribose",
                            "Glucose",
                            "Fructose"
                        ],
                        "answer": "Deoxyribose"
                    },
                    {
                        "question": "Which sugar is found in RNA?",
                        "options": [
                            "Ribose",
                            "Deoxyribose",
                            "Glucose",
                            "Maltose"
                        ],
                        "answer": "Ribose"
                    },
                    {
                        "question": "What is the role of the phosphate group in a nucleotide?",
                        "options": [
                            "It stores energy",
                            "It binds to the nitrogenous base",
                            "It links nucleotides together",
                            "It determines the base pairing"
                        ],
                        "answer": "It links nucleotides together"
                    },
                    {
                        "question": "Which of the following is found in RNA but not in DNA?",
                        "options": [
                            "Thymine",
                            "Deoxyribose",
                            "Uracil",
                            "Guanine"
                        ],
                        "answer": "Uracil"
                    },
                    {
                        "question": "Which of the following bases is found in DNA but not in RNA?",
                        "options": [
                            "Adenine",
                            "Cytosine",
                            "Thymine",
                            "Uracil"
                        ],
                        "answer": "Thymine"
                    },
                    {
                        "question": "Which macromolecule type includes DNA and RNA?",
                        "options": [
                            "Carbohydrates",
                            "Proteins",
                            "Lipids",
                            "Nucleic acids"
                        ],
                        "answer": "Nucleic acids"
                    },
                    {
                        "question": "What does DNA stand for?",
                        "options": [
                            "Double nitrogen acid",
                            "Dimeric nucleic acid",
                            "Deoxyribonucleic acid",
                            "Dynamic ribonucleic acid"
                        ],
                        "answer": "Deoxyribonucleic acid"
                    },
                    {
                        "question": "What does RNA stand for?",
                        "options": [
                            "Ribose nucleotide acid",
                            "Ribonucleic acid",
                            "Ribose nitrogenous acid",
                            "Reactive nucleic acid"
                        ],
                        "answer": "Ribonucleic acid"
                    },
                    {
                        "question": "Which of the following is a major function of DNA?",
                        "options": [
                            "Transporting proteins",
                            "Carrying oxygen",
                            "Storing genetic information",
                            "Producing energy"
                        ],
                        "answer": "Storing genetic information"
                    },
                    {
                        "question": "Which of the following is a major function of RNA?",
                        "options": [
                            "Storing glucose",
                            "Passing on genetic traits to offspring",
                            "Helping build proteins",
                            "Maintaining membrane structure"
                        ],
                        "answer": "Helping build proteins"
                    },
                    {
                        "question": "What type of bond links nucleotides together in a nucleic acid chain?",
                        "options": [
                            "Hydrogen bond",
                            "Peptide bond",
                            "Glycosidic bond",
                            "Phosphodiester bond"
                        ],
                        "answer": "Phosphodiester bond"
                    },
                    {
                        "question": "What component of the nucleotide varies to create different 'letters' of the genetic code?",
                        "options": [
                            "Phosphate group",
                            "Pentose sugar",
                            "Nitrogenous base",
                            "Hydroxyl group"
                        ],
                        "answer": "Nitrogenous base"
                    },
                    {
                        "question": "Which of the following best describes the structure of DNA?",
                        "options": [
                            "Single-stranded",
                            "Triple-helix",
                            "Double-stranded helix",
                            "Circular carbohydrate chain"
                        ],
                        "answer": "Double-stranded helix"
                    },
                    {
                        "question": "RNA differs from DNA in that it is typically:",
                        "options": [
                            "Double-stranded and contains thymine",
                            "Single-stranded and contains uracil",
                            "Double-stranded and contains uracil",
                            "Single-stranded and contains thymine"
                        ],
                        "answer": "Single-stranded and contains uracil"
                    },
                    {
                        "question": "Which part of the nucleotide contains nitrogen?",
                        "options": [
                            "Phosphate group",
                            "Pentose sugar",
                            "Nitrogenous base",
                            "Hydroxyl group"
                        ],
                        "answer": "Nitrogenous base"
                    },
                    {
                        "question": "How many different nitrogenous bases are commonly found in DNA and RNA?",
                        "options": [
                            "2",
                            "3",
                            "4",
                            "5"
                        ],
                        "answer": "5"
                    },
                    {
                        "question": "Which structural difference between DNA and RNA affects their stability?",
                        "options": [
                            "RNA has more phosphate groups",
                            "RNA has a double helix",
                            "RNA has an extra oxygen in the sugar",
                            "DNA contains uracil instead of thymine"
                        ],
                        "answer": "RNA has an extra oxygen in the sugar"
                    },
                    {
                        "question": "Why is DNA more suitable for long-term information storage than RNA?",
                        "options": [
                            "It is single-stranded",
                            "It contains ribose",
                            "It is more chemically stable",
                            "It is shorter"
                        ],
                        "answer": "It is more chemically stable"
                    },
                    {
                        "question": "Which of the following correctly lists all three parts of a nucleotide?",
                        "options": [
                            "Sugar, base, lipid",
                            "Sugar, protein, phosphate",
                            "Phosphate, base, sugar",
                            "Sugar, enzyme, base"
                        ],
                        "answer": "Phosphate, base, sugar"
                    }
                ],
                "blurting": [html.Div([
                                html.P([html.Strong("DNA "), "and ", html.Strong("RNA "), "are types of nucleic acids, big molecules that store and pass on genetic information."]), 
                                html.P("They are composed of smaller units called nucleotides. Each nucleotide has three parts:"),
                                html.Ul([
                                    html.Li("A sugar (DNA = deoxyribose, RNA = ribose)"),
                                    html.Li("A phosphate group"), 
                                    html.Li("A nitrogenous base (like adenine, thymine, cytosine, guanine, or uracil)")
                                ]),
                                html.P("DNA is a long-term storage system for genetic information. RNA helps to build proteins and can act as a messenger.")
                            ])],
                "feynman": [html.Div([
                    html.P("Imagine that DNA and RNA as instruction manuals for life. They are made of smaller building blocks called nucleotides, like letters in the instruction manual."), 
                    html.P("Each nucleotide has three parts:"), 
                    html.Ul([
                        html.Li("A sugar (DNA uses deoxyribose, RNA uses ribose)"),
                        html.Li("A phosphate group (which links the letters together)"), 
                        html.Li("A base, such as A, T, C, G, or U, which carries the actual information")
                    ]),
                    html.P("The main difference between DNA and RNA is that DNA is for long-term storage (like an instruction manual in the archive), while RNA is a working copy used to make proteins (like a copy of the instruction manual taken to the build site.)"),
                    html.P("In summary: DNA and RNA are long chains of these letter-like units, which helps the cells know what to do and how to function.")
                ])]
            },
            "q11": {
                "question": html.P("Be familiar with the structural features of DNA and RNA."),
                "overview": html.Div([
                    html.P(["DNA and RNA are ", html.Strong("nucleic acids "), "made of repeating nucleotides. Their backbones are formed by ", html.Strong("sugars and phosphate groups"), " that are linked by ", html.Strong("phosphodiester bonds.")]),
                    html.P(""),
                    html.P([html.Strong("DNA:")]),
                    html.P("DNA is double-stranded and has deoxyribose (which lacks an oxygen on carbon 2')"),
                    html.P("DNA strands run antiparallel to each other"),
                    html.P(""),
                    html.P([html.Strong("RNA:")]),
                    html.P("RNA is single-stranded and has ribose (which has an OH on carbon 2')"),
                    html.P("Hydrogen bonds help to stabilize RNA's folded structure")    
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("The Backbone Structure:")]),
                    html.P("Both DNA and RNA have a sugar-phosphate backbone. The phosphodiester bond links the 3' carbon of one sugar to the 5' carbon of the next sugar, giving the strand directionality (5' to 3')"),
                    html.P([html.Strong("Sugar Differences:")]),
                    html.P("DNA has deoxyribose, which has a hydrogen (H) on the 2' carbon, whereas RNA has ribose, which has a hydroxyl group (OH) on the 2' carbon."), 
                    html.P("This small difference makes RNA more chemically reactive and less stable than DNA."), 
                    html.P([html.Strong("Strand Structure:")]),
                    html.P("DNA is double-stranded with the two strands running opposite (antiparallel) directions, forming a double helix."), 
                    html.P("RNA is single-stranded, but can form in complex shapes, such as hairpins or loops, which are stabilized by hydrogen bonding between the bases."),
                    html.P([html.Strong("Hydrogen Bonding:")]),
                    html.P("In DNA, hydrogen bonds hold the two strands together (Adenine bonds to Thymine with 2 hydrogen bonds and Guanine binds to Cytosine with 3 hydrogen bonds)"),
                    html.P("In RNA, hydrogen bonds help form internal secondary structures, even though it is single-stranded."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/dna v rna.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.thoughtco.com/dna-versus-rna-608191", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: DNA vs RNA", href = "https://www.youtube.com/watch?v=JQByjprj_mA&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Stated Clearly: DNA vs RNA (Differences in Form and Function)", href = "https://www.youtube.com/watch?v=FNynz6Q12Bw&pp=ygULRG5hIGFuZCBSTkHSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("Nucleus Biology: Overview of DNA and RNA", href = "https://www.youtube.com/watch?v=GhABWQC3YDs&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Medicosis Perfectionalis: DNA & RNA (Introduction to Molecular Biology)", href = "https://www.youtube.com/watch?v=g_FQdmP5d5Q&pp=ygULRG5hIGFuZCBSTkHSBwkJwQkBhyohjO8%3D", target = "_blank")]),
                        html.Li([html.A("2 Minute Classroom: 5 Differences Between DNA and RNA", href = "https://www.youtube.com/watch?v=ruUf7ntRCk8&t=8s&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")]),
                        html.Li([html.A("Whats Up Dude: Structure of Nucleic Acids", href = "https://www.youtube.com/watch?v=apaP9a079po&pp=ygULRG5hIGFuZCBSTkE%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter4/Slide5.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide6.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide7.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide10.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide11.jpg") 
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of bond connects nucleotides in the sugar-phosphate backbone of DNA and RNA?",
                        "options": [
                            "Hydrogen bond",
                            "Ionic bond",
                            "Peptide bond",
                            "Phosphodiester bond"
                        ],
                        "answer": "Phosphodiester bond"
                    },
                    {
                        "question": "Which carbons in the sugar are linked by the phosphodiester bond in a nucleic acid strand?",
                        "options": [
                            "1' and 4'",
                            "2' and 3'",
                            "3' and 5'",
                            "5' and 6'"
                        ],
                        "answer": "3' and 5'"
                    },
                    {
                        "question": "Which sugar is found in RNA?",
                        "options": [
                            "Deoxyribose",
                            "Ribose",
                            "Glucose",
                            "Fructose"
                        ],
                        "answer": "Ribose"
                    },
                    {
                        "question": "Which sugar is found in DNA?",
                        "options": [
                            "Ribose",
                            "Deoxyribose",
                            "Sucrose",
                            "Lactose"
                        ],
                        "answer": "Deoxyribose"
                    },
                    {
                        "question": "Which structural feature distinguishes ribose from deoxyribose?",
                        "options": [
                            "Ribose has an OH at carbon 2'; deoxyribose has an H",
                            "Deoxyribose has a nitrogen group",
                            "Ribose has more carbon atoms",
                            "Deoxyribose is a six-carbon sugar"
                        ],
                        "answer": "Ribose has an OH at carbon 2'; deoxyribose has an H"
                    },
                    {
                        "question": "What is meant by the term 'antiparallel' in DNA structure?",
                        "options": [
                            "The strands are made of different sugars",
                            "The two strands run in opposite 5' to 3' directions",
                            "The strands have opposite charges",
                            "Only one strand is active at a time"
                        ],
                        "answer": "The two strands run in opposite 5' to 3' directions"
                    },
                    {
                        "question": "Which of the following statements about RNA is true?",
                        "options": [
                            "RNA is double-stranded",
                            "RNA contains thymine instead of uracil",
                            "RNA is single-stranded and contains ribose",
                            "RNA is more stable than DNA"
                        ],
                        "answer": "RNA is single-stranded and contains ribose"
                    },
                    {
                        "question": "Which of the following statements about DNA is true?",
                        "options": [
                            "DNA contains uracil",
                            "DNA is usually single-stranded",
                            "DNA contains deoxyribose and is double-stranded",
                            "DNA has no phosphate groups"
                        ],
                        "answer": "DNA contains deoxyribose and is double-stranded"
                    },
                    {
                        "question": "Why is DNA more chemically stable than RNA?",
                        "options": [
                            "It has stronger hydrogen bonds",
                            "It contains more nitrogenous bases",
                            "It lacks a hydroxyl group at the 2' carbon",
                            "It has a triple helix structure"
                        ],
                        "answer": "It lacks a hydroxyl group at the 2' carbon"
                    },
                    {
                        "question": "What stabilizes the folded structure of RNA?",
                        "options": [
                            "Covalent bonds between strands",
                            "Hydrogen bonding between nitrogenous bases",
                            "Ionic bonds between sugars",
                            "Peptide linkages"
                        ],
                        "answer": "Hydrogen bonding between nitrogenous bases"
                    },
                    {
                        "question": "The backbone of a nucleic acid strand is made of:",
                        "options": [
                            "Nitrogenous bases only",
                            "Sugars and phosphate groups",
                            "Sugars and amino acids",
                            "Ribose and deoxyribose"
                        ],
                        "answer": "Sugars and phosphate groups"
                    },
                    {
                        "question": "Which of the following is true about phosphodiester linkages?",
                        "options": [
                            "They form between nitrogenous bases",
                            "They link amino acids together",
                            "They connect sugars and phosphates in nucleic acids",
                            "They form the rungs of the DNA ladder"
                        ],
                        "answer": "They connect sugars and phosphates in nucleic acids"
                    },
                    {
                        "question": "Which end of a nucleic acid has a free phosphate group?",
                        "options": [
                            "3' end",
                            "5' end",
                            "Both ends",
                            "Neither end"
                        ],
                        "answer": "5' end"
                    },
                    {
                        "question": "Which end of a nucleic acid has a free hydroxyl group on the sugar?",
                        "options": [
                            "5' end",
                            "3' end",
                            "Middle of the strand",
                            "The nitrogenous base"
                        ],
                        "answer": "3' end"
                    },
                    {
                        "question": "In RNA, hydrogen bonding helps form:",
                        "options": [
                            "A double helix",
                            "Secondary structures like loops and hairpins",
                            "Only the sugar-phosphate backbone",
                            "Peptide bonds"
                        ],
                        "answer": "Secondary structures like loops and hairpins"
                    },
                    {
                        "question": "What best describes the difference in structure between DNA and RNA?",
                        "options": [
                            "DNA has uracil; RNA has thymine",
                            "DNA is single-stranded; RNA is double-stranded",
                            "DNA has deoxyribose; RNA has ribose",
                            "RNA has no sugar"
                        ],
                        "answer": "DNA has deoxyribose; RNA has ribose"
                    },
                    {
                        "question": "Which of the following contributes to the directionality of a nucleic acid strand?",
                        "options": [
                            "The shape of the base pairs",
                            "The phosphate-sugar 3′ to 5′ connections",
                            "The presence of proteins",
                            "The number of hydrogen bonds"
                        ],
                        "answer": "The phosphate-sugar 3′ to 5′ connections"
                    },
                    {
                        "question": "What term describes the chemical difference between the sugars in DNA and RNA?",
                        "options": [
                            "Polarity",
                            "Hydrolysis",
                            "Presence or absence of an oxygen on carbon 2′",
                            "Hydrogen bonding"
                        ],
                        "answer": "Presence or absence of an oxygen on carbon 2′"
                    },
                    {
                        "question": "Why can RNA fold into complex 3D shapes?",
                        "options": [
                            "It forms double helices with DNA",
                            "It contains more phosphates",
                            "Hydrogen bonding between complementary bases within the same strand",
                            "RNA molecules are very short"
                        ],
                        "answer": "Hydrogen bonding between complementary bases within the same strand"
                    },
                    {
                        "question": "In DNA, the two strands are held together primarily by:",
                        "options": [
                            "Ionic bonds",
                            "Phosphodiester bonds",
                            "Hydrogen bonds between bases",
                            "Covalent bonds between sugars"
                        ],
                        "answer": "Hydrogen bonds between bases"
                    }
                ],
                "blurting": [],
                "feynman": [html.Div([
                    html.P("DNA and RNA are like chains made of sugar and phosphate links. DNA has two strands like a ladder, while RNA has only one. DNA uses deoxyribose (missing one oxygen), while RNA uses ribose (has an extra oxygen). That extra oxygen makes RNA less stable. Even though RNA is single-stranded, it can still hold and make complex shapes using hydrogen bonds.")
                ])]
            }, 
            "q12": {
                "question": html.P("Be able to name the bases present in DNA and RNA and which bases form complementary pairs"),
                "overview": html.Div([
                    html.P("DNA bases are: adenine (A), thymine (T), cytosine (C), and guanine (G)"),
                    html.P("RNA bases are : adenine (A), uracil (U), cytosine (C), and guanine (G)"),
                    html.P("Adenine pairs with Thymine or Uracil with 2 hydrogen bonds"),
                    html.P("Guanine pairs with cytosine with 3 hydrogen bonds")
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Base Pairing:")]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/bases.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.bocsci.com/resources/nucleotide-bases-from-structure-to-modifications.html?srsltid=AfmBOoq26TfNj9u8H7awXok4BDEMUpr4x_1CRFGbU11ADBL5vw8UXkGz", target = "_blank")])
                        ]
                    ),
                    html.P("In DNA, adenine (A) pairs with thymine (T) with two hydrogen bonds."),
                    html.P("In RNA, adenine (A) pairs with uracil (U) with two hydrogen bonds."),
                    html.P("In both DNA and RNA, guanine (G) pairs with cytosine (C) with three hydrogen bonds."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/base pairing.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://knowgenetics.org/nucleotides-and-bases/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Purines and Pyrimidines")]),
                    html.P("Adenine and guanine are purines (two rings) while cytosine and guanine are pyrimidines (one ring)."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/purines v pyrimidines.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://sciencenotes.org/purines-and-pyrimidines/", target = "_blank")])
                        ]
                    ),
                    html.Div([
                        html.P("One easy way to remember this is: "),
                        html.P([html.Strong("A"), "ngry ", html.Strong("G"), "arfield says ", html.Strong("P"), "urr"]),
                        html.P("and"), 
                        html.P([html.Strong("T"), "om ", html.Strong("C"), "ruise is a pirate"]),
                        html.P("It seems silly, but let me explain."), 
                        html.P("Garfield is a cat. You can imagine him as two circles, his head and his body. Just like a PURINE. Adenine and guanine are purines, which have two rings."), 
                        html.P("Pirates wear eyepatches, which is just one circle, just like a PYRIMIDINE. Thymine and cytosine are pyrimidines, which have only one ring.")
                    ], style = {'backgroundColor': "#9ed3a0", 'border': '1px solid #c3e6cb', 'padding':'15px', 'borderRadius':'8px', 'marginTop':'10px'}), 
                    html.P("This is an easy way to not mix up which bases are purines and which bases are pyrimidines."),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Study.com: Complementary Base Pairing", href = "https://www.youtube.com/watch?v=Xkkk3tSs9Wc&pp=ygUXbnVjbGVvdGlkZSBiYXNlIHBhaXJpbmc%3D", target = "_blank")]),
                        html.Li([html.A("Clint Explains: DNA Base Pairing Rules", href = "https://www.youtube.com/watch?v=sSVUjGrifz8&pp=ygUXbnVjbGVvdGlkZSBiYXNlIHBhaXJpbmc%3D", target = "_blank")]),
                        html.Li([html.A("The Organic Chemistry Tutor: Nucleosides vs Nucleotides, Purines vs Pyrimidines", href = "https://www.youtube.com/watch?v=QsFPtprFJks&pp=ygUXbnVjbGVvdGlkZSBiYXNlIHBhaXJpbmc%3D", target = "_blank")]), 
                        html.Li([html.A("DrDiclonius: DNA Base Pairing", href = "https://www.youtube.com/watch?v=alM_BhVfNtg&pp=ygUXbnVjbGVvdGlkZSBiYXNlIHBhaXJpbmc%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter4/Slide7.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide9.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide10.jpg"), 
                    html.Img(src = "/assets/Chapter4/Slide11.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Which base is found in DNA but not in RNA?",
                        "options": ["Uracil", "Adenine", "Thymine", "Guanine"],
                        "answer": "Thymine"
                    },
                    {
                        "question": "Which base is found in RNA but not in DNA?",
                        "options": ["Cytosine", "Uracil", "Thymine", "Adenine"],
                        "answer": "Uracil"
                    },
                    {
                        "question": "In DNA, adenine (A) pairs with:",
                        "options": ["Uracil", "Cytosine", "Guanine", "Thymine"],
                        "answer": "Thymine"
                    },
                    {
                        "question": "In DNA, cytosine (C) pairs with:",
                        "options": ["Thymine", "Guanine", "Adenine", "Uracil"],
                        "answer": "Guanine"
                    },
                    {
                        "question": "Which type of bond holds complementary DNA bases together?",
                        "options": ["Ionic bonds", "Phosphodiester bonds", "Hydrogen bonds", "Peptide bonds"],
                        "answer": "Hydrogen bonds"
                    },
                    {
                        "question": "Which base pairs with adenine in RNA?",
                        "options": ["Thymine", "Guanine", "Cytosine", "Uracil"],
                        "answer": "Uracil"
                    },
                    {
                        "question": "What are the four bases found in DNA?",
                        "options": ["A, U, C, G", "A, C, G, T", "A, T, C, U", "G, C, U, T"],
                        "answer": "A, C, G, T"
                    },
                    {
                        "question": "What are the four bases found in RNA?",
                        "options": ["A, C, G, T", "A, C, G, U", "C, G, U, T", "A, T, C, U"],
                        "answer": "A, C, G, U"
                    },
                    {
                        "question": "What kind of molecule is a DNA base?",
                        "options": ["Lipid", "Protein", "Nitrogenous base", "Sugar"],
                        "answer": "Nitrogenous base"
                    },
                    {
                        "question": "Which bases are purines?",
                        "options": ["Adenine and cytosine", "Thymine and guanine", "Adenine and guanine", "Cytosine and thymine"],
                        "answer": "Adenine and guanine"
                    },
                    {
                        "question": "Which bases are pyrimidines?",
                        "options": ["Adenine and guanine", "Guanine and uracil", "Cytosine, thymine, and uracil", "Adenine and cytosine"],
                        "answer": "Cytosine, thymine, and uracil"
                    },
                    {
                        "question": "Why do purines pair with pyrimidines in DNA?",
                        "options": ["They form stronger covalent bonds", "They are the same size", "To maintain even spacing in the double helix", "They are attracted by phosphate groups"],
                        "answer": "To maintain even spacing in the double helix"
                    },
                    {
                        "question": "How many hydrogen bonds form between cytosine and guanine?",
                        "options": ["1", "2", "3", "4"],
                        "answer": "3"
                    },
                    {
                        "question": "How many hydrogen bonds form between adenine and thymine?",
                        "options": ["1", "2", "3", "4"],
                        "answer": "2"
                    },
                    {
                        "question": "Which base replaces thymine in RNA?",
                        "options": ["Adenine", "Guanine", "Cytosine", "Uracil"],
                        "answer": "Uracil"
                    },
                    {
                        "question": "What kind of base pairing does RNA use for internal folding?",
                        "options": ["Random", "Peptide-based", "Hydrogen bonding between complementary bases", "Covalent base stacking"],
                        "answer": "Hydrogen bonding between complementary bases"
                    },
                    {
                        "question": "Which base pair is stronger due to more hydrogen bonds?",
                        "options": ["A–T", "A–U", "G–C", "T–U"],
                        "answer": "G–C"
                    },
                    {
                        "question": "What is the main role of base pairing in DNA?",
                        "options": ["Allow ribosome binding", "Provide energy for the cell", "Store genetic information and allow accurate replication", "Break down nutrients"],
                        "answer": "Store genetic information and allow accurate replication"
                    },
                    {
                        "question": "Which statement is true about DNA base pairing?",
                        "options": ["A pairs with U, C pairs with T", "A pairs with T, C pairs with G", "A pairs with G, T pairs with C", "C pairs with T, A pairs with U"],
                        "answer": "A pairs with T, C pairs with G"
                    },
                    {
                        "question": "Which base pairing is found in RNA instead of DNA?",
                        "options": ["C–T", "G–T", "A–U", "G–A"],
                        "answer": "A–U"
                    }
                ],
                "blurting": [html.Div([
                                html.P("DNA bases are: adenine (A), thymine (T), cytosine (C), and guanine (G)"),
                                html.P("RNA bases are : adenine (A), uracil (U), cytosine (C), and guanine (G)"),
                                html.P("Adenine pairs with Thymine or Uracil with 2 hydrogen bonds"),
                                html.P("Guanine pairs with cytosine with 3 hydrogen bonds")
                            ])],
                "feynman": [html.Div([
                                html.P("DNA bases are: adenine (A), thymine (T), cytosine (C), and guanine (G)"),
                                html.P("RNA bases are : adenine (A), uracil (U), cytosine (C), and guanine (G)"),
                                html.P("Adenine pairs with Thymine or Uracil with 2 hydrogen bonds"),
                                html.P("Guanine pairs with cytosine with 3 hydrogen bonds")
                            ])]
            },
            "q13": {
                "question": html.P("Understand the difference between the terms “anabolism” and “catabolism” and how these processes relate to the formation or breakdown of each of the three groups of macromolecules."),
                "overview": html.Div([
                    html.P([html.Strong("Catabolism: "), "breaking up large molecules to produce smaller ones by hydrolysis (splitting with water) of covalent bonds"]),
                    html.P([html.Strong("Anabolism: "), "bonding together small molecules to produce larger ones by removing water molecules to allow covalent bond formation (dehydration synthesis) "])
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Catabolism: Breaking Down")]), 
                    html.P("Catabolism is the process by which larger molecules are broken down into smaller subunits. This breakdown typically involves:"),
                    html.Ul([
                        html.Li("A hydrolysis reaction, where a water molecule is used to break a covalent bond"), 
                        html.Li("The release of energy, which the cell can then use for other functions")
                    ]),
                    html.P("Some examples would be proteins being broken down into amino acids, carbohydrates (such as starch) being broken down into simple sugars (such as glucose), and lipids being broken down into fatty acids and glycerol."), 
                    html.P("These catabolic processes are essential for digestion, recycling of cellular materials, and release of energy (especially from sugars and fats)."), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/catabolism.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://study.com/skill/practice/comparing-anabolic-and-catabolic-pathways-questions.html", target = "_blank")])
                        ]
                    ), 
                    html.Br(),
                    html.P([html.Strong("Anabolism: Building Up")]),
                    html.P("Anabolism is the opposite of catabolism. It is the construction of larger, more complex molecules from smaller building blocks. This process involves:"), 
                    html.Ul([
                        html.Li("A hydrolysis reaction, where water is removed to form a new covalent bond"), 
                        html.Li("Energy input, as these reactions often require energy (usually from ATP)")
                    ]),
                    html.P("Some examples would be amino acids linking via peptide bonds to form proteins, monosaccharides linking via glycosidic linkages to form polysaccharides, and fatty acids and glycerols linking via ester linkages to form triglycerides."),
                    html.P("These processes are essential for growth, repair, storage of energy, and building cell structures."), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/anabolism.png", style = {'marginRight':'40px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://study.com/skill/practice/comparing-anabolic-and-catabolic-pathways-questions.html", target = "_blank")])
                        ]
                    ), 
                    html.P(["An easy way to remember which is which is to remember that ", html.Strong("CAT"), "atabolism is 'destructive' (breaking down) like cats are destructive!"]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/anabolism catabolism summary.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://quizlet.com/504202632/lesson-11-metabolism-flash-cards/", target = "_blank")])
                        ]
                    ), 
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("The Organic Chemistry Tutor: Metabolism, Anabolism, and Catabolism (Anabolic vs Catabolic Reactions)", href = "https://www.youtube.com/watch?v=onDQ9KgDSVw&pp=ygUYYW5hYm9saXNtIGFuZCBjYXRhYm9saXNt", target = "_blank")]),
                        html.Li([html.A("Khan Academy Medicine: Overview of Metabolism (Anabolism and Catabolism)", href = "https://www.youtube.com/watch?v=ST1UWnenOo0&t=3s&pp=ygUYYW5hYm9saXNtIGFuZCBjYXRhYm9saXNt", target = "_blank")]),
                        html.Li([html.A("Microbial Zoo: Metabolism (Anabolism and Catabolism)", href = "https://www.youtube.com/watch?v=70O7Cic3J5s&pp=ygUYYW5hYm9saXNtIGFuZCBjYXRhYm9saXNt", target = "_blank")]),
                        html.Li([html.A("Biology Lectures: Anabolism vs Catabolism (Differences Between Anabolism and Catabolism)", href = "https://www.youtube.com/watch?v=ib_AWXnWXHk&pp=ygUYYW5hYm9saXNtIGFuZCBjYXRhYm9saXNt", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter4/Slide12.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                     {
                        "question": "What is catabolism?",
                        "options": ["The process of building large molecules from small ones", "The breakdown of large molecules into smaller ones", "The formation of DNA from RNA", "The replication of cells"],
                        "answer": "The breakdown of large molecules into smaller ones"
                    },
                    {
                        "question": "What is anabolism?",
                        "options": ["The breakdown of glucose for energy", "The breakdown of proteins", "The construction of larger molecules from smaller ones", "The destruction of cells"],
                        "answer": "The construction of larger molecules from smaller ones"
                    },
                    {
                        "question": "Which process typically releases energy?",
                        "options": ["Anabolism", "Protein folding", "Catabolism", "Dehydration synthesis"],
                        "answer": "Catabolism"
                    },
                    {
                        "question": "Which process usually requires an input of energy?",
                        "options": ["Catabolism", "Anabolism", "Hydrolysis", "Digestion"],
                        "answer": "Anabolism"
                    },
                    {
                        "question": "What type of reaction is used in catabolism?",
                        "options": ["Dehydration synthesis", "Phosphorylation", "Hydrolysis", "Oxidation"],
                        "answer": "Hydrolysis"
                    },
                    {
                        "question": "What type of reaction is used in anabolism?",
                        "options": ["Hydrolysis", "Dehydration synthesis", "Oxidation", "Methylation"],
                        "answer": "Dehydration synthesis"
                    },
                    {
                        "question": "Which molecule is typically removed during dehydration synthesis?",
                        "options": ["Oxygen", "Carbon dioxide", "Water", "Hydrogen peroxide"],
                        "answer": "Water"
                    },
                    {
                        "question": "Which molecule is typically added during hydrolysis?",
                        "options": ["Carbon dioxide", "Hydrogen", "Oxygen", "Water"],
                        "answer": "Water"
                    },
                    {
                        "question": "What type of metabolic process is protein digestion?",
                        "options": ["Anabolic", "Catabolic", "Photosynthetic", "Endergonic"],
                        "answer": "Catabolic"
                    },
                    {
                        "question": "What type of metabolic process is the formation of a protein from amino acids?",
                        "options": ["Catabolic", "Anabolic", "Exergonic", "Hydrolytic"],
                        "answer": "Anabolic"
                    },
                    {
                        "question": "Which macromolecule is broken down into amino acids during catabolism?",
                        "options": ["Lipids", "Carbohydrates", "Proteins", "Nucleic acids"],
                        "answer": "Proteins"
                    },
                    {
                        "question": "What are carbohydrates broken down into during catabolism?",
                        "options": ["Amino acids", "Fatty acids", "Monosaccharides", "Nucleotides"],
                        "answer": "Monosaccharides"
                    },
                    {
                        "question": "Which products result from lipid catabolism?",
                        "options": ["Amino acids", "Fatty acids and glycerol", "Monosaccharides", "RNA bases"],
                        "answer": "Fatty acids and glycerol"
                    },
                    {
                        "question": "Dehydration synthesis is used to:",
                        "options": ["Break bonds using water", "Split polymers into monomers", "Build macromolecules by removing water", "Break down glucose for energy"],
                        "answer": "Build macromolecules by removing water"
                    },
                    {
                        "question": "Which of the following is an example of an anabolic process?",
                        "options": ["Glycogen breakdown", "Protein digestion", "DNA synthesis", "Fat breakdown"],
                        "answer": "DNA synthesis"
                    },
                    {
                        "question": "Which of the following is an example of a catabolic process?",
                        "options": ["Glycogen formation", "Protein synthesis", "Lipid breakdown", "DNA replication"],
                        "answer": "Lipid breakdown"
                    },
                    {
                        "question": "During which process is energy typically stored in chemical bonds?",
                        "options": ["Catabolism", "Hydrolysis", "Anabolism", "Fermentation"],
                        "answer": "Anabolism"
                    },
                    {
                        "question": "Which process involves the use of enzymes to break covalent bonds with water?",
                        "options": ["Anabolism", "Hydrogen bonding", "Catabolism", "Photosynthesis"],
                        "answer": "Catabolism"
                    },
                    {
                        "question": "Macromolecule formation, such as protein assembly, is an example of:",
                        "options": ["Digestion", "Catabolism", "Anabolism", "Oxidation"],
                        "answer": "Anabolism"
                    },
                    {
                        "question": "Which best describes the relationship between catabolism and anabolism?",
                        "options": ["They are unrelated", "Catabolism makes energy; anabolism uses it to build", "They both store energy", "Anabolism breaks molecules; catabolism builds them"],
                        "answer": "Catabolism makes energy; anabolism uses it to build"
                    }
                ],
                "blurting": [html.Div([
                                html.P([html.Strong("Catabolism: "), "breaking up large molecules to produce smaller ones by hydrolysis (splitting with water) of covalent bonds"]),
                                html.P([html.Strong("Anabolism: "), "bonding together small molecules to produce larger ones by removing water molecules to allow covalent bond formation (dehydration synthesis) "])
                            ])],
                "feynman": [html.Div([
                    html.P("Imagine your body is a lego builder and breaker. Catabolism is when your body breaks big lego structures into individual pieces. It does this by adding water to the bonds between them. This process is called hydrolysis. This breaking apart also releases energy that your body can use for other things."), 
                    html.P("Anabolism is when your body builds a large lego structure from the individual pieces. It does this by removing water from between two pieces to help them stick together, in a reaction known as dehydration synthesis. This requires energy to do."),
                    html.P("In summary:"),
                    html.Ul([
                        html.Li("Catabolism = BREAKING APART, water in, energy out"),
                        html.Li("Anabolism = PUTTING TOGETHER, water out, energy in")
                    ])
                ])]
            },
            "q14": {
                "question": html.P("Be able to name each of the four scientists that were involved in the discovery of the structure of DNA. Be familiar with the contribution of each scientist to this discovery."),
                "overview": html.Div([
                    html.Ul([
                        html.Li("James Watson: co-discovered the double-helix structure DNA"), 
                        html.Li("Francis Crick: co-discovered the double-helix structure of DNA"),
                        html.Li("Rosalind Franklin: produced critical X-ray diffraction images of DNA, in particular, Photo 51"),
                        html.Li("Maurice Wilkins: shared Rosalind Franklin's work with James Watson and Francis Crick")
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.Ul([
                        html.Li([html.Strong("Rosalind Franklin: "), "produced critical X-ray diffraction images of DNA, which revealed the helical structure of DNA. Her data provided key measurements that Watson and Crick used to develop the double-helix model, which was used without her permission. She died prior to the awarding of the Nobel Prize to Watson, Crick, and Wilkins in 1962 and Nobel Prizes were not awarded posthumously, so she was not credited."]),
                        html.Li([html.Strong("James Watson: "), "a co-discoverer of the double-helix structure. He worked on building models of DNA structure using data from other researchers and collaborated closely with Francis Crick at Cambridge University."]),
                        html.Li([html.Strong("Francis Crick: "), "a co-discoverer of the double-helix structure. he helped to interpret the data from Rosalind Franklin's X-ray images to propose the antiparallel, base-pairing structure of DNA."]),
                        html.Li([html.Strong("Maurice Wilkins: "), "worked in the same lab as Franklin and also used X-ray crystallography. He shared Photo 51 with Watson and Crick (without Franklin's knowledge or consent), which helps them develop the correct model and was awarded the Nobel Prize with Watson and Crick in 1962."])
                    ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Who are the two scientists most often credited with discovering the double-helix structure of DNA?",
                        "options": ["Watson and Wilkins", "Franklin and Crick", "Watson and Crick", "Wilkins and Franklin"],
                        "answer": "Watson and Crick"
                    },
                    {
                        "question": "What critical technique did Rosalind Franklin use to study DNA structure?",
                        "options": ["Gel electrophoresis", "Chromatography", "X-ray crystallography", "DNA sequencing"],
                        "answer": "X-ray crystallography"
                    },
                    {
                        "question": "What was 'Photo 51'?",
                        "options": ["A model of DNA", "An image of a cell nucleus", "An X-ray image showing DNA's helical shape", "A microscope photo of RNA"],
                        "answer": "An X-ray image showing DNA's helical shape"
                    },
                    {
                        "question": "Who took Photo 51?",
                        "options": ["James Watson", "Francis Crick", "Maurice Wilkins", "Rosalind Franklin"],
                        "answer": "Rosalind Franklin"
                    },
                    {
                        "question": "Which scientist showed Photo 51 to James Watson without Franklin’s knowledge?",
                        "options": ["Francis Crick", "Erwin Chargaff", "Maurice Wilkins", "Linus Pauling"],
                        "answer": "Maurice Wilkins"
                    },
                    {
                        "question": "What type of structure did Watson and Crick propose for DNA?",
                        "options": ["Linear chain", "Single helix", "Double helix", "Triple helix"],
                        "answer": "Double helix"
                    },
                    {
                        "question": "Which scientist’s work provided critical measurements that guided Watson and Crick’s model?",
                        "options": ["Erwin Chargaff", "Rosalind Franklin", "Maurice Wilkins", "Barbara McClintock"],
                        "answer": "Rosalind Franklin"
                    },
                    {
                        "question": "Which three scientists received the Nobel Prize in 1962 for the discovery of DNA's structure?",
                        "options": ["Watson, Crick, and Franklin", "Watson, Crick, and Wilkins", "Crick, Wilkins, and Chargaff", "Franklin, Wilkins, and Watson"],
                        "answer": "Watson, Crick, and Wilkins"
                    },
                    {
                        "question": "Why did Rosalind Franklin not receive the Nobel Prize for her contributions?",
                        "options": ["She declined it", "She wasn’t credited at the time", "She was not involved", "She was disqualified for misconduct"],
                        "answer": "She wasn’t credited at the time"
                    },
                    {
                        "question": "What structural feature of DNA was revealed by Photo 51?",
                        "options": ["Double helix", "Triple helix", "Zigzag chain", "Protein coating"],
                        "answer": "Double helix"
                    },
                    {
                        "question": "What important base-pairing rule was used in determining the structure of DNA?",
                        "options": ["A pairs with G, T pairs with C", "A pairs with T, C pairs with G", "T pairs with G, C pairs with A", "C pairs with T, A pairs with G"],
                        "answer": "A pairs with T, C pairs with G"
                    },
                    {
                        "question": "Which base pairs form with two hydrogen bonds?",
                        "options": ["G and C", "A and T", "C and T", "A and G"],
                        "answer": "A and T"
                    },
                    {
                        "question": "Which base pairs form with three hydrogen bonds?",
                        "options": ["A and T", "G and C", "A and C", "T and G"],
                        "answer": "G and C"
                    },
                    {
                        "question": "What ethical issue surrounds the use of Photo 51?",
                        "options": ["Data was stolen from a journal", "Franklin was not credited for her data", "It was fabricated", "It was misinterpreted by Crick"],
                        "answer": "Franklin was not credited for her data"
                    },
                    {
                        "question": "Which scientist worked in the same lab as Rosalind Franklin?",
                        "options": ["James Watson", "Francis Crick", "Maurice Wilkins", "Linus Pauling"],
                        "answer": "Maurice Wilkins"
                    },
                    {
                        "question": "What scientific field was crucial for discovering the shape of DNA?",
                        "options": ["Genomics", "Electrophoresis", "X-ray crystallography", "PCR"],
                        "answer": "X-ray crystallography"
                    },
                    {
                        "question": "Which statement best describes Rosalind Franklin's contribution to DNA discovery?",
                        "options": ["She built the first model of DNA", "She discovered RNA", "She produced the X-ray image that revealed the helix", "She isolated DNA from cells"],
                        "answer": "She produced the X-ray image that revealed the helix"
                    },
                    {
                        "question": "Watson and Crick used data from Franklin’s research to:",
                        "options": ["Disprove the helix model", "Confirm the role of proteins", "Build their DNA model", "Build an RNA model"],
                        "answer": "Build their DNA model"
                    },
                    {
                        "question": "Which scientist suggested the A=T and C=G base pairing rule?",
                        "options": ["Watson", "Franklin", "Chargaff", "Wilkins"],
                        "answer": "Chargaff"
                    },
                    {
                        "question": "What is the main reason Franklin’s role was underrecognized for many years?",
                        "options": ["She withdrew from the project", "She destroyed her data", "She died before receiving full credit", "She worked in another country"],
                        "answer": "She died before receiving full credit"
                    }
                ],
                "blurting": [html.Div([
                                html.Ul([
                                    html.Li("James Watson: co-discovered the double-helix structure DNA"), 
                                    html.Li("Francis Crick: co-discovered the double-helix structure of DNA"),
                                    html.Li("Rosalind Franklin: produced critical X-ray diffraction images of DNA, in particular, Photo 51"),
                                    html.Li("Maurice Wilkins: shared Rosalind Franklin's work with James Watson and Francis Crick")
                                ])
                            ])],
                "feynman": [html.Div([
                                html.Ul([
                                    html.Li("James Watson: co-discovered the double-helix structure DNA"), 
                                    html.Li("Francis Crick: co-discovered the double-helix structure of DNA"),
                                    html.Li("Rosalind Franklin: produced critical X-ray diffraction images of DNA, in particular, Photo 51"),
                                    html.Li("Maurice Wilkins: shared Rosalind Franklin's work with James Watson and Francis Crick")
                                ])
                            ])]
            }, 
            "q15": {
                "question": html.P("Explain how two critical pieces of data led scientists to construct the DNA double helix model."),
                "overview": html.Div([
                    html.P("Two key pieces of evidence led to the discovery of the DNA double helix structure:"),
                    html.Ul([
                        html.Li([html.Strong("Chargaff's Rule: "), "Biochemist Erwin Chargaff found that in any DNA sample, the amount of adenine (A) equals the amount of thymine (T), and the amount of guanine (G) equals the amount of cytosine (C). This hinted at base pairing"]),
                        html.Li([html.Strong("X-ray Diffraction Image (Photo 51): "), "Rosalind Franklin's X-ray image revealed an 'X' pattern that suggested DNA has a helical (spiral) shape with repeating, regular features"])
                    ]),
                    html.P("These data were crucial for Watson and Crick, who used them to develop the correct model of DNA: a double helix with complementary base pairing.")
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Chargaff's Rule (Base Pairing Data):")]),
                    html.P("In the 1940s, Erwin Chargaff analyzed DNA from many organisms and consistently found that:"),
                    html.Ul([
                        html.Li("The proportion of adenine (A) always equaled thymine (T)"),
                        html.Li("The proportion of guanine (G) always equaled cytosine (C)")
                    ]),
                    html.P("This ratio was not random. Chargaff's findings suggested a specific pairing relationship between these nitrogenous bases. Though the exact structural reason was unknown at the time, this observation pointed to complementary base pairing, which was later essential for understanding how the two strands of DNA fit together."),
                    html.P([html.Strong("X-ray Diffraction (Rosalind Franklin's Photo 51)")]),
                    html.P("Rosalind Franklin and Maurice Wilkins were using X-ray crystallography to study DNA fibers. Franklin's Photo 51 showed an X-ray pattern, which indicated:"),
                    html.Ul([
                        html.Li("DNA had a helical shape"),
                        html.Li("The helix had two strands (a double helix)"),
                        html.Li("There was regular spacing of about 3.4 Angstrom per base and a full t3ist every 34 Angstroms, suggesting approximately 10 base pairs per turn")
                    ]),
                    html.P("James Watson saw this image (without Rosalind Franklin's knowledge or consent) and it gave him and Francis Crick the critical insight that DNA was not just a spiral, but a double helix with consistent geometry."),
                    html.P(""),
                    html.P("Together, Chargaff's rules explained the base pairing, and Franklin's X-ray diffraction image revealed the helical structure. These two pieces of data gave Watson and Crick the information they needed to propose the correct double helix model of DNA in 1953.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter4question6.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Who are the two scientists most often credited with discovering the double-helix structure of DNA?",
                        "options": ["Watson and Wilkins", "Franklin and Crick", "Watson and Crick", "Wilkins and Franklin"],
                        "answer": "Watson and Crick"
                    },
                    {
                        "question": "What critical technique did Rosalind Franklin use to study DNA structure?",
                        "options": ["Gel electrophoresis", "Chromatography", "X-ray crystallography", "DNA sequencing"],
                        "answer": "X-ray crystallography"
                    },
                    {
                        "question": "What was 'Photo 51'?",
                        "options": ["A model of DNA", "An image of a cell nucleus", "An X-ray image showing DNA's helical shape", "A microscope photo of RNA"],
                        "answer": "An X-ray image showing DNA's helical shape"
                    },
                    {
                        "question": "Which scientist took Photo 51?",
                        "options": ["James Watson", "Francis Crick", "Maurice Wilkins", "Rosalind Franklin"],
                        "answer": "Rosalind Franklin"
                    },
                    {
                        "question": "What did Chargaff's rules show about the composition of DNA?",
                        "options": [
                            "DNA has more purines than pyrimidines",
                            "DNA contains equal amounts of A and T, and equal amounts of G and C",
                            "DNA bases are randomly arranged",
                            "DNA is made only of purines"
                        ],
                        "answer": "DNA contains equal amounts of A and T, and equal amounts of G and C"
                    },
                    {
                        "question": "Which base pairs with cytosine in DNA?",
                        "options": ["Adenine", "Thymine", "Uracil", "Guanine"],
                        "answer": "Guanine"
                    },
                    {
                        "question": "Which base pairs with adenine in DNA?",
                        "options": ["Uracil", "Guanine", "Thymine", "Cytosine"],
                        "answer": "Thymine"
                    },
                    {
                        "question": "What shape does DNA take in its natural form?",
                        "options": ["Triple helix", "Zigzag", "Double helix", "Ladder with no twist"],
                        "answer": "Double helix"
                    },
                    {
                        "question": "Which of the following scientists received the Nobel Prize for the discovery of DNA’s structure?",
                        "options": ["Watson, Crick, and Franklin", "Watson, Crick, and Wilkins", "Watson, Crick, and Chargaff", "Franklin, Wilkins, and Chargaff"],
                        "answer": "Watson, Crick, and Wilkins"
                    },
                    {
                        "question": "Why didn’t Rosalind Franklin receive the Nobel Prize for DNA structure?",
                        "options": ["She declined it", "She was not involved in the discovery", "She passed away before it was awarded", "She refused to share her data"],
                        "answer": "She passed away before it was awarded"
                    },
                    {
                        "question": "Which scientist's data was used without permission in building the DNA model?",
                        "options": ["Erwin Chargaff", "Maurice Wilkins", "Rosalind Franklin", "Francis Crick"],
                        "answer": "Rosalind Franklin"
                    },
                    {
                        "question": "How many strands make up the DNA molecule?",
                        "options": ["One", "Two", "Three", "Four"],
                        "answer": "Two"
                    },
                    {
                        "question": "What holds the two DNA strands together?",
                        "options": ["Ionic bonds", "Covalent bonds", "Hydrogen bonds between bases", "Phosphodiester bonds"],
                        "answer": "Hydrogen bonds between bases"
                    },
                    {
                        "question": "Which of the following best describes the direction of the two DNA strands?",
                        "options": ["Parallel", "Antiparallel", "Crossing", "Unidirectional"],
                        "answer": "Antiparallel"
                    },
                    {
                        "question": "How many base pairs occur in one full twist of the DNA double helix?",
                        "options": ["5", "10", "20", "100"],
                        "answer": "10"
                    },
                    {
                        "question": "What is the distance between each base pair in the DNA helix?",
                        "options": ["0.34 nanometers", "3.4 nanometers", "10 nanometers", "34 nanometers"],
                        "answer": "0.34 nanometers"
                    },
                    {
                        "question": "What is the full helical turn length of DNA?",
                        "options": ["1 nanometer", "3.4 nanometers", "10 nanometers", "34 nanometers"],
                        "answer": "3.4 nanometers"
                    },
                    {
                        "question": "Which scientist discovered the base-pairing rules?",
                        "options": ["James Watson", "Erwin Chargaff", "Rosalind Franklin", "Francis Crick"],
                        "answer": "Erwin Chargaff"
                    },
                    {
                        "question": "What is the term for DNA’s consistent diameter and twist?",
                        "options": ["Uniform stacking", "Double bond spacing", "Helical symmetry", "Base-pair regularity"],
                        "answer": "Helical symmetry"
                    },
                    {
                        "question": "Which scientist built physical models of DNA to test possible structures?",
                        "options": ["Erwin Chargaff", "Maurice Wilkins", "James Watson and Francis Crick", "Rosalind Franklin"],
                        "answer": "James Watson and Francis Crick"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Two key pieces of evidence led to the discovery of the DNA double helix structure:"),
                                html.Ul([
                                    html.Li([html.Strong("Chargaff's Rule: "), "Biochemist Erwin Chargaff found that in any DNA sample, the amount of adenine (A) equals the amount of thymine (T), and the amount of guanine (G) equals the amount of cytosine (C). This hinted at base pairing"]),
                                    html.Li([html.Strong("X-ray Diffraction Image (Photo 51): "), "Rosalind Franklin's X-ray image revealed an 'X' pattern that suggested DNA has a helical (spiral) shape with repeating, regular features"])
                                ]),
                                html.P("These data were crucial for Watson and Crick, who used them to develop the correct model of DNA: a double helix with complementary base pairing.")
                            ])],
                "feynman": [html.Div([
                                html.H4("🧬 Feynman-Style Summary: How Scientists Figured Out the DNA Double Helix"),
                                html.P("Imagine you're trying to figure out what a mysterious rope ladder looks like, but you can’t see the whole thing—only some clues. That’s what scientists were doing with DNA."),
                                
                                html.H5("🔑 Clue 1: The Base Puzzle (Chargaff’s Rules)"),
                                html.P([
                                    "A scientist named ", html.Strong("Erwin Chargaff"), " looked at DNA from many organisms and noticed something consistent:"
                                ]),
                                html.Ul([
                                    html.Li("The amount of adenine (A) always equaled the amount of thymine (T)"),
                                    html.Li("The amount of guanine (G) always equaled the amount of cytosine (C)")
                                ]),
                                html.P("That’s strange, like always finding equal numbers of puzzle pieces in matching colors. This suggested that A pairs with T and G pairs with C."),

                                html.H5("🔑 Clue 2: The X-ray Picture (Photo 51)"),
                                html.P([
                                    "The second clue came from ", html.Strong("Rosalind Franklin"), ", who used X-ray crystallography to take a photo of DNA. The image, called ",
                                    html.Em("Photo 51"), ", showed a large X pattern — a clue that DNA had a spiral (helical) shape."
                                ]),
                                html.P("The photo also showed regular spacing and repeated features, suggesting DNA had a consistent structure with two strands."),

                                html.H5("💡 Putting It All Together"),
                                html.P("Watson and Crick used these clues:"),
                                html.Ul([
                                    html.Li(html.Strong("Base pairing"), ": A always pairs with T, and G with C"),
                                    html.Li(html.Strong("Helical structure"), ": DNA is a twisted ladder (double helix)")
                                ]),
                                html.P("They built the model of DNA as a double helix: two strands coiled around each other, held together by specific base pairs like rungs on a ladder."),
                                html.P(html.Strong("That’s how scientists figured out the structure of life’s instruction manual."))
                            ])]
            },
            "q16": {
                "question": html.P("Be able to discuss what the “central dogma of molecular biology” means."),
                "overview": html.Div([
                    html.P("The central dogma of biology refers to the creation of proteins, beginning with DNA. In short, the process is DNA =(transcription)=> mRNA (messenger RNA) =(translation)=> protein")
                ]), 
                "deep_dive": html.Div([
                    html.P("Gene expression forms specific polypeptides with two steps:"),
                    html.Ul([
                        html.Li([html.Strong("Transcription: "), "copies information from the DNA sequence (from a gene) to a complementary RNA sequence (messenger RNA; mRNA)"]),
                        html.Li([html.Strong("Translation: "), "converts that RNA sequence into the amino acid sequence of a polypeptide"])
                    ]),
                    html.P("This makes up the central dogma of molecular biology."),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/central dogma.png", style = {'marginRight':'40px', 'width':'750px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/translation/a/intro-to-gene-expression-central-dogma", target = "_blank")])
                        ]
                    ),
                    html.Br(),
                    html.P(["The ", html.Strong("Messenger Hypothesis "), "states that messenger RNA (mRNA) forms as a complementary copy of one DNA strand in a gene. mRNA will travel from the nucleus to the cytoplasm, carrying information as codons. This process is transcription and the mRNA copy is a transcript."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/messenger hypothesis.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://studymind.co.uk/notes/messenger-rna/", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Khan Academy Medicine: Central Dogma of Molecular Biology", href = "https://www.youtube.com/watch?v=KIvBn6gfRgY&t=3s&pp=ygUYY2VudHJhbCBkb2dtYSBvZiBiaW9sb2d5", target = "_blank")]),
                        html.Li([html.A("DNA Learning Center: The Central Dogma of Biology", href = "https://www.youtube.com/watch?v=9kOGOY7vthk&t=4s&pp=ygUYY2VudHJhbCBkb2dtYSBvZiBiaW9sb2d5", target = "_blank")]),
                        html.Li([html.A("BioCASTS: Central Dogma of Biology", href = "https://www.youtube.com/watch?v=FZHs-TZtWKQ&pp=ygUYY2VudHJhbCBkb2dtYSBvZiBiaW9sb2d5", target = "_blank")]),
                        html.Li([html.A("Khan Academy Medicine: Central Dogma - Revisited", href = "https://www.youtube.com/watch?v=Yv94eGD7cUU&pp=ygUYY2VudHJhbCBkb2dtYSBvZiBiaW9sb2d5", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide2.jpg")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does the central dogma of molecular biology describe?",
                        "options": [
                            "How proteins are broken down",
                            "The flow of genetic information from DNA to RNA to protein",
                            "The replication of DNA only",
                            "The process of cell division"
                        ],
                        "answer": "The flow of genetic information from DNA to RNA to protein"
                    },
                    {
                        "question": "What is the first step of gene expression?",
                        "options": ["Translation", "Transcription", "Replication", "Mutation"],
                        "answer": "Transcription"
                    },
                    {
                        "question": "During transcription, what molecule is synthesized?",
                        "options": ["DNA", "mRNA", "tRNA", "Protein"],
                        "answer": "mRNA"
                    },
                    {
                        "question": "Where does transcription occur in eukaryotic cells?",
                        "options": ["Cytoplasm", "Mitochondria", "Nucleus", "Ribosome"],
                        "answer": "Nucleus"
                    },
                    {
                        "question": "What enzyme is responsible for synthesizing mRNA during transcription?",
                        "options": ["DNA polymerase", "RNA polymerase", "Ligase", "Helicase"],
                        "answer": "RNA polymerase"
                    },
                    {
                        "question": "What is the complementary RNA base to the DNA base adenine?",
                        "options": ["Thymine", "Uracil", "Guanine", "Cytosine"],
                        "answer": "Uracil"
                    },
                    {
                        "question": "What is the mRNA sequence called that carries genetic information from DNA?",
                        "options": ["Transcript", "Template", "Codon", "Anticodon"],
                        "answer": "Transcript"
                    },
                    {
                        "question": "Where does translation occur in the cell?",
                        "options": ["Nucleus", "Ribosome", "Golgi apparatus", "Endoplasmic reticulum"],
                        "answer": "Ribosome"
                    },
                    {
                        "question": "What molecules bring amino acids to the ribosome during translation?",
                        "options": ["mRNA", "tRNA", "rRNA", "DNA"],
                        "answer": "tRNA"
                    },
                    {
                        "question": "What is a codon?",
                        "options": [
                            "A three-nucleotide sequence on mRNA that codes for an amino acid",
                            "A type of protein",
                            "An enzyme that makes RNA",
                            "A DNA replication origin"
                        ],
                        "answer": "A three-nucleotide sequence on mRNA that codes for an amino acid"
                    },
                    {
                        "question": "What signals the end of translation?",
                        "options": ["Start codon", "Stop codon", "Promoter", "Terminator"],
                        "answer": "Stop codon"
                    },
                    {
                        "question": "Which of the following is NOT a step in gene expression?",
                        "options": ["Replication", "Transcription", "Translation", "RNA processing"],
                        "answer": "Replication"
                    },
                    {
                        "question": "What is the role of messenger RNA (mRNA)?",
                        "options": [
                            "To carry amino acids to the ribosome",
                            "To form the ribosome structure",
                            "To carry genetic information from DNA to the ribosome",
                            "To replicate DNA"
                        ],
                        "answer": "To carry genetic information from DNA to the ribosome"
                    },
                    {
                        "question": "Which nitrogenous base is found in RNA but NOT in DNA?",
                        "options": ["Adenine", "Thymine", "Uracil", "Guanine"],
                        "answer": "Uracil"
                    },
                    {
                        "question": "What happens during RNA processing in eukaryotic cells?",
                        "options": [
                            "Introns are removed and exons are joined",
                            "DNA is replicated",
                            "Proteins are synthesized",
                            "mRNA is translated into protein"
                        ],
                        "answer": "Introns are removed and exons are joined"
                    },
                    {
                        "question": "Which molecule serves as the template for mRNA synthesis?",
                        "options": ["mRNA", "tRNA", "DNA", "Protein"],
                        "answer": "DNA"
                    },
                    {
                        "question": "What term describes the sequence of three nucleotides on tRNA that pairs with the mRNA codon?",
                        "options": ["Anticodon", "Codon", "Promoter", "Exon"],
                        "answer": "Anticodon"
                    },
                    {
                        "question": "Which process converts the mRNA sequence into a polypeptide chain?",
                        "options": ["Replication", "Transcription", "Translation", "Splicing"],
                        "answer": "Translation"
                    },
                    {
                        "question": "What determines the sequence of amino acids in a protein?",
                        "options": ["DNA sequence", "RNA sequence", "mRNA codons", "All of the above"],
                        "answer": "All of the above"
                    },
                    {
                        "question": "Why is the central dogma important in biology?",
                        "options": [
                            "It explains how cells divide",
                            "It describes how genetic information is used to make proteins",
                            "It explains DNA replication only",
                            "It describes how mutations occur"
                        ],
                        "answer": "It describes how genetic information is used to make proteins"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The central dogma of biology refers to the creation of proteins, beginning with DNA. In short, the process is DNA =(transcription)=> mRNA (messenger RNA) =(translation)=> protein")
                            ])],
                "feynman": [html.Div([
                    html.H4("🧬 Feynman-Style Summary: The Central Dogma of Molecular Biology"),
                    html.P("Imagine your DNA is a cookbook full of recipes. But you don’t want to carry the whole book to the kitchen—you just copy one recipe onto a sticky note and bring that instead. That’s basically what your cells do."),
                    
                    html.H5("📝 Step 1: Transcription — Copy the Recipe"),
                    html.P("Your cell picks one gene (one recipe) from the DNA and makes a copy of it using RNA. This copy is called messenger RNA, or mRNA."),
                    html.P("It’s like writing down just one recipe on a sticky note so you don’t ruin the original book."),

                    html.H5("🍳 Step 2: Translation — Cook the Recipe"),
                    html.P("Next, the cell uses the mRNA to build a protein, kind of like following the recipe to cook a meal."),
                    html.P("Each 3-letter 'word' on the mRNA (called a codon) tells the cell which amino acid to add next. These amino acids link together to form a protein."),

                    html.H5("🔁 The Big Picture"),
                    html.P([
                        "This is the central dogma: ", html.Strong("DNA → RNA → Protein"), ". ",
                        "It’s how instructions stored in your genes become the proteins that run your cells and make you who you are."
                    ])
                ])]
            },
            "q17": {
                "question": html.P("Know the three major classes of RNA and what is the central role for each type."),
                "overview": html.Div([
                    html.P("There are three major classes of RNA:"),
                    html.Ul([
                        html.Li([html.Strong("Messenger RNA (mRNA): "), "carries a copy of a DNA sequence to the site of protein synthesis at the ribosome"]),
                        html.Li([html.Strong("Transfer RNA (tRNA): "), "carries amino acids for polypeptide assembly"]),
                        html.Li([html.Strong("Ribosomal RNA (rRNA): "), "catalyzes peptide bonds and provides a 'workbench' for the protein to be assembled"])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.Div([
                        html.H4("The Three Major Classes of RNA and Their Roles"),
                        
                        html.P("In gene expression, RNA molecules play essential and distinct roles. There are three major types of RNA—"
                            "messenger RNA (mRNA), transfer RNA (tRNA), and ribosomal RNA (rRNA)—each with specialized functions "
                            "that work together to synthesize proteins."),
                        
                        html.H5("Messenger RNA (mRNA): The Genetic Messenger"),
                        html.P("mRNA serves as the intermediary between DNA and protein synthesis. During transcription, a gene’s DNA "
                            "sequence is copied into a complementary mRNA strand. This mRNA molecule carries the genetic code from the "
                            "nucleus (in eukaryotes) to the ribosomes in the cytoplasm, where proteins are made. The mRNA sequence is "
                            "organized into codons, which are three-nucleotide “words” that specify particular amino acids during translation."),
                        
                        html.Div(
                            style = {'display':'flex', 'alignItems':'center'},
                            children = [
                                html.Img(src = "/assets/mRNA.png", style = {'marginRight':'40px'}),
                                html.Div(["Image from ", html.A("here", href = "https://www.researchgate.net/figure/Transcription-of-messenger-RNA-from-1_fig5_226845518", target = "_blank")])
                            ]
                        ), 

                        html.H5("Transfer RNA (tRNA): The Adaptor and Amino Acid Carrier"),
                        html.P("tRNA acts as the adaptor molecule that translates the nucleotide language of mRNA into the amino acid "
                            "language of proteins. Each tRNA has three critical roles:"),
                        html.Ul([
                            html.Li("Amino acid attachment: At its 3’ end, the tRNA covalently binds a specific amino acid, a process called “charging” the tRNA."),
                            html.Li("mRNA codon recognition: The tRNA contains an anticodon at its midpoint, a sequence of three nucleotides that base-pairs specifically with a complementary mRNA codon."),
                            html.Li("Ribosome interaction: The tRNA binds within the ribosome, positioning the attached amino acid for incorporation into the growing polypeptide chain.")
                        ]),
                        html.P("The 3D shape of tRNA is stabilized by internal hydrogen bonds, allowing it to fit precisely into the ribosome "
                            "and pair accurately with the mRNA. This adaptor function ensures that the genetic code is faithfully "
                            "translated into the correct amino acid sequence."),
                        
                        html.Div(
                            style = {'display':'flex', 'alignItems':'center'},
                            children = [
                                html.Img(src = "/assets/tRNA.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                                html.Div(["Image from ", html.A("here", href = "https://www.youtube.com/watch?v=aOE8qDPh4ZQ", target = "_blank")])
                            ]
                        ), 

                        html.H5("Ribosomal RNA (rRNA): The Catalytic and Structural Core"),
                        html.P("rRNA forms the main structural and functional components of the ribosome, the cellular machine that synthesizes proteins. "
                            "rRNA molecules provide a scaffold that holds ribosomal proteins in place and catalyze the formation of peptide bonds between amino acids. "
                            "This catalytic activity means that rRNA is not just structural but also acts as a ribozyme—an RNA molecule with enzymatic function. "
                            "The ribosome’s ability to link amino acids efficiently depends heavily on rRNA, making it central to the translation process."),
                        
                        html.Div(
                            style = {'display':'flex', 'alignItems':'center'},
                            children = [
                                html.Img(src = "/assets/rRNA.png", style = {'marginRight':'40px', 'width':'600px'}),
                                html.Div(["Image from ", html.A("here", href = "https://www.geeksforgeeks.org/biology/ribosomes-diagram/", target = "_blank")])
                            ]
                        ), 

                        html.H5("Summary"),
                        html.P("Together, these three RNA types coordinate the accurate transfer of genetic information from DNA to functional proteins:"),
                        html.Ul([
                            html.Li("mRNA brings the instructions,"),
                            html.Li("tRNA brings the building blocks (amino acids) and reads the code,"),
                            html.Li("rRNA builds the machinery and catalyzes protein assembly.")
                        ]),

                        html.Div(
                            style = {'display':'flex', 'alignItems':'center'},
                            children = [
                                html.Img(src = "/assets/RNA types.png", style = {'marginRight':'40px', 'width':'600px'}),
                                html.Div(["Image from ", html.A("here", href = "https://www.yourgenome.org/theme/what-is-rna/", target = "_blank")])
                            ]
                        ), 

                        html.P("Without the interplay of these RNAs, the essential process of gene expression and protein synthesis could not occur."),
                        html.P([html.Strong("Helpful Outside Resources:")]),
                        html.Ul([
                            html.Li([html.A("2 Minute Classroom: mRNA, tRNA, and rRNA Function", href = "https://www.youtube.com/watch?v=1THyMOk3WU0&pp=ygUNdHlwZXMgb2YgUk5BIA%3D%3D", target = "_blank")]),
                            html.Li([html.A("Beverly Biology: Types of RNA (mRNA, tRNA, rRNA)", href = "https://www.youtube.com/watch?v=B4YbNm06bD8&pp=ygUNdHlwZXMgb2YgUk5BIA%3D%3D", target = "_blank")]),
                            html.Li([html.A("Medicosis Perfectionalis: RNA (mRNA, tRNA, rRNA) and Genetic Mutations", href = "https://www.youtube.com/watch?v=UxCTmzserEU&pp=ygUNdHlwZXMgb2YgUk5BIA%3D%3D", target = "_blank")]),
                            html.Li([html.A("Bio Scholar: RNA Structure, Function, and Types (PRimary Structure of RNA)", href = "https://www.youtube.com/watch?v=1H_h26YqP0s&pp=ygUNdHlwZXMgb2YgUk5BIA%3D%3D", target = "_blank")])
                        ])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide3.jpg"), 
                    html.Img(src = "/assets/Chapter14/Slide4.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide15.jpg"),  
                    html.Img(src = "/assets/Chapter14/Slide16.jpg"), 
                    html.Img(src = "/assets/Chapter14/Slide18.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Which type of RNA carries a copy of the DNA sequence to the ribosome?",
                        "options": ["rRNA", "tRNA", "mRNA", "snRNA"],
                        "answer": "mRNA"
                    },
                    {
                        "question": "What is the central function of tRNA?",
                        "options": ["Carries genetic information", "Catalyzes peptide bond formation", "Transports amino acids to the ribosome", "Replicates DNA"],
                        "answer": "Transports amino acids to the ribosome"
                    },
                    {
                        "question": "Which type of RNA catalyzes peptide bond formation?",
                        "options": ["mRNA", "rRNA", "tRNA", "snRNA"],
                        "answer": "rRNA"
                    },
                    {
                        "question": "Where on the tRNA does the amino acid attach?",
                        "options": ["5' end", "Middle loop", "Anticodon site", "3' end"],
                        "answer": "3' end"
                    },
                    {
                        "question": "Which part of tRNA base pairs with mRNA codons?",
                        "options": ["Amino acid attachment site", "Anticodon", "5' cap", "Poly-A tail"],
                        "answer": "Anticodon"
                    },
                    {
                        "question": "What is the role of mRNA in translation?",
                        "options": ["Transfers amino acids", "Catalyzes reactions", "Provides the code for protein synthesis", "Forms peptide bonds"],
                        "answer": "Provides the code for protein synthesis"
                    },
                    {
                        "question": "Which RNA type has enzymatic activity?",
                        "options": ["mRNA", "rRNA", "tRNA", "snRNA"],
                        "answer": "rRNA"
                    },
                    {
                        "question": "What structure allows tRNA to fold into its 3D shape?",
                        "options": ["Ionic bonding", "Hydrogen bonding", "Disulfide bridges", "Peptide bonds"],
                        "answer": "Hydrogen bonding"
                    },
                    {
                        "question": "What makes a tRNA molecule 'charged'?",
                        "options": ["It binds to a ribosome", "It forms hydrogen bonds", "It binds to an mRNA codon", "It binds to an amino acid"],
                        "answer": "It binds to an amino acid"
                    },
                    {
                        "question": "Which RNA acts as an adaptor between mRNA codons and amino acids?",
                        "options": ["mRNA", "rRNA", "tRNA", "siRNA"],
                        "answer": "tRNA"
                    },
                    {
                        "question": "What is the function of ribosomal RNA (rRNA) in the ribosome?",
                        "options": ["Reads mRNA", "Binds amino acids", "Transfers genetic material", "Catalyzes peptide bond formation"],
                        "answer": "Catalyzes peptide bond formation"
                    },
                    {
                        "question": "How does tRNA contribute to translation?",
                        "options": ["It creates peptide bonds", "It carries codons", "It brings amino acids and matches them with codons", "It transcribes DNA"],
                        "answer": "It brings amino acids and matches them with codons"
                    },
                    {
                        "question": "Which RNA type is synthesized during transcription?",
                        "options": ["rRNA", "tRNA", "mRNA", "All of the above"],
                        "answer": "All of the above"
                    },
                    {
                        "question": "Which molecule ensures that the correct amino acid is added during translation?",
                        "options": ["mRNA", "tRNA", "rRNA", "DNA"],
                        "answer": "tRNA"
                    },
                    {
                        "question": "The anticodon is located on which molecule?",
                        "options": ["mRNA", "rRNA", "DNA", "tRNA"],
                        "answer": "tRNA"
                    },
                    {
                        "question": "Which RNA provides the instructions for protein synthesis?",
                        "options": ["rRNA", "mRNA", "tRNA", "snRNA"],
                        "answer": "mRNA"
                    },
                    {
                        "question": "How many primary functions does tRNA have?",
                        "options": ["One", "Two", "Three", "Four"],
                        "answer": "Three"
                    },
                    {
                        "question": "Which of the following is NOT a function of tRNA?",
                        "options": ["Associates with mRNA", "Binds amino acids", "Creates mRNA", "Interacts with ribosomes"],
                        "answer": "Creates mRNA"
                    },
                    {
                        "question": "Which type of RNA makes up the structural and enzymatic core of the ribosome?",
                        "options": ["mRNA", "tRNA", "rRNA", "snRNA"],
                        "answer": "rRNA"
                    },
                    {
                        "question": "Which of the following RNAs does NOT directly participate in peptide bond formation?",
                        "options": ["mRNA", "rRNA", "tRNA", "All of them participate"],
                        "answer": "mRNA"
                    }
                ],
                "blurting": [html.Div([
                                html.P("There are three major classes of RNA:"),
                                html.Ul([
                                    html.Li([html.Strong("Messenger RNA (mRNA): "), "carries a copy of a DNA sequence to the site of protein synthesis at the ribosome"]),
                                    html.Li([html.Strong("Transfer RNA (tRNA): "), "carries amino acids for polypeptide assembly"]),
                                    html.Li([html.Strong("Ribosomal RNA (rRNA): "), "catalyzes peptide bonds and provides a 'workbench' for the protein to be assembled"])
                                ])
                            ])],
                "feynman": [html.Div([
                                html.H4("The Three Major Classes of RNA"),
                                html.P("Think of RNA as the team that helps turn DNA’s instructions into proteins."),
                                
                                html.H5("Messenger RNA (mRNA)"),
                                html.P("mRNA is like a messenger that carries a copy of a DNA recipe from the nucleus to the ribosome, where proteins are made."),
                                
                                html.H5("Transfer RNA (tRNA)"),
                                html.P("tRNA is the adaptor that brings the right amino acid to the ribosome by matching its anticodon with the mRNA’s codon."),
                                html.P("It looks like a tiny folded molecule with a special site to hold an amino acid."),
                                
                                html.H5("Ribosomal RNA (rRNA)"),
                                html.P("rRNA is the builder and catalyst in the ribosome. It helps link amino acids together to form a protein and gives the ribosome its shape."),
                                
                                html.P("Together, these RNAs work as a team to read the genetic code and build proteins that keep cells alive.")
                            ])]
            },
            "q18": {
                "question": html.P("Be familiar with the necessary components of transcription and be able to explain each of the main transcriptional phases (initiation, elongation, and termination)."),
                "overview": html.Div([
                    html.P("The necessary components of transcription are:"),
                    html.Ul([
                        html.Li("A DNA template for base pairing (one of the two strands of DNA)"), 
                        html.Li("Nucleotside triphosphates (ATP, GTP, CTP, UTP)"), 
                        html.Li("RNA polymerase enzyme")
                    ]),
                    html.P(["An ", html.Strong("RNA polymerase enzyme"), " catalyzes the synthesis of mRNA. RNA polymerases are processive (meaning that a single enzyme-template binding results in the polymerization of hundreds of RNA bases), does not need primers, and lacks a proofreading function. In contrast, DNA polymerases do require primers and have a proofreading function."]),
                    html.P("The three steps of transcription are:"), 
                    html.Ul([
                        html.Li([html.Strong("Initiation: "), "RNA polymerase binds to the promoter (a special sequence of DNA that tells the RNA polymerase where to bind and which strand of DNA to transcribe). The promoter contains a site called the initiator site."]),
                        html.Li([html.Strong("Elongation: "), "RNA polymerase unwinds the DNA about 10 base pairs at a time and reads the template in a 3' to 5' direction. The RNA transcript is made antiparallel to the DNA strand and nucleotides are added to the 3' end."]),
                        html.Li([html.Strong("Termination: "), "Termination begins with the RNA polymerase reaches a specific DNA sequence called the terminator. For some genes, the RNA transcript will just fall away from the DNA strand and the RNA polymerase, but for others, a helper protein will pull the RNA transcript away."])
                    ])
                ]), 
                "deep_dive": html.Div([
                    html.P([html.Strong("Key Components Required for Transcription:")]),
                    html.Ul([
                        html.Li(html.Strong("DNA Template: "), "Only one of the two DNA strands is used as a template for RNA synthesis. The template strand is read in the 3' to 5' direction so that the RNA can be built in the 5' to 3' direction, where new nucleotides are added to the 3' end of the RNA transcript"),
                        html.Li(html.Strong("Nucleoside Triphosphates (NTPs): "), "These are the building blocks of RNA and include ATP, CTP, GTP, and UTP. Each nucleotide added to the RNA strand releases two phosphates, which provides energy for the reaction"),
                        html.Li(html.Strong("RNA Polymerase: "), "This is the enzyme which catalyzes RNA synthesis by linking together NTPs. It is processive, meaning that it stays attached to DNA and can add hundreds of nucleotides in one go. RNA polymerase does not need a primer to start synthesis, and unlike DNA polymerase, it lacks proofreading ability, so occassional errors in transcription may occur.")
                    ]),
                    html.P("The errors that may occur during transcription are generally not problematic or harmful because RNA has a very short life span in the cell."),
                    html.P([html.Strong("The Phases of Transcription:")]),
                    html.Ul([html.Li([html.Strong("Initiation: "), "Begins with RNA polymerase binds to a promoter, which is a specific DNA sequence located at the start of a gene. The promoter region includes an initiator site, which tells RNA polymerase where to begin transcription and which strand to use as the template. This phase establishes the correct reading frame and the transcriptional direction"])]), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/initiation.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/transcription-and-rna-processing/a/overview-of-transcription", target = "_blank")])
                        ]
                    ), 

                    html.Ul([html.Li([html.Strong("Elongation: "), "RNA polymerase unwinds the DNA ahead of it about 10 base pairs at a time. It reads the template strand in the 3' to 5' direction. The growing RNA strand (the RNA transcript) is antiparallel to the DNA template and is built 5' to 3', where NTPs are added to the 3' end. No proofreading means that mistakes in base-pairing may occur, but usually have a very minimal impact"])]), 
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/elongation.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/transcription-and-rna-processing/a/overview-of-transcription", target = "_blank")])
                        ]
                    ), 
                    html.Br(),
                    html.Div([
                        html.P(["Remember that the ", html.Strong("template strand "), "is the DNA strand that is being used by RNA polymerase to build the messenger RNA (mRNA) while the ", html.Strong("coding strand "), "is the DNA strand that is not being used. It will have the same nucleotide sequence as the newly built mRNA strand."]),
                        html.P("The coding strand and the template strand are antiparallel and complementary."),
                        html.P("For example:"),
                        html.Ul([
                            html.Li([html.Strong("Coding Strand: 5' - ATG CCG TAA - 3'"), "<- this will match the newly synthesized mRNA except that the T (thymine) will become U (uracil)"]),
                            html.Li([html.Strong("Template Strand: 3' - TAC GGC ATT - 5'"), "<- this is the DNA strand that is used synthesize the mRNA and will therefore be complementary to the newly synthesized mRNA"])
                        ]),
                        html.P("To put it all together:"),
                        html.Div([
                            # Table Header
                            html.Div([
                                html.Div("Strand", style={"width": "25%", "fontWeight": "bold"}),
                                html.Div("Direction", style={"width": "25%", "fontWeight": "bold"}),
                                html.Div("Sequence", style={"width": "50%", "fontWeight": "bold"})
                            ], style={"display": "flex", "borderBottom": "1px solid black", "padding": "8px 0"}),

                            # Coding Strand Row
                            html.Div([
                                html.Div("Coding (DNA)", style={"width": "25%"}),
                                html.Div("5' → 3'", style={"width": "25%"}),
                                html.Div("A T G C C G T A A", style={"width": "50%"})
                            ], style={"display": "flex", "padding": "4px 0"}),

                            # Template Strand Row
                            html.Div([
                                html.Div("Template (DNA)", style={"width": "25%"}),
                                html.Div("3' → 5'", style={"width": "25%"}),
                                html.Div("T A C G G C A T T", style={"width": "50%"})
                            ], style={"display": "flex", "padding": "4px 0"}),

                            # mRNA Row
                            html.Div([
                                html.Div("mRNA", style={"width": "25%"}),
                                html.Div("5' → 3'", style={"width": "25%"}),
                                html.Div("A U G C C G U A A", style={"width": "50%"})
                            ], style={"display": "flex", "padding": "4px 0"})
                        ])
                    ], style = {'border':'1 px solid #ccc',
                                'padding':'15px',
                                'borderRadius':'5px',
                                'backgroundColor':'#ccd5ae',
                                'margin':'10px 0'}),
                    html.Br(),
                    html.Ul([html.Li([html.Strong("Termination: "), "A specific DNA sequence called a terminator signals the end of transcription. In some genes, the new RNA transcript will detach on its own, while in others a helper protein will assist in pulling the transcript away. Once complete, the RNA transcript may go on to be processed (such as capping and splicing), before translation"])]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/termination.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/transcription-and-rna-processing/a/overview-of-transcription", target = "_blank")])
                        ]
                    ), 
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Protein Synthesis", href = "https://www.youtube.com/watch?v=oefAI2x2CQM&t=163s&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("Professor Dave Explains: Transcription and Translation (From DNA to Protein)", href = "https://www.youtube.com/watch?v=bKIpDtJdK8Q&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("The Organic Chemistry Tutor: Transcription and Translation (Protein Synthesis from DNA)", href = "https://www.youtube.com/watch?v=8wAwLwJAGHs&t=2s&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("Nucleus Biology: DNA and RNA - Transcription", href = "https://www.youtube.com/watch?v=YlOqI3PQwjo&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("2 Minute Classroom: Transcription & Translation (From DNA to RNA to Protein)", href = "https://www.youtube.com/watch?v=GZRwQpb_sdQ&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("Khan Academy: Transcription and mRNA Processing", href = "https://www.youtube.com/watch?v=JQIwwJqF5D0&t=1s&pp=ygUNdHJhbnNjcmlwdGlvbtIHCQnBCQGHKiGM7w%3D%3D", target = "_blank")]),
                        html.Li([html.A("Crash Course: How mRNA Helped Save Lives", href = "https://www.youtube.com/watch?v=j6YaOqKORYY&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide4.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide5.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide6.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide7.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide8.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide9.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide10.jpg")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What enzyme is responsible for synthesizing RNA during transcription?",
                        "options": ["DNA polymerase", "RNA polymerase", "Ligase", "Helicase"],
                        "answer": "RNA polymerase"
                    },
                    {
                        "question": "What is the name of the DNA sequence where transcription begins?",
                        "options": ["Start codon", "Initiator site", "Promoter", "Operator"],
                        "answer": "Promoter"
                    },
                    {
                        "question": "Which of the following is NOT required for transcription?",
                        "options": ["DNA template", "RNA polymerase", "Nucleoside triphosphates", "DNA ligase"],
                        "answer": "DNA ligase"
                    },
                    {
                        "question": "What direction does RNA polymerase read the DNA template?",
                        "options": ["5’ to 3’", "3’ to 5’", "Random", "It switches directions"],
                        "answer": "3’ to 5’"
                    },
                    {
                        "question": "Which strand of DNA is used to build the RNA transcript?",
                        "options": ["Leading strand", "Lagging strand", "Coding strand", "Template strand"],
                        "answer": "Template strand"
                    },
                    {
                        "question": "In which direction is the RNA transcript synthesized?",
                        "options": ["3’ to 5’", "5’ to 3’", "It varies", "Both directions"],
                        "answer": "5’ to 3’"
                    },
                    {
                        "question": "Which nucleotides are used as substrates during transcription?",
                        "options": ["ATP, GTP, CTP, TTP", "ATP, GTP, CTP, UTP", "A, T, C, G", "dATP, dGTP, dCTP, dTTP"],
                        "answer": "ATP, GTP, CTP, UTP"
                    },
                    {
                        "question": "What feature makes RNA polymerase processive?",
                        "options": ["It can switch strands", "It does not require energy", "It stays attached and adds many nucleotides", "It proofreads its work"],
                        "answer": "It stays attached and adds many nucleotides"
                    },
                    {
                        "question": "What is the role of the promoter in transcription?",
                        "options": ["It adds RNA bases", "It codes for protein", "It signals where to start transcription", "It terminates transcription"],
                        "answer": "It signals where to start transcription"
                    },
                    {
                        "question": "What happens during elongation in transcription?",
                        "options": ["RNA polymerase binds to the promoter", "DNA unwinds and RNA is synthesized", "RNA is spliced", "The RNA leaves the nucleus"],
                        "answer": "DNA unwinds and RNA is synthesized"
                    },
                    {
                        "question": "Why is the RNA strand antiparallel to the DNA template?",
                        "options": ["Because DNA is single-stranded", "Because of base pairing rules", "To match the 5’ to 3’ synthesis direction", "RNA and DNA are the same"],
                        "answer": "To match the 5’ to 3’ synthesis direction"
                    },
                    {
                        "question": "What happens when RNA polymerase reaches a terminator sequence?",
                        "options": ["RNA polymerase keeps transcribing", "The RNA transcript is released", "Replication begins", "The DNA is destroyed"],
                        "answer": "The RNA transcript is released"
                    },
                    {
                        "question": "What is unique about RNA polymerase compared to DNA polymerase?",
                        "options": ["It needs primers", "It proofreads", "It doesn’t need a primer", "It uses dNTPs"],
                        "answer": "It doesn’t need a primer"
                    },
                    {
                        "question": "Which of the following is TRUE about transcription termination?",
                        "options": ["It always requires a helper protein", "It always happens at the promoter", "It involves a stop codon", "It can occur naturally or with help from proteins"],
                        "answer": "It can occur naturally or with help from proteins"
                    },
                    {
                        "question": "Which of these does NOT occur during transcription?",
                        "options": ["Base pairing with DNA", "RNA strand elongation", "Proofreading by RNA polymerase", "Unwinding of DNA"],
                        "answer": "Proofreading by RNA polymerase"
                    },
                    {
                        "question": "What is the role of the initiator site?",
                        "options": ["It signals where RNA polymerase should stop", "It marks the start of the promoter", "It helps align the ribosome", "It directs splicing"],
                        "answer": "It marks the start of the promoter"
                    },
                    {
                        "question": "Which statement best describes the function of RNA polymerase during transcription?",
                        "options": ["It unwinds DNA, reads the template strand, and builds RNA", "It proofreads DNA", "It translates RNA into protein", "It repairs mismatched DNA"],
                        "answer": "It unwinds DNA, reads the template strand, and builds RNA"
                    },
                    {
                        "question": "Which of the following is a difference between DNA replication and transcription?",
                        "options": ["Transcription uses both DNA strands", "Replication doesn’t require a primer", "Transcription makes RNA, not DNA", "Transcription occurs in the cytoplasm in all cells"],
                        "answer": "Transcription makes RNA, not DNA"
                    },
                    {
                        "question": "During transcription, which molecule is synthesized?",
                        "options": ["DNA", "tRNA", "mRNA", "Protein"],
                        "answer": "mRNA"
                    },
                    {
                        "question": "Why doesn’t RNA polymerase need a primer?",
                        "options": ["It uses DNA directly", "It begins synthesis at the promoter without one", "It has proofreading ability", "It only works on single-stranded DNA"],
                        "answer": "It begins synthesis at the promoter without one"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The necessary components of transcription are:"),
                                html.Ul([
                                    html.Li("A DNA template for base pairing (one of the two strands of DNA)"), 
                                    html.Li("Nucleotside triphosphates (ATP, GTP, CTP, UTP)"), 
                                    html.Li("RNA polymerase enzyme")
                                ]),
                                html.P(["An ", html.Strong("RNA polymerase enzyme"), " catalyzes the synthesis of mRNA. RNA polymerases are processive (meaning that a single enzyme-template binding results in the polymerization of hundreds of RNA bases), does not need primers, and lacks a proofreading function. In contrast, DNA polymerases do require primers and have a proofreading function."]),
                                html.P("The three steps of transcription are:"), 
                                html.Ul([
                                    html.Li([html.Strong("Initiation: "), "RNA polymerase binds to the promoter (a special sequence of DNA that tells the RNA polymerase where to bind and which strand of DNA to transcribe). The promoter contains a site called the initiator site."]),
                                    html.Li([html.Strong("Elongation: "), "RNA polymerase unwinds the DNA about 10 base pairs at a time and reads the template in a 3' to 5' direction. The RNA transcript is made antiparallel to the DNA strand and nucleotides are added to the 3' end."]),
                                    html.Li([html.Strong("Termination: "), "Termination begins with the RNA polymerase reaches a specific DNA sequence called the terminator. For some genes, the RNA transcript will just fall away from the DNA strand and the RNA polymerase, but for others, a helper protein will pull the RNA transcript away."])
                                ])
                            ])],
                "feynman": [html.Div([
                                html.P("Transcription is the process by which RNA is made from DNA. It requires three main ingredients:"),
                                html.Ul([
                                    html.Li("One strand of DNA to act as the template"),
                                    html.Li("RNA nucleotides (ATP, GTP, CTP, UTP) to build the RNA strand"),
                                    html.Li("RNA polymerase, the enzyme that puts it all together")
                                ]),
                                html.P([
                                    html.Strong("RNA polymerase "), 
                                    "doesn’t need a primer to start, doesn’t proofread its work, and can add hundreds of bases in one go without falling off the DNA."
                                ]),
                                html.P("Transcription happens in three steps:"),
                                html.Ul([
                                    html.Li([html.Strong("Initiation: "), "RNA polymerase binds to a promoter on the DNA to figure out where to start and which strand to copy."]),
                                    html.Li([html.Strong("Elongation: "), "The enzyme moves along the DNA, unwinding it and building the RNA strand by matching bases. The RNA grows in the 5' to 3' direction."]),
                                    html.Li([html.Strong("Termination: "), "When RNA polymerase hits a stop signal (called a terminator), it stops and releases the new RNA transcript."])
                                ])
                            ])]
            },
            "q19": {
                "question": html.P("Be prepared to define the terms: genetic code, codon, introns, exons. Know how to use a genetic code table to identify amino acids associated with specific codons."),
                "overview": html.Div([
                    html.P("The genetic code determines which amino acids are used to build proteins."), 
                    html.Ul([
                        html.Li([html.Strong("Codon: "), "A sequence of three RNA bases that code for a specific amino acid"]),
                        html.Li([html.Strong("Start Codon: "), "AUG, signals the beginning of translation and codes for methionine"]), 
                        html.Li([html.Strong("Stop Codons: "), "Signal the end of translation. They do not code for amino acids and are either UAA, UAG, or UGA"]), 
                    ]),
                    html.P("In eukaryotes, genes contain:"),
                    html.Ul([
                        html.Li([html.Strong("Exons: "), "Coding sequences that will be translated into a protein"]), 
                        html.Li([html.Strong("Introns: "), "Noncoding sequences that will be removed during RNA processing"])
                    ]),
                    html.P(["The first mRNA transcript is called ", html.Strong("pre-mRNA "), "and it contains both introns and exons. Before translation, ", html.Strong("RNA splicing "), "will remove introns and join exons together to form the final mRNA."])
                ]), 
                "deep_dive": html.Div([
                    html.P(["The genetic code is a set of instructions in the form of nucleotide triplets, or ", html.Strong("codons, "), "which tell the cell how to build proteins. Each codon consists of three RNA bases (e.g., AUG, GCU, UGA, for example), and each codon coresponds to a specific amino acid or a specific signal (start or stop)."]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/codon table.png", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/ap-biology/gene-expression-and-regulation/translation/a/the-genetic-code-discovery-and-properties", target = "_blank")])
                        ]
                    ),
                    html.Br(), 
                    html.Ul([
                        html.Li("There are 64 possible codons and 61 of them code for the 20 standard amino acids"), 
                        html.Li("AUG is the only start codon, marking where the ribosome should begin translating mRNA. It codes for the amino acid methionine"), 
                        html.Li("UAA, UAG, and UGA are stop codons. They do not code for an amino acid. Instead, they signal the ribosome to release the finished polypeptide (protein)")
                    ]),
                    html.P("In eukaryotic genes, DNA contains both:"),
                    html.Ul([
                        html.Li([html.Strong("Exons: "), "coding regions that determine the amino acid sequence"]), 
                        html.Li([html.Strong("Introns: "), "non-coding regions that interrupt the sequence"])
                    ]),
                    html.P(["After transcription, the resulting pre-mRNA includes both exons and introns. Before the mRNA can be translated, it must undergo ", html.Strong("RNA splicing, "), "where:"]),
                    html.Ul([
                        html.Li("Introns are removed"), 
                        html.Li("Exons are spliced together to form a continuous coding sequence")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'}, 
                        children = [
                            html.Img(src = "/assets/intron exon.jpg", style = {'marginRight':'40px'}),
                            html.Div(["Image from ", html.A("here", href = "https://en.citizendium.org/wiki/Intron", target = "_blank")])
                        ]
                    ),
                    html.P("Only the processed mRNA (with exons only) is exported to the cytoplasm and used for protein synthesis."),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: How to Read a Codon Chart", href = "https://www.youtube.com/watch?v=LsEYgwuP6ko&pp=ygUGY29kb25z", target = "_blank")]),
                        html.Li([html.A("learnbiologically: Codons", href = "https://www.youtube.com/watch?v=XwTExa8rs5A&pp=ygUGY29kb25z0gcJCcEJAYcqIYzv", target = "_blank")]),
                        html.Li([html.A("Khan Academy: The Genetic Code", href = "https://www.youtube.com/watch?v=dijqYyFY1GM&pp=ygUGY29kb25z", target = "_blank")]),
                        html.Li([html.A("Lucas Learns: How to Translate mRNA to Amino Acids (Decoding the Genetic Code)", href = "https://www.youtube.com/watch?v=QLhIg60hK9M&pp=ygUGY29kb25z", target = "_blank")]),
                        html.Li([html.A("Biology Lectures: Genetics for Beginners (Genetic Code and Codons)", href = "https://www.youtube.com/watch?v=SR-5CPQ-Sxg&pp=ygUGY29kb25z", target = "_blank")]),
                        html.Li([html.A("Andrey K: Start and Stop Codons", href = "https://www.youtube.com/watch?v=HxOGxj2jEfA&pp=ygUGY29kb25z", target = "_blank")])
                    ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide11.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide12.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide13.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide14.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide17.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does the genetic code specify?",
                        "options": ["The order of DNA replication", "The structure of the cell membrane", "Which amino acids are used to build a protein", "The sequence of ribosomes in the cell"],
                        "answer": "Which amino acids are used to build a protein"
                    },
                    {
                        "question": "What is a codon?",
                        "options": ["A sequence of two RNA bases", "A sequence of three RNA bases", "A ribosome unit", "A DNA polymerase subunit"],
                        "answer": "A sequence of three RNA bases"
                    },
                    {
                        "question": "What does the codon AUG signal?",
                        "options": ["A stop in transcription", "Start of translation", "An intron", "RNA splicing"],
                        "answer": "Start of translation"
                    },
                    {
                        "question": "Which of the following is a stop codon?",
                        "options": ["AUG", "UAC", "UAA", "GGA"],
                        "answer": "UAA"
                    },
                    {
                        "question": "How many RNA bases make up one codon?",
                        "options": ["1", "2", "3", "4"],
                        "answer": "3"
                    },
                    {
                        "question": "What type of RNA is read by the ribosome to build a protein?",
                        "options": ["tRNA", "rRNA", "mRNA", "snRNA"],
                        "answer": "mRNA"
                    },
                    {
                        "question": "How many amino acids are coded for by the standard genetic code?",
                        "options": ["4", "20", "64", "3"],
                        "answer": "20"
                    },
                    {
                        "question": "What do stop codons do?",
                        "options": ["Start transcription", "Signal the end of translation", "Code for methionine", "Initiate RNA splicing"],
                        "answer": "Signal the end of translation"
                    },
                    {
                        "question": "What is the function of exons?",
                        "options": ["They are removed from pre-mRNA", "They code for protein", "They stop transcription", "They help RNA polymerase bind"],
                        "answer": "They code for protein"
                    },
                    {
                        "question": "Which part of a gene is removed during RNA splicing?",
                        "options": ["Codons", "Start codon", "Introns", "Exons"],
                        "answer": "Introns"
                    },
                    {
                        "question": "Which process removes introns from pre-mRNA?",
                        "options": ["Translation", "Transcription", "Replication", "RNA splicing"],
                        "answer": "RNA splicing"
                    },
                    {
                        "question": "What are introns?",
                        "options": ["Coding sequences", "RNA polymerase subunits", "Non-coding sequences", "Ribosome components"],
                        "answer": "Non-coding sequences"
                    },
                    {
                        "question": "What happens to exons during RNA processing?",
                        "options": ["They are removed", "They are replaced by introns", "They are spliced together", "They are degraded"],
                        "answer": "They are spliced together"
                    },
                    {
                        "question": "Where can you find introns and exons together?",
                        "options": ["Final mRNA", "Pre-mRNA", "tRNA", "Protein"],
                        "answer": "Pre-mRNA"
                    },
                    {
                        "question": "Which codon acts as both a start signal and codes for methionine?",
                        "options": ["UAA", "AUG", "UGA", "UAG"],
                        "answer": "AUG"
                    },
                    {
                        "question": "How many stop codons exist in the standard genetic code?",
                        "options": ["1", "2", "3", "4"],
                        "answer": "3"
                    },
                    {
                        "question": "What tool do you use to find the amino acid for a given codon?",
                        "options": ["Punnett square", "Codon wheel or genetic code table", "PCR machine", "DNA ladder"],
                        "answer": "Codon wheel or genetic code table"
                    },
                    {
                        "question": "Which of the following codons is NOT a stop codon?",
                        "options": ["UGA", "UAA", "AUG", "UAG"],
                        "answer": "AUG"
                    },
                    {
                        "question": "Which type of sequence appears in the final mRNA used in translation?",
                        "options": ["Only introns", "Only exons", "Both introns and exons", "Neither introns nor exons"],
                        "answer": "Only exons"
                    },
                    {
                        "question": "If a codon reads 'GAA', what kind of information does it carry?",
                        "options": ["It signals RNA splicing", "It identifies an intron", "It codes for a specific amino acid", "It binds ribosomes"],
                        "answer": "It codes for a specific amino acid"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The genetic code determines which amino acids are used to build proteins."), 
                                html.Ul([
                                    html.Li([html.Strong("Codon: "), "A sequence of three RNA bases that code for a specific amino acid"]),
                                    html.Li([html.Strong("Start Codon: "), "AUG, signals the beginning of translation and codes for methionine"]), 
                                    html.Li([html.Strong("Stop Codons: "), "Signal the end of translation. They do not code for amino acids and are either UAA, UAG, or UGA"]), 
                                ]),
                                html.P("In eukaryotes, genes contain:"),
                                html.Ul([
                                    html.Li([html.Strong("Exons: "), "Coding sequences that will be translated into a protein"]), 
                                    html.Li([html.Strong("Introns: "), "Noncoding sequences that will be removed during RNA processing"])
                                ]),
                                html.P(["The first mRNA transcript is called ", html.Strong("pre-mRNA "), "and it contains both introns and exons. Before translation, ", html.Strong("RNA splicing "), "will remove introns and join exons together to form the final mRNA."])
                            ])],
                "feynman": [
                    html.P("The genetic code is like a recipe that tells the cell which amino acids to use. It reads mRNA in groups of three bases called codons. Each codon matches an amino acid, except for three stop codons that tell it when to stop, and one start codon (AUG) to begin. In eukaryotes, genes have exons (coding parts) and introns (non-coding parts). The first version of mRNA has both, but before it gets used, the introns are cut out in a process called RNA splicing, and the exons are stitched together to make the final message for building a protein.")
                ]
            },
            "q20": {
                "question": html.P("Understand how ribosomes contribute to the three main steps of the translation process."),
                "overview": html.Div([
                                html.H4("Ribosome Function in Translation"),
                                html.P("The ribosome is the site of protein synthesis. It holds mRNA and charged tRNAs in position to assemble the growing polypeptide chain."),
                                html.P("It has a fidelity function that checks for correct codon–anticodon pairing using hydrogen bonding. If the match is incorrect, the tRNA is rejected. Fidelity refers to accuracy in translating mRNA to the correct sequence of amino acids in the polypeptide. In other words, making sure that the amino acid sequence is accurate based on what the mRNA says."),
                                html.P("Translation occurs in three phases:"),
                                html.Ul([
                                    html.Li([html.Strong("Initiation: "), "The small ribosomal subunit, mRNA, and a charged tRNA form a complex. The large subunit joins, placing the tRNA in the P-site."]),
                                    html.Li([html.Strong("Elongation: "), "A second charged tRNA enters the A-site. The ribosome forms a peptide bond and shifts the tRNAs, releasing the first tRNA from the E-site."]),
                                    html.Li([html.Strong("Termination: "), "A stop codon brings in a release factor, which helps detach the polypeptide chain from the ribosome."])
                                ]) 
                            ]),
                "deep_dive": html.Div([
                    html.H4("Ribosome Function in Translation"),
                    html.P("The ribosome is the site of protein synthesis. It holds mRNA and charged tRNAs in position to assemble the growing polypeptide chain."),
                    html.P("It has a fidelity function that checks for correct codon–anticodon pairing using hydrogen bonding. If the match is incorrect, the tRNA is rejected."),
                    html.P("Translation occurs in three phases:"),
                    html.Ul([
                        html.Li([html.Strong("Initiation: "), "The small ribosomal subunit, mRNA, and a charged tRNA form a complex. The large subunit joins, placing the tRNA in the P-site."]),
                        html.Li([html.Strong("Elongation: "), "A second charged tRNA enters the A-site. The ribosome forms a peptide bond and shifts the tRNAs, releasing the first tRNA from the E-site."]),
                        html.Li([html.Strong("Termination: "), "A stop codon brings in a release factor, which helps detach the polypeptide chain from the ribosome."])
                    ]),
                    html.Hr(),
                    html.P("The ribosome is made of a small and large subunit, both composed of rRNA and proteins. It acts like a workbench for reading mRNA and linking amino acids together."),
                    html.P([
                        html.Strong("Fidelity function: "), 
                        "When a charged tRNA enters, its anticodon must perfectly match the mRNA codon. Hydrogen bonds form between all three base pairs. ",
                        "The small subunit’s rRNA validates the match—if it's incorrect, the tRNA is rejected."
                    ]),
                    html.P([html.Strong("Initiation: ")]),
                    html.Ul([
                        html.Li("Begins when the small ribosomal subunit binds mRNA and a charged tRNA (usually carrying methionine)."),
                        html.Li("The large subunit joins, placing the first tRNA in the P-site where translation begins.")
                    ]),
                    html.P([html.Strong("Elongation: ")]),
                    html.Ul([
                        html.Li("A new charged tRNA enters the A-site, matching the next codon."),
                        html.Li("The ribosome catalyzes two reactions: (1) the amino acid in the P-site is released from its tRNA, and (2) a peptide bond is formed with the amino acid in the A-site."),
                        html.Li("The empty tRNA exits via the E-site, and the ribosome shifts to the next codon. Elongation repeats with help from elongation factors.")
                    ]),
                    html.P([html.Strong("Termination: ")]),
                    html.Ul([
                        html.Li("A stop codon enters the A-site. No tRNA matches it."),
                        html.Li("Instead, a release factor binds, triggering hydrolysis of the bond between the last amino acid and its tRNA."),
                        html.Li("The finished protein is released from the P-site, with the C-terminus as the final amino acid added.")
                    ]),
                    html.Div(
                        style = {'display':'flex', 'alignItems':'center'},
                        children = [
                            html.Img(src = "/assets/translation.png", style = {'marginRight':'40px', 'width':'600px'}),
                            html.Div(["Image adapted from ", html.A("here", href = "https://www.pnas.org/post/journal-club/new-role-transfer-rna-protein-synthesis", target = "_blank")])
                        ]
                    ),
                    html.P([html.Strong("Helpful Outside Resources:")]),
                    html.Ul([
                        html.Li([html.A("Amoeba Sisters: Protein Synthesis", href = "https://www.youtube.com/watch?v=oefAI2x2CQM&t=163s&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("Professor Dave Explains: Transcription and Translation (From DNA to Protein)", href = "https://www.youtube.com/watch?v=bKIpDtJdK8Q&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("The Organic Chemistry Tutor: Transcription and Translation (Protein Synthesis from DNA)", href = "https://www.youtube.com/watch?v=8wAwLwJAGHs&t=2s&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                        html.Li([html.A("2 Minute Classroom: Transcription & Translation (From DNA to RNA to Protein)", href = "https://www.youtube.com/watch?v=GZRwQpb_sdQ&pp=ygUNdHJhbnNjcmlwdGlvbg%3D%3D", target = "_blank")]),
                    ]), 
                ]),
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide18.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide19.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide20.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide21.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide22.jpg"),
                    html.Img(src = "/assets/Chapter14/Slide23.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the primary function of the ribosome in translation?",
                        "options": ["Synthesizing DNA", "Holding mRNA and tRNAs to assemble proteins", "Transcribing RNA", "Breaking down proteins"],
                        "answer": "Holding mRNA and tRNAs to assemble proteins"
                    },
                    {
                        "question": "How does the ribosome ensure the correct tRNA binds to the mRNA codon?",
                        "options": ["By matching the anticodon to the codon using hydrogen bonds", "By proofreading the DNA", "By chemically modifying tRNA", "By altering the mRNA sequence"],
                        "answer": "By matching the anticodon to the codon using hydrogen bonds"
                    },
                    {
                        "question": "During initiation, where is the first charged tRNA positioned in the ribosome?",
                        "options": ["A-site", "P-site", "E-site", "Exit tunnel"],
                        "answer": "P-site"
                    },
                    {
                        "question": "What happens during the elongation phase of translation?",
                        "options": ["A charged tRNA enters the A-site and a peptide bond forms", "The ribosome disassembles", "mRNA is transcribed", "DNA is replicated"],
                        "answer": "A charged tRNA enters the A-site and a peptide bond forms"
                    },
                    {
                        "question": "What role do elongation factors play in translation?",
                        "options": ["Help tRNAs bind and assist ribosome movement", "Terminate translation", "Start transcription", "Process introns"],
                        "answer": "Help tRNAs bind and assist ribosome movement"
                    },
                    {
                        "question": "What signals the termination of translation?",
                        "options": ["Start codon", "Stop codon entering the A-site", "Elongation factor binding", "tRNA release"],
                        "answer": "Stop codon entering the A-site"
                    },
                    {
                        "question": "What binds to the stop codon to trigger termination?",
                        "options": ["tRNA", "Release factor protein", "Elongation factor", "RNA polymerase"],
                        "answer": "Release factor protein"
                    },
                    {
                        "question": "What happens to the polypeptide chain during termination?",
                        "options": ["It is extended", "It is released from the ribosome", "It binds to another tRNA", "It enters the nucleus"],
                        "answer": "It is released from the ribosome"
                    },
                    {
                        "question": "Which ribosomal site is responsible for exit of the empty tRNA?",
                        "options": ["A-site", "P-site", "E-site", "S-site"],
                        "answer": "E-site"
                    },
                    {
                        "question": "What molecule carries amino acids to the ribosome?",
                        "options": ["mRNA", "tRNA", "rRNA", "DNA"],
                        "answer": "tRNA"
                    },
                    {
                        "question": "The ribosome is composed mainly of which molecules?",
                        "options": ["Proteins only", "rRNA and proteins", "DNA and proteins", "mRNA and tRNA"],
                        "answer": "rRNA and proteins"
                    },
                    {
                        "question": "What ensures that the amino acid is correctly matched to the mRNA codon?",
                        "options": ["Ribosome's proofreading ability", "Hydrogen bonding between codon and anticodon", "RNA polymerase activity", "DNA ligase"],
                        "answer": "Hydrogen bonding between codon and anticodon"
                    },
                    {
                        "question": "In which site does the peptide bond form during elongation?",
                        "options": ["A-site", "P-site", "E-site", "C-site"],
                        "answer": "A-site"
                    },
                    {
                        "question": "What happens to the tRNA after its amino acid is added to the chain?",
                        "options": ["It stays in the P-site", "It moves to the E-site and exits", "It becomes part of the polypeptide", "It degrades immediately"],
                        "answer": "It moves to the E-site and exits"
                    },
                    {
                        "question": "Which subunit of the ribosome validates codon-anticodon pairing?",
                        "options": ["Large subunit", "Small subunit", "Both subunits", "Neither subunit"],
                        "answer": "Small subunit"
                    },
                    {
                        "question": "Where does translation occur in the cell?",
                        "options": ["Nucleus", "Cytoplasm", "Mitochondria", "Golgi apparatus"],
                        "answer": "Cytoplasm"
                    },
                    {
                        "question": "What is the role of the P-site in the ribosome?",
                        "options": ["Entry site for tRNA", "Site where peptide bonds form", "Site where the first charged tRNA binds and holds the growing polypeptide chain", "Exit site for tRNA"],
                        "answer": "Site where the first charged tRNA binds and holds the growing polypeptide chain"
                    },
                    {
                        "question": "What chemical reaction breaks the bond between the polypeptide and tRNA during termination?",
                        "options": ["Hydrolysis", "Condensation", "Phosphorylation", "Oxidation"],
                        "answer": "Hydrolysis"
                    },
                    {
                        "question": "What does the term 'charged tRNA' mean?",
                        "options": ["tRNA with an amino acid attached", "tRNA without an amino acid", "tRNA that has left the ribosome", "tRNA bound to DNA"],
                        "answer": "tRNA with an amino acid attached"
                    },
                    {
                        "question": "What ensures accuracy during protein synthesis at the ribosome?",
                        "options": ["Elongation factors", "Fidelity checking by the small subunit rRNA", "DNA proofreading", "Splicing"],
                        "answer": "Fidelity checking by the small subunit rRNA"
                    }
                ],
                "blurting": [html.Div([
                                html.H4("Ribosome Function in Translation"),
                                html.P("The ribosome is the site of protein synthesis. It holds mRNA and charged tRNAs in position to assemble the growing polypeptide chain."),
                                html.P("It has a fidelity function that checks for correct codon–anticodon pairing using hydrogen bonding. If the match is incorrect, the tRNA is rejected."),
                                html.P("Translation occurs in three phases:"),
                                html.Ul([
                                    html.Li([html.Strong("Initiation: "), "The small ribosomal subunit, mRNA, and a charged tRNA form a complex. The large subunit joins, placing the tRNA in the P-site."]),
                                    html.Li([html.Strong("Elongation: "), "A second charged tRNA enters the A-site. The ribosome forms a peptide bond and shifts the tRNAs, releasing the first tRNA from the E-site."]),
                                    html.Li([html.Strong("Termination: "), "A stop codon brings in a release factor, which helps detach the polypeptide chain from the ribosome."])
                                ]) 
                            ])],
                "feynman": [html.Div([
                    html.P("The ribosome is where proteins get built. It reads mRNA and checks that each tRNA matches the codon. If the match is wrong, it throws the tRNA out."),
                    html.Ul([
                        html.Li([html.Strong("Initiation: "), "The ribosome locks in the start codon and first tRNA."]),
                        html.Li([html.Strong("Elongation: "), "tRNAs bring amino acids, and the ribosome links them into a chain."]),
                        html.Li([html.Strong("Termination: "), "A stop codon tells the ribosome to release the finished protein."])
                    ])
                ])]
            },
            "q21": {
                "question": html.P("Be able to describe three main types of protein modifications and where they occur."),
                "overview": html.Div([
                                html.H4("Three Main Types of Protein Modifications"),
                                html.P("Proteins undergo several modifications after synthesis that alter their function and properties."),
                                html.Ul([
                                    html.Li("Proteolysis: cleavage of proteins by proteases."),
                                    html.Li("Glycosylation: addition of sugar molecules to form glycoproteins."),
                                    html.Li("Phosphorylation: addition of phosphate groups by kinases, which can change protein conformation."),
                                ]),
                                html.P("Most of these modifications happen in the Golgi apparatus, where proteins are packaged and finalized."),
                            ]), 
                "deep_dive": html.Div([
                                html.H4("Understanding Protein Modifications and Their Cellular Location"),
                                html.P("Protein modifications are crucial for the final function, stability, and localization of proteins."),
                                html.P([
                                    html.Strong("Proteolysis:"), 
                                    " This modification involves the cutting of peptide bonds by enzymes called proteases. It can activate or deactivate proteins and remove signal sequences."
                                ]),
                                html.P([
                                    html.Strong("Glycosylation:"), 
                                    " Sugars are covalently attached to proteins to form glycoproteins, influencing protein folding, stability, and cell signaling."
                                ]),
                                html.P([
                                    html.Strong("Phosphorylation:"), 
                                    " Kinases add negatively charged phosphate groups to specific amino acids, often causing a conformational change that can regulate protein activity."
                                ]),
                                html.P("These modifications primarily occur in the Golgi apparatus, a cellular organelle responsible for modifying, sorting, and packaging proteins for their final destinations."),
                                html.Hr(),
                                html.P([html.Strong("A Deeper Dive:")]),
                                html.P([html.Strong("Proteolysis: "), "often occurs in the ", html.Strong("Endoplasmic Reticulum (ER), "), "where signal sequences, which are short peptide 'flags' that direct the protein to the ER are cleaved, allowing the protein to begin folding or enter the secretory pathway."]),
                                html.P("An example would be preproinsulin, which is cleaved to proinsulin, through cleavage of the signal peptide in the ER."),
                                html.P([html.Strong("Glycosylation: "), "also often occurs in the ", html.Strong("Endoplasmic Reticulum (ER), "), "where a core oligosaccharide is added to the nitrogen atom of asparagine residues in a consensus sequence. This helps with protein folding and quality control."]), 
                                html.P("An example would be membrane and secreted proteins entering the lumen of the ER."), 
                                html.P(["In this context, a ", html.Strong("consensus sequence "), "is a theoretical or actual sequence of DNA derived from aligning multiple biological sequences (DNA, RNA, or protein) to identify the most frequently occuring residue (nucleotide or amino acid) at each position. In other words, a consensus sequence is like the most 'popular' version of a sequence. You look at a bunch of similar DNA or protein sequences and see which nucleotide or amino aic dappears most often at each spot and the result is the consensus sequence."]),
                                html.P("For example, if you have the following sequences:"), 
                                html.P("A T G C A"),
                                html.P("A T G T A"), 
                                html.P("A T G C A"), 
                                html.P(["The consensus sequence is ", html.Strong("A T G C A "), "because those are the most common letters at each position."]),
                                html.P([html.Strong("Phosphorylation: "), "can occur in the cytosol or on the ribosome-associated nascent (newly formed) protein."]),
                                html.P("An example would be regulatory proteins, such as transcription factors, or signaling intermediates, which phosphorylate proteins to cause something to happen."),
                                html.Hr(), 
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Khan Academy Medicine: Post Translational Modifications", href = "https://www.youtube.com/watch?v=5yZjM-SndyE&t=41s&pp=ygUrcG9zdC10cmFuc2xhdGlvbmFsIG1vZGlmaWNhdGlvbiBvZiBwcm90ZWlucw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("PremedHQ Science Academy: Post-Translational Modification of Proteins", href = "https://www.youtube.com/watch?v=_g-YXBF7ym8&pp=ygUrcG9zdC10cmFuc2xhdGlvbmFsIG1vZGlmaWNhdGlvbiBvZiBwcm90ZWlucw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("theCrux: Post-Translational Modifications in Prokaryotes and Eukaryotes (Types, Functions, and Examples)", href = "https://www.youtube.com/watch?v=7EPP3_WL-HM&pp=ygUrcG9zdC10cmFuc2xhdGlvbmFsIG1vZGlmaWNhdGlvbiBvZiBwcm90ZWlucw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Medicosis Perfectionalis: Translation (mRNA to Proteins) & Ribosomes (rER) - Post-Translational Modification", href = "https://www.youtube.com/watch?v=VbDGBKivPYA&pp=ygUrcG9zdC10cmFuc2xhdGlvbmFsIG1vZGlmaWNhdGlvbiBvZiBwcm90ZWlucw%3D%3D", target = "_blank")])
                                ])
                            ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter14/Slide24.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter14question6.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is proteolysis?",
                        "options": ["Adding a sugar group", "Cleaving a protein using proteases", "Binding RNA to a protein", "Removing phosphate groups from proteins"],
                        "answer": "Cleaving a protein using proteases"
                    },
                    {
                        "question": "What is glycosylation?",
                        "options": ["Adding lipids to proteins", "Adding sugars to proteins", "Cleaving peptide bonds", "Phosphorylating DNA"],
                        "answer": "Adding sugars to proteins"
                    },
                    {
                        "question": "What is the main effect of phosphorylation on proteins?",
                        "options": ["Destroys the protein", "Causes the protein to fold into alpha helices", "Alters protein conformation and function", "Detaches the protein from DNA"],
                        "answer": "Alters protein conformation and function"
                    },
                    {
                        "question": "What enzymes carry out proteolysis?",
                        "options": ["Kinases", "Glycosidases", "Proteases", "Ligases"],
                        "answer": "Proteases"
                    },
                    {
                        "question": "Which type of protein modification is commonly used to activate zymogens (inactive enzymes)?",
                        "options": ["Phosphorylation", "Glycosylation", "Proteolysis", "Methylation"],
                        "answer": "Proteolysis"
                    },
                    {
                        "question": "What type of molecule is added during glycosylation?",
                        "options": ["Phosphate", "Amino acid", "Sugar", "Lipid"],
                        "answer": "Sugar"
                    },
                    {
                        "question": "Which enzyme adds phosphate groups to proteins?",
                        "options": ["Phosphatase", "Protease", "Kinase", "Glycosylase"],
                        "answer": "Kinase"
                    },
                    {
                        "question": "What is the name of the cellular organelle where most protein modifications occur?",
                        "options": ["Nucleus", "Endoplasmic reticulum", "Golgi apparatus", "Ribosome"],
                        "answer": "Golgi apparatus"
                    },
                    {
                        "question": "How do phosphate groups change proteins?",
                        "options": ["They shorten the amino acid chain", "They signal the protein for destruction", "They add charge and change protein shape", "They fold the protein into a helix"],
                        "answer": "They add charge and change protein shape"
                    },
                    {
                        "question": "What kind of protein is produced by glycosylation?",
                        "options": ["Phosphoprotein", "Zymogen", "Glycoprotein", "Lipoprotein"],
                        "answer": "Glycoprotein"
                    },
                    {
                        "question": "Which of the following processes involves enzyme-catalyzed cleavage of a protein?",
                        "options": ["Glycosylation", "Phosphorylation", "Proteolysis", "Replication"],
                        "answer": "Proteolysis"
                    },
                    {
                        "question": "What is the main purpose of the Golgi apparatus in protein processing?",
                        "options": ["DNA replication", "Initial protein synthesis", "Protein packaging and modification", "tRNA synthesis"],
                        "answer": "Protein packaging and modification"
                    },
                    {
                        "question": "Which of the following could activate a protein by removing part of it?",
                        "options": ["Proteolysis", "Methylation", "Glycosylation", "Transcription"],
                        "answer": "Proteolysis"
                    },
                    {
                        "question": "Which protein modification would most directly affect the interaction with cell surface receptors?",
                        "options": ["Proteolysis", "Glycosylation", "Phosphorylation", "Splicing"],
                        "answer": "Glycosylation"
                    },
                    {
                        "question": "Which modification involves the addition of a negatively charged group to a protein?",
                        "options": ["Acetylation", "Phosphorylation", "Methylation", "Glycosylation"],
                        "answer": "Phosphorylation"
                    },
                    {
                        "question": "What cellular function is most likely impacted by faulty glycosylation?",
                        "options": ["RNA splicing", "Protein folding and cell recognition", "DNA replication", "Translation accuracy"],
                        "answer": "Protein folding and cell recognition"
                    },
                    {
                        "question": "What do kinases do?",
                        "options": ["Remove sugar groups", "Add phosphate groups", "Break down RNA", "Splice DNA"],
                        "answer": "Add phosphate groups"
                    },
                    {
                        "question": "Where are glycoproteins usually finalized?",
                        "options": ["Cytoplasm", "Nucleus", "Golgi apparatus", "Mitochondria"],
                        "answer": "Golgi apparatus"
                    },
                    {
                        "question": "What is the result of protein phosphorylation?",
                        "options": ["Protein destruction", "Conformational change", "RNA splicing", "Exon removal"],
                        "answer": "Conformational change"
                    },
                    {
                        "question": "Which protein modification is most likely to act as a molecular switch?",
                        "options": ["Proteolysis", "Glycosylation", "Phosphorylation", "Hydroxylation"],
                        "answer": "Phosphorylation"
                    }
                ],
                "blurting": [html.Div([
                                html.H4("Three Main Types of Protein Modifications"),
                                html.P("Proteins undergo several modifications after synthesis that alter their function and properties."),
                                html.Ul([
                                    html.Li("Proteolysis: cleavage of proteins by proteases."),
                                    html.Li("Glycosylation: addition of sugar molecules to form glycoproteins."),
                                    html.Li("Phosphorylation: addition of phosphate groups by kinases, which can change protein conformation."),
                                ]),
                                html.P("Most of these modifications happen in the Golgi apparatus, where proteins are packaged and finalized."),
                            ])],
                "feynman": [html.Div([
                                html.P("Proteins get changed after they are made to work properly."),
                                html.Ul([
                                    html.Li("Proteolysis cuts proteins into active forms."),
                                    html.Li("Glycosylation adds sugars to proteins."),
                                    html.Li("Phosphorylation adds phosphate groups that can change protein shape."),
                                    html.Li("Most changes happen in the Golgi apparatus where proteins are finished and packed.")
                                ])
                            ])]
            },
        }
    }, #end of Study Guide #1 material

    "sg2": {
        "questions": {
            "q1": {
                "question": html.P("Know the formal definitions of the terms, “Signal Transduction Pathway”, “Autocrine” and “Paracrine” and “Endocrine”."),
                "overview": html.Div([
                                html.H4("Signal Transduction and Types of Signaling"),
                                html.P("A signal transduction pathway is how cells convert an external signal into a functional response. This involves a signal molecule, a receptor, and a cellular response."),
                                html.Ul([
                                    html.Li([html.Strong("Autocrine:"), " the signal affects the same cell that produces it."]),
                                    html.Li([html.Strong("Paracrine:"), " the signal affects nearby cells."]),
                                    html.Li([html.Strong("Endocrine:"), " the signal (hormone) travels through the bloodstream to reach distant target cells."])
                                ]),
                                html.P("The signal binds to a receptor, causing it to change shape and activate kinase activity. This starts a phosphorylation cascade, amplifying the signal and changing gene expression.")
                            ]), 
                "deep_dive": html.Div([
                                html.H4("Understanding Signal Transduction and Signal Range"),
                                html.P("Cells communicate through chemical signals. These signals can act locally or travel long distances, depending on the mechanism:"),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Autocrine signals: "), 
                                        "Produced and received by the same cell. Useful for feedback loops and local control."
                                    ])]),
                                html.Img(src = "/assets/autocrine.png", style = {'width':'400px'}),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Paracrine signals: "), 
                                        "Released by a cell and affect nearby cells. Common in tissue-level communication."
                                    ])]),
                                html.Img(src = "/assets/paracrine.png", style = {'width':'400px'}),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Endocrine signals: "), 
                                        "Hormones released into the bloodstream to reach distant target cells. Used for coordination across body systems."
                                    ])
                                ]),
                                html.Img(src = "/assets/endocrine.png", style = {'width':'400px'}),
                                html.P("In a signal transduction pathway, the signal (like a hormone or ligand) binds to a specific receptor protein on the cell surface. This binding causes a shape change in the receptor, often giving it protein kinase activity."),
                                html.P("The receptor then phosphorylates a responder protein, altering its function. This sets off a cascade where each step amplifies the signal. Eventually, a transcription factor is activated, altering gene expression and changing the cell’s activity."),
                                html.Img(src = "/assets/signal transduction.png", style = {'width':'600px'}),
                                html.Br(), 
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Henrik's Lab: Cell Signaling Types", href = "https://www.youtube.com/watch?v=QL8yAtQXwuo&pp=ygUrYXV0b2NyaW5lIGVuZG9jcmluZSBhbmQgcGFyYWNyaW5lIHNpZ25hbGluZw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Amoeba Sisters: Intro to Cell Signaling", href = "https://www.youtube.com/watch?v=-dbRterutHY&pp=ygUrYXV0b2NyaW5lIGVuZG9jcmluZSBhbmQgcGFyYWNyaW5lIHNpZ25hbGluZw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Osmosis from Elsevier: Common Cell Signaling Pathways", href = "https://www.youtube.com/watch?v=9sF_h-bAnIE&pp=ygUrYXV0b2NyaW5lIGVuZG9jcmluZSBhbmQgcGFyYWNyaW5lIHNpZ25hbGluZw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("BMH Learning: Autocrine, Paracrine, and Endocrine Signaling", href = "https://www.youtube.com/watch?v=FVGlz1oWzWI&pp=ygUrYXV0b2NyaW5lIGVuZG9jcmluZSBhbmQgcGFyYWNyaW5lIHNpZ25hbGluZw%3D%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter7/Slide2.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide3.jpg"), 
                    html.Img(src = "/assets/Chapter7/Slide4.jpg"), 
                    html.Img(src = "/assets/Chapter7/Slide5.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter7question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What are the three basic components of a signal transduction pathway?",
                        "options": ["Signal, receptor, response", "Ligand, enzyme, hormone", "DNA, RNA, protein", "Neuron, synapse, target"],
                        "answer": "Signal, receptor, response"
                    },
                    {
                        "question": "Which term describes a cell that releases a signal and responds to it itself?",
                        "options": ["Paracrine", "Autocrine", "Endocrine", "Exocrine"],
                        "answer": "Autocrine"
                    },
                    {
                        "question": "What is the function of a receptor in signal transduction?",
                        "options": ["It produces the signal", "It circulates the signal", "It detects the signal and changes shape", "It transports DNA"],
                        "answer": "It detects the signal and changes shape"
                    },
                    {
                        "question": "What type of signaling affects nearby cells?",
                        "options": ["Autocrine", "Endocrine", "Paracrine", "Neuronal"],
                        "answer": "Paracrine"
                    },
                    {
                        "question": "Which signaling type involves hormones traveling through the bloodstream?",
                        "options": ["Autocrine", "Endocrine", "Paracrine", "Synaptic"],
                        "answer": "Endocrine"
                    },
                    {
                        "question": "What happens to the receptor protein after it binds a signal molecule?",
                        "options": ["It breaks down", "It becomes a hormone", "It changes conformation and becomes active", "It leaves the cell"],
                        "answer": "It changes conformation and becomes active"
                    },
                    {
                        "question": "What enzyme activity is often activated by signal transduction receptors?",
                        "options": ["Polymerase", "Protease", "Kinase", "Ligase"],
                        "answer": "Kinase"
                    },
                    {
                        "question": "How does phosphorylation affect a responder protein?",
                        "options": ["Destroys it", "Deactivates it", "Alters its function", "Exports it from the cell"],
                        "answer": "Alters its function"
                    },
                    {
                        "question": "What is the result of a phosphorylation cascade in a signal transduction pathway?",
                        "options": ["Signal is stopped", "Signal is weakened", "Signal is amplified", "Signal is exported"],
                        "answer": "Signal is amplified"
                    },
                    {
                        "question": "What ultimately changes inside the cell due to signal transduction?",
                        "options": ["DNA replication", "Gene expression", "Cell death", "Lipid synthesis"],
                        "answer": "Gene expression"
                    },
                    {
                        "question": "Which of the following is required for a cell to respond to a specific signal?",
                        "options": ["ATP", "A receptor for the signal", "A nearby neuron", "An active nucleus"],
                        "answer": "A receptor for the signal"
                    },
                    {
                        "question": "Endocrine signals most commonly travel through which system?",
                        "options": ["Digestive", "Respiratory", "Circulatory", "Nervous"],
                        "answer": "Circulatory"
                    },
                    {
                        "question": "Which type of signal travels the longest distance?",
                        "options": ["Autocrine", "Paracrine", "Endocrine", "Juxtacrine"],
                        "answer": "Endocrine"
                    },
                    {
                        "question": "What binds to DNA to change gene expression during signal transduction?",
                        "options": ["Ligand", "Hormone", "Transcription factor", "Kinase"],
                        "answer": "Transcription factor"
                    },
                    {
                        "question": "What kind of molecule is typically the signal in an endocrine pathway?",
                        "options": ["Neurotransmitter", "Ion", "Hormone", "Enzyme"],
                        "answer": "Hormone"
                    },
                    {
                        "question": "What would happen if a target cell lacked the correct receptor for a signal?",
                        "options": ["The signal would have no effect", "The cell would amplify the signal", "The signal would change gene expression", "The receptor would be created later"],
                        "answer": "The signal would have no effect"
                    },
                    {
                        "question": "Which of the following best describes the first step of signal transduction?",
                        "options": ["DNA transcription", "Receptor changes shape", "Gene activation", "Protein synthesis"],
                        "answer": "Receptor changes shape"
                    },
                    {
                        "question": "What is a signal transduction pathway primarily used for?",
                        "options": ["Producing ATP", "Communicating information inside a cell", "Synthesizing lipids", "Transporting oxygen"],
                        "answer": "Communicating information inside a cell"
                    },
                    {
                        "question": "What allows signal transduction to produce a large cellular response from a small signal?",
                        "options": ["Negative feedback", "Gene duplication", "Signal amplification", "Active transport"],
                        "answer": "Signal amplification"
                    },
                    {
                        "question": "If a hormone is produced in the pancreas and affects liver cells, what kind of signaling is this?",
                        "options": ["Autocrine", "Paracrine", "Endocrine", "Local"],
                        "answer": "Endocrine"
                    }
                ],
                "blurting": [html.Div([
                                html.H4("Signal Transduction and Types of Signaling"),
                                html.P("A signal transduction pathway is how cells convert an external signal into a functional response. This involves a signal molecule, a receptor, and a cellular response."),
                                html.Ul([
                                    html.Li([html.Strong("Autocrine:"), " the signal affects the same cell that produces it."]),
                                    html.Li([html.Strong("Paracrine:"), " the signal affects nearby cells."]),
                                    html.Li([html.Strong("Endocrine:"), " the signal (hormone) travels through the bloodstream to reach distant target cells."])
                                ]),
                                html.P("The signal binds to a receptor, causing it to change shape and activate kinase activity. This starts a phosphorylation cascade, amplifying the signal and changing gene expression.")
                            ])],
                "feynman": [html.Div([
                                html.P("Cells use signals to talk. The signal fits into a receptor, which flips on and starts a chain reaction."),
                                html.Ul([
                                    html.Li("If a cell talks to itself, it’s autocrine."),
                                    html.Li("If it talks to a neighbor, it’s paracrine."),
                                    html.Li("If it sends messages through the blood to faraway cells, it’s endocrine."),
                                    html.Li("The signal causes a shape change in the receptor, switches on kinases, and turns genes on or off.")
                                ])
                            ])]
            },
            "q2": {
                "question": html.P("Be familiar with examples of the main types of cytoplasmic receptors including “Ion Channels”, “Protein Kinase Receptors” and “G protein-linked Receptors”.  Understand the specific activation process of these receptors and how the activation leads to signal transduction.  What are some of the general potential outcomes of these pathways (i.e. Insulin)?"),
                "overview": html.Div([
                                html.H4("Cytoplasmic and Membrane Receptors"),
                                html.P("Receptors detect signaling molecules and start cellular responses. Receptors can be cytoplasmic or membrane-bound depending on the nature of the ligand."),
                                html.Ul([
                                    html.Li([html.Strong("Cytoplasmic Receptors:"), " Bind small or nonpolar ligands like estrogen. Once bound, the receptor changes shape, enters the nucleus, and alters gene expression."]),
                                    html.Li([html.Strong("Ion Channels:"), " Act as gates that open when a signal is received, allowing ions to flow across the membrane (e.g. acetylcholine receptor)."]),
                                    html.Li([html.Strong("Protein Kinase Receptors:"), " Bind ligands like insulin. These receptors phosphorylate themselves and other proteins to activate a response."]),
                                    html.Li([html.Strong("G protein-linked Receptors:"), " Ligand binding changes the receptor's shape, activating a G protein that switches from GDP-bound (inactive) to GTP-bound (active)."])
                                ]),
                                html.P("These pathways can lead to a variety of responses such as altered gene expression, activation of transporters, and changes in cell behavior (e.g., insulin stimulates glucose uptake).")
                ]), 
                "deep_dive": html.Div([
                                html.H4("Activation and Function of Major Receptor Types"),
                                html.P([html.Strong("Cytoplasmic Receptors:"), " These bind small or nonpolar ligands that can pass through the plasma membrane. The ligand-receptor complex often moves into the nucleus to regulate gene transcription. An example is estrogen. Often, the receptor is initially bound to a chaperonin protein, which is released upon ligand binding."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/cytoplasmic receptor.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/biology/cell-signaling/mechanisms-of-cell-signaling/a/signal-perception", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Membrane Receptors:"), " These bind large or polar ligands that cannot enter the cell. They transmit signals by changing shape or interacting with intracellular proteins."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/membrane receptor.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.open.edu/openlearn/science-maths-technology/cell-signalling/content-section-1.3", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Ion Channels:"), " These membrane proteins open or close in response to a signal, allowing ions like Na⁺ or K⁺ to flow into or out of the cell. The acetylcholine receptor on muscle cells is a gated ion channel triggered by the neurotransmitter acetylcholine."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/ion channel.jpeg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.moleculardevices.com/applications/ion-channels", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Protein Kinase Receptors:"), " When a ligand like insulin binds, the receptor phosphorylates itself and downstream targets (like insulin response substrates). This triggers cellular effects, such as the insertion of glucose transporters into the cell membrane."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/protein kinase.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://digfir-published.macmillanusa.com/life11e/life11e_ch07_8.html", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("G Protein-linked Receptors:"), " Ligand binding changes the receptor shape, enabling it to bind to a G protein. The G protein swaps GDP for GTP, becoming active. It then interacts with downstream enzymes or channels to amplify and transmit the signal."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/G protein.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://ditki.com/course/cell-biology/glossary/cellular-anatomy-physiology/g-coupled-receptor", target = "_blank")])
                                    ]
                                ),
                                html.P("Each of these pathways can trigger gene expression changes, activate enzymes, or move molecules like glucose into cells, depending on the specific signal."),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Khan Academy Medicine: Ligand Gated Ion Channels", href = "https://www.youtube.com/watch?v=Pl7nzXaVqak&pp=ygUMaW9uIGNoYW5uZWxz", target = "_blank")]),
                                    html.Li([html.A("The Artful Medic: Ion Channels Explained", href = "https://www.youtube.com/watch?v=jTrGwO6CwZQ&pp=ygUMaW9uIGNoYW5uZWxz", target = "_blank")]),
                                    html.Li([html.A("biologyexams4u: 3 Types of Cell Surface Receptors", href = "https://www.youtube.com/watch?v=5EfX-FhewMc&pp=ygUYcHJvdGVpbiBraW5hc2UgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Professor Dave Explains: Receptors (Signal Transduction and Phosphorylation Cascade)", href = "https://www.youtube.com/watch?v=VatdTJka3_M&t=185s&pp=ygUYcHJvdGVpbiBraW5hc2UgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Dirty Medicine: Signal Transduction Pathways (G-Protein, Receptor Tyrosine Kinase, cGMP)", href = "https://www.youtube.com/watch?v=MoHQAyMGCFw&pp=ygUYcHJvdGVpbiBraW5hc2UgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Med Today: G Protein Coupled Receptors (GPCRs)", href = "https://www.youtube.com/watch?v=N7o0Fkz9iGE&pp=ygUaZy1wcm90ZWluIGxpbmtlZCByZWNlcHRvcnM%3D", target = "_blank")]),
                                    html.Li([html.A("Khan Academy Medicine: G Protein Coupled Receptors", href = "https://www.youtube.com/watch?v=ZBSo_GFN3qI&pp=ygUaZy1wcm90ZWluIGxpbmtlZCByZWNlcHRvcnM%3D", target = "_blank")]),
                                    html.Li([html.A("HeyNowScience: G-Protein Linked Receptors", href = "https://www.youtube.com/watch?v=XqJGivTYGWw&pp=ygUaZy1wcm90ZWluIGxpbmtlZCByZWNlcHRvcnM%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter7/Slide6.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide7.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide8.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide9.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide10.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide11.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide12.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide13.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide14.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter7question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of ligand can bind to cytoplasmic receptors?",
                        "options": ["Large and polar", "Small and nonpolar", "Only ions", "Proteins"],
                        "answer": "Small and nonpolar"
                    },
                    {
                        "question": "What happens to a cytoplasmic receptor after binding its ligand?",
                        "options": ["It breaks down the ligand", "It changes shape and enters the nucleus", "It activates a G protein", "It opens an ion channel"],
                        "answer": "It changes shape and enters the nucleus"
                    },
                    {
                        "question": "What is the role of chaperonin proteins in cytoplasmic receptor activation?",
                        "options": ["They help phosphorylate the receptor", "They release the receptor upon ligand binding", "They destroy excess ligands", "They carry ligands into the nucleus"],
                        "answer": "They release the receptor upon ligand binding"
                    },
                    {
                        "question": "Which of the following is a correct example of a ligand-receptor pair?",
                        "options": ["Estrogen – Membrane Receptor", "Insulin – Cytoplasmic Receptor", "Prolactin – Membrane Receptor", "Oxygen – Protein Kinase Receptor"],
                        "answer": "Prolactin – Membrane Receptor"
                    },
                    {
                        "question": "What type of receptor does insulin bind to?",
                        "options": ["G protein-linked receptor", "Cytoplasmic receptor", "Protein kinase receptor", "Ion channel"],
                        "answer": "Protein kinase receptor"
                    },
                    {
                        "question": "What happens when a protein kinase receptor binds its ligand?",
                        "options": ["It activates a G protein", "It opens a membrane pore", "It phosphorylates itself and other proteins", "It breaks down the ligand"],
                        "answer": "It phosphorylates itself and other proteins"
                    },
                    {
                        "question": "Which receptor type typically leads to changes in gene expression?",
                        "options": ["Ion channels", "G protein-linked receptors", "Cytoplasmic receptors", "All of the above"],
                        "answer": "Cytoplasmic receptors"
                    },
                    {
                        "question": "Which of the following is an example of a ligand that binds a gated ion channel?",
                        "options": ["Insulin", "Estrogen", "Acetylcholine", "Cortisol"],
                        "answer": "Acetylcholine"
                    },
                    {
                        "question": "What happens when acetylcholine binds its receptor on muscle cells?",
                        "options": ["A G protein is activated", "The receptor enters the nucleus", "The receptor opens and lets ions through", "Phosphate groups are added to DNA"],
                        "answer": "The receptor opens and lets ions through"
                    },
                    {
                        "question": "What is the function of a G protein in signal transduction?",
                        "options": ["Carries ligands into the cell", "Becomes phosphorylated by kinases", "Activates downstream effectors when bound to GTP", "Releases ions across the membrane"],
                        "answer": "Activates downstream effectors when bound to GTP"
                    },
                    {
                        "question": "What does a G protein do when it is activated?",
                        "options": ["Binds GDP", "Binds GTP", "Binds to DNA", "Releases a hormone"],
                        "answer": "Binds GTP"
                    },
                    {
                        "question": "Which type of receptor is associated with mobile membrane proteins made of three subunits?",
                        "options": ["Protein kinase receptor", "Ion channel", "G protein-linked receptor", "Steroid receptor"],
                        "answer": "G protein-linked receptor"
                    },
                    {
                        "question": "What kind of receptor changes its shape to open a passage for ions?",
                        "options": ["Cytoplasmic receptor", "G protein-linked receptor", "Protein kinase receptor", "Ion channel"],
                        "answer": "Ion channel"
                    },
                    {
                        "question": "What initiates the insertion of glucose transporters into the membrane in response to insulin?",
                        "options": ["Ion influx", "G protein activation", "Phosphorylation by a kinase receptor", "ATP hydrolysis"],
                        "answer": "Phosphorylation by a kinase receptor"
                    },
                    {
                        "question": "What kind of molecule can pass directly through the plasma membrane to bind intracellular receptors?",
                        "options": ["Glucose", "Estrogen", "Insulin", "Acetylcholine"],
                        "answer": "Estrogen"
                    },
                    {
                        "question": "Which receptor type is involved in activating second messengers like cAMP?",
                        "options": ["Ion channel", "Protein kinase receptor", "G protein-linked receptor", "Cytoplasmic receptor"],
                        "answer": "G protein-linked receptor"
                    },
                    {
                        "question": "What happens to a G protein when its receptor is activated by a ligand?",
                        "options": ["It enters the nucleus", "It binds GDP", "It swaps GDP for GTP", "It becomes an ion channel"],
                        "answer": "It swaps GDP for GTP"
                    },
                    {
                        "question": "What is a common cellular response to receptor activation?",
                        "options": ["Gene expression changes", "Membrane depolarization", "Transporter insertion", "All of the above"],
                        "answer": "All of the above"
                    },
                    {
                        "question": "Which of the following receptors does NOT typically involve phosphorylation?",
                        "options": ["G protein-linked receptor", "Protein kinase receptor", "Insulin receptor", "Cytoplasmic receptor"],
                        "answer": "G protein-linked receptor"
                    },
                    {
                        "question": "Which type of receptor can initiate a cascade that changes transcription in the nucleus?",
                        "options": ["G protein-linked receptor", "Ion channel", "Cytoplasmic receptor", "None of the above"],
                        "answer": "Cytoplasmic receptor"
                    }
                ],
                "blurting": [html.Div([
                                html.H4("Cytoplasmic and Membrane Receptors"),
                                html.P("Receptors detect signaling molecules and start cellular responses. Receptors can be cytoplasmic or membrane-bound depending on the nature of the ligand."),
                                html.Ul([
                                    html.Li([html.Strong("Cytoplasmic Receptors:"), " Bind small or nonpolar ligands like estrogen. Once bound, the receptor changes shape, enters the nucleus, and alters gene expression."]),
                                    html.Li([html.Strong("Ion Channels:"), " Act as gates that open when a signal is received, allowing ions to flow across the membrane (e.g. acetylcholine receptor)."]),
                                    html.Li([html.Strong("Protein Kinase Receptors:"), " Bind ligands like insulin. These receptors phosphorylate themselves and other proteins to activate a response."]),
                                    html.Li([html.Strong("G protein-linked Receptors:"), " Ligand binding changes the receptor's shape, activating a G protein that switches from GDP-bound (inactive) to GTP-bound (active)."])
                                ]),
                                html.P("These pathways can lead to a variety of responses such as altered gene expression, activation of transporters, and changes in cell behavior (e.g., insulin stimulates glucose uptake).")
                ])],
                "feynman": [html.Div([
                                html.P("Some molecules can pass into the cell and bind to receptors inside. Others are too big or charged, so they bind to receptors on the surface."),
                                html.Ul([
                                    html.Li("Small molecules like estrogen go into the cell and change what genes are turned on."),
                                    html.Li("Ion channels open up to let ions in or out, like turning on a faucet."),
                                    html.Li("Protein kinase receptors (like insulin) turn themselves on and pass the message by adding phosphate groups."),
                                    html.Li("G protein-linked receptors use a helper (G protein) that switches on when it grabs GTP and sends the message further.")
                                ])
                ])]
            },
            "q3": {
                "question": html.P("Be able to explain the mechanisms of action associated with cytoplasmic receptors. Be familiar with the names of different ligands that act through cytoplasmic receptors."),
                "overview": html.Div([
                                html.P("Cytoplasmic receptors bind signals that can pass through the plasma membrane. These signals are usually small and nonpolar."),
                                html.Ul([
                                    html.Li("Ligands include: estrogen, insulin, and cholesterol."),
                                    html.Li("After binding, the receptor undergoes a conformational change."),
                                    html.Li("The receptor-ligand complex enters the nucleus and alters gene expression."),
                                    html.Li("This leads to a change in the cell’s behavior or function.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Cytoplasmic receptors are specialized proteins found inside the cell. Because they are located in the cytoplasm, the signals (ligands) that activate them must be able to diffuse through the lipid bilayer of the cell membrane."),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/cytoplasmic receptor.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/biology/cell-signaling/mechanisms-of-cell-signaling/a/signal-perception", target = "_blank")])
                                    ]
                                ),
                                html.P("Typical ligands are small, nonpolar molecules like:"),
                                html.Ul([
                                    html.Li("Estrogen (a steroid hormone)"),
                                    html.Li("Cholesterol-derived molecules"),
                                    html.Li("Insulin (though insulin can also act via membrane-bound receptors in some contexts)")
                                ]),
                                html.P("Once the ligand binds, the receptor changes shape. This change allows the receptor-ligand complex to travel into the nucleus."),
                                html.P("Inside the nucleus, the receptor acts as a transcription factor. It binds to specific DNA sequences and regulates which genes are turned on or off. The resulting change in gene expression leads to changes in the cell’s function or behavior."),
                                html.Hr(), 
                                html.P([html.Strong("Mechanism of Action: Estrogen")]),
                                html.Ul([
                                    html.Li("Estrogen enters the cell. It can do so because it is a small, non-polar (lipid-soluble) molecule, which allows it to diffuse through the cell membrane"),
                                    html.Li("Estrogen binds to its cytoplasmic receptor (called the estrogen receptor, or ER), which is normally inactive if estrogen is not present"), 
                                    html.Li("After Estrogen binds, the receptor changes shape and becomes active. Two estrogen-receptor complexes will then come together to form a pair, called a dimer"), 
                                    html.Li("The dimer is able to enter the nucleus of the cell and will bind to specific DNA regions"), 
                                    html.Li("Binding to those regions activates the target genes, which will lead to the production of specific proteins")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/estrogen.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.researchgate.net/figure/A-simplified-schematic-diagram-of-intracellular-action-of-estrogens-via-estrogen-receptor_fig2_242358011", target = "_blank")])
                                    ]
                                ),
                                html.Hr(), 
                                html.P([html.Strong("Mechanism of Action: Insulin")]),
                                html.Ul([
                                    html.Li("Insulin is released in the bloodstream by the pancreas (beta cells) as blood glucose levels rise"), 
                                    html.Li("Insulin travels through the blood and binds to insulin receptors on or in target cells"),
                                    html.Li("Binding of insulin triggers a shape change (a conformational change) in the receptor"), 
                                    html.Li("This conformational change activates the receptor and triggers a cascade of phosphorylation events"), 
                                    html.Li("This chain of events ultimately leads to glucose transporter proteins being inserted into the cell membrane, usage or storage of glucose, protein synthesis, fat storage, and inhibition of glucose production in the liver"),
                                    html.Li("As blood sugar levels return to normal, insulin levels drop as receptors are deactivated and signaling stops")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/insulin.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.Div(["Image from ", html.A("here", href = "https://www.nature.com/articles/s41422-019-0185-0", target = "_blank")])
                                    ]
                                ),
                                html.Hr(), 
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Rebekah Borup: 11 Cytoplasmic Receptors", href = "https://www.youtube.com/watch?v=YYU2-Ds4i3E&pp=ygUVY3l0b3BsYXNtaWMgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Osmosis from Elsevier: Common Cell Signaling Pathways", href = "https://www.youtube.com/watch?v=9sF_h-bAnIE&t=137s&pp=ygUVY3l0b3BsYXNtaWMgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Amoeba Sisters: Intro to Cell Signaling", href = "https://www.youtube.com/watch?v=-dbRterutHY&pp=ygUVY3l0b3BsYXNtaWMgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Baylor Tutoring Center: Intracellular Receptors", href = "https://www.youtube.com/watch?v=c-Tonv0upT8&pp=ygUVY3l0b3BsYXNtaWMgcmVjZXB0b3Jz", target = "_blank")]),
                                    html.Li([html.A("Armando Hasudungan: Insulin Signaling Pathway", href = "https://www.youtube.com/watch?v=f_5DCfGKdaA&pp=ygUcaW5zdWxpbiBjeXRvcGxhc21pYyByZWNlcHRvctIHCQnYCQGHKiGM7w%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Hussain Biology: Estrogen Signaling Pathway", href = "https://www.youtube.com/watch?v=jctKiI1I63U&pp=ygUdZXN0cm9nZW4gY3l0b3BsYXNtaWMgcmVjZXB0b3I%3D", target = "_blank")]),
                                    html.Li([html.A("Nonstop Neuron: Nuclear Receptors and Signaling Pathway", href = "https://www.youtube.com/watch?v=T0-fRSvNWjE&pp=ygUdZXN0cm9nZW4gY3l0b3BsYXNtaWMgcmVjZXB0b3I%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter7/Slide12.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter7question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Where are cytoplasmic receptors located?",
                        "options": ["In the nucleus", "On the plasma membrane", "In the cytoplasm", "In the mitochondria"],
                        "answer": "In the cytoplasm"
                    },
                    {
                        "question": "What type of molecules typically bind to cytoplasmic receptors?",
                        "options": ["Large and polar", "Ions", "Small and nonpolar", "Proteins only"],
                        "answer": "Small and nonpolar"
                    },
                    {
                        "question": "What happens to a cytoplasmic receptor when it binds its ligand?",
                        "options": ["It opens a membrane channel", "It breaks the ligand apart", "It changes shape", "It activates a G protein"],
                        "answer": "It changes shape"
                    },
                    {
                        "question": "Where does a cytoplasmic receptor go after binding its ligand?",
                        "options": ["It remains in the cytoplasm", "It is secreted from the cell", "It enters the nucleus", "It is degraded by lysosomes"],
                        "answer": "It enters the nucleus"
                    },
                    {
                        "question": "What is the main role of a cytoplasmic receptor inside the nucleus?",
                        "options": ["To activate ion channels", "To alter gene expression", "To bind to ribosomes", "To break down mRNA"],
                        "answer": "To alter gene expression"
                    },
                    {
                        "question": "Which of the following is an example of a ligand that binds to a cytoplasmic receptor?",
                        "options": ["Estrogen", "Sodium", "Glucose", "ATP"],
                        "answer": "Estrogen"
                    },
                    {
                        "question": "What kind of change does a cytoplasmic receptor undergo after binding a ligand?",
                        "options": ["Conformational change", "Replication", "Translation", "Ionization"],
                        "answer": "Conformational change"
                    },
                    {
                        "question": "What effect does the ligand-receptor complex have in the nucleus?",
                        "options": ["Initiates transcription", "Blocks translation", "Synthesizes glucose", "Replicates DNA"],
                        "answer": "Initiates transcription"
                    },
                    {
                        "question": "What kind of hormone is estrogen?",
                        "options": ["Protein hormone", "Steroid hormone", "Peptide hormone", "Amine hormone"],
                        "answer": "Steroid hormone"
                    },
                    {
                        "question": "Which of the following best describes the signaling mechanism of cytoplasmic receptors?",
                        "options": ["They use G proteins", "They open membrane pores", "They regulate DNA transcription", "They trigger ion flow"],
                        "answer": "They regulate DNA transcription"
                    },
                    {
                        "question": "Why can ligands like estrogen bind to cytoplasmic receptors?",
                        "options": ["They are electrically charged", "They are very large", "They are lipid-soluble", "They are proteins"],
                        "answer": "They are lipid-soluble"
                    },
                    {
                        "question": "What is the end result of cytoplasmic receptor activation?",
                        "options": ["Receptor destruction", "Production of second messengers", "A change in gene expression", "Cell death"],
                        "answer": "A change in gene expression"
                    },
                    {
                        "question": "What part of the cell do cytoplasmic receptors help regulate after activation?",
                        "options": ["Mitochondria", "Golgi apparatus", "Nucleus", "Endoplasmic reticulum"],
                        "answer": "Nucleus"
                    },
                    {
                        "question": "What allows cytoplasmic ligands to cross the plasma membrane?",
                        "options": ["Carrier proteins", "Active transport", "Their small, nonpolar nature", "Endocytosis"],
                        "answer": "Their small, nonpolar nature"
                    },
                    {
                        "question": "Which of the following is NOT typically a cytoplasmic receptor ligand?",
                        "options": ["Cholesterol", "Insulin", "Estrogen", "Prolactin"],
                        "answer": "Prolactin"
                    },
                    {
                        "question": "What does a cytoplasmic receptor do once inside the nucleus?",
                        "options": ["Binds and activates GTP", "Releases Ca²⁺ ions", "Interacts with DNA", "Phosphorylates itself"],
                        "answer": "Interacts with DNA"
                    },
                    {
                        "question": "What kind of cell behavior can cytoplasmic receptors influence?",
                        "options": ["Gene transcription", "Signal termination", "Ion transport", "Phagocytosis"],
                        "answer": "Gene transcription"
                    },
                    {
                        "question": "How do cytoplasmic receptors contribute to cellular specificity?",
                        "options": ["Only some cells have the right receptors", "They all produce the same effect in all cells", "They require ATP to activate", "They use the sodium-potassium pump"],
                        "answer": "Only some cells have the right receptors"
                    },
                    {
                        "question": "What feature is common among cytoplasmic receptor ligands?",
                        "options": ["They are hydrophilic", "They are unable to diffuse through membranes", "They are often steroid-based", "They are protein-based only"],
                        "answer": "They are often steroid-based"
                    },
                    {
                        "question": "Which of the following is true about the insulin receptor?",
                        "options": ["It is strictly a cytoplasmic receptor", "It always acts through ion channels", "It may also act through membrane-bound pathways", "It binds inside the nucleus"],
                        "answer": "It may also act through membrane-bound pathways"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Cytoplasmic receptors bind signals that can pass through the plasma membrane. These signals are usually small and nonpolar."),
                                html.Ul([
                                    html.Li("Ligands include: estrogen, insulin, and cholesterol."),
                                    html.Li("After binding, the receptor undergoes a conformational change."),
                                    html.Li("The receptor-ligand complex enters the nucleus and alters gene expression."),
                                    html.Li("This leads to a change in the cell’s behavior or function.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Some signal molecules can sneak through the cell membrane."),
                                html.Ul([
                                    html.Li("They find a receptor inside the cell."),
                                    html.Li("Once they bind, the receptor changes shape and moves into the nucleus."),
                                    html.Li("There, it helps decide what genes should be turned on or off."),
                                    html.Li("This changes what the cell does."),
                                    html.Li("Examples: estrogen, insulin, cholesterol.")
                                ])
                ])]
            },
            "q4": {
                "question": html.P("Be familiar with the major components of the MAPK pathway.  Know how the players in this pathway become sequentially activated."),
                "overview": html.Div([
                                html.P("The MAPK pathway is a type of protein kinase cascade. One kinase activates the next in a sequence, amplifying the signal and ultimately leading to changes in gene expression."),
                                html.Ul([
                                    html.Li("The pathway starts with activation of RAS, a GTP-binding protein."),
                                    html.Li("RAS activates RAF (a kinase), which then activates MEK (another kinase)."),
                                    html.Li("MEK phosphorylates and activates MAPK, which enters the nucleus."),
                                    html.Li("MAPK acts as a transcription factor, altering gene expression.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("The MAPK pathway is a classic example of a kinase cascade: a signal triggers a series of phosphorylation events. The major components of the pathway are:"),
                                html.Ul([
                                    html.Li([html.Strong("RAS:"), " A GTPase that acts like a molecular switch. It is inactive when bound to GDP and becomes active when it binds GTP."]),
                                    html.Li([html.Strong("RAF:"), " A protein kinase that is activated by RAS and begins the phosphorylation cascade."]),
                                    html.Li([html.Strong("MEK:"), " A kinase that is phosphorylated by RAF and, in turn, phosphorylates MAPK."]),
                                    html.Li([html.Strong("MAPK:"), " A kinase that is phosphorylated by MEK. Once activated, it can enter the nucleus and regulate transcription."])
                                ]),
                                html.P("Here’s how it works step-by-step:"),
                                html.Ol([
                                    html.Li("A signal activates RAS, switching it from GDP-bound (inactive) to GTP-bound (active)."),
                                    html.Li("RAS activates RAF."),
                                    html.Li("RAF phosphorylates and activates MEK."),
                                    html.Li("MEK phosphorylates and activates MAPK."),
                                    html.Li("MAPK enters the nucleus and regulates gene expression, altering the cell’s response.")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/MAPK.png", style = {'marginRight':'40px'}),
                                        html.P("Image taken from Chapter 7 Lecture Slides")
                                    ]
                                ),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Animated Biology with Arpan: Ras-MAPK Pathway (Ras-MAPK in Cancer)", href = "https://www.youtube.com/watch?v=Pa11Jw0JAdk&pp=ygUWTUFQSyBzaWduYWxpbmcgY2FzY2FkZQ%3D%3D", target = "_blank")]),
                                    html.Li([html.A("JJ Medicine: Ras Raf MEK ERK Signaling Pathway", href = "https://www.youtube.com/watch?v=i1f2RbogiDw&pp=ygUWTUFQSyBzaWduYWxpbmcgY2FzY2FkZQ%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Hussain Biology: MAPK/ERK Signaling Pathway", href = "https://www.youtube.com/watch?v=thLsxvqDZ04&pp=ygUWTUFQSyBzaWduYWxpbmcgY2FzY2FkZQ%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Rethink Biology: MAPK Signaling Pathway", href = "https://www.youtube.com/watch?v=GrnSHDf8Zqo&pp=ygUWTUFQSyBzaWduYWxpbmcgY2FzY2FkZQ%3D%3D", target = "_blank")])
                                ])

                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter7/Slide13.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide14.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter7question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of signaling pathway is the MAPK pathway an example of?",
                        "options": ["G protein-coupled pathway", "Ligand-gated channel", "Protein kinase cascade", "Ion pump cascade"],
                        "answer": "Protein kinase cascade"
                    },
                    {
                        "question": "What does the protein RAS bind when it is active?",
                        "options": ["ATP", "GTP", "GDP", "Calcium"],
                        "answer": "GTP"
                    },
                    {
                        "question": "What is the function of RAS in the MAPK pathway?",
                        "options": ["Transcription factor", "Ion channel", "GTPase that activates RAF", "Kinase that activates MEK"],
                        "answer": "GTPase that activates RAF"
                    },
                    {
                        "question": "Which of the following sequences correctly orders the activation cascade in the MAPK pathway?",
                        "options": ["MAPK → MEK → RAF → RAS", "RAS → RAF → MEK → MAPK", "RAF → RAS → MEK → MAPK", "RAS → MEK → RAF → MAPK"],
                        "answer": "RAS → RAF → MEK → MAPK"
                    },
                    {
                        "question": "What kind of molecule is RAF?",
                        "options": ["Ion channel", "Ligand", "Protein kinase", "GTPase"],
                        "answer": "Protein kinase"
                    },
                    {
                        "question": "Which protein directly activates MEK?",
                        "options": ["RAS", "MAPK", "RAF", "GTP"],
                        "answer": "RAF"
                    },
                    {
                        "question": "Which protein enters the nucleus to regulate gene expression?",
                        "options": ["RAS", "RAF", "MEK", "MAPK"],
                        "answer": "MAPK"
                    },
                    {
                        "question": "What happens when RAS is bound to GDP?",
                        "options": ["It is active", "It activates MAPK", "It is inactive", "It enters the nucleus"],
                        "answer": "It is inactive"
                    },
                    {
                        "question": "Which of the following describes a function of MAPK?",
                        "options": ["Membrane transport", "DNA replication", "Transcription regulation", "Protein folding"],
                        "answer": "Transcription regulation"
                    },
                    {
                        "question": "What type of enzyme is MEK?",
                        "options": ["GTPase", "Ligase", "Kinase", "Protease"],
                        "answer": "Kinase"
                    },
                    {
                        "question": "What activates MAPK in the cascade?",
                        "options": ["RAS", "RAF", "MEK", "GTP"],
                        "answer": "MEK"
                    },
                    {
                        "question": "What is the functional role of a kinase in a signaling pathway?",
                        "options": ["To hydrolyze DNA", "To add phosphate groups to other proteins", "To bind mRNA", "To degrade proteins"],
                        "answer": "To add phosphate groups to other proteins"
                    },
                    {
                        "question": "How is the signal amplified in the MAPK pathway?",
                        "options": ["One protein activates many downstream proteins", "All proteins enter the nucleus", "The receptor is reused", "Calcium is released"],
                        "answer": "One protein activates many downstream proteins"
                    },
                    {
                        "question": "What activates RAF?",
                        "options": ["GTP-bound RAS", "GDP-bound RAS", "MAPK", "ATP"],
                        "answer": "GTP-bound RAS"
                    },
                    {
                        "question": "What role does phosphorylation play in the MAPK cascade?",
                        "options": ["Terminates the signal", "Reduces signal strength", "Activates the next kinase", "Breaks down the receptor"],
                        "answer": "Activates the next kinase"
                    },
                    {
                        "question": "Which protein in the MAPK pathway acts directly as a transcription factor?",
                        "options": ["RAS", "RAF", "MEK", "MAPK"],
                        "answer": "MAPK"
                    },
                    {
                        "question": "What kind of protein is RAS?",
                        "options": ["Receptor kinase", "Membrane channel", "GTPase", "Phosphatase"],
                        "answer": "GTPase"
                    },
                    {
                        "question": "What happens if MAPK is never activated?",
                        "options": ["RAS remains bound to GTP", "Gene expression changes will not occur", "The receptor becomes inactive", "Calcium channels open"],
                        "answer": "Gene expression changes will not occur"
                    },
                    {
                        "question": "Why is the MAPK pathway considered a cascade?",
                        "options": ["It causes water to enter the cell", "It releases many hormones", "Each protein activates another in a sequence", "It only functions once"],
                        "answer": "Each protein activates another in a sequence"
                    },
                    {
                        "question": "What is the main purpose of the MAPK signaling cascade?",
                        "options": ["To speed up cell division", "To increase glucose uptake", "To carry a signal from membrane to nucleus", "To produce ATP"],
                        "answer": "To carry a signal from membrane to nucleus"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The MAPK pathway is a type of protein kinase cascade. One kinase activates the next in a sequence, amplifying the signal and ultimately leading to changes in gene expression."),
                                html.Ul([
                                    html.Li("The pathway starts with activation of RAS, a GTP-binding protein."),
                                    html.Li("RAS activates RAF (a kinase), which then activates MEK (another kinase)."),
                                    html.Li("MEK phosphorylates and activates MAPK, which enters the nucleus."),
                                    html.Li("MAPK acts as a transcription factor, altering gene expression.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Imagine a line of falling dominoes. A signal flips RAS on by giving it GTP."),
                                html.Ul([
                                    html.Li("RAS turns on RAF."),
                                    html.Li("RAF turns on MEK."),
                                    html.Li("MEK turns on MAPK."),
                                    html.Li("MAPK goes into the nucleus and tells the cell which genes to turn on."),
                                    html.Li("Each step adds energy and makes the signal louder inside the cell.")
                                ])
                ])]
            }, 
            "q5": {
                "question": html.P("Know what a “Second Messenger” is and be able to give some examples (i.e. NO, cAMP, IP3, cGMP). Be able to explain how Acetylcholine leads to the formation of NO in endothelial cells.  Know how NO initiates relaxation in smooth muscle cells to cause vasodilation in arteries."),
                "overview": html.Div([
                                html.P("Second messengers are small molecules that amplify signals from membrane-bound receptors inside the cell."),
                                html.Ul([
                                    html.Li("Examples include: cAMP, cGMP, IP3, and nitric oxide (NO)."),
                                    html.Li("Epinephrine activates cAMP to trigger glucose release."),
                                    html.Li("Acetylcholine activates IP3, leading to Ca²⁺ influx and NO production."),
                                    html.Li("NO promotes cGMP formation, which causes smooth muscle relaxation and vasodilation.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Second messengers are internal signaling molecules produced in response to the activation of membrane receptors. These messengers amplify the initial signal and cause downstream cellular responses."),
                                html.P("Some common second messengers and their roles:"),
                                html.Ul([
                                    html.Li([html.Strong("cAMP:"), " Produced in response to epinephrine. Activates enzymes like glycogen phosphorylase, promoting glucose release from glycogen."]),
                                    html.Li([html.Strong("IP3:"), " A lipid-derived molecule that increases Ca²⁺ release from intracellular stores."]),
                                    html.Li([html.Strong("NO (Nitric Oxide):"), " A gas that diffuses between cells and activates cGMP production."]),
                                    html.Li([html.Strong("cGMP:"), " A second messenger that causes smooth muscle relaxation."])
                                ]),
                                html.P("One specific and important signaling sequence involves acetylcholine:"),
                                html.Ol([
                                    html.Li("Acetylcholine binds to receptors on endothelial cells (lining blood vessels)."),
                                    html.Li("This activates the IP3 pathway, releasing Ca²⁺ inside the endothelial cell."),
                                    html.Li("Calcium stimulates the production of NO (nitric oxide)."),
                                    html.Li("NO diffuses into adjacent smooth muscle cells."),
                                    html.Li("In smooth muscle, NO activates an enzyme that forms cGMP."),
                                    html.Li("cGMP causes the muscle to relax, leading to vasodilation (widening of blood vessels).")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/NO muscle relax.png", style = {'marginRight':'40px'}),
                                        html.P("Image taken from Chapter 7 Lecture Slides")
                                    ]
                                ),
                                html.P("This mechanism is important in cardiovascular function and is the basis of drugs like nitroglycerin and sildenafil (Viagra)."),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Osmosis from Elsevier: Common Cell Signaling Pathways", href = "https://www.youtube.com/watch?v=9sF_h-bAnIE&pp=ygUad2hhdCBhcmUgc2Vjb25kIG1lc3NlbmdlcnM%3D", target = "_blank")]),
                                    html.Li([html.A("Animated Biology with Arpan: Second Messengers (cAMP, cGMP, IP3, DAG, Calcium)", href = "https://www.youtube.com/watch?v=PzA5Z3DXfrQ&pp=ygURc2Vjb25kIG1lc3NlbmdlcnM%3D", target = "_blank")]),
                                    html.Li([html.A("Katharine Hubbard: Secondary Messengers in Cell Signaling", href = "https://www.youtube.com/watch?v=C0hiSbIMMGw&pp=ygURc2Vjb25kIG1lc3NlbmdlcnM%3D", target = "_blank")]),
                                    html.Li([html.A("Hussain Biology: Mechanism of Smooth Muscle Relaxation", href = "https://www.youtube.com/watch?v=F4n1IYq2kEc&pp=ygUZbml0cmljIG9jaWRlIG11c2NsZSByZWxhZNIHCQnYCQGHKiGM7w%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Metabolism Made Easy: Nitric Oxide and cGMP in Smooth Muscle Relaxation", href = "https://www.youtube.com/shorts/1_up9nrnvY4", target = "_blank")]),
                                    html.Li([html.A("Pharmacology Animation: Nitric Oxide Vasodilation", href = "https://www.youtube.com/watch?v=8ZbzSLFuLdY&t=165s&pp=ygUZbml0cmljIG9jaWRlIG11c2NsZSByZWxhZA%3D%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter7/Slide15.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide16.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide17.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide18.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide19.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide20.jpg"),
                    html.Img(src = "/assets/Chapter7/Slide21.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter7question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is a second messenger?",
                        "options": ["A hormone that binds to DNA", "A molecule that amplifies signals inside the cell", "An ion channel protein", "A membrane receptor"],
                        "answer": "A molecule that amplifies signals inside the cell"
                    },
                    {
                        "question": "Which of the following is NOT a second messenger?",
                        "options": ["cAMP", "NO", "IP3", "Insulin"],
                        "answer": "Insulin"
                    },
                    {
                        "question": "What triggers the production of cAMP in liver cells?",
                        "options": ["Acetylcholine binding", "Epinephrine binding to its receptor", "NO production", "Calcium influx"],
                        "answer": "Epinephrine binding to its receptor"
                    },
                    {
                        "question": "What enzyme is activated by cAMP to promote glucose release?",
                        "options": ["Glycogen phosphorylase", "Protein kinase A", "Adenylate cyclase", "Phospholipase C"],
                        "answer": "Glycogen phosphorylase"
                    },
                    {
                        "question": "Which signaling molecule activates the IP3 pathway in endothelial cells?",
                        "options": ["Epinephrine", "Acetylcholine", "Insulin", "Nitric oxide"],
                        "answer": "Acetylcholine"
                    },
                    {
                        "question": "What is the role of IP3 in the signaling pathway?",
                        "options": ["Activates adenylate cyclase", "Causes calcium release from intracellular stores", "Directly relaxes smooth muscle", "Binds to nuclear receptors"],
                        "answer": "Causes calcium release from intracellular stores"
                    },
                    {
                        "question": "How is nitric oxide (NO) produced in endothelial cells?",
                        "options": ["By adenylate cyclase", "In response to calcium increase triggered by IP3", "By protein kinase activation", "Through ligand binding to cytoplasmic receptors"],
                        "answer": "In response to calcium increase triggered by IP3"
                    },
                    {
                        "question": "What is the effect of nitric oxide on smooth muscle cells?",
                        "options": ["Triggers contraction", "Causes vasodilation by muscle relaxation", "Activates glycogen breakdown", "Blocks calcium channels"],
                        "answer": "Causes vasodilation by muscle relaxation"
                    },
                    {
                        "question": "What second messenger does NO stimulate the production of in smooth muscle cells?",
                        "options": ["cAMP", "cGMP", "IP3", "Calcium"],
                        "answer": "cGMP"
                    },
                    {
                        "question": "What physiological process results from smooth muscle relaxation caused by NO?",
                        "options": ["Vasoconstriction", "Vasodilation", "Cell proliferation", "Apoptosis"],
                        "answer": "Vasodilation"
                    },
                    {
                        "question": "Which molecule acts as the initial signal in acetylcholine-induced vasodilation?",
                        "options": ["NO", "IP3", "Calcium", "Acetylcholine"],
                        "answer": "Acetylcholine"
                    },
                    {
                        "question": "What is the main way cells regulate the balance of signaling by second messengers?",
                        "options": ["Synthesis and breakdown of enzymes", "Releasing hormones", "Opening ion channels", "Changing membrane potential"],
                        "answer": "Synthesis and breakdown of enzymes"
                    },
                    {
                        "question": "Which enzyme synthesizes cAMP upon epinephrine receptor activation?",
                        "options": ["Phospholipase C", "Adenylate cyclase", "Guanylate cyclase", "Protein kinase A"],
                        "answer": "Adenylate cyclase"
                    },
                    {
                        "question": "Which second messenger is directly responsible for triggering Ca²⁺ release inside cells?",
                        "options": ["cAMP", "IP3", "cGMP", "NO"],
                        "answer": "IP3"
                    },
                    {
                        "question": "How does NO move from endothelial cells to smooth muscle cells?",
                        "options": ["Through gap junctions", "By diffusion", "By vesicle transport", "Through ion channels"],
                        "answer": "By diffusion"
                    },
                    {
                        "question": "Which drug mimics the effects of NO to cause vasodilation?",
                        "options": ["Nitroglycerin", "Insulin", "Epinephrine", "Acetylcholine"],
                        "answer": "Nitroglycerin"
                    },
                    {
                        "question": "What is the role of cGMP in smooth muscle cells?",
                        "options": ["Stimulates contraction", "Activates protein kinase G leading to relaxation", "Inhibits glycogen breakdown", "Causes calcium influx"],
                        "answer": "Activates protein kinase G leading to relaxation"
                    },
                    {
                        "question": "Which of the following best describes acetylcholine’s role in vascular signaling?",
                        "options": ["Directly opens ion channels in smooth muscle", "Stimulates endothelial cells to produce NO", "Binds to cytoplasmic receptors", "Activates adenylate cyclase"],
                        "answer": "Stimulates endothelial cells to produce NO"
                    },
                    {
                        "question": "Why is nitric oxide considered a unique second messenger?",
                        "options": ["It is a protein", "It is a gas that diffuses freely across membranes", "It binds DNA", "It is stored in vesicles"],
                        "answer": "It is a gas that diffuses freely across membranes"
                    },
                    {
                        "question": "What causes the initial increase in intracellular calcium during acetylcholine signaling?",
                        "options": ["Opening of voltage-gated calcium channels", "IP3-mediated release from intracellular stores", "Calcium influx through ion channels", "Calcium synthesis"],
                        "answer": "IP3-mediated release from intracellular stores"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Second messengers are small molecules that amplify signals from membrane-bound receptors inside the cell."),
                                html.Ul([
                                    html.Li("Examples include: cAMP, cGMP, IP3, and nitric oxide (NO)."),
                                    html.Li("Epinephrine activates cAMP to trigger glucose release."),
                                    html.Li("Acetylcholine activates IP3, leading to Ca²⁺ influx and NO production."),
                                    html.Li("NO promotes cGMP formation, which causes smooth muscle relaxation and vasodilation.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Sometimes, the cell needs to pass a message from the outside of the membrane to the inside. That’s where second messengers come in."),
                                html.Ul([
                                    html.Li("Epinephrine tells liver cells to break down glycogen using cAMP."),
                                    html.Li("Acetylcholine starts a chain reaction using IP3 and calcium to make nitric oxide (NO)."),
                                    html.Li("NO floats into nearby muscle cells and makes cGMP."),
                                    html.Li("cGMP tells the muscle to relax, which opens up blood vessels."),
                                    html.Li("This helps lower blood pressure and improve blood flow.")
                                ])
                ])]
            },
            "q6": {
                "question": html.P("Be able to explain what the fluid mosaic model of membranes means.  Know the general components of a lipid bilayer."),
                "overview": html.Div([
                                html.P("The fluid mosaic model describes the cell membrane as a flexible, shifting 'sea' of phospholipids in which proteins float and move."),
                                html.Ul([
                                    html.Li("Membranes are composed mainly of phospholipids, proteins (peripheral and integral), cholesterol, glycoproteins, and glycolipids."),
                                    html.Li("Proteins can move laterally within the bilayer, making the membrane dynamic, not static."),
                                    html.Li("Membrane fluidity varies with lipid composition and temperature."),
                                    html.Li("Cells recognize and bind to each other using glycoproteins and glycolipids.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("The plasma membrane is primarily a bilayer of phospholipids, molecules with hydrophilic heads and hydrophobic tails."),
                                html.P("Key components include:"),
                                html.Ul([
                                    html.Li([html.Strong("Phospholipids:"), " Form the bilayer with hydrophobic tails inside and hydrophilic heads outside. Fatty acid chains vary in length and saturation, affecting membrane fluidity."]),
                                    html.Li([html.Strong("Cholesterol:"), " A steroid that modulates membrane fluidity and stability."]),
                                    html.Li([html.Strong("Peripheral proteins:"), " Associate loosely with membrane surfaces and do not penetrate the bilayer; lack exposed hydrophobic regions."]),
                                    html.Li([html.Strong("Integral proteins:"), " Embed within the bilayer; contain both hydrophobic and hydrophilic domains."]),
                                    html.Li([html.Strong("Transmembrane proteins:"), " A type of integral protein that spans the entire bilayer, often involved in transport and signaling."]),
                                    html.Li([html.Strong("Glycoproteins and glycolipids:"), " Carbohydrate groups attached to proteins or lipids, important for cell recognition and adhesion."])
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'}, 
                                    children = [
                                        html.Img(src = "/assets/plasma membrane.png", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.khanacademy.org/science/biology/structure-of-a-cell/prokaryotic-and-eukaryotic-cells/a/plasma-membrane-and-cytoplasm", target = "_blank")])
                                    ]
                                ),
                                html.P("Because the membrane is fluid, these proteins and lipids move laterally, allowing the membrane to adapt and function dynamically."),
                                html.P("Temperature and lipid composition influence how fluid or rigid the membrane is; unsaturated fatty acid tails increase fluidity, while saturated tails and cholesterol generally reduce it."),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/sat vs unsat.jpeg", style = {'marginRight':'20px', 'width':'400px'}),
                                        html.Div([html.P(["Image from ", html.A("here", href = "https://old-ib.bioninja.com.au/standard-level/topic-1-cell-biology/13-membrane-structure/membrane-fluidity.html", target = "_blank")])], style = {'marginRight':'20px'}),
                                        html.Img(src = "/assets/cholesterol.png", style = {'marginRight':'20px', 'width':'300px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.labxchange.org/library/items/lb:LabXchange:15be9659:html:1", target = "_blank")])
                                    ]
                                ),
                                html.P("Cells use glycoproteins and glycolipids on their surfaces to recognize other cells and stick together to form tissues."),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'}, 
                                    children = [
                                        html.Img(src = "/assets/glycoproteins and glycolipids.png", style = {'marginRight':'40px', 'width':'500px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.savemyexams.com/dp/biology/ib/23/hl/revision-notes/form-and-function/membranes-and-membrane-transport/glycolipids-and-glycoproteins/", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Amoeba Sisters: Inside the Cell Membrane", href = "https://www.youtube.com/watch?v=qBCVVszQQNs&t=272s&pp=ygUTZmx1aWQgbW9zYWljIG1vZGVsIA%3D%3D", target = "_blank")]),
                                    html.Li([html.A("FuseSchool - Global Education: Fluid Mosaic Model", href = "https://www.youtube.com/watch?v=ipa1vmQ7H_4&pp=ygUTZmx1aWQgbW9zYWljIG1vZGVsIA%3D%3D", target = "_blank")]),
                                    html.Li([html.A("The Organic Chemistry Tutor: Fluid Mosaic Model of the Plasma Membrane", href = "https://www.youtube.com/watch?v=xQjzPZZ4olE&t=4s&pp=ygUTZmx1aWQgbW9zYWljIG1vZGVsIA%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Fluid Mosaic Model of Cell Membranes", href = "https://www.youtube.com/watch?v=cP8iQu57dQo&pp=ygUTZmx1aWQgbW9zYWljIG1vZGVsIA%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Khan Academy Medicine: Cell Membrane Overview and Fluid Mosaic Model", href = "https://www.youtube.com/watch?v=LXaPt9i9hqk&pp=ygUTZmx1aWQgbW9zYWljIG1vZGVsIA%3D%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter6/Slide2.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide3.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter6question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does the fluid mosaic model describe?",
                        "options": ["A rigid, static membrane structure", "A flexible membrane with proteins floating in a lipid bilayer", "A membrane made only of proteins", "A membrane with no movement of molecules"],
                        "answer": "A flexible membrane with proteins floating in a lipid bilayer"
                    },
                    {
                        "question": "Which component forms the basic structure of the cell membrane?",
                        "options": ["Proteins", "Phospholipids", "Cholesterol", "Carbohydrates"],
                        "answer": "Phospholipids"
                    },
                    {
                        "question": "What is the main role of cholesterol in the membrane?",
                        "options": ["To increase membrane fluidity at all temperatures", "To stabilize and modulate membrane fluidity", "To form ion channels", "To act as a receptor"],
                        "answer": "To stabilize and modulate membrane fluidity"
                    },
                    {
                        "question": "Peripheral membrane proteins are characterized by:",
                        "options": ["Spanning the entire membrane", "Being embedded partially in the membrane", "Being loosely attached without penetrating the bilayer", "Having transmembrane domains"],
                        "answer": "Being loosely attached without penetrating the bilayer"
                    },
                    {
                        "question": "Integral membrane proteins:",
                        "options": ["Do not interact with the hydrophobic core", "Have both hydrophobic and hydrophilic regions", "Are only found outside the membrane", "Are always enzymes"],
                        "answer": "Have both hydrophobic and hydrophilic regions"
                    },
                    {
                        "question": "Which proteins extend completely through the lipid bilayer?",
                        "options": ["Peripheral proteins", "Integral proteins", "Transmembrane proteins", "Glycoproteins"],
                        "answer": "Transmembrane proteins"
                    },
                    {
                        "question": "Glycoproteins and glycolipids are important for:",
                        "options": ["Energy production", "Cell recognition and adhesion", "DNA replication", "Protein synthesis"],
                        "answer": "Cell recognition and adhesion"
                    },
                    {
                        "question": "Which factor affects membrane fluidity?",
                        "options": ["Temperature", "Protein synthesis", "DNA replication", "ATP production"],
                        "answer": "Temperature"
                    },
                    {
                        "question": "How do unsaturated fatty acid tails affect membrane fluidity?",
                        "options": ["Decrease fluidity by packing tightly", "Increase fluidity by introducing kinks", "Have no effect", "Make the membrane rigid"],
                        "answer": "Increase fluidity by introducing kinks"
                    },
                    {
                        "question": "What type of bond keeps the phospholipids together in the bilayer?",
                        "options": ["Covalent bonds", "Hydrogen bonds", "Hydrophobic interactions", "Ionic bonds"],
                        "answer": "Hydrophobic interactions"
                    },
                    {
                        "question": "Why is the membrane described as a 'mosaic'?",
                        "options": ["Because it is made of many different molecules like proteins and lipids", "Because it is rigid and uniform", "Because it contains only phospholipids", "Because it is crystalline"],
                        "answer": "Because it is made of many different molecules like proteins and lipids"
                    },
                    {
                        "question": "Which of the following is NOT a component of the plasma membrane?",
                        "options": ["Phospholipids", "Glycoproteins", "RNA", "Cholesterol"],
                        "answer": "RNA"
                    },
                    {
                        "question": "How do peripheral proteins attach to the membrane?",
                        "options": ["By embedding deeply in the lipid bilayer", "By weak interactions with integral proteins or lipids", "By covalent bonding to lipids", "By spanning the membrane"],
                        "answer": "By weak interactions with integral proteins or lipids"
                    },
                    {
                        "question": "What happens to membrane fluidity at lower temperatures?",
                        "options": ["It increases", "It decreases", "It stays the same", "It becomes infinite"],
                        "answer": "It decreases"
                    },
                    {
                        "question": "Which statement about integral proteins is true?",
                        "options": ["They are always enzymes", "They never move within the membrane", "They have regions that interact with both the lipid bilayer and the aqueous environment", "They are only found on the membrane surface"],
                        "answer": "They have regions that interact with both the lipid bilayer and the aqueous environment"
                    },
                    {
                        "question": "What role do glycolipids play in the membrane?",
                        "options": ["Signal transduction", "Cell recognition", "Energy storage", "DNA repair"],
                        "answer": "Cell recognition"
                    },
                    {
                        "question": "How does cholesterol affect the membrane at high temperatures?",
                        "options": ["Makes it more fluid", "Makes it less fluid", "Has no effect", "Removes proteins"],
                        "answer": "Makes it less fluid"
                    },
                    {
                        "question": "Which part of the phospholipid is hydrophilic?",
                        "options": ["Fatty acid tails", "Glycerol backbone", "Phosphate head group", "All parts are hydrophobic"],
                        "answer": "Phosphate head group"
                    },
                    {
                        "question": "What kind of movement is typical for membrane lipids and proteins?",
                        "options": ["Lateral movement within the membrane", "Movement across the membrane from inside to outside", "No movement", "Random jumping off the membrane"],
                        "answer": "Lateral movement within the membrane"
                    },
                    {
                        "question": "Cell adhesion and recognition are primarily mediated by:",
                        "options": ["Integral proteins", "Cholesterol", "Glycoproteins and glycolipids", "Phospholipids"],
                        "answer": "Glycoproteins and glycolipids"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The fluid mosaic model describes the cell membrane as a flexible, shifting 'sea' of phospholipids in which proteins float and move."),
                                html.Ul([
                                    html.Li("Membranes are composed mainly of phospholipids, proteins (peripheral and integral), cholesterol, glycoproteins, and glycolipids."),
                                    html.Li("Proteins can move laterally within the bilayer, making the membrane dynamic, not static."),
                                    html.Li("Membrane fluidity varies with lipid composition and temperature."),
                                    html.Li("Cells recognize and bind to each other using glycoproteins and glycolipids.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Think of the cell membrane like a waterbed full of floating icebergs."),
                                html.Ul([
                                    html.Li("The water is the phospholipid bilayer — it’s fluid and lets things move around."),
                                    html.Li("The icebergs are proteins — some float on the surface (peripheral), some stick halfway in, and some go all the way through (transmembrane)."),
                                    html.Li("Cholesterol is like little pebbles that keep the waterbed from getting too soft or too stiff."),
                                    html.Li("Carbohydrates on proteins and lipids help cells recognize and stick to each other."),
                                    html.Li("This whole setup lets the membrane be flexible but still strong and functional.")
                                ])
                ])]
            },
            "q7": {
                "question": html.P("Be familiar with the 3 different types of cell junctions: Tight junctions, desmosomes and gap junctions.  Know the differences in their specific functions."),
                "overview": html.Div([
                                html.P("Cells connect to each other using specialized junctions that serve different functions in maintaining tissue structure and communication."),
                                html.Ul([
                                    html.Li("Tight junctions create a seal between epithelial cells, preventing the passage of materials between them."),
                                    html.Li("Desmosomes act like spot welds, holding cells tightly together but still allowing materials to pass around them."),
                                    html.Li("Gap junctions form channels that let molecules and signals pass directly between adjacent cells, enabling communication.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Cell junctions are critical for maintaining the integrity and function of tissues by connecting adjacent cells."),
                                html.Ul([
                                    html.Li([html.Strong("Tight Junctions:"), 
                                            " These junctions seal the space between epithelial cells tightly like a quilted barrier, ensuring directional movement of substances and preventing leaks." ]),
                                    html.Li([html.Strong("Desmosomes:"), 
                                            " Known as 'spot welds', they provide strong mechanical attachments between cells, allowing tissues to resist stretching and shearing forces. They link cells tightly but permit extracellular fluid and materials to move in the spaces around them." ]),
                                    html.Li([html.Strong("Gap Junctions:"), 
                                            " Consist of channels called connexons that directly connect the cytoplasm of adjacent cells, allowing ions, nutrients, and signaling molecules to pass through for cell-to-cell communication." ])
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/junctions.png", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.researchgate.net/figure/Epithelial-intercellular-junctions-Schematic-drawing-of-the-epithelial-junction-in_fig1_330565608", target = "_blank")])
                                    ]
                                ),
                                html.P("Don't worry about adheren junctions -- while they are important, we do not cover them at this time!"),
                                html.P("Each type of junction serves a unique role: tight junctions maintain barriers, desmosomes provide strength, and gap junctions enable rapid communication."),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Khan Academy Medicine: Cell Junctions", href = "https://www.youtube.com/watch?v=pVWQm-GYK_Y&pp=ygUOY2VsbCBqdW5jdGlvbnM%3D", target = "_blank")]),
                                    html.Li([html.A("Ninja Nerd: Cell Junctions", href = "https://www.youtube.com/watch?v=gmlA8V2zMv4&pp=ygUOY2VsbCBqdW5jdGlvbnM%3D", target = "_blank")]),
                                    html.Li([html.A("Hussain Biology: Cell Junctions", href = "https://www.youtube.com/watch?v=zZESsZZvhVk&pp=ygUOY2VsbCBqdW5jdGlvbnM%3D", target = "_blank")]),
                                    html.Li([html.A("Scientist Cindy: Cell Junctions for Anatomy and Physiology (Gap, Cadherens, Adherens, Anchoring, Tight Junctions)", href = "https://www.youtube.com/watch?v=WYU_CJCqMEM&pp=ygUOY2VsbCBqdW5jdGlvbnM%3D", target = "_blank")]),
                                    html.Li([html.A("Whats Up Dude: Cell Connections (How Cells Are Connected, What Are Cell Junctions, Types of Cell Connections)", href = "https://www.youtube.com/watch?v=zzP87Zdf9ik&pp=ygUOY2VsbCBqdW5jdGlvbnM%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter6/Slide7.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide8.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide9.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter6question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the primary function of tight junctions?",
                        "options": ["Allow communication between cells", "Hold cells together strongly", "Create a seal to prevent material passage between cells", "Anchor cells to the extracellular matrix"],
                        "answer": "Create a seal to prevent material passage between cells"
                    },
                    {
                        "question": "Desmosomes are best described as:",
                        "options": ["Channels for molecule passage", "Seals that prevent leakage", "Spot welds that hold cells tightly together", "Receptors for signal transduction"],
                        "answer": "Spot welds that hold cells tightly together"
                    },
                    {
                        "question": "Gap junctions primarily function to:",
                        "options": ["Provide mechanical strength", "Create a waterproof barrier", "Allow passage of molecules and signals between adjacent cells", "Transport materials outside the cell"],
                        "answer": "Allow passage of molecules and signals between adjacent cells"
                    },
                    {
                        "question": "Which type of junction prevents dissolved materials from passing between epithelial cells?",
                        "options": ["Desmosomes", "Tight junctions", "Gap junctions", "Hemidesmosomes"],
                        "answer": "Tight junctions"
                    },
                    {
                        "question": "What allows gap junctions to enable cell-to-cell communication?",
                        "options": ["Connexons forming channels", "Tight sealing proteins", "Spot weld proteins", "Ligand binding"],
                        "answer": "Connexons forming channels"
                    },
                    {
                        "question": "Desmosomes allow materials to move:",
                        "options": ["Through the cells", "Between cells in the intercellular space", "Only inside the nucleus", "Only through gap junctions"],
                        "answer": "Between cells in the intercellular space"
                    },
                    {
                        "question": "Which cell junction acts like a 'quilted' seal?",
                        "options": ["Tight junction", "Desmosome", "Gap junction", "Adhesion junction"],
                        "answer": "Tight junction"
                    },
                    {
                        "question": "The strength provided by desmosomes helps tissues resist:",
                        "options": ["Chemical signals", "Stretching and shearing forces", "Water movement", "Electrical impulses"],
                        "answer": "Stretching and shearing forces"
                    },
                    {
                        "question": "Which junction type is found primarily in epithelial tissues to prevent leaks?",
                        "options": ["Gap junctions", "Desmosomes", "Tight junctions", "Plasmodesmata"],
                        "answer": "Tight junctions"
                    },
                    {
                        "question": "Which of the following is NOT a function of cell junctions?",
                        "options": ["Allow cell communication", "Provide mechanical strength", "Seal spaces between cells", "Produce energy for the cell"],
                        "answer": "Produce energy for the cell"
                    },
                    {
                        "question": "Which junction type forms direct cytoplasmic connections between adjacent cells?",
                        "options": ["Tight junction", "Gap junction", "Desmosome", "Hemidesmosome"],
                        "answer": "Gap junction"
                    },
                    {
                        "question": "What type of proteins primarily make up tight junctions?",
                        "options": ["Connexins", "Cadherins", "Claudins and occludins", "Integrins"],
                        "answer": "Claudins and occludins"
                    },
                    {
                        "question": "Desmosomes connect cells by linking to:",
                        "options": ["Microfilaments", "Intermediate filaments", "Microtubules", "Actin filaments"],
                        "answer": "Intermediate filaments"
                    },
                    {
                        "question": "Which junction type would most likely be involved in electrical signaling between heart muscle cells?",
                        "options": ["Tight junctions", "Desmosomes", "Gap junctions", "Adhesion junctions"],
                        "answer": "Gap junctions"
                    },
                    {
                        "question": "How do tight junctions contribute to directional movement of materials?",
                        "options": ["By sealing the space between cells to prevent leakage", "By transporting molecules through channels", "By signaling neighboring cells", "By mechanically linking cells together"],
                        "answer": "By sealing the space between cells to prevent leakage"
                    },
                    {
                        "question": "Which of the following is true about gap junctions?",
                        "options": ["They are impermeable to ions", "They allow direct exchange of small molecules", "They are the strongest type of cell junction", "They prevent passage of all substances"],
                        "answer": "They allow direct exchange of small molecules"
                    },
                    {
                        "question": "Which cell junction type is most responsible for maintaining tissue integrity during mechanical stress?",
                        "options": ["Tight junctions", "Desmosomes", "Gap junctions", "Adherens junctions"],
                        "answer": "Desmosomes"
                    },
                    {
                        "question": "What is the main structural difference between desmosomes and tight junctions?",
                        "options": ["Desmosomes form seals; tight junctions form spot welds", "Desmosomes form spot welds; tight junctions form seals", "Both form channels", "Both allow molecule passage"],
                        "answer": "Desmosomes form spot welds; tight junctions form seals"
                    },
                    {
                        "question": "Which cell junction type would most likely be found in cardiac muscle cells?",
                        "options": ["Tight junctions", "Desmosomes and gap junctions", "Only tight junctions", "Only desmosomes"],
                        "answer": "Desmosomes and gap junctions"
                    },
                    {
                        "question": "What role do gap junctions play in nutrient distribution?",
                        "options": ["Block nutrients", "Allow nutrients to pass between adjacent cells", "Store nutrients", "Digest nutrients"],
                        "answer": "Allow nutrients to pass between adjacent cells"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Cells connect to each other using specialized junctions that serve different functions in maintaining tissue structure and communication."),
                                html.Ul([
                                    html.Li("Tight junctions create a seal between epithelial cells, preventing the passage of materials between them."),
                                    html.Li("Desmosomes act like spot welds, holding cells tightly together but still allowing materials to pass around them."),
                                    html.Li("Gap junctions form channels that let molecules and signals pass directly between adjacent cells, enabling communication.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Imagine cells in a tissue as neighbors in a community."),  
                                html.Ul([
                                    html.Li("Tight junctions are like fences that keep neighbors' yards separate and prevent anything from leaking between them."),
                                    html.Li("Desmosomes are like strong bolts or spot welds holding houses tightly together so they don’t fall apart."),
                                    html.Li("Gap junctions are like windows or tunnels allowing neighbors to pass messages and things back and forth."),
                                    html.Li("Together, these junctions keep the community organized, strong, and well-connected.")
                                ])
                ])]
            },
            "q8": {
                "question": html.P("Understand the concept diffusion/osmosis and the factors that affect their rates.  Know the terms hypertonic, isotonic and hypotonic."),
                "overview": html.Div([
                                html.P("Diffusion is the movement of solutes from high to low concentration until equilibrium is reached. Osmosis is the movement of water across a membrane toward higher solute concentration."),
                                html.Ul([
                                    html.Li("Diffusion rate depends on solute size, concentration gradient, and temperature."),
                                    html.Li("Simple diffusion allows small, nonpolar molecules to pass through membranes."),
                                    html.Li("Osmosis moves water from regions of high water concentration to low water concentration."),
                                    html.Li("Tonicity describes relative solute concentrations: hypertonic (higher solute), hypotonic (lower solute), isotonic (equal solute).")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Diffusion is a passive transport process where solutes move down their concentration gradient."),
                                html.P("Factors influencing diffusion include:"),
                                html.Ul([
                                    html.Li("Diameter of solute molecules: smaller molecules diffuse faster."),
                                    html.Li("Concentration gradient: greater differences speed diffusion."),
                                    html.Li("Temperature: higher temperatures increase molecular motion and diffusion rates.")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/diffusion.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://biologydictionary.net/diffusion/", target = "_blank")])
                                    ]
                                ),
                                html.P("Simple diffusion allows lipid-soluble or very small molecules (like oxygen, carbon dioxide, and water) to cross membranes without assistance."),
                                html.P("Polar or charged molecules generally cannot cross membranes easily by simple diffusion."),
                                html.P("Osmosis is the diffusion of water through a selectively permeable membrane toward an area of higher solute concentration, or equivalently, lower water potential."),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/osmosis.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://en.wikipedia.org/wiki/Osmosis", target = "_blank")])
                                    ]
                                ),
                                html.P("Tonicity refers to the relative concentration of solutes between two solutions:"),
                                html.Ul([
                                    html.Li([html.Strong("Hypertonic:"), " solution has higher solute concentration than another."]),
                                    html.Li([html.Strong("Hypotonic:"), " solution has lower solute concentration than another."]),
                                    html.Li([html.Strong("Isotonic:"), " solutions have equal solute concentration."])
                                ]),
                                html.P("Different tonicity will cause cells to behave in different ways:"),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/tonicity.png", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.labxchange.org/library/items/lb:LabXchange:1c15140a:lx_image:1", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Amoeba Sisters: Diffusion", href = "https://www.youtube.com/watch?v=jhszFBtBPoI&pp=ygUJZGlmZnVzaW9u", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Diffusion and Osmosis (Membranes and Transport)", href = "https://www.youtube.com/watch?v=aubZU0iWtgI&pp=ygUJZGlmZnVzaW9u", target = "_blank")]),
                                    html.Li([html.A("Nonstop Neuron: Diffusion (Simple Diffusion vs Facilitated Diffusion, Factors Affecting Rate of Diffution)", href = "https://www.youtube.com/watch?v=tSKWtj2S2QU&pp=ygUJZGlmZnVzaW9u", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Diffusion (Membranes and Transport)", href = "https://www.youtube.com/watch?v=a_Y9wBQ610o&pp=ygUJZGlmZnVzaW9u", target = "_blank")]),
                                    html.Li([html.A("Amoeba Sisters: Osmosis and Water Potential", href = "https://www.youtube.com/watch?v=L-osEc07vMs&pp=ygUHb3Ntb3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Cognito: GCSE Biology - Osmosis", href = "https://www.youtube.com/watch?v=vCJVXYmXkzM&pp=ygUUb3Ntb3NpcyBjcmFzaCBjb3Vyc2U%3D", target = "_blank")])     
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter6/Slide10.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide11.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide12.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide13.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter6question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is diffusion?",
                        "options": ["Movement of solutes from low to high concentration", "Movement of solutes from high to low concentration", "Movement of water across a membrane", "Energy-requiring transport"],
                        "answer": "Movement of solutes from high to low concentration"
                    },
                    {
                        "question": "Which factor does NOT affect the rate of diffusion?",
                        "options": ["Diameter of solute molecules", "Concentration gradient", "Temperature", "Color of solute molecules"],
                        "answer": "Color of solute molecules"
                    },
                    {
                        "question": "Simple diffusion allows which molecules to pass through the membrane easily?",
                        "options": ["Large polar molecules", "Small nonpolar molecules", "Charged ions", "Proteins"],
                        "answer": "Small nonpolar molecules"
                    },
                    {
                        "question": "What is osmosis?",
                        "options": ["Movement of solutes from high to low concentration", "Movement of water across a membrane from low to high solute concentration", "Active transport of ions", "Bulk transport of proteins"],
                        "answer": "Movement of water across a membrane from low to high solute concentration"
                    },
                    {
                        "question": "Water moves toward the solution with:",
                        "options": ["Higher water concentration", "Lower water concentration", "Equal water concentration", "No solutes"],
                        "answer": "Lower water concentration"
                    },
                    {
                        "question": "A hypertonic solution has:",
                        "options": ["Lower solute concentration than another solution", "Higher solute concentration than another solution", "Equal solute concentration to another solution", "No solutes at all"],
                        "answer": "Higher solute concentration than another solution"
                    },
                    {
                        "question": "What happens to a cell placed in a hypotonic solution?",
                        "options": ["It shrinks", "It swells", "It stays the same size", "It becomes rigid"],
                        "answer": "It swells"
                    },
                    {
                        "question": "An isotonic solution means:",
                        "options": ["Solute concentration is higher outside the cell", "Solute concentration is lower outside the cell", "Solute concentration is equal inside and outside the cell", "No solute is present"],
                        "answer": "Solute concentration is equal inside and outside the cell"
                    },
                    {
                        "question": "Which type of molecule generally cannot pass through the membrane by simple diffusion?",
                        "options": ["Oxygen", "Carbon dioxide", "Glucose", "Water"],
                        "answer": "Glucose"
                    },
                    {
                        "question": "Increasing temperature generally:",
                        "options": ["Decreases diffusion rate", "Increases diffusion rate", "Has no effect", "Stops diffusion"],
                        "answer": "Increases diffusion rate"
                    },
                    {
                        "question": "Which of the following best describes the driving force behind diffusion?",
                        "options": ["Active transport", "Concentration gradient", "Energy input", "Membrane pumps"],
                        "answer": "Concentration gradient"
                    },
                    {
                        "question": "Osmosis is specifically the diffusion of:",
                        "options": ["Solutes", "Water", "Proteins", "Lipids"],
                        "answer": "Water"
                    },
                    {
                        "question": "In osmosis, water moves toward:",
                        "options": ["Higher water potential", "Lower water potential", "Lower solute concentration", "Equal solute concentration"],
                        "answer": "Lower water potential"
                    },
                    {
                        "question": "What limits the passage of electrically charged molecules across the membrane by simple diffusion?",
                        "options": ["Membrane polarity", "Molecule size", "Membrane thickness", "Molecule charge"],
                        "answer": "Molecule charge"
                    },
                    {
                        "question": "Which solution would cause a red blood cell to shrink?",
                        "options": ["Hypotonic", "Isotonic", "Hypertonic", "None of the above"],
                        "answer": "Hypertonic"
                    },
                    {
                        "question": "Which of the following molecules can freely diffuse across the membrane?",
                        "options": ["Glucose", "Na+ ions", "Oxygen", "Proteins"],
                        "answer": "Oxygen"
                    },
                    {
                        "question": "The concentration gradient is the difference in:",
                        "options": ["Temperature between two regions", "Solute concentration between two regions", "Pressure between two regions", "pH between two regions"],
                        "answer": "Solute concentration between two regions"
                    },
                    {
                        "question": "What term describes a solution with equal solute concentration compared to the cell?",
                        "options": ["Hypotonic", "Hypertonic", "Isotonic", "None of the above"],
                        "answer": "Isotonic"
                    },
                    {
                        "question": "Which of these factors would increase the rate of diffusion?",
                        "options": ["Larger solute molecules", "Smaller concentration gradient", "Higher temperature", "Lower temperature"],
                        "answer": "Higher temperature"
                    },
                    {
                        "question": "Why can water pass through the membrane by simple diffusion despite being polar?",
                        "options": ["It is very small", "It has no charge", "It binds to lipids", "It is nonpolar"],
                        "answer": "It is very small"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Diffusion is the movement of solutes from high to low concentration until equilibrium is reached. Osmosis is the movement of water across a membrane toward higher solute concentration."),
                                html.Ul([
                                    html.Li("Diffusion rate depends on solute size, concentration gradient, and temperature."),
                                    html.Li("Simple diffusion allows small, nonpolar molecules to pass through membranes."),
                                    html.Li("Osmosis moves water from regions of high water concentration to low water concentration."),
                                    html.Li("Tonicity describes relative solute concentrations: hypertonic (higher solute), hypotonic (lower solute), isotonic (equal solute).")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Imagine a crowded room where people want to spread out evenly—that's diffusion."),
                                html.Ul([
                                    html.Li("Diffusion moves stuff from where there's a lot to where there's less, like perfume spreading in air."),
                                    html.Li("Osmosis is water moving toward where there's more stuff dissolved, to balance things out."),
                                    html.Li("If a cell is in a salty (hypertonic) solution, water leaves the cell."),
                                    html.Li("If a cell is in pure water (hypotonic), water rushes in."),
                                    html.Li("If the concentration is equal (isotonic), water moves in and out evenly, so the cell stays the same.")
                                ])
                ])]
            },
            "q9": {
                "question": html.P("Be able to explain the difference between facilitated diffusion and primary/secondary active transport across membranes.  Be prepared to give specific examples of transporters for each."),
                "overview": html.Div([
                                html.P("Cells move substances across membranes using passive and active mechanisms. Facilitated diffusion helps polar molecules cross membranes without energy, while active transport requires energy to move substances against their concentration gradients."),
                                html.Ul([
                                    html.Li([html.Strong("Facilitated Diffusion:"), " passive transport that uses transmembrane proteins to help polar molecules move across the membrane (e.g., glucose transporters)."]),
                                    html.Li([html.Strong("Primary Active Transport:"), " uses ATP directly to move substances against their concentration gradient (e.g., sodium-potassium pump)."]),
                                    html.Li([html.Strong("Secondary Active Transport:"), " uses a proton or ion gradient established by primary transport to move other substances (e.g., glucose or amino acid uptake)."])
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Facilitated diffusion enables molecules that cannot cross the lipid bilayer on their own—usually polar or charged molecules—to move passively with the help of membrane proteins."),
                                html.P("Key types of proteins used in facilitated diffusion include:"),
                                html.Ul([
                                    html.Li([html.Strong("Channel Proteins:"), " create water-filled pores lined with polar amino acids. Example: ", html.Em("aquaporins")]),
                                    html.Li([html.Strong("Ion Channels:"), " allow specific ions to pass; can be gated (ligand-gated or voltage-gated). Voltage-gated channels respond to membrane potential."]),
                                    html.Li([html.Strong("Carrier Proteins:"), " bind specific molecules and undergo conformational changes to shuttle them across the membrane."])
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/facilitated diffusion.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.biologyonline.com/dictionary/facilitated-diffusion", target = "_blank")])
                                    ]
                                ),
                                html.P("Active transport moves substances against the concentration gradient, which requires energy."),
                                html.Ul([
                                    html.Li([html.Strong("Primary Active Transport:"), " uses ATP to pump substances across membranes."]),
                                    html.Li("Example: sodium-potassium pump (Na+/K+ antiporter) moves 3 Na+ out and 2 K+ in using ATP."),
                                    html.Li([html.Strong("Secondary Active Transport:"), " uses the electrochemical gradient created by primary active transport to power the transport of other molecules."]),
                                    html.Li("Example: protons pumped out by ATPase create a gradient that can bring glucose or amino acids into the cell via symporters.")
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/primary v secondary.jpg", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://digfir-published.macmillanusa.com/life11e/life11e_ch06_22.html", target = "_blank")])
                                    ]
                                ), 
                                html.P("Three functional classes of transport proteins used in active transport:"),
                                html.Ul([
                                    html.Li([html.Strong("Uniporter:"), " transports one substance in one direction."]),
                                    html.Li([html.Strong("Symporter:"), " transports two substances in the same direction."]),
                                    html.Li([html.Strong("Antiporter:"), " transports two substances in opposite directions."])
                                ]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/uni sym anti.png", style = {'marginRight':'40px', 'width':'600px'}),
                                        html.P(["Image from ", html.A("here", href = "https://neurotext.library.stonybrook.edu/C1/C1_7/C1_7.html", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("Amoeba Sisters: Cell Transport", href = "https://www.youtube.com/watch?v=Ptmlvtei8hw&pp=ygUpZmFjaWxpdGF0ZWQgZGlmZnVzaW9uIHZzIGFjdGl2ZSB0cmFuc3BvcnQ%3D", target = "_blank")]),
                                    html.Li([html.A("Mr Pollock: Diffusion, Facilitated Diffusion, and Active Transport", href = "https://www.youtube.com/watch?v=UgN76naeA1Q&pp=ygUpZmFjaWxpdGF0ZWQgZGlmZnVzaW9uIHZzIGFjdGl2ZSB0cmFuc3BvcnQ%3D", target = "_blank")]),
                                    html.Li([html.A("MooMooMath and Science: Cell Transport (Passive and Active Transport)", href = "https://www.youtube.com/watch?v=OmJwEi9ZuL0&pp=ygUpZmFjaWxpdGF0ZWQgZGlmZnVzaW9uIHZzIGFjdGl2ZSB0cmFuc3BvcnQ%3D", target = "_blank")]),
                                    html.Li([html.A("GHC Biology: Active Transport (Primary and Secondary)", href = "https://www.youtube.com/watch?v=xmXCswxPjQg&pp=ygUtcHJpbWFyeSBhY3RpdmUgYW5kIHNlY29uZGFyeSBhY3RpdmUgdHJhbnNwb3J0", target = "_blank")]),
                                    html.Li([html.A("Nonstop Neuron: Primary Active Transport vs Secondary Active Transport", href = "https://www.youtube.com/watch?v=N-iBdwtQn4Q&pp=ygUtcHJpbWFyeSBhY3RpdmUgYW5kIHNlY29uZGFyeSBhY3RpdmUgdHJhbnNwb3J0", target = "_blank")]),
                                    html.Li([html.A("LabXchange: Carrier Proteins (Uniporters, Symporters, and Antiporters)", href = "https://www.youtube.com/watch?v=j-9z_p9yly0&pp=ygUedW5pcG9ydGVyIHN5bXBvcnRlciBhbnRpcG9ydGVy", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Uniporters, Symporters, and Antiporters", href = "https://www.youtube.com/watch?v=-aGYytZ7K7M&pp=ygUedW5pcG9ydGVyIHN5bXBvcnRlciBhbnRpcG9ydGVy", target = "_blank")]),
                                    html.Li([html.A("Nonstop Neuron: Transport Proteins (Pumps, Channels, and Carriers)", href = "https://www.youtube.com/watch?v=A9ihz5gYxU4&pp=ygUedW5pcG9ydGVyIHN5bXBvcnRlciBhbnRpcG9ydGVy", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter6/Slide10.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide14.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide16.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide17.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide18.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide19.jpg"),
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter6question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Which type of transport moves substances down their concentration gradient without energy input?",
                        "options": ["Facilitated diffusion", "Primary active transport", "Secondary active transport", "Endocytosis"],
                        "answer": "Facilitated diffusion"
                    },
                    {
                        "question": "Which of the following is an example of a molecule moved by facilitated diffusion?",
                        "options": ["Glucose", "Sodium", "Cholesterol", "ATP"],
                        "answer": "Glucose"
                    },
                    {
                        "question": "What is the main energy source for primary active transport?",
                        "options": ["Sunlight", "GTP", "ATP", "Electrochemical gradient"],
                        "answer": "ATP"
                    },
                    {
                        "question": "Which protein allows water to move across the membrane rapidly?",
                        "options": ["Sodium-potassium pump", "Aquaporin", "G protein", "Symporter"],
                        "answer": "Aquaporin"
                    },
                    {
                        "question": "In facilitated diffusion, how do carrier proteins work?",
                        "options": ["Bind to the solute and change shape to move it", "Use ATP to pump ions", "Use vesicles to transport molecules", "Form tight junctions"],
                        "answer": "Bind to the solute and change shape to move it"
                    },
                    {
                        "question": "What is an antiporter?",
                        "options": ["A transporter that moves one substance in one direction", "A transporter that moves two substances in the same direction", "A transporter that moves two substances in opposite directions", "A transporter that uses light energy"],
                        "answer": "A transporter that moves two substances in opposite directions"
                    },
                    {
                        "question": "Which transport mechanism uses the gradient of one molecule to move another molecule?",
                        "options": ["Facilitated diffusion", "Primary active transport", "Secondary active transport", "Simple diffusion"],
                        "answer": "Secondary active transport"
                    },
                    {
                        "question": "Which type of channel opens in response to an electrical change across the membrane?",
                        "options": ["Ligand-gated channel", "Voltage-gated channel", "Aquaporin", "Carrier protein"],
                        "answer": "Voltage-gated channel"
                    },
                    {
                        "question": "What does the sodium-potassium pump do?",
                        "options": ["Moves 3 Na+ in and 2 K+ out", "Moves 2 Na+ in and 3 K+ out", "Moves 3 Na+ out and 2 K+ in", "Moves glucose into the cell"],
                        "answer": "Moves 3 Na+ out and 2 K+ in"
                    },
                    {
                        "question": "Which of the following best describes a symporter?",
                        "options": ["Moves two molecules in opposite directions", "Moves one molecule using ATP", "Moves two molecules in the same direction", "Passively diffuses ions across the membrane"],
                        "answer": "Moves two molecules in the same direction"
                    },
                    {
                        "question": "What enables secondary active transport to occur?",
                        "options": ["ATP hydrolysis", "Direct protein phosphorylation", "A concentration gradient created by primary active transport", "Endocytosis"],
                        "answer": "A concentration gradient created by primary active transport"
                    },
                    {
                        "question": "Which of the following is an example of a ligand-gated channel?",
                        "options": ["Aquaporin", "Acetylcholine receptor", "Sodium-potassium pump", "Glucose transporter"],
                        "answer": "Acetylcholine receptor"
                    },
                    {
                        "question": "Which process moves ions against their concentration gradient using ATP?",
                        "options": ["Facilitated diffusion", "Primary active transport", "Simple diffusion", "Exocytosis"],
                        "answer": "Primary active transport"
                    },
                    {
                        "question": "What determines the direction of movement in facilitated diffusion?",
                        "options": ["Membrane potential", "ATP availability", "Concentration gradient", "Ligand binding"],
                        "answer": "Concentration gradient"
                    },
                    {
                        "question": "Which of the following is true about carrier proteins?",
                        "options": ["They always use ATP", "They are always open", "They bind to molecules and change shape to transport them", "They only move ions"],
                        "answer": "They bind to molecules and change shape to transport them"
                    },
                    {
                        "question": "Voltage-gated ion channels are activated by:",
                        "options": ["ATP hydrolysis", "Binding of a hormone", "Change in membrane potential", "Interaction with G proteins"],
                        "answer": "Change in membrane potential"
                    },
                    {
                        "question": "What is the role of the sodium-potassium pump in cells?",
                        "options": ["Move glucose into cells", "Maintain membrane potential by pumping ions", "Transport oxygen", "Break down ATP"],
                        "answer": "Maintain membrane potential by pumping ions"
                    },
                    {
                        "question": "What type of transport is involved in nutrient uptake like amino acids and sugars using gradients?",
                        "options": ["Primary active transport", "Secondary active transport", "Osmosis", "Simple diffusion"],
                        "answer": "Secondary active transport"
                    },
                    {
                        "question": "What does the membrane potential depend on?",
                        "options": ["ATP concentration", "K+ concentration gradient", "Cholesterol content", "Membrane thickness"],
                        "answer": "K+ concentration gradient"
                    },
                    {
                        "question": "Which of these is NOT used in facilitated diffusion?",
                        "options": ["Carrier proteins", "Channel proteins", "Ion channels", "ATPase enzymes"],
                        "answer": "ATPase enzymes"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Cells move substances across membranes using passive and active mechanisms. Facilitated diffusion helps polar molecules cross membranes without energy, while active transport requires energy to move substances against their concentration gradients."),
                                html.Ul([
                                    html.Li([html.Strong("Facilitated Diffusion:"), " passive transport that uses transmembrane proteins to help polar molecules move across the membrane (e.g., glucose transporters)."]),
                                    html.Li([html.Strong("Primary Active Transport:"), " uses ATP directly to move substances against their concentration gradient (e.g., sodium-potassium pump)."]),
                                    html.Li([html.Strong("Secondary Active Transport:"), " uses a proton or ion gradient established by primary transport to move other substances (e.g., glucose or amino acid uptake)."])
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Think of the cell membrane as a door with guards."),
                                html.Ul([
                                    html.Li("Facilitated diffusion is like someone opening the door for molecules who can't go through on their own — no energy needed. This is how glucose or water might enter."),
                                    html.Li("Primary active transport is like pushing something uphill using fuel — it needs ATP. That’s how cells pump out sodium and bring in potassium."),
                                    html.Li("Secondary active transport borrows the energy from that first push (like riding a wave after someone creates it) to bring in sugars and amino acids."),
                                    html.Li("Transport proteins can work alone (uniporter), with a buddy in the same direction (symporter), or swap places (antiporter).")
                                ])
                ])]
            },
            "q10": {
                "question": html.P("Understand the terms phagocytosis, pinocytosis, receptor mediated endocytosis and exocytosis."),
                "overview": html.Div([
                                html.P("Cells use vesicles to move large or specific materials into or out of the cell. This process includes phagocytosis, pinocytosis, receptor-mediated endocytosis, and exocytosis."),
                                html.Ul([
                                    html.Li([html.Strong("Phagocytosis:"), " cell engulfs large particles or entire cells (e.g., white blood cells engulf bacteria)."]),
                                    html.Li([html.Strong("Pinocytosis:"), " cell takes in fluids and dissolved solutes through small vesicles; common in endothelial cells."]),
                                    html.Li([html.Strong("Receptor-Mediated Endocytosis:"), " specific molecules bind to receptors in coated pits and are brought into the cell via vesicle formation (e.g., cholesterol uptake)."]),
                                    html.Li([html.Strong("Exocytosis:"), " vesicles fuse with the plasma membrane to release contents outside the cell."])
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Cells can bring in or send out substances that are too large or too specific for passive or active transport."),
                                html.P([html.Strong("Phagocytosis:"), " involves the cell membrane wrapping around large particles like microbes or debris. A vesicle called a phagosome forms and later fuses with a lysosome for digestion. Example: white blood cells removing pathogens."]),                        
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/phagocytosis.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.alamy.com/stock-photo/phagocytosis.html?cutout=1&sortBy=relevant", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Pinocytosis:"), " or 'cell drinking,' is the ingestion of extracellular fluid and small solutes. It uses small vesicles and occurs constantly in some cells like capillary endothelial cells."]), 
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/pinocytosis.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://en.wikipedia.org/wiki/Pinocytosis", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Receptor-Mediated Endocytosis:"), " enables cells to take in specific substances like cholesterol. Molecules bind to specific receptors clustered in areas called coated pits, which are lined with a protein like clathrin. Once filled, the membrane folds inward to form a coated vesicle."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/receptor mediated.png", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.geeksforgeeks.org/biology/endocytosis-function-types-process/", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Exocytosis:"), " is the process of exporting materials from the cell. Vesicles filled with substances like neurotransmitters or proteins fuse with the membrane and release their contents into the extracellular space."]),
                                html.Div(
                                    style = {'display':'flex', 'alignItems':'center'},
                                    children = [
                                        html.Img(src = "/assets/exocytosis.jpg", style = {'marginRight':'40px', 'width':'400px'}),
                                        html.P(["Image from ", html.A("here", href = "https://www.thoughtco.com/what-is-exocytosis-4114427", target = "_blank")])
                                    ]
                                ),
                                html.P([html.Strong("Helpful Outside Resources:")]),
                                html.Ul([
                                    html.Li([html.A("The Organic Chemistry Tutor: Cell Transport (Endocytosis, Exocytosis, Phagocytosis, and Pinocytosis)", href = "https://www.youtube.com/watch?v=jn4MTkqbZjg&pp=ygUZcGhhZ29jeXRvc2lzLCBwaW5vY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Nonstop Neuron: Endocytosis (Pinocytosis and Phagocytosis - Eating, Digesting, and Pooping by the Cell)", href = "https://www.youtube.com/watch?v=hSA4rPtmNxE&pp=ygUZcGhhZ29jeXRvc2lzLCBwaW5vY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Endocytosis, Phagocytosis, and Pinocytosis", href = "https://www.youtube.com/watch?v=QspmZf_yWyU&pp=ygUZcGhhZ29jeXRvc2lzLCBwaW5vY3l0b3Npc9IHCQnYCQGHKiGM7w%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Animated Biology with Arpan: Receptor Mediated Endocytosis", href = "https://www.youtube.com/watch?v=Hy4DKmJvC1U&pp=ygUZcGhhZ29jeXRvc2lzLCBwaW5vY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Khan Academy: Exocytosis (Membranes and Transport)", href = "https://www.youtube.com/watch?v=VOzV4d0HKis&pp=ygUKZXhvY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("Jeremy LeCornu: What is Exocytosis?", href = "https://www.youtube.com/watch?v=4I5WFnUh7dk&pp=ygUKZXhvY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("BioMan Biology: Exocytosis Animation (with a real paramecium)", href = "https://www.youtube.com/watch?v=qRSsFYLA-hI&pp=ygUKZXhvY3l0b3Npcw%3D%3D", target = "_blank")]),
                                    html.Li([html.A("DrDiclonius: Receptor Mediated Endocytosis", href = "https://www.youtube.com/watch?v=PjrH1dpCyyE&pp=ygUfcmVjZXB0b3IgbWVkaWF0ZWQgZW5kb2N5dG9zaXMgXA%3D%3D", target = "_blank")])
                                ])
                ]), 
                "lecture": html.Div([
                    html.Img(src = "/assets/Chapter6/Slide20.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide21.jpg"),
                    html.Img(src = "/assets/Chapter6/Slide22.jpg")
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter6question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What process involves a cell engulfing large particles or entire cells?",
                        "options": ["Pinocytosis", "Phagocytosis", "Exocytosis", "Osmosis"],
                        "answer": "Phagocytosis"
                    },
                    {
                        "question": "What type of vesicle transport is used to take in extracellular fluid and small solutes?",
                        "options": ["Phagocytosis", "Pinocytosis", "Endocytosis", "Diffusion"],
                        "answer": "Pinocytosis"
                    },
                    {
                        "question": "Which of the following involves the use of receptor proteins in coated pits?",
                        "options": ["Simple diffusion", "Receptor-mediated endocytosis", "Exocytosis", "Facilitated diffusion"],
                        "answer": "Receptor-mediated endocytosis"
                    },
                    {
                        "question": "What is the primary function of exocytosis?",
                        "options": ["Ingest large particles", "Move water across the membrane", "Release materials from the cell", "Create vesicles for digestion"],
                        "answer": "Release materials from the cell"
                    },
                    {
                        "question": "What forms during phagocytosis to contain the engulfed material?",
                        "options": ["Lysosome", "Phagosome", "Exosome", "Nucleosome"],
                        "answer": "Phagosome"
                    },
                    {
                        "question": "What happens after a phagosome forms during phagocytosis?",
                        "options": ["It fuses with a lysosome", "It is released from the cell", "It binds to a receptor", "It becomes a vacuole"],
                        "answer": "It fuses with a lysosome"
                    },
                    {
                        "question": "Which process is often used to take in cholesterol?",
                        "options": ["Phagocytosis", "Pinocytosis", "Receptor-mediated endocytosis", "Exocytosis"],
                        "answer": "Receptor-mediated endocytosis"
                    },
                    {
                        "question": "Which protein is associated with coated pits during receptor-mediated endocytosis?",
                        "options": ["Myosin", "Clathrin", "Actin", "Tubulin"],
                        "answer": "Clathrin"
                    },
                    {
                        "question": "What is the key feature of pinocytosis compared to phagocytosis?",
                        "options": ["It uses clathrin-coated pits", "It takes in fluid and small solutes", "It only occurs in muscle cells", "It involves fusion with the Golgi"],
                        "answer": "It takes in fluid and small solutes"
                    },
                    {
                        "question": "Which of the following is true of phagocytosis?",
                        "options": ["It is used to expel materials", "It only occurs in plant cells", "It engulfs large particles", "It requires receptor proteins"],
                        "answer": "It engulfs large particles"
                    },
                    {
                        "question": "What process allows cells to communicate by releasing signals like neurotransmitters?",
                        "options": ["Receptor-mediated endocytosis", "Phagocytosis", "Exocytosis", "Pinocytosis"],
                        "answer": "Exocytosis"
                    },
                    {
                        "question": "Which process is continuous in capillary endothelial cells?",
                        "options": ["Pinocytosis", "Phagocytosis", "Endocytosis", "Osmosis"],
                        "answer": "Pinocytosis"
                    },
                    {
                        "question": "What is a characteristic of receptor-mediated endocytosis?",
                        "options": ["It is random", "It does not use proteins", "It is highly specific", "It is slower than phagocytosis"],
                        "answer": "It is highly specific"
                    },
                    {
                        "question": "What type of endocytosis involves binding to specific molecules on the membrane?",
                        "options": ["Pinocytosis", "Phagocytosis", "Receptor-mediated endocytosis", "Exocytosis"],
                        "answer": "Receptor-mediated endocytosis"
                    },
                    {
                        "question": "What kind of molecule is taken in during pinocytosis?",
                        "options": ["Proteins", "Cells", "Fluids and small solutes", "DNA"],
                        "answer": "Fluids and small solutes"
                    },
                    {
                        "question": "Which vesicle process is responsible for exporting waste or cell products?",
                        "options": ["Endocytosis", "Pinocytosis", "Exocytosis", "Phagocytosis"],
                        "answer": "Exocytosis"
                    },
                    {
                        "question": "During receptor-mediated endocytosis, what initiates vesicle formation?",
                        "options": ["Random invagination", "Binding of ligands to receptors", "High membrane pressure", "ATP binding to vesicles"],
                        "answer": "Binding of ligands to receptors"
                    },
                    {
                        "question": "Which process helps white blood cells engulf bacteria?",
                        "options": ["Pinocytosis", "Phagocytosis", "Exocytosis", "Osmosis"],
                        "answer": "Phagocytosis"
                    },
                    {
                        "question": "Which process uses small vesicles and does not require specific receptor binding?",
                        "options": ["Pinocytosis", "Receptor-mediated endocytosis", "Phagocytosis", "Active transport"],
                        "answer": "Pinocytosis"
                    },
                    {
                        "question": "What are 'coated pits' made of?",
                        "options": ["Lipid rafts", "Myosin", "Clathrin", "Collagen"],
                        "answer": "Clathrin"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Cells use vesicles to move large or specific materials into or out of the cell. This process includes phagocytosis, pinocytosis, receptor-mediated endocytosis, and exocytosis."),
                                html.Ul([
                                    html.Li([html.Strong("Phagocytosis:"), " cell engulfs large particles or entire cells (e.g., white blood cells engulf bacteria)."]),
                                    html.Li([html.Strong("Pinocytosis:"), " cell takes in fluids and dissolved solutes through small vesicles; common in endothelial cells."]),
                                    html.Li([html.Strong("Receptor-Mediated Endocytosis:"), " specific molecules bind to receptors in coated pits and are brought into the cell via vesicle formation (e.g., cholesterol uptake)."]),
                                    html.Li([html.Strong("Exocytosis:"), " vesicles fuse with the plasma membrane to release contents outside the cell."])
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Cells eat, drink, and spit things out using membrane pockets."),
                                html.Ul([
                                    html.Li("Phagocytosis is like the cell taking a big bite—it wraps around a large object and swallows it."),
                                    html.Li("Pinocytosis is like the cell sipping—taking small gulps of fluid and solutes."),
                                    html.Li("Receptor-mediated endocytosis is like the cell using a key—only specific molecules that fit into a receptor get invited in."),
                                    html.Li("Exocytosis is how the cell takes out the trash—vesicles fuse with the membrane and release their contents outside.")
                                ])
                ])]
            },
            "q11": {
                "question": html.P(" Be able to define the terms metabolism, anabolic reactions and catabolic reaction.  Know the laws of thermodynamics."),
                "overview": html.Div([
                                html.P("Metabolism refers to all the chemical reactions within an organism. These reactions are classified as either anabolic or catabolic, and are governed by the laws of thermodynamics."),
                                html.Ul([
                                    html.Li([html.Strong("Metabolism:"), " the total sum of all chemical reactions in an organism."]),
                                    html.Li([html.Strong("Anabolic reactions:"), " build larger, complex molecules from smaller ones; these reactions require energy (endergonic)."]),
                                    html.Li([html.Strong("Catabolic reactions:"), " break down larger molecules into smaller ones; these reactions release energy (exergonic)."]),
                                    html.Li([html.Strong("First Law of Thermodynamics:"), " energy cannot be created or destroyed — it only changes form."]),
                                    html.Li([html.Strong("Second Law of Thermodynamics:"), " every energy transfer increases entropy (disorder); energy transfer is never 100% efficient — some is lost as heat."])
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("All life processes depend on energy transformations. Metabolism includes two types of reactions:"),
                                html.Ul([
                                    html.Li([html.Strong("Anabolic Reactions:"), " link small molecules to form larger, complex ones — such as building proteins from amino acids. These require an input of energy and are considered endergonic."]),
                                    html.Li([html.Strong("Catabolic Reactions:"), " break down large molecules into smaller units — such as digesting starch into glucose. These reactions release energy and are exergonic."])
                                ]),
                                html.P([html.Strong("The First Law of Thermodynamics"), " ensures that in all biological reactions, the total amount of energy remains constant. For example, energy stored in food is transformed into ATP, not destroyed."]),
                                html.P([html.Strong("The Second Law of Thermodynamics"), " reminds us that not all energy transformations are perfectly efficient. Some of the energy is always lost as heat, and without constant energy input, systems will become more disordered (increase in entropy)."])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter8question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does metabolism refer to?",
                        "options": ["Only digestion", "Only energy release", "All chemical reactions in an organism", "Only photosynthesis"],
                        "answer": "All chemical reactions in an organism"
                    },
                    {
                        "question": "What type of reaction builds larger molecules from smaller ones and requires energy?",
                        "options": ["Catabolic reaction", "Fermentation", "Anabolic reaction", "Hydrolysis"],
                        "answer": "Anabolic reaction"
                    },
                    {
                        "question": "What type of reaction breaks down larger molecules and releases energy?",
                        "options": ["Anabolic reaction", "Catabolic reaction", "Endergonic reaction", "Condensation reaction"],
                        "answer": "Catabolic reaction"
                    },
                    {
                        "question": "Which of the following is an example of an anabolic reaction?",
                        "options": ["Breaking down glucose in cellular respiration", "Digesting proteins into amino acids", "Synthesizing DNA from nucleotides", "Hydrolyzing ATP"],
                        "answer": "Synthesizing DNA from nucleotides"
                    },
                    {
                        "question": "Which of the following is a catabolic process?",
                        "options": ["DNA replication", "Protein synthesis", "Cellular respiration", "Photosynthesis"],
                        "answer": "Cellular respiration"
                    },
                    {
                        "question": "Which law states that energy cannot be created or destroyed?",
                        "options": ["Second Law of Thermodynamics", "Law of Conservation of Mass", "First Law of Thermodynamics", "Law of Entropy"],
                        "answer": "First Law of Thermodynamics"
                    },
                    {
                        "question": "What does the Second Law of Thermodynamics state?",
                        "options": ["Energy is always lost as sound", "Energy is stored in the nucleus", "Energy transfers are always 100% efficient", "Energy transfers increase disorder (entropy)"],
                        "answer": "Energy transfers increase disorder (entropy)"
                    },
                    {
                        "question": "What is entropy?",
                        "options": ["Energy needed to build molecules", "The heat produced by a reaction", "A measure of disorder", "The speed of a reaction"],
                        "answer": "A measure of disorder"
                    },
                    {
                        "question": "Which of the following best describes an endergonic reaction?",
                        "options": ["Releases energy", "Requires energy input", "Is always spontaneous", "Decreases entropy"],
                        "answer": "Requires energy input"
                    },
                    {
                        "question": "What type of energy transformation is involved in a catabolic reaction?",
                        "options": ["Energy storage", "Energy absorption", "Energy release", "Energy conversion to mass"],
                        "answer": "Energy release"
                    },
                    {
                        "question": "Which of the following best describes the First Law of Thermodynamics in biology?",
                        "options": ["Organisms create new energy", "Energy is destroyed during metabolism", "Energy is conserved and transformed", "Energy transfer is perfectly efficient"],
                        "answer": "Energy is conserved and transformed"
                    },
                    {
                        "question": "What is typically released as a byproduct of energy transformation according to the Second Law of Thermodynamics?",
                        "options": ["Oxygen", "Heat", "Water", "Carbon dioxide"],
                        "answer": "Heat"
                    },
                    {
                        "question": "What does a catabolic pathway provide to anabolic pathways?",
                        "options": ["Water", "Glucose", "ATP and building blocks", "Enzymes"],
                        "answer": "ATP and building blocks"
                    },
                    {
                        "question": "Which of the following is an endergonic process?",
                        "options": ["ATP hydrolysis", "Protein synthesis", "Glucose breakdown", "Lactic acid fermentation"],
                        "answer": "Protein synthesis"
                    },
                    {
                        "question": "What happens to total energy in a closed system, according to the First Law?",
                        "options": ["It increases over time", "It decreases with entropy", "It remains constant", "It is converted into matter"],
                        "answer": "It remains constant"
                    },
                    {
                        "question": "Which of the following would increase entropy?",
                        "options": ["Freezing water", "Building a DNA molecule", "Breaking down starch", "Decreasing temperature"],
                        "answer": "Breaking down starch"
                    },
                    {
                        "question": "Why do anabolic reactions require an input of energy?",
                        "options": ["They occur at high temperatures", "They increase entropy", "They build complex molecules", "They generate heat"],
                        "answer": "They build complex molecules"
                    },
                    {
                        "question": "Which process is most directly responsible for generating the heat your body releases?",
                        "options": ["Exocytosis", "Endocytosis", "Energy loss during metabolic reactions", "Photosynthesis"],
                        "answer": "Energy loss during metabolic reactions"
                    },
                    {
                        "question": "Which of the following is NOT true of anabolic reactions?",
                        "options": ["They require energy", "They build complex molecules", "They release energy", "They are endergonic"],
                        "answer": "They release energy"
                    },
                    {
                        "question": "Which of these best represents the Second Law of Thermodynamics in biology?",
                        "options": ["Organisms lose all their energy over time", "Energy transformations are always efficient", "Living systems require energy to maintain order", "All metabolic reactions reduce entropy"],
                        "answer": "Living systems require energy to maintain order"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Metabolism refers to all the chemical reactions within an organism. These reactions are classified as either anabolic or catabolic, and are governed by the laws of thermodynamics."),
                                html.Ul([
                                    html.Li([html.Strong("Metabolism:"), " the total sum of all chemical reactions in an organism."]),
                                    html.Li([html.Strong("Anabolic reactions:"), " build larger, complex molecules from smaller ones; these reactions require energy (endergonic)."]),
                                    html.Li([html.Strong("Catabolic reactions:"), " break down larger molecules into smaller ones; these reactions release energy (exergonic)."]),
                                    html.Li([html.Strong("First Law of Thermodynamics:"), " energy cannot be created or destroyed — it only changes form."]),
                                    html.Li([html.Strong("Second Law of Thermodynamics:"), " every energy transfer increases entropy (disorder); energy transfer is never 100% efficient — some is lost as heat."])
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Metabolism is just the sum of every little chemical reaction happening inside your body."),
                                html.Ul([
                                    html.Li("Anabolic reactions build things up, like Lego blocks forming a castle. They use energy."),
                                    html.Li("Catabolic reactions break things down, like smashing that Lego castle apart. They release energy."),
                                    html.Li("The First Law of Thermodynamics is like saying energy is never lost — just moved around."),
                                    html.Li("The Second Law says that every time you move energy, you waste some as heat, and everything tends toward messiness unless you keep adding energy.")
                                ])
                ])]
            },
            "q12": {
                "question": html.P("Understand the concept of free energy (G) and its relationship to enthalpy (H) and entropy (S). Be able to explain and give examples of exergonic and endergonic reactions."),
                "overview": html.Div([
                                html.P("Free energy (G) is the energy available to do work in a system. It is determined by the system’s enthalpy (H) and entropy (S), and helps predict whether a reaction will occur spontaneously."),
                                html.Ul([
                                    html.Li([html.Strong("Free Energy (G):"), " the usable energy in a system, or energy available to do work."]),
                                    html.Li([html.Strong("Enthalpy (H):"), " the total heat content of a system."]),
                                    html.Li([html.Strong("Entropy (S):"), " the measure of disorder or randomness in a system."]),
                                    html.Li([html.Strong("Gibbs Free Energy Equation:"), " ΔG = ΔH – TΔS (T = absolute temperature in Kelvin)."]),
                                    html.Li([html.Strong("Exergonic Reaction:"), " releases free energy (ΔG < 0); example: cellular respiration."]),
                                    html.Li([html.Strong("Endergonic Reaction:"), " consumes free energy (ΔG > 0); example: cell movement, active transport."])
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.H4("Predicting Reactions with Gibbs Free Energy"),
                                html.P("The change in Gibbs Free Energy (ΔG) determines whether a chemical reaction can occur without additional energy input."),
                                html.P([html.Strong("ΔG < 0: Exergonic Reaction."), " These reactions release free energy and can occur spontaneously. They are usually associated with catabolic processes, such as cellular respiration."]),                         
                                html.P([html.Strong("ΔG > 0: Endergonic Reaction."), " These reactions require an input of free energy and are not spontaneous. They are typical of anabolic processes like building proteins or pumping ions across membranes."]),                           
                                html.P("ΔG is influenced by:"),
                                html.Ul([
                                    html.Li("ΔH: change in enthalpy (heat released or absorbed)."),
                                    html.Li("T: absolute temperature (Kelvin)."),
                                    html.Li("ΔS: change in entropy (order → disorder).")
                                ]),                           
                                html.P("If a reaction results in higher disorder (increased entropy), it may be more likely to occur — especially at higher temperatures, which amplify the entropy term (TΔS) in the equation.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter8question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What does Gibbs Free Energy (G) represent?",
                        "options": ["Total energy in the universe", "Energy lost as heat", "Energy available to do work", "Energy stored in bonds"],
                        "answer": "Energy available to do work"
                    },
                    {
                        "question": "What is the equation for Gibbs Free Energy?",
                        "options": ["ΔG = ΔH + TΔS", "ΔG = ΔH – TΔS", "ΔG = TΔS – ΔH", "ΔG = ΔH × ΔS"],
                        "answer": "ΔG = ΔH – TΔS"
                    },
                    {
                        "question": "What does ΔH represent in the Gibbs Free Energy equation?",
                        "options": ["Change in entropy", "Change in energy stored", "Change in heat (enthalpy)", "Change in work done"],
                        "answer": "Change in heat (enthalpy)"
                    },
                    {
                        "question": "What does ΔS represent in the Gibbs Free Energy equation?",
                        "options": ["Change in energy", "Change in volume", "Change in pressure", "Change in disorder (entropy)"],
                        "answer": "Change in disorder (entropy)"
                    },
                    {
                        "question": "What does a negative ΔG indicate about a reaction?",
                        "options": ["Energy is required", "Energy is released", "Reaction will not occur", "It’s an endergonic reaction"],
                        "answer": "Energy is released"
                    },
                    {
                        "question": "What kind of reaction is indicated by a positive ΔG?",
                        "options": ["Exergonic", "Endergonic", "Spontaneous", "Exothermic"],
                        "answer": "Endergonic"
                    },
                    {
                        "question": "Which of the following is an example of an exergonic process?",
                        "options": ["Active transport", "Cellular respiration", "Protein synthesis", "Photosynthesis"],
                        "answer": "Cellular respiration"
                    },
                    {
                        "question": "Which of the following is an example of an endergonic reaction?",
                        "options": ["Cellular respiration", "ATP hydrolysis", "Cell movement", "Breaking down starch"],
                        "answer": "Cell movement"
                    },
                    {
                        "question": "What happens if ΔG is zero?",
                        "options": ["The reaction releases energy", "The reaction requires energy", "The system is at equilibrium", "The reaction is endergonic"],
                        "answer": "The system is at equilibrium"
                    },
                    {
                        "question": "Which condition increases the effect of entropy (ΔS) on ΔG?",
                        "options": ["Low temperature", "Zero enthalpy", "High temperature", "No change in entropy"],
                        "answer": "High temperature"
                    },
                    {
                        "question": "What is true about exergonic reactions?",
                        "options": ["They require an input of energy", "They have a positive ΔG", "They release free energy", "They increase molecular order"],
                        "answer": "They release free energy"
                    },
                    {
                        "question": "Which reaction would most likely occur spontaneously?",
                        "options": ["ΔG = +5 kcal/mol", "ΔG = 0 kcal/mol", "ΔG = –10 kcal/mol", "ΔG = +20 kcal/mol"],
                        "answer": "ΔG = –10 kcal/mol"
                    },
                    {
                        "question": "What kind of reaction is protein synthesis?",
                        "options": ["Exergonic", "Catabolic", "Endergonic", "Spontaneous"],
                        "answer": "Endergonic"
                    },
                    {
                        "question": "Which of the following terms describes a measure of disorder?",
                        "options": ["Enthalpy", "Entropy", "Exergonic", "Activation energy"],
                        "answer": "Entropy"
                    },
                    {
                        "question": "Which term describes a reaction that absorbs energy?",
                        "options": ["Exergonic", "Spontaneous", "Endergonic", "Thermodynamic"],
                        "answer": "Endergonic"
                    },
                    {
                        "question": "If a process increases entropy and decreases enthalpy, what is the most likely ΔG?",
                        "options": ["Positive", "Negative", "Zero", "Undefined"],
                        "answer": "Negative"
                    },
                    {
                        "question": "In cellular respiration, the breakdown of glucose is considered:",
                        "options": ["Anabolic and endergonic", "Catabolic and exergonic", "Anabolic and exergonic", "Catabolic and endergonic"],
                        "answer": "Catabolic and exergonic"
                    },
                    {
                        "question": "What does a positive ΔG suggest about the spontaneity of a reaction?",
                        "options": ["It is spontaneous", "It is non-spontaneous", "It will occur rapidly", "It is irreversible"],
                        "answer": "It is non-spontaneous"
                    },
                    {
                        "question": "Which factor is NOT part of the Gibbs Free Energy equation?",
                        "options": ["Enthalpy", "Entropy", "Volume", "Temperature"],
                        "answer": "Volume"
                    },
                    {
                        "question": "Which of the following would make a reaction more spontaneous?",
                        "options": ["Decrease in entropy", "Increase in enthalpy", "Decrease in temperature", "Increase in entropy"],
                        "answer": "Increase in entropy"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Free energy (G) is the energy available to do work in a system. It is determined by the system’s enthalpy (H) and entropy (S), and helps predict whether a reaction will occur spontaneously."),
                                html.Ul([
                                    html.Li([html.Strong("Free Energy (G):"), " the usable energy in a system, or energy available to do work."]),
                                    html.Li([html.Strong("Enthalpy (H):"), " the total heat content of a system."]),
                                    html.Li([html.Strong("Entropy (S):"), " the measure of disorder or randomness in a system."]),
                                    html.Li([html.Strong("Gibbs Free Energy Equation:"), " ΔG = ΔH – TΔS (T = absolute temperature in Kelvin)."]),
                                    html.Li([html.Strong("Exergonic Reaction:"), " releases free energy (ΔG < 0); example: cellular respiration."]),
                                    html.Li([html.Strong("Endergonic Reaction:"), " consumes free energy (ΔG > 0); example: cell movement, active transport."])
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Free energy is how much ‘usable’ energy a reaction has to do something useful."),
                                html.Ul([
                                    html.Li("If ΔG is negative, the reaction gives off energy — like a battery running. That’s exergonic."),
                                    html.Li("If ΔG is positive, the reaction needs a push (energy input) — like charging a battery. That’s endergonic."),
                                    html.Li("ΔG depends on heat (H), disorder (S), and temperature. The more disorder a reaction creates, the more likely it is to happen."),
                                    html.Li("Example: Cellular respiration is exergonic. Active transport is endergonic.")
                                ])
                ])]
            },
            "q13": {
                "question": html.P("Be familiar with the role of ATP in biochemical energetics."),
                "overview": html.Div([
                                html.P("ATP (adenosine triphosphate) is the main energy currency of the cell. It powers cellular processes by releasing energy through hydrolysis and transferring phosphate groups to other molecules."),
                                html.Ul([
                                    html.Li([html.Strong("ATP: "), "a molecule that captures and transfers free energy within the cell."]),
                                    html.Li([html.Strong("Hydrolysis of ATP: "), "releases a large amount of energy (exergonic)."]),
                                    html.Li([html.Strong("Phosphorylation: "), "ATP transfers a phosphate group to another molecule, activating or energizing it."]),
                                    html.Li([html.Strong("ATP couples reactions: "), "it links exergonic and endergonic reactions so energy can flow through biological systems."])
                                ])
                            ]), 
                "deep_dive": html.Div([
                                html.P("ATP contains three phosphate groups that are negatively charged and repel one another. This makes the molecule unstable and full of potential energy."),
                                html.P([
                                    "When ATP is hydrolyzed (broken down into ADP + Pi), a large amount of energy is released. This exergonic reaction can be ",
                                    html.Strong("coupled"),
                                    " to an endergonic process — such as building macromolecules or transporting ions — to drive it forward."
                                ]),                              
                                html.P([
                                    "The phosphate group from ATP can be ",
                                    html.Strong("transferred"),
                                    " to another molecule. This phosphorylation changes the shape or activity of the target molecule — essentially turning it 'on' or 'off'."
                                ]),
                                html.P("In this way, ATP functions not just as an energy source, but as an energy shuttle that connects energy-yielding and energy-consuming reactions.")
                            ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter8question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the main role of ATP in cells?",
                        "options": ["Store genetic information", "Catalyze chemical reactions", "Transfer energy for cellular work", "Break down nutrients"],
                        "answer": "Transfer energy for cellular work"
                    },
                    {
                        "question": "What type of reaction is ATP hydrolysis?",
                        "options": ["Endergonic", "Exergonic", "Neutral", "Isotonic"],
                        "answer": "Exergonic"
                    },
                    {
                        "question": "What does ATP become after hydrolysis?",
                        "options": ["AMP", "ADP and a phosphate group", "NADH", "Glucose"],
                        "answer": "ADP and a phosphate group"
                    },
                    {
                        "question": "Which part of ATP is responsible for its energy-carrying function?",
                        "options": ["The adenine base", "The ribose sugar", "The phosphate groups", "The hydrogen atoms"],
                        "answer": "The phosphate groups"
                    },
                    {
                        "question": "What does phosphorylation refer to?",
                        "options": ["Removal of electrons", "Binding of ATP to DNA", "Addition of a phosphate group to a molecule", "Loss of heat energy"],
                        "answer": "Addition of a phosphate group to a molecule"
                    },
                    {
                        "question": "How does ATP power endergonic reactions?",
                        "options": ["By donating electrons", "By storing glucose", "By coupling with exergonic reactions", "By breaking DNA"],
                        "answer": "By coupling with exergonic reactions"
                    },
                    {
                        "question": "Which process releases energy stored in ATP?",
                        "options": ["ATP synthesis", "Phosphorylation", "Hydrolysis", "Glycolysis"],
                        "answer": "Hydrolysis"
                    },
                    {
                        "question": "What type of bond holds ATP's phosphate groups together?",
                        "options": ["Hydrogen bonds", "Ionic bonds", "Covalent bonds", "High-energy phosphate bonds"],
                        "answer": "High-energy phosphate bonds"
                    },
                    {
                        "question": "Which of the following is an example of an ATP-powered activity?",
                        "options": ["Passive diffusion", "Facilitated diffusion", "Protein synthesis", "Simple osmosis"],
                        "answer": "Protein synthesis"
                    },
                    {
                        "question": "What happens when ATP phosphorylates another molecule?",
                        "options": ["The molecule becomes inactive", "The molecule gains energy", "The molecule is digested", "The molecule is dehydrated"],
                        "answer": "The molecule gains energy"
                    },
                    {
                        "question": "Where does the energy in ATP primarily come from?",
                        "options": ["Breaking the adenine base", "Breaking the sugar ring", "Breaking the phosphate bonds", "Breaking ribosomes"],
                        "answer": "Breaking the phosphate bonds"
                    },
                    {
                        "question": "Why is ATP considered the 'energy currency' of the cell?",
                        "options": ["It stores water", "It holds DNA", "It transfers usable energy for cellular processes", "It produces oxygen"],
                        "answer": "It transfers usable energy for cellular processes"
                    },
                    {
                        "question": "What is a typical result of coupling ATP hydrolysis to another reaction?",
                        "options": ["Heat is produced only", "A cell enters mitosis", "The other reaction becomes energetically favorable", "No change occurs"],
                        "answer": "The other reaction becomes energetically favorable"
                    },
                    {
                        "question": "What is constantly regenerated in cells to provide a continuous supply of energy?",
                        "options": ["Glucose", "DNA", "ATP", "mRNA"],
                        "answer": "ATP"
                    },
                    {
                        "question": "Which of the following is an example of a cellular process that requires ATP?",
                        "options": ["Diffusion of oxygen", "Osmosis", "Active transport of ions", "Passive movement of water"],
                        "answer": "Active transport of ions"
                    },
                    {
                        "question": "How does ATP relate to exergonic reactions?",
                        "options": ["ATP is always consumed in exergonic reactions", "Exergonic reactions break down ATP", "ATP is regenerated by exergonic reactions", "Exergonic reactions prevent ATP production"],
                        "answer": "ATP is regenerated by exergonic reactions"
                    },
                    {
                        "question": "In the ATP cycle, what recharges ADP back into ATP?",
                        "options": ["Glucose binding", "Protein synthesis", "Energy from catabolic reactions", "DNA replication"],
                        "answer": "Energy from catabolic reactions"
                    },
                    {
                        "question": "Which is true of ATP's phosphate groups?",
                        "options": ["They are stable and inert", "They are joined by weak ionic bonds", "They repel each other, making ATP unstable", "They contain no usable energy"],
                        "answer": "They repel each other, making ATP unstable"
                    },
                    {
                        "question": "Why is the hydrolysis of ATP useful to cells?",
                        "options": ["It cools the cell", "It stores oxygen", "It releases free energy for work", "It builds nucleic acids"],
                        "answer": "It releases free energy for work"
                    },
                    {
                        "question": "Which term best describes the function of ATP in energy transfer?",
                        "options": ["Enzyme", "Substrate", "Coupler", "Battery"],
                        "answer": "Battery"
                    }
                ],
                "blurting": [html.Div([
                                html.P("ATP (adenosine triphosphate) is the main energy currency of the cell. It powers cellular processes by releasing energy through hydrolysis and transferring phosphate groups to other molecules."),
                                html.Ul([
                                    html.Li([html.Strong("ATP: "), "a molecule that captures and transfers free energy within the cell."]),
                                    html.Li([html.Strong("Hydrolysis of ATP: "), "releases a large amount of energy (exergonic)."]),
                                    html.Li([html.Strong("Phosphorylation: "), "ATP transfers a phosphate group to another molecule, activating or energizing it."]),
                                    html.Li([html.Strong("ATP couples reactions: "), "it links exergonic and endergonic reactions so energy can flow through biological systems."])
                                ])
                            ])],
                "feynman": [html.Div([
                                html.P("ATP is like a little battery for your cells."),
                                html.Ul([
                                    html.Li("When you break it (hydrolyze it), it gives off energy."),
                                    html.Li("It can attach a piece of itself (a phosphate) to other molecules to make them do something."),
                                    html.Li("It helps power things that need energy — like muscle contractions or building proteins — by linking to energy-releasing reactions."),
                                    html.Li("ATP is constantly being used and remade — like recharging your battery.")
                                ])
                            ])]
            },
            "q14": {
                "question": html.P("Be able to explain 3 different mechanisms by which enzymes catalyze reactions."),
                "overview": html.Div([
                                html.P("Enzymes speed up reactions by lowering the activation energy needed to reach the transition state."),
                                html.Ul([
                                    html.Li("They bring substrates together and orient them to increase reaction likelihood."),
                                    html.Li("They add functional groups temporarily (covalent catalysis) to make reactions easier."),
                                    html.Li("They use acid-base catalysis by donating or accepting protons, or metal ion catalysis by changing electron states."),
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Activation energy is the energy needed to convert reactants into high-energy transition states before forming products."),
                                html.P("Enzymes lower this barrier in several ways:"),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Substrate Orientation:"), 
                                        " Enzymes bind substrates in precise 3D orientations that favor reactions."
                                    ]),
                                    html.Li([
                                        html.Strong("Covalent Catalysis:"), 
                                        " Functional groups in enzyme side chains form temporary covalent bonds with substrates to stabilize transition states."
                                    ]),
                                    html.Li([
                                        html.Strong("Acid-Base Catalysis:"), 
                                        " Enzymes donate or accept protons to facilitate bond breakage or formation."
                                    ]),
                                    html.Li([
                                        html.Strong("Metal Ion Catalysis:"), 
                                        " Metal ions on enzymes can gain or lose electrons, helping to stabilize charged intermediates."
                                    ]),
                                ]),
                                html.P("Substrates bind the enzyme's active site forming an enzyme-substrate complex held by hydrogen bonds, ionic interactions, or covalent bonds."),
                                html.P("Enzyme specificity depends on the 3D shape of the active site."),
                                html.P("Some enzymes need helpers:"),
                                html.Ul([
                                    html.Li("Cofactors: inorganic ions essential for enzyme activity."),
                                    html.Li("Coenzymes: small organic molecules that transiently assist enzymes."),
                                    html.Li("Prosthetic groups: non-protein groups permanently bound to enzymes."),
                                ]),
                                html.P("The overall free energy change (ΔG) of the reaction remains unchanged by the enzyme; only the activation energy barrier is lowered.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter8question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the main effect of enzymes on activation energy?",
                        "options": ["They increase it", "They eliminate it", "They lower it", "They have no effect"],
                        "answer": "They lower it"
                    },
                    {
                        "question": "Which mechanism involves enzymes bringing substrates together in the correct orientation?",
                        "options": ["Covalent catalysis", "Substrate orientation", "Metal ion catalysis", "Acid-base catalysis"],
                        "answer": "Substrate orientation"
                    },
                    {
                        "question": "What type of catalysis involves temporary covalent bonds between enzyme and substrate?",
                        "options": ["Acid-base catalysis", "Covalent catalysis", "Metal ion catalysis", "Allosteric catalysis"],
                        "answer": "Covalent catalysis"
                    },
                    {
                        "question": "In acid-base catalysis, enzymes act by:",
                        "options": ["Transferring electrons", "Adding or removing protons", "Breaking covalent bonds", "Changing substrate shape"],
                        "answer": "Adding or removing protons"
                    },
                    {
                        "question": "Metal ion catalysis helps by:",
                        "options": ["Binding substrates permanently", "Changing electron states to stabilize intermediates", "Adding phosphate groups", "Breaking peptide bonds"],
                        "answer": "Changing electron states to stabilize intermediates"
                    },
                    {
                        "question": "What holds the enzyme-substrate complex together?",
                        "options": ["Hydrogen bonds", "Electrical attraction", "Covalent bonds", "All of the above"],
                        "answer": "All of the above"
                    },
                    {
                        "question": "What determines the specificity of an enzyme?",
                        "options": ["The temperature", "The pH", "The 3D shape of the active site", "The size of the substrate"],
                        "answer": "The 3D shape of the active site"
                    },
                    {
                        "question": "Which term describes inorganic ions needed by some enzymes?",
                        "options": ["Coenzymes", "Cofactors", "Prosthetic groups", "Substrates"],
                        "answer": "Cofactors"
                    },
                    {
                        "question": "What are small organic molecules that assist enzymes but do not permanently bind called?",
                        "options": ["Cofactors", "Coenzymes", "Prosthetic groups", "Inhibitors"],
                        "answer": "Coenzymes"
                    },
                    {
                        "question": "What are non-amino acid groups permanently bound to enzymes called?",
                        "options": ["Cofactors", "Coenzymes", "Prosthetic groups", "Substrates"],
                        "answer": "Prosthetic groups"
                    },
                    {
                        "question": "Does the enzyme change the overall free energy change (ΔG) of the reaction?",
                        "options": ["Yes, it makes ΔG more negative", "Yes, it makes ΔG more positive", "No, ΔG remains the same", "Yes, it eliminates ΔG"],
                        "answer": "No, ΔG remains the same"
                    },
                    {
                        "question": "Enzymes speed up reactions by:",
                        "options": ["Increasing temperature", "Decreasing substrate concentration", "Lowering activation energy", "Changing product concentration"],
                        "answer": "Lowering activation energy"
                    },
                    {
                        "question": "Which of the following is NOT a mechanism by which enzymes catalyze reactions?",
                        "options": ["Substrate orientation", "Covalent catalysis", "Metal ion catalysis", "Increasing substrate size"],
                        "answer": "Increasing substrate size"
                    },
                    {
                        "question": "What is a transition state intermediate?",
                        "options": ["A stable reactant", "An unstable, high-energy form of reactants", "A product", "An enzyme-substrate complex"],
                        "answer": "An unstable, high-energy form of reactants"
                    },
                    {
                        "question": "Which mechanism involves enzyme side chains donating or accepting protons?",
                        "options": ["Covalent catalysis", "Acid-base catalysis", "Metal ion catalysis", "Substrate orientation"],
                        "answer": "Acid-base catalysis"
                    },
                    {
                        "question": "How do enzymes affect the speed of a chemical reaction?",
                        "options": ["They slow it down", "They stop it", "They speed it up", "They have no effect"],
                        "answer": "They speed it up"
                    },
                    {
                        "question": "Which helper molecule binds temporarily and assists enzyme function?",
                        "options": ["Coenzyme", "Prosthetic group", "Substrate", "Inhibitor"],
                        "answer": "Coenzyme"
                    },
                    {
                        "question": "Which helper molecule is permanently attached to an enzyme?",
                        "options": ["Coenzyme", "Cofactor", "Prosthetic group", "Substrate"],
                        "answer": "Prosthetic group"
                    },
                    {
                        "question": "Why do enzymes not affect the equilibrium of a reaction?",
                        "options": ["They only speed up forward reaction", "They only speed up reverse reaction", "They speed up both directions equally", "They change product stability"],
                        "answer": "They speed up both directions equally"
                    },
                    {
                        "question": "Which of these is an example of covalent catalysis?",
                        "options": ["Proton transfer", "Temporary bond formation between enzyme and substrate", "Metal ion stabilization", "Substrate binding orientation"],
                        "answer": "Temporary bond formation between enzyme and substrate"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Enzymes speed up reactions by lowering the activation energy needed to reach the transition state."),
                                html.Ul([
                                    html.Li("They bring substrates together and orient them to increase reaction likelihood."),
                                    html.Li("They add functional groups temporarily (covalent catalysis) to make reactions easier."),
                                    html.Li("They use acid-base catalysis by donating or accepting protons, or metal ion catalysis by changing electron states."),
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Enzymes are like matchmakers for molecules."),
                                html.Ul([
                                    html.Li("They hold molecules in the perfect position to react."),
                                    html.Li("They can temporarily grab onto molecules to help the reaction along."),
                                    html.Li("They can pass or take protons to make bonds easier to break or form."),
                                    html.Li("Sometimes, metals in the enzyme help by handling electrons."),
                                    html.Li("Helpers like cofactors or coenzymes assist enzymes when needed."),
                                    html.Li("Enzymes don’t change the overall energy, just make the path easier to get there."),
                                ])
                ])]
            },
            "q15": {
                "question": html.P(" Know the different manners by which the activity of enzymes is regulated, including; irreversible inhibition, reversible inhibition, competitive inhibition, noncompetitive inhibition and allosteric regulation."),
                "overview": html.Div([
                                html.P("Enzyme activity can be controlled through different types of inhibition and regulation mechanisms."),
                                html.Ul([
                                    html.Li("Irreversible inhibition: inhibitor binds covalently and permanently to the enzyme."),
                                    html.Li("Reversible inhibition: inhibitor binds noncovalently and can detach."),
                                    html.Li("Competitive inhibition: inhibitor competes with substrate for the active site."),
                                    html.Li("Noncompetitive inhibition: inhibitor binds elsewhere causing shape change, preventing substrate binding."),
                                    html.Li("Allosteric regulation: effectors bind regulatory subunits to switch enzyme between active and inactive forms."),
                                    html.Li("Feedback inhibition: end-product acts as a noncompetitive inhibitor of the first enzyme, shutting down the pathway."),
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Irreversible inhibitors form covalent bonds with enzymes, permanently blocking activity."),
                                html.P("Reversible inhibitors bind temporarily through weak interactions and can be displaced."),
                                html.P("Competitive inhibitors resemble substrates and block active sites, preventing substrate binding."),
                                html.P("Noncompetitive inhibitors bind to different sites, causing conformational changes that reduce enzyme activity."),
                                html.P("Allosteric enzymes have multiple subunits with regulatory and catalytic parts."),
                                html.P("Binding of activators or inhibitors to regulatory subunits changes the enzyme’s shape and activity."),
                                html.P("Feedback inhibition uses the pathway’s final product to inhibit the initial enzyme, efficiently controlling metabolic flux.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter8question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of inhibition involves a covalent bond that permanently inactivates an enzyme?",
                        "options": ["Reversible inhibition", "Competitive inhibition", "Noncompetitive inhibition", "Irreversible inhibition"],
                        "answer": "Irreversible inhibition"
                    },
                    {
                        "question": "Which inhibition type can be reversed because the inhibitor binds noncovalently?",
                        "options": ["Irreversible inhibition", "Reversible inhibition", "Competitive inhibition", "Feedback inhibition"],
                        "answer": "Reversible inhibition"
                    },
                    {
                        "question": "In competitive inhibition, the inhibitor binds to:",
                        "options": ["A site other than the active site", "The active site", "The regulatory subunit", "The substrate"],
                        "answer": "The active site"
                    },
                    {
                        "question": "Noncompetitive inhibitors bind:",
                        "options": ["At the active site", "At a different site causing a shape change", "To the substrate", "To the product"],
                        "answer": "At a different site causing a shape change"
                    },
                    {
                        "question": "Feedback inhibition is an example of:",
                        "options": ["Competitive inhibition", "Noncompetitive inhibition", "Irreversible inhibition", "Allosteric activation"],
                        "answer": "Noncompetitive inhibition"
                    },
                    {
                        "question": "Allosteric regulation involves:",
                        "options": ["Inhibitors binding the active site", "Effectors binding regulatory subunits", "Covalent bonding to the enzyme", "Substrate competing for the active site"],
                        "answer": "Effectors binding regulatory subunits"
                    },
                    {
                        "question": "Allosteric enzymes have:",
                        "options": ["Only catalytic subunits", "Only regulatory subunits", "Both catalytic and regulatory subunits", "No subunits"],
                        "answer": "Both catalytic and regulatory subunits"
                    },
                    {
                        "question": "Which of the following is true about irreversible inhibitors?",
                        "options": ["They bind temporarily", "They cannot be removed once bound", "They bind only at the regulatory site", "They increase enzyme activity"],
                        "answer": "They cannot be removed once bound"
                    },
                    {
                        "question": "Competitive inhibitors affect enzyme activity by:",
                        "options": ["Binding to a different site and changing enzyme shape", "Blocking the active site", "Binding permanently", "Activating the enzyme"],
                        "answer": "Blocking the active site"
                    },
                    {
                        "question": "In feedback inhibition, the final product acts as:",
                        "options": ["A competitive inhibitor", "A noncompetitive inhibitor", "An activator", "A coenzyme"],
                        "answer": "A noncompetitive inhibitor"
                    },
                    {
                        "question": "Which regulatory mechanism can switch enzymes between active and inactive states?",
                        "options": ["Irreversible inhibition", "Allosteric regulation", "Competitive inhibition", "Substrate inhibition"],
                        "answer": "Allosteric regulation"
                    },
                    {
                        "question": "Reversible inhibition means the inhibitor:",
                        "options": ["Binds permanently", "Can detach from the enzyme", "Only binds to the substrate", "Only binds after the reaction"],
                        "answer": "Can detach from the enzyme"
                    },
                    {
                        "question": "Noncompetitive inhibitors prevent substrate binding by:",
                        "options": ["Competing for the active site", "Changing enzyme conformation", "Destroying the substrate", "Binding to the substrate"],
                        "answer": "Changing enzyme conformation"
                    },
                    {
                        "question": "What is the effect of competitive inhibition on substrate binding?",
                        "options": ["Substrate binds more easily", "Substrate cannot bind when inhibitor is bound", "Inhibitor binds to a regulatory site", "Substrate is activated"],
                        "answer": "Substrate cannot bind when inhibitor is bound"
                    },
                    {
                        "question": "Which type of enzyme regulation uses the end product to control the pathway?",
                        "options": ["Irreversible inhibition", "Feedback inhibition", "Competitive inhibition", "Allosteric activation"],
                        "answer": "Feedback inhibition"
                    },
                    {
                        "question": "Allosteric inhibitors bind to:",
                        "options": ["The active site", "Regulatory subunits", "Substrate molecules", "Products"],
                        "answer": "Regulatory subunits"
                    },
                    {
                        "question": "Which of the following is NOT true about allosteric enzymes?",
                        "options": ["They have quaternary structure", "They only have one active site", "They have regulatory and catalytic subunits", "They can switch between active and inactive forms"],
                        "answer": "They only have one active site"
                    },
                    {
                        "question": "An inhibitor that resembles the substrate and competes for the active site is called:",
                        "options": ["Noncompetitive inhibitor", "Irreversible inhibitor", "Competitive inhibitor", "Allosteric inhibitor"],
                        "answer": "Competitive inhibitor"
                    },
                    {
                        "question": "Which inhibition type changes the enzyme shape without binding the active site?",
                        "options": ["Competitive inhibition", "Irreversible inhibition", "Noncompetitive inhibition", "Feedback inhibition"],
                        "answer": "Noncompetitive inhibition"
                    },
                    {
                        "question": "Enzyme activity can be increased or decreased by:",
                        "options": ["Only inhibitors", "Only activators", "Both activators and inhibitors", "Only substrates"],
                        "answer": "Both activators and inhibitors"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Enzyme activity can be controlled through different types of inhibition and regulation mechanisms."),
                                html.Ul([
                                    html.Li("Irreversible inhibition: inhibitor binds covalently and permanently to the enzyme."),
                                    html.Li("Reversible inhibition: inhibitor binds noncovalently and can detach."),
                                    html.Li("Competitive inhibition: inhibitor competes with substrate for the active site."),
                                    html.Li("Noncompetitive inhibition: inhibitor binds elsewhere causing shape change, preventing substrate binding."),
                                    html.Li("Allosteric regulation: effectors bind regulatory subunits to switch enzyme between active and inactive forms."),
                                    html.Li("Feedback inhibition: end-product acts as a noncompetitive inhibitor of the first enzyme, shutting down the pathway."),
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Enzymes can be turned off or slowed down in different ways:"),
                                html.Ul([
                                    html.Li("Some inhibitors stick on tight and never let go (irreversible)."),
                                    html.Li("Others stick on but can let go (reversible)."),
                                    html.Li("Some blockers fight the substrate for the same spot (competitive)."),
                                    html.Li("Others bind somewhere else and change the enzyme’s shape (noncompetitive)."),
                                    html.Li("Sometimes enzymes have special ‘on/off’ switches (allosteric regulation)."),
                                    html.Li("The end product of a reaction can come back to shut the process down (feedback inhibition)."),
                                ])
                ])]
            },
            "q16": {
                "question": html.P("Know the 3 types of vegetative organs of angiosperms and the organization of their 2 main systems.  What is the difference between monocots and eudicots?"),
                "overview": html.Div([
                                html.P("Angiosperms have three main vegetative organs: leaves, stems, and roots."),
                                html.P("These organs are organized into two main systems:"),
                                html.Ul([
                                    html.Li("Root system – anchors the plant and absorbs water and nutrients."),
                                    html.Li("Shoot system – includes stems and leaves, supports reproductive structures."),
                                ]),
                                html.P("Stems support and elevate flowers and leaves and contain buds, which are undeveloped shoots."),
                                html.P("Shoots are made up of repeating units called phytomers, each consisting of one or more leaves, a node, an internode, and one or more axillary buds."),
                                html.P("The petiole is the stalk that attaches the leaf blade to the stem.")       
                ]), 
                "deep_dive": html.Div([
                                html.P("The root system mainly anchors plants and facilitates water and nutrient uptake from the soil, while the shoot system supports reproductive structures and carries out photosynthesis. "
                                        "Stems provide structural support and bear buds that can grow into new shoots or flowers. Phytomers are modular units of shoots with leaves, nodes (points where leaves attach), internodes (stem segments between nodes), and axillary buds (potential new shoots). "
                                        "The petiole is the stalk connecting leaf blades to stems, allowing flexibility and nutrient flow. "
                                        "Monocots and eudicots differ in leaf shape, root system architecture, and vascular tissue arrangement. Monocots generally have parallel-veined narrow leaves, fibrous roots, and scattered vascular bundles. "
                                        "Eudicots have net-veined broad leaves, a taproot system, and vascular bundles arranged in a ring.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter34question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What are the three main vegetative organs of angiosperms?",
                        "options": ["Roots, flowers, seeds", "Leaves, stems, roots", "Stems, flowers, fruits", "Leaves, seeds, roots"],
                        "answer": "Leaves, stems, roots"
                    },
                    {
                        "question": "The two main systems in plants are:",
                        "options": ["Shoot and root systems", "Leaf and flower systems", "Seed and fruit systems", "Stem and leaf systems"],
                        "answer": "Shoot and root systems"
                    },
                    {
                        "question": "Which plant system is responsible for anchoring and nutrient absorption?",
                        "options": ["Shoot system", "Root system", "Flower system", "Leaf system"],
                        "answer": "Root system"
                    },
                    {
                        "question": "What is the function of stems in angiosperms?",
                        "options": ["Absorb nutrients", "Elevate and support flowers and leaves", "Produce seeds", "Store food"],
                        "answer": "Elevate and support flowers and leaves"
                    },
                    {
                        "question": "A phytomer consists of:",
                        "options": ["One or more leaves, a node, an internode, and one or more axillary buds", "Only leaves and flowers", "Roots and stems", "Seeds and flowers"],
                        "answer": "One or more leaves, a node, an internode, and one or more axillary buds"
                    },
                    {
                        "question": "The petiole is:",
                        "options": ["The root tip", "The stalk that attaches the leaf blade to the stem", "The tip of a flower", "The main stem"],
                        "answer": "The stalk that attaches the leaf blade to the stem"
                    },
                    {
                        "question": "Which of the following is a characteristic of monocots?",
                        "options": ["Broad leaves", "Thin, narrow leaves", "Taproot system", "Vascular bundles arranged in a ring"],
                        "answer": "Thin, narrow leaves"
                    },
                    {
                        "question": "Which of these plants is an example of a monocot?",
                        "options": ["Maple", "Soybean", "Palm", "Rose"],
                        "answer": "Palm"
                    },
                    {
                        "question": "Eudicots typically have:",
                        "options": ["Narrow, parallel-veined leaves", "Broad leaves with net-like veins", "Scattered vascular bundles", "Fibrous roots"],
                        "answer": "Broad leaves with net-like veins"
                    },
                    {
                        "question": "Which root system is typical of eudicots?",
                        "options": ["Fibrous root system", "Taproot system", "No roots", "Adventitious root system"],
                        "answer": "Taproot system"
                    },
                    {
                        "question": "What is the main difference between the shoot and root systems?",
                        "options": ["Shoot system absorbs nutrients; root system supports flowers", "Root system anchors the plant; shoot system supports leaves and flowers", "Shoot system stores water; root system stores food", "They are the same"],
                        "answer": "Root system anchors the plant; shoot system supports leaves and flowers"
                    },
                    {
                        "question": "Where are axillary buds located?",
                        "options": ["At the root tip", "At the junction of the leaf and stem (nodes)", "On the leaf blade", "At the flower base"],
                        "answer": "At the junction of the leaf and stem (nodes)"
                    },
                    {
                        "question": "Which of the following is NOT a part of a phytomer?",
                        "options": ["Leaf", "Node", "Internode", "Flower"],
                        "answer": "Flower"
                    },
                    {
                        "question": "Monocots have vascular bundles that are:",
                        "options": ["Arranged in a ring", "Scattered throughout the stem", "Absent", "Grouped in clusters"],
                        "answer": "Scattered throughout the stem"
                    },
                    {
                        "question": "Eudicots have vascular bundles that are:",
                        "options": ["Scattered throughout the stem", "Arranged in a ring", "Grouped randomly", "Only in roots"],
                        "answer": "Arranged in a ring"
                    },
                    {
                        "question": "Which of the following plants is a eudicot?",
                        "options": ["Grass", "Lily", "Maple", "Palm"],
                        "answer": "Maple"
                    },
                    {
                        "question": "The internode is:",
                        "options": ["The segment of stem between two nodes", "The point where leaves attach", "The root tip", "The leaf stalk"],
                        "answer": "The segment of stem between two nodes"
                    },
                    {
                        "question": "What is the main function of leaves?",
                        "options": ["Support the plant", "Absorb water", "Conduct photosynthesis", "Store food"],
                        "answer": "Conduct photosynthesis"
                    },
                    {
                        "question": "Which of the following is TRUE about monocot leaves?",
                        "options": ["They have broad, net-veined leaves", "They have narrow, parallel-veined leaves", "They have a taproot system", "They lack petioles"],
                        "answer": "They have narrow, parallel-veined leaves"
                    },
                    {
                        "question": "What distinguishes eudicot stems from monocot stems?",
                        "options": ["Eudicot stems have scattered vascular bundles", "Monocot stems have vascular bundles arranged in a ring", "Eudicot stems have vascular bundles arranged in a ring", "Monocot stems have a taproot system"],
                        "answer": "Eudicot stems have vascular bundles arranged in a ring"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Angiosperms have three main vegetative organs: leaves, stems, and roots."),
                                html.P("These organs are organized into two main systems:"),
                                html.Ul([
                                    html.Li("Root system – anchors the plant and absorbs water and nutrients."),
                                    html.Li("Shoot system – includes stems and leaves, supports reproductive structures."),
                                ]),
                                html.P("Stems support and elevate flowers and leaves and contain buds, which are undeveloped shoots."),
                                html.P("Shoots are made up of repeating units called phytomers, each consisting of one or more leaves, a node, an internode, and one or more axillary buds."),
                                html.P("The petiole is the stalk that attaches the leaf blade to the stem.")       
                ])],
                "feynman": [html.Div([
                    html.P("Plants have three main parts: leaves, stems, and roots. These parts form two systems—roots that hold the plant and take up water, and shoots that hold leaves and flowers. "
                            "Stems hold leaves and flowers up and have buds that can grow into new shoots. "
                            "Monocots have narrow leaves like grasses, palms, and lilies. Eudicots have broad leaves like roses and maples.")
                ])]
            },
            "q17": {
                "question": html.P("Be familiar with the 3 structural components that make plant cells unique.  What are the 3 types of sugars that constitute the primary cell wall?"),
                "overview": html.Div([
                                html.P("Plant cells have three unique structural components that distinguish them from animal cells:"),
                                html.Ul([
                                    html.Li("Chloroplasts (plastids): Contain pigments that capture sunlight to produce food for the plant."),
                                    html.Li("Rigid cell wall: Made primarily of cellulose, providing structural support."),
                                    html.Li("Large central vacuole: Occupies up to 90% of the cell volume and stores sugars, amino acids, and enzymes. Its membrane is called the tonoplast, which contains transporter proteins.")
                                ]),
                                html.P("During cell division, plant cells form a cell plate between daughter cells. "
                                    "A glue-like substance called the middle lamella is deposited on this plate to hold cells together."),
                                    html.P("The primary cell wall consists mainly of three types of sugars:"),
                                html.Ul([
                                    html.Li(html.Strong("Cellulose:"), " A polymer of glucose molecules organized into bundles of microfibrils that form a strong lattice."),
                                    html.Li(html.Strong("Hemicellulose:"), " Highly branched polysaccharide chains that cross-link cellulose microfibrils, providing strength and flexibility."),
                                    html.Li(html.Strong("Pectins:"), " Heterogeneous polysaccharides that create a gel-like matrix and help with adhesion between cells.")
                                ]),
                                html.P("Together, these components give the plant cell wall its unique mechanical properties.")
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    "Plant cells possess several specialized structures that distinguish them from animal cells. Key among these are ",
                                    html.Strong("chloroplasts (plastids)"), ", which contain pigments such as chlorophyll. These pigments allow plants to capture sunlight and convert it into chemical energy through ",
                                    html.Strong("photosynthesis"), ", producing food that sustains the plant."
                                ]),                             
                                html.P([
                                    "Another critical structure is the ", html.Strong("rigid cell wall"), ", which encases the cell membrane and provides both ",
                                    html.Strong("structural support"), " and protection. The main component of this wall is ",
                                    html.Strong("cellulose"), ", a polysaccharide composed of glucose units linked into bundles called ",
                                    html.Strong("microfibrils"), ". These microfibrils form a lattice-like framework, granting the cell wall its ",
                                    html.Strong("tensile strength"), " and rigidity."
                                ]),                               
                                html.P([
                                    "The ", html.Strong("large central vacuole"), " is another hallmark of plant cells, often occupying up to ", 
                                    html.Strong("90% of the cell's volume"), ". It stores sugars, amino acids, enzymes, and other solutes. The vacuole's membrane, called the ",
                                    html.Strong("tonoplast"), ", contains transporter proteins that regulate the movement of substances, maintaining cellular ",
                                    html.Strong("homeostasis"), "."
                                ]),                               
                                html.P([
                                    "During plant cell division, a process called ", html.Strong("cytokinesis"), " occurs. Unlike animal cells, plant cells form a ",
                                    html.Strong("cell plate"), " at the division site. This plate develops into a new cell wall separating daughter cells. A glue-like substance, the ",
                                    html.Strong("middle lamella"), ", is deposited onto the cell plate, cementing adjacent cells together and ensuring tissue ",
                                    html.Strong("integrity"), "."
                                ]),                               
                                html.P([
                                    "The ", html.Strong("primary cell wall"), " is composed mainly of three polysaccharides that interact to form a robust and dynamic matrix:"
                                ]),                               
                                html.Ul([
                                    html.Li([html.Strong("Cellulose:"), " A linear polymer of glucose forming microfibrils that serve as the primary load-bearing structure."]),
                                    html.Li([html.Strong("Hemicellulose:"), " Branched polysaccharides that cross-link cellulose microfibrils, enhancing flexibility and strength."]),
                                    html.Li([html.Strong("Pectins:"), " Heterogeneous polysaccharides forming a gel-like matrix that fills spaces between cellulose and hemicellulose, contributing to cell adhesion and wall porosity."])
                                ]),                               
                                html.P([
                                    "Together, these components create a composite material that balances ", html.Strong("strength"), " and ", html.Strong("flexibility"), ", "
                                    "allowing plant cells to withstand mechanical stresses while enabling growth and expansion."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter34question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "Which organelle in plant cells contains pigments that capture sunlight for photosynthesis?",
                        "options": ["Mitochondria", "Chloroplasts", "Golgi apparatus", "Lysosomes", "Ribosomes"],
                        "answer": "Chloroplasts"
                    },
                    {
                        "question": "What is the primary component of the plant cell wall?",
                        "options": ["Hemicellulose", "Pectins", "Cellulose", "Chitin", "Lignin"],
                        "answer": "Cellulose"
                    },
                    {
                        "question": "The large central vacuole in plant cells can occupy up to what percentage of the cell's volume?",
                        "options": ["10%", "30%", "50%", "70%", "90%"],
                        "answer": "90%"
                    },
                    {
                        "question": "What is the name of the membrane that surrounds the central vacuole?",
                        "options": ["Tonoplast", "Plasma membrane", "Cell wall", "Endoplasmic reticulum", "Golgi membrane"],
                        "answer": "Tonoplast"
                    },
                    {
                        "question": "During plant cell cytokinesis, what structure forms to separate the daughter cells?",
                        "options": ["Cleavage furrow", "Cell plate", "Spindle fibers", "Contractile ring", "Middle lamella"],
                        "answer": "Cell plate"
                    },
                    {
                        "question": "What is the function of the middle lamella in plant cells?",
                        "options": ["Provides energy", "Cements adjacent cells together", "Transports proteins", "Synthesizes lipids", "Controls water flow"],
                        "answer": "Cements adjacent cells together"
                    },
                    {
                        "question": "Which polysaccharide forms bundles called microfibrils in the primary cell wall?",
                        "options": ["Pectins", "Hemicellulose", "Cellulose", "Starch", "Chitin"],
                        "answer": "Cellulose"
                    },
                    {
                        "question": "Hemicellulose in the plant cell wall primarily functions to:",
                        "options": ["Provide rigidity", "Cross-link cellulose microfibrils", "Store energy", "Transport water", "Act as enzymes"],
                        "answer": "Cross-link cellulose microfibrils"
                    },
                    {
                        "question": "Pectins in the primary cell wall help with:",
                        "options": ["Energy storage", "Cell adhesion and wall porosity", "DNA replication", "Protein synthesis", "Transport of ions"],
                        "answer": "Cell adhesion and wall porosity"
                    },
                    {
                        "question": "Which of the following is NOT a unique structural component of plant cells?",
                        "options": ["Chloroplasts", "Central vacuole", "Cell wall", "Lysosomes", "Tonoplast"],
                        "answer": "Lysosomes"
                    },
                    {
                        "question": "The main function of chloroplasts is to:",
                        "options": ["Produce ATP by cellular respiration", "Synthesize proteins", "Capture light energy for photosynthesis", "Store genetic information", "Digest cellular waste"],
                        "answer": "Capture light energy for photosynthesis"
                    },
                    {
                        "question": "The tonoplast contains transporter proteins that regulate:",
                        "options": ["Movement of substances in and out of the vacuole", "Protein synthesis", "Cell division", "DNA replication", "Lipid synthesis"],
                        "answer": "Movement of substances in and out of the vacuole"
                    },
                    {
                        "question": "The plant cell wall provides:",
                        "options": ["Flexibility only", "Structural support and protection", "Energy storage", "Protein synthesis", "Membrane transport"],
                        "answer": "Structural support and protection"
                    },
                    {
                        "question": "The lattice-like framework in the cell wall is primarily made of:",
                        "options": ["Proteins", "Lipids", "Cellulose microfibrils", "Starch granules", "Nucleic acids"],
                        "answer": "Cellulose microfibrils"
                    },
                    {
                        "question": "Which statement about the central vacuole is TRUE?",
                        "options": [
                            "It synthesizes proteins",
                            "It occupies most of the cell volume",
                            "It is surrounded by the plasma membrane",
                            "It is responsible for photosynthesis",
                            "It contains ribosomes"
                        ],
                        "answer": "It occupies most of the cell volume"
                    },
                    {
                        "question": "The middle lamella is primarily composed of:",
                        "options": ["Cellulose", "Pectins", "Proteins", "Lignin", "Hemicellulose"],
                        "answer": "Pectins"
                    },
                    {
                        "question": "Which polysaccharide acts as a gel-like matrix filling spaces between cellulose and hemicellulose?",
                        "options": ["Cellulose", "Pectins", "Hemicellulose", "Starch", "Chitin"],
                        "answer": "Pectins"
                    },
                    {
                        "question": "Microfibrils in the plant cell wall are made up of:",
                        "options": ["Glucose polymers", "Amino acids", "Fatty acids", "Nucleotides", "Cholesterol"],
                        "answer": "Glucose polymers"
                    },
                    {
                        "question": "The primary cell wall balances:",
                        "options": ["Rigidity only", "Flexibility only", "Strength and flexibility", "Elasticity and permeability", "Porosity only"],
                        "answer": "Strength and flexibility"
                    },
                    {
                        "question": "Which of the following correctly pairs a plant cell component with its function?",
                        "options": [
                            "Chloroplasts – Protein synthesis",
                            "Tonoplast – Photosynthesis",
                            "Central vacuole – Storage and maintaining homeostasis",
                            "Cellulose – Energy storage",
                            "Middle lamella – Cell respiration"
                        ],
                        "answer": "Central vacuole – Storage and maintaining homeostasis"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Plant cells have three unique structural components that distinguish them from animal cells:"),
                                html.Ul([
                                    html.Li("Chloroplasts (plastids): Contain pigments that capture sunlight to produce food for the plant."),
                                    html.Li("Rigid cell wall: Made primarily of cellulose, providing structural support."),
                                    html.Li("Large central vacuole: Occupies up to 90% of the cell volume and stores sugars, amino acids, and enzymes. Its membrane is called the tonoplast, which contains transporter proteins.")
                                ]),
                                html.P("During cell division, plant cells form a cell plate between daughter cells. "
                                    "A glue-like substance called the middle lamella is deposited on this plate to hold cells together."),
                                    html.P("The primary cell wall consists mainly of three types of sugars:"),
                                html.Ul([
                                    html.Li(html.Strong("Cellulose:"), " A polymer of glucose molecules organized into bundles of microfibrils that form a strong lattice."),
                                    html.Li(html.Strong("Hemicellulose:"), " Highly branched polysaccharide chains that cross-link cellulose microfibrils, providing strength and flexibility."),
                                    html.Li(html.Strong("Pectins:"), " Heterogeneous polysaccharides that create a gel-like matrix and help with adhesion between cells.")
                                ]),
                                html.P("Together, these components give the plant cell wall its unique mechanical properties.")
                ])],
                "feynman": [html.Div([
                                html.P("Plant cells have three special parts:"),
                                html.Ul([
                                    html.Li("Chloroplasts that make food from sunlight."),
                                    html.Li("A strong cell wall mostly made of cellulose."),
                                    html.Li("A big central vacuole that stores important substances.")
                                ]),
                                html.P("The cell wall sugars are:"),
                                html.Ul([
                                    html.Li("Cellulose – forms strong fibers."),
                                    html.Li("Hemicellulose – connects those fibers."),
                                    html.Li("Pectins – act like glue to hold cells together.")
                                ]),
                                html.P("When plant cells divide, a cell plate forms between them with a sticky middle lamella that keeps them stuck together.")
                ])]
            },
            "q18": {
                "question": html.P("Be able to describe the function, and example cell types, associated with the Dermal tissue, ground tissue and vascular tissue systems."),
                "overview": html.Div([
                                html.P([
                                    "Plants have three main tissue systems that work together to support life functions:",
                                ]),
                                html.Ul([
                                    html.Li("The ground tissue system provides support, storage, and photosynthesis and forms most of the plant body."),
                                    html.Li("The vascular tissue system transports water, minerals, and nutrients through xylem and phloem vessels."),
                                    html.Li("The dermal tissue system forms the protective outer layer (epidermis) and includes specialized cells like guard cells, trichomes, and root hairs."),
                                ]),
                                html.P("These systems extend throughout the plant in a concentric arrangement, enabling coordination of growth, transport, and protection.")
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    "Plants have three main tissue systems that work together to support growth, transport, and protection:"
                                ]),                             
                                html.Ul([
                                    html.Li([
                                        html.Strong("Ground Tissue System:"), 
                                        " This system makes up most of the plant body and is responsible for ", 
                                        html.Strong("support, storage, and photosynthesis"), "."
                                    ]),
                                    html.Li([
                                        html.Strong("Vascular Tissue System:"), 
                                        " Specialized for ", html.Strong("transport"), " within the plant. It includes the ", 
                                        html.Strong("xylem"), ", which moves water and minerals from the roots to the rest of the plant, and the ", 
                                        html.Strong("phloem"), ", which transports carbohydrates from sources to sinks."
                                    ]),
                                    html.Li([
                                        html.Strong("Dermal Tissue System:"), 
                                        " Forms the plant’s outer protective layer called the ", html.Strong("epidermis"), 
                                        ", usually a single cell layer."
                                    ])
                                ]),                              
                                html.P("Within these systems, different specialized cell types serve unique roles:"),                             
                                html.Ul([
                                    html.Li([
                                        html.Strong("Ground tissue cell types:"), 
                                        html.Ul([
                                            html.Li("Parenchyma: thin-walled cells with large central vacuoles; sites of photosynthesis in leaves and storage in fruits and roots."),
                                            html.Li("Collenchyma: provide flexible structural support."),
                                            html.Li("Sclerenchyma: provide rigid structural support with thickened cell walls.")
                                        ])
                                    ]),
                                    html.Li([
                                        html.Strong("Dermal tissue cell types:"), 
                                        html.Ul([
                                            html.Li("Epidermal cells: form the outer layer protecting the plant."),
                                            html.Li("Stomatal guard cells: control pores (stomata) for gas exchange."),
                                            html.Li("Trichomes: leaf hairs that protect against insects and solar radiation."),
                                            html.Li("Root hairs: increase surface area for water and mineral uptake.")
                                        ])
                                    ])
                                ]),
                                html.P([
                                    "These tissue systems are arranged concentrically throughout the plant body, ensuring that the functions of support, protection, and transport are coordinated across all plant organs."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter34question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What are the three main tissue systems in plants?",
                        "options": ["Ground, Vascular, Dermal", "Xylem, Phloem, Epidermis", "Parenchyma, Collenchyma, Sclerenchyma", "Roots, Stems, Leaves"],
                        "answer": "Ground, Vascular, Dermal"
                    },
                    {
                        "question": "Which plant tissue system is primarily responsible for photosynthesis?",
                        "options": ["Dermal tissue", "Vascular tissue", "Ground tissue", "Epidermis"],
                        "answer": "Ground tissue"
                    },
                    {
                        "question": "What is the function of vascular tissue in plants?",
                        "options": ["Support and storage", "Protection against insects", "Transport of water, minerals, and nutrients", "Photosynthesis"],
                        "answer": "Transport of water, minerals, and nutrients"
                    },
                    {
                        "question": "Which cells make up the dermal tissue system?",
                        "options": ["Xylem and Phloem", "Guard cells, trichomes, root hairs", "Parenchyma and collenchyma", "Sclerenchyma and parenchyma"],
                        "answer": "Guard cells, trichomes, root hairs"
                    },
                    {
                        "question": "What is the role of guard cells in plants?",
                        "options": ["Store nutrients", "Transport water", "Control the opening and closing of stomata for gas exchange", "Provide structural support"],
                        "answer": "Control the opening and closing of stomata for gas exchange"
                    },
                    {
                        "question": "Which plant tissue system forms the protective outer layer called the epidermis?",
                        "options": ["Ground tissue", "Vascular tissue", "Dermal tissue", "Phloem"],
                        "answer": "Dermal tissue"
                    },
                    {
                        "question": "Xylem is part of which plant tissue system?",
                        "options": ["Dermal", "Ground", "Vascular", "Parenchyma"],
                        "answer": "Vascular"
                    },
                    {
                        "question": "What type of transport does phloem perform?",
                        "options": ["Water transport", "Carbohydrate transport from sources to sinks", "Gas exchange", "Structural support"],
                        "answer": "Carbohydrate transport from sources to sinks"
                    },
                    {
                        "question": "What is the primary function of parenchyma cells in ground tissue?",
                        "options": ["Transport water", "Storage and photosynthesis", "Protection", "Transport sugars"],
                        "answer": "Storage and photosynthesis"
                    },
                    {
                        "question": "Which plant tissue system includes trichomes?",
                        "options": ["Ground tissue", "Dermal tissue", "Vascular tissue", "Phloem"],
                        "answer": "Dermal tissue"
                    },
                    {
                        "question": "Root hairs are specialized cells found in which tissue system?",
                        "options": ["Vascular", "Dermal", "Ground", "Xylem"],
                        "answer": "Dermal"
                    },
                    {
                        "question": "Collenchyma cells provide what type of support in plants?",
                        "options": ["Rigid and inflexible support", "Flexible structural support", "Water transport", "Nutrient storage"],
                        "answer": "Flexible structural support"
                    },
                    {
                        "question": "Sclerenchyma cells are known for:",
                        "options": ["Flexible support", "Photosynthesis", "Rigid structural support with thickened walls", "Transport of minerals"],
                        "answer": "Rigid structural support with thickened walls"
                    },
                    {
                        "question": "Which tissue system is the largest by volume in most plants?",
                        "options": ["Dermal tissue", "Ground tissue", "Vascular tissue", "Phloem"],
                        "answer": "Ground tissue"
                    },
                    {
                        "question": "What type of arrangement do the three tissue systems have within the plant body?",
                        "options": ["Random", "Concentric", "Linear", "Scattered"],
                        "answer": "Concentric"
                    },
                    {
                        "question": "The epidermis typically consists of how many cell layers?",
                        "options": ["Multiple layers", "Two layers", "One layer", "No layers"],
                        "answer": "One layer"
                    },
                    {
                        "question": "What is the main role of trichomes on leaves?",
                        "options": ["Photosynthesis", "Protection against insects and solar radiation", "Transporting water", "Storing nutrients"],
                        "answer": "Protection against insects and solar radiation"
                    },
                    {
                        "question": "Which tissue system contains the phloem?",
                        "options": ["Ground tissue", "Vascular tissue", "Dermal tissue", "Parenchyma"],
                        "answer": "Vascular tissue"
                    },
                    {
                        "question": "What is the main function of root hairs?",
                        "options": ["Absorbing water and minerals", "Photosynthesis", "Protection", "Transporting sugars"],
                        "answer": "Absorbing water and minerals"
                    },
                    {
                        "question": "Which cell type is the main site of photosynthesis in leaves?",
                        "options": ["Sclerenchyma", "Parenchyma", "Collenchyma", "Xylem"],
                        "answer": "Parenchyma"
                    }
                ],
                "blurting": [html.Div([
                                html.P([
                                    "Plants have three main tissue systems that work together to support life functions:",
                                ]),
                                html.Ul([
                                    html.Li("The ground tissue system provides support, storage, and photosynthesis and forms most of the plant body."),
                                    html.Li("The vascular tissue system transports water, minerals, and nutrients through xylem and phloem vessels."),
                                    html.Li("The dermal tissue system forms the protective outer layer (epidermis) and includes specialized cells like guard cells, trichomes, and root hairs."),
                                ]),
                                html.P("These systems extend throughout the plant in a concentric arrangement, enabling coordination of growth, transport, and protection.")
                ])],
                "feynman": [html.Div([
                                html.P("Plants have three main tissue systems that do different jobs:"),
                                html.Ul([
                                    html.Li("Ground tissue: acts like the plant’s body—it stores food, helps with photosynthesis, and provides support."),
                                    html.Li("Vascular tissue: works like the plant’s plumbing system—it moves water and food using xylem and phloem."),
                                    html.Li("Dermal tissue: functions like the plant’s skin—it protects the plant and has special cells such as:"),
                                ]),
                                html.Ul([
                                    html.Li("Guard cells that open and close pores (stomata) for gas exchange."),
                                    html.Li("Trichomes (tiny hairs) that protect against insects and sunlight."),
                                    html.Li("Root hairs that increase water and mineral absorption."),
                                ]),
                                html.P("All these systems are arranged in layers and work together throughout the plant.")
                ])]
            },
            "q19": {
                "question": html.P("Understand how apical and lateral meristems lead to primary and secondary growth, respectively."),
                "overview": html.Div([
                                html.P("Plants grow in two main ways through specialized regions called meristems:"),
                                html.Ul([
                                    html.Li(html.Strong("Apical meristems:"), " zones of cell division that cause primary growth, resulting in lengthening of shoots and roots."),
                                    html.Li(html.Strong("Lateral meristems:"), " enable secondary growth by increasing the plant's diameter, producing wood and bark."),
                                ]),
                                html.P("Primary growth forms the non-woody parts of the plant (herbaceous plants and monocots). Secondary growth creates the woody parts seen in trees and shrubs.")
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    "Apical meristems are located at the tips of roots and shoots and are responsible for the elongation of these structures. ",
                                    "These meristems actively divide cells, producing new cells that differentiate into various tissues, allowing the plant to grow taller and roots to extend deeper. ",
                                    "This process is called ", html.Strong("primary growth"), ", and it forms the primary plant body, which consists mostly of non-woody tissues. ",
                                    "Herbaceous plants and monocots only have this primary growth."
                                ]),
                                html.P([
                                    "Lateral meristems, on the other hand, are found along the sides of stems and roots. ",
                                    "They are responsible for ", html.Strong("secondary growth"), ", which increases the girth or diameter of the plant. ",
                                    "This process produces the secondary plant body, which includes wood (from the vascular cambium) and bark (from the cork cambium). ",
                                    "Trees and shrubs undergo significant secondary growth, allowing them to become thicker and sturdier."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter34question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What type of growth do apical meristems contribute to?",
                        "options": ["Secondary growth", "Diameter growth", "Primary growth", "Woody tissue growth"],
                        "answer": "Primary growth"
                    },
                    {
                        "question": "What is the result of primary growth in plants?",
                        "options": ["Increase in diameter", "Formation of bark", "Lengthening of shoots and roots", "Production of wood"],
                        "answer": "Lengthening of shoots and roots"
                    },
                    {
                        "question": "Which type of plant body is formed by primary growth?",
                        "options": ["Secondary plant body", "Wood and bark", "Primary plant body", "Cambium layer"],
                        "answer": "Primary plant body"
                    },
                    {
                        "question": "What is the main function of lateral meristems?",
                        "options": ["Root elongation", "Branch formation", "Increase in diameter", "Leaf development"],
                        "answer": "Increase in diameter"
                    },
                    {
                        "question": "Which type of growth produces wood and bark?",
                        "options": ["Primary growth", "Apical growth", "Herbaceous growth", "Secondary growth"],
                        "answer": "Secondary growth"
                    },
                    {
                        "question": "Which types of plants consist entirely of the primary plant body?",
                        "options": ["Woody plants and trees", "Herbaceous plants and monocots", "Shrubs and ferns", "Gymnosperms and mosses"],
                        "answer": "Herbaceous plants and monocots"
                    },
                    {
                        "question": "Where are apical meristems located?",
                        "options": ["Along stems and roots", "Inside vascular bundles", "At the tips of roots and shoots", "In the bark"],
                        "answer": "At the tips of roots and shoots"
                    },
                    {
                        "question": "Which part of the plant is affected by lateral meristems?",
                        "options": ["Height", "Leaf size", "Root depth", "Width (diameter)"],
                        "answer": "Width (diameter)"
                    },
                    {
                        "question": "What kind of plant body do trees and shrubs have?",
                        "options": ["Primary only", "Secondary only", "Both primary and secondary", "Neither primary nor secondary"],
                        "answer": "Both primary and secondary"
                    },
                    {
                        "question": "Which meristem is responsible for producing the vascular cambium and cork cambium?",
                        "options": ["Apical meristem", "Lateral meristem", "Axillary meristem", "Intercalary meristem"],
                        "answer": "Lateral meristem"
                    },
                    {
                        "question": "What kind of growth results in branching of plants?",
                        "options": ["Secondary growth", "Cambial growth", "Apical meristem growth", "Xylem expansion"],
                        "answer": "Apical meristem growth"
                    },
                    {
                        "question": "What is a major difference between primary and secondary growth?",
                        "options": ["Primary growth increases thickness; secondary growth increases height", "Primary growth forms wood; secondary forms leaves", "Primary increases height; secondary increases diameter", "They occur at the same plant locations"],
                        "answer": "Primary increases height; secondary increases diameter"
                    },
                    {
                        "question": "Which structure produces the primary plant body?",
                        "options": ["Cork cambium", "Xylem", "Apical meristem", "Lateral meristem"],
                        "answer": "Apical meristem"
                    },
                    {
                        "question": "What part of the plant results from the activity of lateral meristems?",
                        "options": ["Leaves and flowers", "Roots and stems", "Wood and bark", "Fruits and seeds"],
                        "answer": "Wood and bark"
                    },
                    {
                        "question": "Which meristem is responsible for forming new branches?",
                        "options": ["Apical meristem", "Lateral meristem", "Cambium meristem", "Trichome meristem"],
                        "answer": "Apical meristem"
                    },
                    {
                        "question": "Which type of growth is most visible in tree trunks?",
                        "options": ["Primary growth", "Apical growth", "Secondary growth", "Parenchymal growth"],
                        "answer": "Secondary growth"
                    },
                    {
                        "question": "What do we call the body formed by secondary growth?",
                        "options": ["Primary plant body", "Cambial structure", "Secondary plant body", "Monocot framework"],
                        "answer": "Secondary plant body"
                    },
                    {
                        "question": "Which type of growth occurs in herbaceous plants only?",
                        "options": ["Secondary growth", "Xylem expansion", "Primary growth", "Cambial splitting"],
                        "answer": "Primary growth"
                    },
                    {
                        "question": "Which process adds girth to stems and roots?",
                        "options": ["Photosynthesis", "Primary growth", "Secondary growth", "Apical elongation"],
                        "answer": "Secondary growth"
                    },
                    {
                        "question": "In which part of the plant would you expect apical meristems to be most active?",
                        "options": ["Stem base", "Root tip", "Leaf midrib", "Bark surface"],
                        "answer": "Root tip"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Plants grow in two main ways through specialized regions called meristems:"),
                                html.Ul([
                                    html.Li(html.Strong("Apical meristems:"), " zones of cell division that cause primary growth, resulting in lengthening of shoots and roots."),
                                    html.Li(html.Strong("Lateral meristems:"), " enable secondary growth by increasing the plant's diameter, producing wood and bark."),
                                ]),
                                html.P("Primary growth forms the non-woody parts of the plant (herbaceous plants and monocots). Secondary growth creates the woody parts seen in trees and shrubs.")
                ])],
                "feynman": [html.Div([
                                html.P([
                                    "Plants grow taller and longer because of special growing spots at their tips called apical meristems. ",
                                    "These make new cells that add to the length of roots and shoots. ",
                                    "To grow wider and thicker, plants use other growing spots on the sides called lateral meristems. ",
                                    "These make wood and bark, helping trees and shrubs get big and strong."
                                ])
                ])]
            },
            "q20": {
                "question": html.P("Be familiar with the 3 major zones of development in the plant root."),
                "overview": html.Div([
                                html.P("Plant roots grow and develop through three main zones:"),
                                html.Ul([
                                    html.Li(html.Strong("Zone of Division:"), " Includes the apical and primary meristems, where cells are actively dividing."),
                                    html.Li(html.Strong("Zone of Elongation:"), " Cells lengthen and push the root tip forward through the soil."),
                                    html.Li(html.Strong("Zone of Maturation:"), " Cells differentiate into specialized cell types to perform various functions.")
                                ]),
                                html.P(["A special region called the ", html.Strong("quiescent center"), " lies in the root apical meristem and can become active if needed."])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                "Root development in plants is organized into three major zones that each serve a unique function in growth and differentiation."
                                ]),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Zone of Division: "),
                                        "Located at the tip of the root and includes both the apical and primary meristems. ",
                                        "This is where cells are actively undergoing mitosis to increase the number of cells. ",
                                        "The region also contains a ", html.Strong("quiescent center"), ", a group of cells that divide very slowly but can become active when the root is damaged or in need of growth."
                                    ]),
                                    html.Li([
                                        html.Strong("Zone of Elongation: "),
                                        "Just above the zone of division, this is where newly formed cells increase in size. ",
                                        "The elongation of these cells pushes the root cap and the root tip further into the soil. ",
                                        "In plants undergoing secondary growth, this zone also helps push outward to develop tissues like bark through activity in the cork cambium."
                                    ]),
                                    html.Li([
                                        html.Strong("Zone of Maturation (also called differentiation): "),
                                        "This is where the elongated cells specialize into distinct cell types such as xylem, phloem, or root hairs. ",
                                        "These mature cells contribute to nutrient absorption, transport, and support."
                                    ])
                                ]), 
                ]),
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter34question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the primary function of the zone of division in a plant root?",
                        "options": ["Cell elongation", "Cell differentiation", "Cell division", "Nutrient absorption", "Root hair formation"],
                        "answer": "Cell division"
                    },
                    {
                        "question": "Which zone in a developing root is responsible for pushing the root tip through the soil?",
                        "options": ["Zone of Maturation", "Zone of Division", "Quiescent Center", "Zone of Elongation", "Root Cap"],
                        "answer": "Zone of Elongation"
                    },
                    {
                        "question": "Where do cells begin to specialize into distinct types such as xylem and phloem?",
                        "options": ["Zone of Division", "Zone of Elongation", "Zone of Maturation", "Root Cap", "Meristem"],
                        "answer": "Zone of Maturation"
                    },
                    {
                        "question": "Which region contains cells that divide slowly but can become active when needed?",
                        "options": ["Zone of Elongation", "Cortex", "Root Cap", "Quiescent Center", "Phloem"],
                        "answer": "Quiescent Center"
                    },
                    {
                        "question": "What is the role of the quiescent center in the root apical meristem?",
                        "options": ["Absorb nutrients", "Push root through soil", "Divide rapidly", "Serve as a reserve of stem cells", "Transport water"],
                        "answer": "Serve as a reserve of stem cells"
                    },
                    {
                        "question": "What process primarily occurs in the zone of elongation?",
                        "options": ["Photosynthesis", "Cell specialization", "Cell growth and lengthening", "Seed formation", "Flowering"],
                        "answer": "Cell growth and lengthening"
                    },
                    {
                        "question": "What happens to cells in the zone of maturation?",
                        "options": ["They divide rapidly", "They absorb water", "They differentiate into specific cell types", "They elongate", "They die"],
                        "answer": "They differentiate into specific cell types"
                    },
                    {
                        "question": "The root apical meristem is located in which zone?",
                        "options": ["Zone of Elongation", "Zone of Maturation", "Zone of Division", "Endodermis", "Xylem"],
                        "answer": "Zone of Division"
                    },
                    {
                        "question": "Which of the following does NOT occur in the zone of elongation?",
                        "options": ["Cell division", "Cell growth", "Root lengthening", "Expansion of cells", "Pushing root forward"],
                        "answer": "Cell division"
                    },
                    {
                        "question": "The zone of maturation is also known as the zone of:",
                        "options": ["Extension", "Differentiation", "Division", "Replication", "Regeneration"],
                        "answer": "Differentiation"
                    },
                    {
                        "question": "Which zone is directly above the root cap?",
                        "options": ["Zone of Elongation", "Zone of Maturation", "Zone of Division", "Phloem", "Endodermis"],
                        "answer": "Zone of Division"
                    },
                    {
                        "question": "Which of the following structures protects the root tip?",
                        "options": ["Xylem", "Root hairs", "Root cap", "Zone of Maturation", "Vascular tissue"],
                        "answer": "Root cap"
                    },
                    {
                        "question": "What is one of the first steps in root growth?",
                        "options": ["Cell specialization", "Root hair formation", "Rapid cell division", "Cork formation", "Photosynthesis"],
                        "answer": "Rapid cell division"
                    },
                    {
                        "question": "What causes the root tip to grow deeper into the soil?",
                        "options": ["Cell specialization", "Photosynthesis", "Cell elongation", "Cork cambium activity", "Vascular tissue expansion"],
                        "answer": "Cell elongation"
                    },
                    {
                        "question": "What would happen if the quiescent center becomes damaged?",
                        "options": ["Root stops growing", "Photosynthesis increases", "It activates and resumes cell division", "Water transport ceases", "Nutrients stop being absorbed"],
                        "answer": "It activates and resumes cell division"
                    },
                    {
                        "question": "In which zone are root hairs typically found?",
                        "options": ["Zone of Division", "Zone of Elongation", "Zone of Maturation", "Quiescent Center", "Root Cap"],
                        "answer": "Zone of Maturation"
                    },
                    {
                        "question": "What is the function of root hairs?",
                        "options": ["Protect root tip", "Push root forward", "Absorb water and minerals", "Anchor the plant", "Produce energy"],
                        "answer": "Absorb water and minerals"
                    },
                    {
                        "question": "Secondary growth in roots is mainly associated with which part of the developmental zones?",
                        "options": ["Zone of Division", "Zone of Elongation", "Zone of Maturation", "Root Cap", "Xylem"],
                        "answer": "Zone of Elongation"
                    },
                    {
                        "question": "Which zone comes last in the developmental sequence of a root?",
                        "options": ["Zone of Maturation", "Zone of Division", "Zone of Elongation", "Root Cap", "Quiescent Center"],
                        "answer": "Zone of Maturation"
                    },
                    {
                        "question": "Which process occurs first as a root grows?",
                        "options": ["Cell differentiation", "Root hair formation", "Cell elongation", "Cell division", "Photosynthesis"],
                        "answer": "Cell division"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Plant roots grow and develop through three main zones:"),
                                html.Ul([
                                    html.Li(html.Strong("Zone of Division:"), " Includes the apical and primary meristems, where cells are actively dividing."),
                                    html.Li(html.Strong("Zone of Elongation:"), " Cells lengthen and push the root tip forward through the soil."),
                                    html.Li(html.Strong("Zone of Maturation:"), " Cells differentiate into specialized cell types to perform various functions.")
                                ]),
                                html.P(["A special region called the ", html.Strong("quiescent center"), " lies in the root apical meristem and can become active if needed."])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    "Plant roots grow in sections. ",
                                    "At the very tip, there’s a spot where new cells are made—that’s the ", html.Strong("zone of division"), ". ",
                                    "Right above it, the ", html.Strong("zone of elongation"), " stretches those new cells so the root can grow longer and move through soil. ",
                                    "Finally, in the ", html.Strong("zone of maturation"), ", the cells get their jobs, like carrying water or nutrients. ",
                                    "There’s also a quiet area called the ", html.Strong("quiescent center"), " that can jump into action if the plant needs help growing or healing."
                                ])
                ])]
            },
            "q21": {
                "question": html.P("Understand the concept of water potential and how it relates to solute and pressure potential.  If given a diffusion scenario with megapascal units, be able to predict in which direction water will move."),
                "overview": html.Div([
                                html.P("Water potential determines the direction water moves across membranes. It is calculated as:"),
                                html.P(html.Strong("Water Potential (Ψ) = Solute Potential (Ψs) + Pressure Potential (Ψp)")),
                                html.Ul([
                                    html.Li("Water moves toward areas with more negative water potential."),
                                    html.Li("Solute potential lowers water potential (adding solutes makes Ψ more negative)."),
                                    html.Li("Pressure potential increases water potential (adding pressure makes Ψ less negative or even positive)."),
                                    html.Li("Measured in megapascals (MPa).")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P("Water potential is a key concept in plant water transport. It describes the overall tendency of a solution to take up water from pure water across a selectively permeable membrane."),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Solute Potential (Ψs): "),
                                        "Solutes bind to water molecules and reduce the number of free water molecules. This lowers the water potential. "
                                        "The more solutes present, the more negative the solute potential becomes."
                                    ]),
                                    html.Li([
                                        html.Strong("Pressure Potential (Ψp): "),
                                        "Refers to the physical pressure on water. Positive pressure (e.g., turgor pressure inside a plant cell) "
                                        "increases water potential and resists further water uptake. Negative pressure (e.g., in xylem) decreases it."
                                    ]),
                                    html.Li([
                                        html.Strong("Water Movement: "),
                                        "Water always moves from a region of higher (less negative) water potential to lower (more negative) water potential."
                                    ]),
                                    html.Li([
                                        html.Strong("Turgor Pressure: "),
                                        "When a plant cell is placed in pure water, water enters the cell due to a negative solute potential. "
                                        "The cell swells until pressure builds up (turgor pressure) to oppose further water entry."
                                    ])
                                ]),
                                html.P("Water potential explains how plants take up water from the soil and how internal water distribution is maintained.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter35question1.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the formula for calculating water potential (Ψ)?",
                        "options": [
                            "Ψ = Solute Potential - Pressure Potential",
                            "Ψ = Solute Potential + Pressure Potential",
                            "Ψ = Pressure Potential - Solute Potential",
                            "Ψ = Osmosis Rate x Pressure",
                            "Ψ = Water Volume / Solute Volume"
                        ],
                        "answer": "Ψ = Solute Potential + Pressure Potential"
                    },
                    {
                        "question": "In which direction does water move based on water potential?",
                        "options": [
                            "From high to low pressure",
                            "From high to low solute concentration",
                            "Toward the area with the highest water potential",
                            "Toward the area with the most negative water potential",
                            "Away from turgor pressure"
                        ],
                        "answer": "Toward the area with the most negative water potential"
                    },
                    {
                        "question": "Which of the following will make water potential more negative?",
                        "options": [
                            "Adding pure water",
                            "Applying pressure",
                            "Adding solutes",
                            "Reducing temperature",
                            "Increasing cell size"
                        ],
                        "answer": "Adding solutes"
                    },
                    {
                        "question": "Which of the following increases water potential?",
                        "options": [
                            "Adding solutes",
                            "Adding negative pressure",
                            "Decreasing temperature",
                            "Adding pressure",
                            "Removing water"
                        ],
                        "answer": "Adding pressure"
                    },
                    {
                        "question": "What does turgor pressure refer to?",
                        "options": [
                            "Water leaving a plant cell",
                            "The water pressure in the soil",
                            "The pressure from the central vacuole against the cell wall",
                            "The osmotic potential in xylem",
                            "The amount of dissolved solutes in the cell"
                        ],
                        "answer": "The pressure from the central vacuole against the cell wall"
                    },
                    {
                        "question": "If a plant cell is placed in pure water, what happens initially?",
                        "options": [
                            "Water leaves the cell",
                            "The cell shrinks",
                            "Water enters the cell due to its more negative solute potential",
                            "The solute concentration increases",
                            "No change occurs"
                        ],
                        "answer": "Water enters the cell due to its more negative solute potential"
                    },
                    {
                        "question": "What happens when solute potential is very negative?",
                        "options": [
                            "Water potential increases",
                            "Pressure potential decreases",
                            "Water enters the region",
                            "Water exits the region",
                            "Turgor pressure decreases"
                        ],
                        "answer": "Water enters the region"
                    },
                    {
                        "question": "What happens to the rate of osmosis when pressure potential increases?",
                        "options": [
                            "It stops entirely",
                            "It decreases",
                            "It increases indefinitely",
                            "It becomes erratic",
                            "It causes exocytosis"
                        ],
                        "answer": "It decreases"
                    },
                    {
                        "question": "Which of the following conditions results in the highest water potential?",
                        "options": [
                            "High solute potential and low pressure potential",
                            "Pure water with no solutes and no pressure",
                            "High solute concentration and no pressure",
                            "Negative solute potential and negative pressure potential",
                            "Presence of ATP"
                        ],
                        "answer": "Pure water with no solutes and no pressure"
                    },
                    {
                        "question": "Why can’t a plant cell expand indefinitely in water?",
                        "options": [
                            "Because the cell loses solutes",
                            "Because the cell wall limits expansion",
                            "Because it runs out of ATP",
                            "Because it excretes excess water",
                            "Because cytoplasm solidifies"
                        ],
                        "answer": "Because the cell wall limits expansion"
                    },
                    {
                        "question": "What units is water potential measured in?",
                        "options": [
                            "Bars",
                            "Joules",
                            "Megapascals (MPa)",
                            "Milliliters (mL)",
                            "Volts"
                        ],
                        "answer": "Megapascals (MPa)"
                    },
                    {
                        "question": "Which of the following would most likely happen if solutes were added to the inside of a plant cell?",
                        "options": [
                            "Water would exit the cell",
                            "The cell would lyse",
                            "Water would enter the cell",
                            "No water movement would occur",
                            "Turgor pressure would disappear"
                        ],
                        "answer": "Water would enter the cell"
                    },
                    {
                        "question": "If Ψ of cell A is -0.4 MPa and Ψ of cell B is -0.8 MPa, which way will water move?",
                        "options": [
                            "From B to A",
                            "From A to B",
                            "No movement will occur",
                            "Both directions",
                            "Depends on temperature"
                        ],
                        "answer": "From A to B"
                    },
                    {
                        "question": "What is the role of the cell wall during water uptake?",
                        "options": [
                            "It attracts solutes",
                            "It stores pressure potential",
                            "It prevents ion movement",
                            "It limits how much the cell can swell",
                            "It keeps enzymes inside"
                        ],
                        "answer": "It limits how much the cell can swell"
                    },
                    {
                        "question": "Which of the following would result in a decrease in turgor pressure?",
                        "options": [
                            "Water entering the cell",
                            "Water leaving the cell",
                            "Solute accumulation",
                            "Starch digestion",
                            "Protein synthesis"
                        ],
                        "answer": "Water leaving the cell"
                    },
                    {
                        "question": "How does pressure potential affect water movement?",
                        "options": [
                            "Higher pressure always draws water in",
                            "Higher pressure resists water entry",
                            "Pressure has no effect on osmosis",
                            "Only negative pressure influences osmosis",
                            "Pressure potential drives diffusion of solutes"
                        ],
                        "answer": "Higher pressure resists water entry"
                    },
                    {
                        "question": "Why does water potential include both solute and pressure potential?",
                        "options": [
                            "Solutes don't bind water",
                            "Pressure potential only applies in animals",
                            "Because both affect water's ability to move",
                            "Only solutes can cause osmosis",
                            "It simplifies calculations"
                        ],
                        "answer": "Because both affect water's ability to move"
                    },
                    {
                        "question": "What would happen to a turgid plant cell in a hypertonic solution?",
                        "options": [
                            "It gains water",
                            "It bursts",
                            "It shrinks",
                            "No change",
                            "It creates ATP"
                        ],
                        "answer": "It shrinks"
                    },
                    {
                        "question": "What happens to water potential if pressure is added to a solution?",
                        "options": [
                            "It becomes more negative",
                            "It increases",
                            "It causes solutes to increase",
                            "It causes osmosis to reverse",
                            "It breaks the membrane"
                        ],
                        "answer": "It increases"
                    },
                    {
                        "question": "What is the water potential of pure water under normal conditions?",
                        "options": [
                            "0 MPa",
                            "-1 MPa",
                            "+1 MPa",
                            "-0.5 MPa",
                            "100 MPa"
                        ],
                        "answer": "0 MPa"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Water potential determines the direction water moves across membranes. It is calculated as:"),
                                html.P(html.Strong("Water Potential (Ψ) = Solute Potential (Ψs) + Pressure Potential (Ψp)")),
                                html.Ul([
                                    html.Li("Water moves toward areas with more negative water potential."),
                                    html.Li("Solute potential lowers water potential (adding solutes makes Ψ more negative)."),
                                    html.Li("Pressure potential increases water potential (adding pressure makes Ψ less negative or even positive)."),
                                    html.Li("Measured in megapascals (MPa).")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P("Water potential tells us where water will go. Think of it like a tug-of-war: water moves toward where it’s needed most—where water is 'low' (more negative)."),
                                html.Ul([
                                    html.Li("Adding salt (solute) lowers water potential—water rushes in."),
                                    html.Li("Adding pressure pushes water out."),
                                    html.Li("Plants use this rule to take water in through their roots and keep their cells full and firm."),
                                    html.Li("Turgor pressure is like the cell getting puffed up until it can’t take in more water.")
                                ])
                ])]
            },
            "q22": {
                "question": html.P("Be able to explain how the apoplast and symplast contribute to the uptake of water in plant roots.  Know how to identify these structures on a diagram."),
                "overview": html.Div([
                                html.P("Water and minerals enter plant roots through two main pathways:"),
                                html.Ul([
                                    html.Li(html.Strong("Apoplast Pathway:"), " Water moves through cell walls and intercellular spaces without crossing membranes."),
                                    html.Li(html.Strong("Symplast Pathway:"), " Water moves from cell to cell through plasmodesmata, passing through selectively permeable membranes.")
                                ]),
                                html.P(["The ", html.Strong("Casparian strip"), " blocks water in the apoplast from entering the stele, forcing it to pass through endodermal cells into the symplast. "
                                        "Once in the stele, water and minerals are loaded into the xylem and transported as xylem sap."])
                ]), 
                "deep_dive": html.Div([
                                html.P("Water and minerals are absorbed by roots and transported to the stele (vascular cylinder) through two distinct routes:"),
                                html.Ul([
                                    html.Li([
                                        html.Strong("Apoplast (Fast Lane): "),
                                        "Composed of cell walls and intercellular spaces, forming a meshwork for rapid movement of water. "
                                        "Water travels freely until reaching the ",
                                        html.Strong("Casparian strips"),
                                        ", water-repelling barriers made of suberin in endodermal cells. These strips prevent passive flow of substances into the stele, requiring water to enter through the symplast."
                                    ]),
                                    html.Li([
                                        html.Strong("Symplast (Slow Lane): "),
                                        "Water moves through the cytoplasm of cells via ",
                                        html.Strong("plasmodesmata"),
                                        ". Entry into the symplast is regulated by membrane-bound proteins in root hairs, providing selective control over solutes."
                                    ])
                                ]),
                                html.P([
                                    "Once water and minerals reach the ",
                                    html.Strong("stele"),
                                    ", mineral ions are actively transported into the apoplast of the stele, making the water potential more negative. "
                                    "Water then follows via osmosis, accumulating as ",
                                    html.Strong("xylem sap"),
                                    "."
                                ]),
                                html.P([
                                    html.Strong("Xylem vessels"),
                                    " are non-living tubes composed of lignified cell walls. They serve as hollow conduits for upward water transport, forming long, continuous straws."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter35question2.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What are the two main pathways for water movement through plant roots?",
                        "options": ["Xylem and Phloem", "Apoplast and Symplast", "Casparian and Endodermal", "Lignin and Suberin", "Plasmodesmata and Guard Cells"],
                        "answer": "Apoplast and Symplast"
                    },
                    {
                        "question": "Which pathway allows water to move through cell walls and spaces between cells?",
                        "options": ["Symplast", "Endodermis", "Apoplast", "Casparian", "Vascular"],
                        "answer": "Apoplast"
                    },
                    {
                        "question": "What is the Casparian strip made of?",
                        "options": ["Cellulose", "Pectin", "Lignin", "Suberin", "Protein"],
                        "answer": "Suberin"
                    },
                    {
                        "question": "What is the role of the Casparian strip?",
                        "options": [
                            "To speed up water movement through the apoplast",
                            "To allow water to freely enter the stele",
                            "To block passive water flow through the apoplast into the stele",
                            "To regulate xylem sap pressure",
                            "To facilitate plasmodesmata formation"
                        ],
                        "answer": "To block passive water flow through the apoplast into the stele"
                    },
                    {
                        "question": "Water moves through the symplast pathway using which structures?",
                        "options": ["Stomata", "Trichomes", "Plasmodesmata", "Guard cells", "Casparian strips"],
                        "answer": "Plasmodesmata"
                    },
                    {
                        "question": "Which pathway is faster for water movement?",
                        "options": ["Symplast", "Xylem", "Phloem", "Apoplast", "Cambium"],
                        "answer": "Apoplast"
                    },
                    {
                        "question": "What must water do when it reaches the Casparian strip in the apoplast?",
                        "options": [
                            "Continue through the apoplast",
                            "Turn into xylem sap immediately",
                            "Pass through an aquaporin channel",
                            "Enter the symplast via endodermal cells",
                            "Bind to hemicellulose"
                        ],
                        "answer": "Enter the symplast via endodermal cells"
                    },
                    {
                        "question": "Which type of transport is used by mineral ions to enter the stele?",
                        "options": ["Passive transport", "Facilitated diffusion", "Active transport", "Osmosis", "Phagocytosis"],
                        "answer": "Active transport"
                    },
                    {
                        "question": "The buildup of mineral ions in the stele makes the water potential:",
                        "options": ["More positive", "Neutral", "Equal to root hairs", "More negative", "Dependent on sunlight"],
                        "answer": "More negative"
                    },
                    {
                        "question": "What causes water to move into the xylem from surrounding tissues?",
                        "options": [
                            "Light absorption",
                            "Active transport of water",
                            "More positive water potential in xylem",
                            "More negative water potential in stele",
                            "Casparian strip pressure"
                        ],
                        "answer": "More negative water potential in stele"
                    },
                    {
                        "question": "Xylem vessels are composed of:",
                        "options": ["Living cytoplasm", "Bundles of collagen", "Dead cells with lignified walls", "Turgid vacuoles", "Root hairs"],
                        "answer": "Dead cells with lignified walls"
                    },
                    {
                        "question": "What forms the continuous tubular pathway for water to move up the plant?",
                        "options": ["Phloem cells", "Plasmodesmata", "Xylem vessels", "Guard cells", "Apoplast meshwork"],
                        "answer": "Xylem vessels"
                    },
                    {
                        "question": "What is the main difference between the apoplast and symplast pathways?",
                        "options": [
                            "Symplast uses passive transport while apoplast uses active transport",
                            "Apoplast moves water between cells while symplast moves through cells",
                            "Symplast is impermeable to water",
                            "Apoplast occurs only in leaves",
                            "There is no difference"
                        ],
                        "answer": "Apoplast moves water between cells while symplast moves through cells"
                    },
                    {
                        "question": "Where are Casparian strips located?",
                        "options": ["Root hairs", "Stele", "Endodermis", "Xylem", "Cortex"],
                        "answer": "Endodermis"
                    },
                    {
                        "question": "Which pathway involves selective uptake due to plasma membranes?",
                        "options": ["Apoplast", "Phloem", "Xylem", "Symplast", "Stomatal"],
                        "answer": "Symplast"
                    },
                    {
                        "question": "The water-repelling chemical in Casparian strips is:",
                        "options": ["Cellulose", "Lignin", "Suberin", "Chitin", "Starch"],
                        "answer": "Suberin"
                    },
                    {
                        "question": "Which pathway allows unregulated, rapid movement of water until blocked?",
                        "options": ["Symplast", "Phloem", "Apoplast", "Cambium", "Xylem"],
                        "answer": "Apoplast"
                    },
                    {
                        "question": "How does xylem sap form?",
                        "options": [
                            "Photosynthesis in root hairs",
                            "Osmotic movement of water into xylem after minerals enter stele",
                            "Filtration through guard cells",
                            "Starch breakdown in cortex",
                            "Exocytosis of water through phloem"
                        ],
                        "answer": "Osmotic movement of water into xylem after minerals enter stele"
                    },
                    {
                        "question": "What prevents harmful substances from entering the stele via the apoplast?",
                        "options": ["Endodermal cell walls", "Lignin rings", "Casparian strips", "Root hairs", "Plasmodesmata"],
                        "answer": "Casparian strips"
                    },
                    {
                        "question": "Which structure must water pass through to enter the xylem from the apoplast?",
                        "options": ["Trichomes", "Plasma membrane of endodermal cells", "Stomata", "Cuticle", "Phloem companion cells"],
                        "answer": "Plasma membrane of endodermal cells"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Water and minerals enter plant roots through two main pathways:"),
                                html.Ul([
                                    html.Li(html.Strong("Apoplast Pathway:"), " Water moves through cell walls and intercellular spaces without crossing membranes."),
                                    html.Li(html.Strong("Symplast Pathway:"), " Water moves from cell to cell through plasmodesmata, passing through selectively permeable membranes.")
                                ]),
                                html.P(["The ", html.Strong("Casparian strip"), " blocks water in the apoplast from entering the stele, forcing it to pass through endodermal cells into the symplast. "
                                        "Once in the stele, water and minerals are loaded into the xylem and transported as xylem sap."])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    "Water gets into plant roots in two main ways. First, it can go around cells through the spaces in the cell walls—this is the ",
                                    html.Strong("apoplast"),
                                    " route. Second, it can go through the cells themselves using small bridges called ",
                                    html.Strong("plasmodesmata"),
                                    "—this is the ",
                                    html.Strong("symplast"),
                                    " route. The apoplast route is blocked by the ",
                                    html.Strong("Casparian strip"),
                                    ", so water must enter the cells to keep going. Once it gets to the center of the root, water and minerals get pushed into the ",
                                    html.Strong("xylem"),
                                    ", which are like hollow tubes that send water up the plant."
                                ])
                ])]
            },
            "q23": {
                "question": html.P("Know the details of how the transpiration-cohesion-tension mechanism promotes water transport in the xylem of plants."),
                "overview": html.Div([
                                html.P("The transpiration-cohesion-tension mechanism explains how water moves up through the plant xylem without any energy input. "
                                    "Key points include:"),
                                html.Ul([
                                    html.Li("Water evaporates from the leaves through tiny openings called stomata in a process called transpiration."),
                                    html.Li("This evaporation creates negative pressure (tension) in the leaf's air spaces."),
                                    html.Li("Tension pulls water from the leaf veins, then up through the xylem vessels in the stem and roots."),
                                    html.Li("Water molecules stick together due to hydrogen bonding, known as cohesion, forming a continuous water column."),
                                    html.Li("Water moves along a gradient of water potential—from the soil (higher potential) to the dry air (lower potential).")
                                ]),
                                html.P("This passive mechanism allows plants to efficiently transport water and dissolved minerals from roots to leaves.")
                ]), 
                "deep_dive": html.Div([
                                html.P("Water transport in the xylem occurs via the transpiration-cohesion-tension mechanism, a passive process driven by water loss from leaves."),
                                html.Ul([
                                    html.Li([html.Strong("Transpiration:"), " Water vapor diffuses from the leaf to the atmosphere through the stomata. This creates a negative pressure potential in the leaf."]),
                                    html.Li("Water evaporates from the cell walls of mesophyll cells into the intercellular space."),
                                    html.Li("This evaporation creates a shrinking film of water on the cells, generating surface tension that draws more water into the wall from the xylem."),
                                    html.Li("Water moves from the veins to the mesophyll cells, creating a pull (tension) on the entire water column in the xylem."),
                                    html.Li([html.Strong("Cohesion:"), " Hydrogen bonds between water molecules allow them to stick together, maintaining a continuous water column."]),
                                    html.Li("The narrower the xylem tube, the greater the tension the water column can withstand."),
                                    html.Li(["Water moves by ", html.Strong("bulk flow"), " from regions of higher to lower water potential."]),
                                    html.Li([html.Strong("Water potential gradient:"), " Water potential is most negative in the dry air and least negative in the soil, pulling water upward."]),
                                    html.Li(["As water rises, it carries ", html.Strong("dissolved minerals"), " with it in the xylem sap."])
                                ]),
                                html.P("This entire process does not require direct energy input from the plant.")
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter35question3.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What drives the upward movement of water in the transpiration-cohesion-tension mechanism?",
                        "options": ["Root pressure", "Active transport", "Negative pressure from transpiration", "Gravity"],
                        "answer": "Negative pressure from transpiration"
                    },
                    {
                        "question": "Where does transpiration primarily occur in a plant?",
                        "options": ["Roots", "Stem", "Stomata on leaves", "Xylem vessels"],
                        "answer": "Stomata on leaves"
                    },
                    {
                        "question": "What role does cohesion play in water transport through the xylem?",
                        "options": [
                            "Breaks water molecules apart",
                            "Helps water molecules stick together",
                            "Repels water molecules",
                            "Produces energy for water movement"
                        ],
                        "answer": "Helps water molecules stick together"
                    },
                    {
                        "question": "What creates the negative pressure (tension) that pulls water up through the xylem?",
                        "options": [
                            "Evaporation of water from leaf surfaces",
                            "Root absorption of water",
                            "Wind blowing on leaves",
                            "Gravity"
                        ],
                        "answer": "Evaporation of water from leaf surfaces"
                    },
                    {
                        "question": "In the transpiration-cohesion-tension mechanism, water moves from areas of ____ water potential to ____ water potential.",
                        "options": [
                            "Lower to higher",
                            "Higher to lower",
                            "Equal to equal",
                            "No change in"
                        ],
                        "answer": "Higher to lower"
                    },
                    {
                        "question": "What are the tiny pores on leaves through which water vapor exits?",
                        "options": ["Lenticels", "Stomata", "Hydathodes", "Trichomes"],
                        "answer": "Stomata"
                    },
                    {
                        "question": "Which of the following best describes the role of the xylem in plants?",
                        "options": [
                            "Transport of sugars",
                            "Transport of water and minerals",
                            "Production of food",
                            "Storage of nutrients"
                        ],
                        "answer": "Transport of water and minerals"
                    },
                    {
                        "question": "What prevents the water column in xylem from breaking under tension?",
                        "options": [
                            "Adhesion of water to vessel walls",
                            "Hydrogen bonding (cohesion) between water molecules",
                            "Active pumping by cells",
                            "Root pressure"
                        ],
                        "answer": "Hydrogen bonding (cohesion) between water molecules"
                    },
                    {
                        "question": "Why does water evaporate from the mesophyll cells in the leaf?",
                        "options": [
                            "Because the air outside has lower water vapor concentration",
                            "Because the soil has more water",
                            "Because xylem pushes it out",
                            "Due to root pressure"
                        ],
                        "answer": "Because the air outside has lower water vapor concentration"
                    },
                    {
                        "question": "Which component of water potential is most negative in dry air?",
                        "options": ["Solute potential", "Pressure potential", "Water potential", "Osmotic potential"],
                        "answer": "Water potential"
                    },
                    {
                        "question": "Which factor does NOT directly contribute to the transpiration-cohesion-tension mechanism?",
                        "options": [
                            "Hydrogen bonding",
                            "Transpiration from stomata",
                            "Active transport of water",
                            "Water potential gradient"
                        ],
                        "answer": "Active transport of water"
                    },
                    {
                        "question": "What property of water allows it to move in a continuous column up the xylem?",
                        "options": [
                            "High surface tension",
                            "Low density",
                            "Cohesion due to hydrogen bonding",
                            "Hydrophobicity"
                        ],
                        "answer": "Cohesion due to hydrogen bonding"
                    },
                    {
                        "question": "What happens to the water film on mesophyll cell walls during transpiration?",
                        "options": [
                            "It expands and increases pressure",
                            "It shrinks, increasing surface tension and negative pressure",
                            "It becomes saturated with solutes",
                            "It solidifies"
                        ],
                        "answer": "It shrinks, increasing surface tension and negative pressure"
                    },
                    {
                        "question": "Which of the following best describes how minerals move during transpiration?",
                        "options": [
                            "They actively move against the flow",
                            "They dissolve in xylem sap and move passively with water",
                            "They move through the phloem",
                            "They do not move during transpiration"
                        ],
                        "answer": "They dissolve in xylem sap and move passively with water"
                    },
                    {
                        "question": "How does the diameter of xylem vessels affect the transpiration-cohesion-tension mechanism?",
                        "options": [
                            "Narrower tubes can withstand greater tension without breaking the water column",
                            "Wider tubes allow for faster flow but less tension resistance",
                            "Diameter has no effect",
                            "Wider tubes increase water potential"
                        ],
                        "answer": "Narrower tubes can withstand greater tension without breaking the water column"
                    },
                    {
                        "question": "Which part of the plant has the least negative water potential during transpiration?",
                        "options": [
                            "Soil",
                            "Leaf air spaces",
                            "Atmosphere",
                            "Xylem"
                        ],
                        "answer": "Soil"
                    },
                    {
                        "question": "What is the role of stomata in the transpiration-cohesion-tension mechanism?",
                        "options": [
                            "To pump water actively into the leaf",
                            "To allow water vapor to exit, driving transpiration",
                            "To prevent water loss",
                            "To absorb minerals"
                        ],
                        "answer": "To allow water vapor to exit, driving transpiration"
                    },
                    {
                        "question": "Why does the transpiration-cohesion-tension mechanism not require energy input from the plant?",
                        "options": [
                            "Because it relies on passive physical forces like evaporation and cohesion",
                            "Because ATP is generated in the roots",
                            "Because water is actively pumped upwards",
                            "Because stomata close during the process"
                        ],
                        "answer": "Because it relies on passive physical forces like evaporation and cohesion"
                    },
                    {
                        "question": "What happens to the tension created by water loss in the leaf mesophyll cells?",
                        "options": [
                            "It draws water from nearby veins into the mesophyll",
                            "It pushes water out of the roots",
                            "It breaks the water column",
                            "It causes active transport of ions"
                        ],
                        "answer": "It draws water from nearby veins into the mesophyll"
                    },
                    {
                        "question": "Which of these is NOT part of the transpiration-cohesion-tension mechanism?",
                        "options": [
                            "Transpiration through stomata",
                            "Cohesion between water molecules",
                            "Active pumping by xylem cells",
                            "Tension created by evaporation"
                        ],
                        "answer": "Active pumping by xylem cells"
                    }
                ],
                "blurting": [html.Div([
                                html.P("The transpiration-cohesion-tension mechanism explains how water moves up through the plant xylem without any energy input. "
                                    "Key points include:"),
                                html.Ul([
                                    html.Li("Water evaporates from the leaves through tiny openings called stomata in a process called transpiration."),
                                    html.Li("This evaporation creates negative pressure (tension) in the leaf's air spaces."),
                                    html.Li("Tension pulls water from the leaf veins, then up through the xylem vessels in the stem and roots."),
                                    html.Li("Water molecules stick together due to hydrogen bonding, known as cohesion, forming a continuous water column."),
                                    html.Li("Water moves along a gradient of water potential—from the soil (higher potential) to the dry air (lower potential).")
                                ]),
                                html.P("This passive mechanism allows plants to efficiently transport water and dissolved minerals from roots to leaves.")
                ])],
                "feynman": [html.Div([
                                html.P("Plants don’t need to push water up — they pull it. When water evaporates from the leaves, it pulls on the water below, like a straw. Water sticks together because of cohesion, so as one molecule leaves, it tugs the whole chain up. This all happens passively — the plant doesn't spend energy.")
                ])]
            },
            "q24": {
                "question": html.P("Be able to describe the mechanisms by which blue light, K+, and the proton pump contribute to stomata opening and CO2 uptake."),
                "overview": html.Div([
                                html.P("Stomatal opening and CO2 uptake are controlled by changes in guard cell turgor pressure driven by potassium ion (K+) movement."),
                                html.P("Blue light activates proton pumps in guard cells, creating an electrochemical gradient that allows K+ to enter."),
                                html.P("Water follows by osmosis, increasing turgor pressure and opening the stomata for gas exchange."),
                                html.P("Stomata close when blue light is absent, K+ diffuses out, or the plant experiences water stress, often signaled by abscisic acid.")
                ]), 
                "deep_dive": html.Div([
                                html.P("The leaf and stem epidermis are covered by a waxy cuticle that reduces water loss but also blocks gas exchange. To facilitate gas exchange, plants have pores called stomata, formed by pairs of guard cells."),
                                html.P("The opening and closing of stomata regulate CO2 entry and water loss."),
                                html.P("Key points:"),
                                html.Ul([
                                    html.Li([html.Strong("Turgor pressure in guard cells"), ": Controls stomatal aperture by changing guard cell shape."]),
                                    html.Li([html.Strong("Role of Blue Light"), ": Blue light is absorbed by pigments in guard cells and activates proton pumps (H+-ATPases)."]),
                                    html.Li([html.Strong("Proton Pump Activity"), ": Pumps H+ ions out of guard cells, creating an electrochemical gradient."]),
                                    html.Li([html.Strong("Potassium Ion (K+) Uptake"), ": K+ ions enter guard cells passively driven by the proton pump-generated gradient."]),
                                    html.Li([html.Strong("Water Movement"), ": Water follows K+ into guard cells by osmosis, lowering water potential inside."]),
                                    html.Li([html.Strong("Increase in Turgor Pressure"), ": Causes guard cells to swell and open the stomatal pore."]),
                                    html.Li([html.Strong("Stomatal Closing"), ": Occurs when blue light is absent, proton pumps slow, K+ ions exit, water leaves, and guard cells become flaccid."]),
                                    html.Li([html.Strong("Stress Response"),": Under drought or water stress, plants produce abscisic acid which signals stomata to close."]),
                                    html.Li([html.Strong("CO2 Levels"), ": High internal CO2 concentrations can also trigger stomatal closing."]),
                                    html.Li([html.Strong("Plant Adaptations"), ": Plants can reduce water loss by controlling stomatal density and shedding leaves during stress."])
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter35question4.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What role does blue light play in stomatal opening?",
                        "options": [
                            "It directly opens the stomata by changing guard cell shape",
                            "It activates proton pumps in guard cells",
                            "It causes potassium ions to exit the guard cells",
                            "It blocks water from entering guard cells",
                            "It triggers abscisic acid production"
                        ],
                        "answer": "It activates proton pumps in guard cells"
                    },
                    {
                        "question": "Which ion's movement into guard cells primarily drives the increase in turgor pressure during stomatal opening?",
                        "options": [
                            "Calcium (Ca2+)",
                            "Chloride (Cl-)",
                            "Potassium (K+)",
                            "Sodium (Na+)",
                            "Magnesium (Mg2+)"
                        ],
                        "answer": "Potassium (K+)"
                    },
                    {
                        "question": "How does the proton pump contribute to stomatal opening?",
                        "options": [
                            "By pumping protons into guard cells",
                            "By pumping protons out of guard cells",
                            "By pumping potassium ions into guard cells",
                            "By pumping water into guard cells",
                            "By releasing abscisic acid"
                        ],
                        "answer": "By pumping protons out of guard cells"
                    },
                    {
                        "question": "What causes water to enter guard cells during stomatal opening?",
                        "options": [
                            "Active pumping of water molecules",
                            "Osmosis due to lowered water potential inside guard cells",
                            "Pressure from surrounding cells",
                            "Direct diffusion of water vapor",
                            "Photosynthesis producing water"
                        ],
                        "answer": "Osmosis due to lowered water potential inside guard cells"
                    },
                    {
                        "question": "Why do stomata close when blue light is absent?",
                        "options": [
                            "The proton pump activity slows down",
                            "Potassium ions enter guard cells",
                            "Water potential inside guard cells becomes more negative",
                            "Guard cells increase in size",
                            "Abscisic acid concentration decreases"
                        ],
                        "answer": "The proton pump activity slows down"
                    },
                    {
                        "question": "What hormone signals stomatal closure under drought conditions?",
                        "options": [
                            "Auxin",
                            "Gibberellin",
                            "Abscisic acid",
                            "Cytokinin",
                            "Ethylene"
                        ],
                        "answer": "Abscisic acid"
                    },
                    {
                        "question": "Which structure in leaves regulates gas exchange and water loss?",
                        "options": [
                            "Cuticle",
                            "Stomata",
                            "Phloem",
                            "Xylem",
                            "Mesophyll cells"
                        ],
                        "answer": "Stomata"
                    },
                    {
                        "question": "What causes guard cells to change shape and open the stomata?",
                        "options": [
                            "Loss of water",
                            "Increase in turgor pressure",
                            "Decreased potassium levels",
                            "Decrease in proton pump activity",
                            "Abscisic acid binding"
                        ],
                        "answer": "Increase in turgor pressure"
                    },
                    {
                        "question": "How do potassium ions enter the guard cells?",
                        "options": [
                            "Active transport using ATP directly",
                            "Passive diffusion through open pores",
                            "Driven by electrochemical gradient created by proton pumps",
                            "Transport via water flow",
                            "Endocytosis"
                        ],
                        "answer": "Driven by electrochemical gradient created by proton pumps"
                    },
                    {
                        "question": "Which of the following is NOT a function of guard cells?",
                        "options": [
                            "Controlling stomatal aperture",
                            "Regulating CO2 uptake",
                            "Regulating water loss",
                            "Producing abscisic acid",
                            "Responding to light signals"
                        ],
                        "answer": "Producing abscisic acid"
                    },
                    {
                        "question": "What effect does abscisic acid have on stomata?",
                        "options": [
                            "It opens stomata",
                            "It closes stomata",
                            "It increases potassium uptake",
                            "It activates proton pumps",
                            "It increases water absorption"
                        ],
                        "answer": "It closes stomata"
                    },
                    {
                        "question": "How does high CO2 concentration inside the leaf affect stomata?",
                        "options": [
                            "It causes stomata to open wider",
                            "It causes stomata to close",
                            "It has no effect",
                            "It increases potassium influx",
                            "It stimulates proton pumps"
                        ],
                        "answer": "It causes stomata to close"
                    },
                    {
                        "question": "What is the primary purpose of stomatal opening?",
                        "options": [
                            "To release oxygen",
                            "To allow CO2 to enter for photosynthesis",
                            "To absorb water from the atmosphere",
                            "To transport sugars",
                            "To fix nitrogen"
                        ],
                        "answer": "To allow CO2 to enter for photosynthesis"
                    },
                    {
                        "question": "Which factor does NOT influence stomatal opening?",
                        "options": [
                            "Blue light presence",
                            "Potassium ion concentration in guard cells",
                            "Abscisic acid levels",
                            "Temperature above 50°C",
                            "Water availability"
                        ],
                        "answer": "Temperature above 50°C"
                    },
                    {
                        "question": "What happens to guard cells when they lose potassium ions?",
                        "options": [
                            "They swell and open stomata",
                            "They become flaccid and close stomata",
                            "They increase proton pump activity",
                            "They produce more abscisic acid",
                            "They initiate photosynthesis"
                        ],
                        "answer": "They become flaccid and close stomata"
                    },
                    {
                        "question": "Which statement about the guard cell proton pump is TRUE?",
                        "options": [
                            "It pumps potassium into the cell",
                            "It uses ATP to pump protons out of the cell",
                            "It directly transports water molecules",
                            "It closes the stomatal pore",
                            "It produces abscisic acid"
                        ],
                        "answer": "It uses ATP to pump protons out of the cell"
                    },
                    {
                        "question": "Which of these is a direct effect of proton pumping in guard cells?",
                        "options": [
                            "Increased water potential inside the cell",
                            "Decreased potassium uptake",
                            "Hyperpolarization of the membrane",
                            "Stomatal closure",
                            "Release of abscisic acid"
                        ],
                        "answer": "Hyperpolarization of the membrane"
                    },
                    {
                        "question": "How does abscisic acid affect K+ channels in guard cells?",
                        "options": [
                            "Opens channels to allow K+ influx",
                            "Closes channels to prevent K+ influx",
                            "Increases proton pump activity",
                            "Decreases water potential inside guard cells",
                            "Triggers stomatal opening"
                        ],
                        "answer": "Closes channels to prevent K+ influx"
                    },
                    {
                        "question": "What is the effect of water stress on stomata?",
                        "options": [
                            "Stomata open wider to increase CO2 intake",
                            "Stomata close to conserve water",
                            "Stomata become larger in size",
                            "Guard cells increase potassium uptake",
                            "Proton pump activity increases"
                        ],
                        "answer": "Stomata close to conserve water"
                    },
                    {
                        "question": "Which ion movement causes guard cells to lose turgor pressure?",
                        "options": [
                            "Influx of sodium ions",
                            "Efflux of potassium ions",
                            "Influx of calcium ions",
                            "Efflux of chloride ions",
                            "Influx of magnesium ions"
                        ],
                        "answer": "Efflux of potassium ions"
                    }
                ],
                "blurting": [html.Div([
                                html.P("Stomatal opening and CO2 uptake are controlled by changes in guard cell turgor pressure driven by potassium ion (K+) movement."),
                                html.P("Blue light activates proton pumps in guard cells, creating an electrochemical gradient that allows K+ to enter."),
                                html.P("Water follows by osmosis, increasing turgor pressure and opening the stomata for gas exchange."),
                                html.P("Stomata close when blue light is absent, K+ diffuses out, or the plant experiences water stress, often signaled by abscisic acid.")
                ])],
                "feynman": [html.Div([
                                html.P([
                                    "Stomata are tiny holes in leaves that let air in and out. Guard cells around these holes act like gates.",
                                    "When blue light shines, it turns on pumps in guard cells that push out tiny charged particles (protons).",
                                    "This makes the cells suck in potassium ions, and water follows, making the cells swell up and open the gate.",
                                    "If there’s no blue light or if the plant is thirsty, the potassium leaves, water follows, and the guard cells shrink to close the gate.",
                                    "This way, plants can take in CO2 for food while saving water."
                                ])
                ])]
            },
            "q25": {
                "question": html.P("Understand the concepts of loading and unloading and how they relate to substance transport in the phloem."),
                "overview": html.Div([
                                html.P([
                                    html.Strong("Translocation in Plants:"),
                                    " Translocation in plants is the movement of carbohydrates through the phloem from sources (like leaves) to sinks (growth or storage sites).",
                                    " This process depends on energy and involves two key steps: loading (active transport of solutes into sieve tubes) and unloading (removal of solutes at sinks).",
                                    " Water follows solutes osmotically, creating pressure that drives bulk flow of phloem sap."
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Translocation in Plants:"),
                                    " Translocation transports sugars primarily sucrose, from sources that produce more sugar than needed (e.g., leaves or storage organs) to sinks that consume or store sugars (e.g., roots, fruits, seeds).",
                                    " The phloem is composed of sieve tube elements connected end-to-end by sieve plates, which have enlarged plasmodesmata allowing sap flow. Companion cells support sieve tubes metabolically and are connected by plasmodesmata.",
                                ]),
                                html.Ul([
                                    html.Li([html.Strong("Loading:"), " Solutes are actively transported into sieve tubes at source regions, increasing solute concentration inside. This causes water to enter by osmosis, increasing pressure potential and pushing the sap towards sinks."]),
                                    html.Li([html.Strong("Unloading:"), " At sink regions, solutes are removed actively or passively from sieve tubes into surrounding cells, causing water to leave and return to the xylem. This maintains the pressure gradient for flow."])
                                ]),
                                html.P([
                                    "Solutes can move into sieve elements via both symplastic (through cells) and apoplastic (between cells) pathways, requiring specific transport mechanisms.",
                                    " Loading involves secondary active transport of sucrose using a proton gradient generated by proton pumps to bring sucrose into companion cells and sieve tubes.",
                                    " Unobstructed sieve plates allow rapid bulk flow of phloem sap, carrying sugars and nutrients efficiently.",
                                    " Translocation stops if phloem cells are damaged or if ATP supply is inhibited."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/chapter35question5.png",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the main function of translocation in plants?",
                        "options": [
                            "Transport of water through xylem",
                            "Movement of carbohydrates through phloem from sources to sinks",
                            "Transport of minerals through phloem",
                            "Movement of proteins through roots"
                        ],
                        "answer": "Movement of carbohydrates through phloem from sources to sinks"
                    },
                    {
                        "question": "What are the two energy-requiring steps in phloem translocation?",
                        "options": [
                            "Water uptake and evaporation",
                            "Loading of solutes into sieve tubes and unloading at sinks",
                            "Cell division and differentiation",
                            "Transpiration and photosynthesis"
                        ],
                        "answer": "Loading of solutes into sieve tubes and unloading at sinks"
                    },
                    {
                        "question": "What structure connects sieve tube elements and allows flow of phloem sap?",
                        "options": [
                            "Casparian strip",
                            "Sieve plates",
                            "Xylem vessels",
                            "Plasmodesmata"
                        ],
                        "answer": "Sieve plates"
                    },
                    {
                        "question": "What is the role of companion cells in the phloem?",
                        "options": [
                            "Transport water in xylem",
                            "Provide metabolic support to sieve tube elements",
                            "Form the cell wall",
                            "Store starch"
                        ],
                        "answer": "Provide metabolic support to sieve tube elements"
                    },
                    {
                        "question": "What causes water to enter sieve tubes during loading?",
                        "options": [
                            "Increase in temperature",
                            "Increase in solute concentration inside sieve tubes",
                            "Decrease in atmospheric pressure",
                            "Decrease in soil moisture"
                        ],
                        "answer": "Increase in solute concentration inside sieve tubes"
                    },
                    {
                        "question": "How is the pressure potential created in the phloem?",
                        "options": [
                            "By active pumping of water",
                            "By osmosis of water following solutes into sieve tubes",
                            "By root pressure alone",
                            "By evaporation at leaves"
                        ],
                        "answer": "By osmosis of water following solutes into sieve tubes"
                    },
                    {
                        "question": "What happens to solutes during unloading in the phloem?",
                        "options": [
                            "They are transported actively or passively out of sieve tubes into surrounding tissues",
                            "They accumulate in the phloem permanently",
                            "They evaporate",
                            "They are converted into water"
                        ],
                        "answer": "They are transported actively or passively out of sieve tubes into surrounding tissues"
                    },
                    {
                        "question": "What maintains the pressure gradient required for bulk flow in the phloem?",
                        "options": [
                            "Continuous loading and unloading of solutes",
                            "Temperature changes",
                            "Soil moisture variations",
                            "Light intensity fluctuations"
                        ],
                        "answer": "Continuous loading and unloading of solutes"
                    },
                    {
                        "question": "Which pathway involves movement of solutes between cells (through cell cytoplasm) to reach sieve elements?",
                        "options": [
                            "Apoplastic pathway",
                            "Symplastic pathway",
                            "Transpiration stream",
                            "Casparian strip"
                        ],
                        "answer": "Symplastic pathway"
                    },
                    {
                        "question": "What powers the secondary active transport of sucrose into companion cells?",
                        "options": [
                            "ATP directly hydrolyzed by sucrose transporter",
                            "Proton gradient established by proton pumps",
                            "Passive diffusion",
                            "Water pressure"
                        ],
                        "answer": "Proton gradient established by proton pumps"
                    },
                    {
                        "question": "What would happen if the phloem were damaged or respiration inhibited?",
                        "options": [
                            "Translocation would stop",
                            "Xylem would increase transport",
                            "Photosynthesis would speed up",
                            "Water uptake would increase"
                        ],
                        "answer": "Translocation would stop"
                    },
                    {
                        "question": "Which cells have enlarged plasmodesmata forming sieve plates?",
                        "options": [
                            "Companion cells",
                            "Sieve tube elements",
                            "Parenchyma cells",
                            "Xylem vessels"
                        ],
                        "answer": "Sieve tube elements"
                    },
                    {
                        "question": "What types of molecules are primarily transported by phloem sap?",
                        "options": [
                            "Sugars and carbohydrates",
                            "Minerals and water",
                            "Proteins and lipids",
                            "Hormones only"
                        ],
                        "answer": "Sugars and carbohydrates"
                    },
                    {
                        "question": "What is the function of plasmodesmata in phloem transport?",
                        "options": [
                            "Block movement of molecules",
                            "Connect companion cells and sieve tube elements for molecule exchange",
                            "Store nutrients",
                            "Pump water"
                        ],
                        "answer": "Connect companion cells and sieve tube elements for molecule exchange"
                    },
                    {
                        "question": "Why must sieve plates be unobstructed?",
                        "options": [
                            "To allow bulk flow of phloem sap",
                            "To prevent water loss",
                            "To strengthen the cell wall",
                            "To trap pathogens"
                        ],
                        "answer": "To allow bulk flow of phloem sap"
                    },
                    {
                        "question": "What role does osmosis play in phloem loading?",
                        "options": [
                            "Water moves into sieve tubes following solutes increasing pressure",
                            "Water evaporates from the phloem",
                            "Water is actively pumped into leaves",
                            "Water is removed from sieve tubes"
                        ],
                        "answer": "Water moves into sieve tubes following solutes increasing pressure"
                    },
                    {
                        "question": "What is a 'source' in plant translocation?",
                        "options": [
                            "A site where sugars are produced or stored",
                            "A site where sugars are consumed",
                            "The root tip",
                            "The xylem"
                        ],
                        "answer": "A site where sugars are produced or stored"
                    },
                    {
                        "question": "What is a 'sink' in plant translocation?",
                        "options": [
                            "A site where sugars are used or stored",
                            "A site where sugars are produced",
                            "The leaf epidermis",
                            "The phloem companion cells"
                        ],
                        "answer": "A site where sugars are used or stored"
                    },
                    {
                        "question": "How is the sucrose concentration in the apoplast maintained during loading?",
                        "options": [
                            "By active transport and proton pumps",
                            "By diffusion alone",
                            "By transpiration",
                            "By xylem pressure"
                        ],
                        "answer": "By active transport and proton pumps"
                    },
                    {
                        "question": "Which statement about companion cells is correct?",
                        "options": [
                            "They retain organelles and support sieve tube elements",
                            "They are dead at maturity",
                            "They transport water through xylem",
                            "They block plasmodesmata"
                        ],
                        "answer": "They retain organelles and support sieve tube elements"
                    }
                ],
                "blurting": [html.Div([
                                html.P([
                                    html.Strong("Translocation in Plants:"),
                                    " Translocation in plants is the movement of carbohydrates through the phloem from sources (like leaves) to sinks (growth or storage sites).",
                                    " This process depends on energy and involves two key steps: loading (active transport of solutes into sieve tubes) and unloading (removal of solutes at sinks).",
                                    " Water follows solutes osmotically, creating pressure that drives bulk flow of phloem sap."
                                ])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    html.Strong("Translocation in Plants:"),
                                    " Plants move sugars from places that make lots of sugar (like leaves) to places that need or store it (like fruits or roots).",
                                    " They do this by loading sugar into special tubes called phloem. This makes water rush in, pushing the sugar-water mix to where it’s needed.",
                                    " At the other end, sugar is taken out and water leaves too, keeping the flow going.",
                                    " This whole process needs energy to move sugar in and out at the right places, but the water movement helps push everything along.",
                                    " If the phloem gets hurt or the plant runs out of energy, the sugar transport stops."
                                ])
                ])]
            },
        }
    }, #end of Study Guide #2 material 

    "sg3": {
        "questions": {
            "q1": {
                "question": html.P("Be familiar with the processes of spermatogenesis and oogenesis.  Know what the beginning components are as compared to the endpoints."),
                "overview": html.Div([
                        html.P([
                            html.Strong("Spermatogenesis and Oogenesis:"),
                            " These are the processes by which male and female gametes are formed through meiosis.",
                            " Spermatogenesis begins with diploid spermatogonia and produces four haploid sperm.",
                            " Oogenesis begins with diploid oogonia and results in one haploid ovum and two or three non-functional polar bodies.",
                            " The key difference from mitosis is that meiosis reduces chromosome number by half, creating genetically unique haploid cells."
                            ])
                        ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Spermatogenesis:"),
                                    " Occurs in the testes and starts with a diploid spermatogonium (2n), which undergoes mitosis to form a primary spermatocyte.",
                                    " The primary spermatocyte completes meiosis I to form two haploid secondary spermatocytes, which then undergo meiosis II to form four haploid spermatids.",
                                    " These spermatids differentiate into mature spermatozoa, each carrying one set of chromosomes and contributing centrioles during fertilization."
                                ]),
                                html.P([
                                    html.Strong("Oogenesis:"),
                                    " Occurs in the ovaries and begins before birth with oogonia (2n) undergoing mitosis to form primary oocytes.",
                                    " Primary oocytes begin meiosis I but pause in prophase I until puberty.",
                                    " Upon ovulation, meiosis I completes to form a secondary oocyte and a polar body.",
                                    " The secondary oocyte pauses in meiosis II and only completes division if fertilized, producing one ovum and another polar body.",
                                    " The ovum contributes DNA, cytoplasm, and organelles (but not centrioles) to the embryo."
                                ]),
                                html.P([
                                    html.Strong("Comparison to Mitosis:"),
                                    " Mitosis maintains diploid chromosome number and produces identical cells, whereas meiosis produces haploid cells with genetic variation.",
                                    " This reduction in chromosome number is critical for maintaining genetic stability across generations."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the starting cell in spermatogenesis?",
                        "options": [
                            "Oogonium",
                            "Spermatogonium",
                            "Primary oocyte",
                            "Spermatid"
                        ],
                        "answer": "Spermatogonium"
                    },
                    {
                        "question": "What is the ploidy of a mature sperm cell?",
                        "options": [
                            "Diploid (2n)",
                            "Tetraploid (4n)",
                            "Haploid (n)",
                            "Triploid (3n)"
                        ],
                        "answer": "Haploid (n)"
                    },
                    {
                        "question": "How many functional sperm are produced from one spermatogonium?",
                        "options": [
                            "1",
                            "2",
                            "3",
                            "4"
                        ],
                        "answer": "4"
                    },
                    {
                        "question": "Which organelle do sperm contribute during fertilization?",
                        "options": [
                            "Mitochondria",
                            "Nucleus",
                            "Centrioles",
                            "Ribosomes"
                        ],
                        "answer": "Centrioles"
                    },
                    {
                        "question": "Where does oogenesis occur?",
                        "options": [
                            "Testes",
                            "Epididymis",
                            "Ovaries",
                            "Uterus"
                        ],
                        "answer": "Ovaries"
                    },
                    {
                        "question": "What is the ploidy of an oogonium?",
                        "options": [
                            "Haploid (n)",
                            "Diploid (2n)",
                            "Triploid (3n)",
                            "Tetraploid (4n)"
                        ],
                        "answer": "Diploid (2n)"
                    },
                    {
                        "question": "What is the final product of oogenesis?",
                        "options": [
                            "Two ovum",
                            "One ovum and two or three polar bodies",
                            "Four identical eggs",
                            "One sperm and one egg"
                        ],
                        "answer": "One ovum and two or three polar bodies"
                    },
                    {
                        "question": "When does meiosis II complete in oogenesis?",
                        "options": [
                            "Before birth",
                            "At ovulation",
                            "After fertilization",
                            "During puberty"
                        ],
                        "answer": "After fertilization"
                    },
                    {
                        "question": "What is a polar body?",
                        "options": [
                            "A mature sperm cell",
                            "A cell that helps the egg develop",
                            "A small cell that forms during oogenesis and usually degenerates",
                            "An organelle in the ovum"
                        ],
                        "answer": "A small cell that forms during oogenesis and usually degenerates"
                    },
                    {
                        "question": "Which process reduces the chromosome number by half?",
                        "options": [
                            "Mitosis",
                            "Meiosis",
                            "Fertilization",
                            "Translation"
                        ],
                        "answer": "Meiosis"
                    },
                    {
                        "question": "Which of the following happens during meiosis but not mitosis?",
                        "options": [
                            "Replication of DNA",
                            "Production of identical cells",
                            "Formation of polar bodies",
                            "Chromosome number remains the same"
                        ],
                        "answer": "Formation of polar bodies"
                    },
                    {
                        "question": "At what stage is the primary oocyte arrested until puberty?",
                        "options": [
                            "Prophase I",
                            "Metaphase I",
                            "Anaphase II",
                            "Telophase II"
                        ],
                        "answer": "Prophase I"
                    },
                    {
                        "question": "What is the function of the ovum’s cytoplasm after fertilization?",
                        "options": [
                            "It is discarded like polar bodies",
                            "It provides nutrients and organelles for the embryo",
                            "It forms sperm centrioles",
                            "It fuses with polar bodies"
                        ],
                        "answer": "It provides nutrients and organelles for the embryo"
                    },
                    {
                        "question": "How many chromosomes are in a human haploid gamete?",
                        "options": [
                            "23",
                            "46",
                            "69",
                            "92"
                        ],
                        "answer": "23"
                    },
                    {
                        "question": "Which of the following is TRUE of sperm production?",
                        "options": [
                            "It begins before birth and pauses until fertilization",
                            "It produces one sperm per division",
                            "It begins at puberty and continues throughout life",
                            "It produces only one mature sperm and three polar bodies"
                        ],
                        "answer": "It begins at puberty and continues throughout life"
                    },
                    {
                        "question": "What structure does the sperm provide that helps organize cell division in the zygote?",
                        "options": [
                            "Mitochondria",
                            "Ribosome",
                            "Centrioles",
                            "Golgi apparatus"
                        ],
                        "answer": "Centrioles"
                    },
                    {
                        "question": "Which gamete contributes more cytoplasm to the zygote?",
                        "options": [
                            "Sperm",
                            "Ovum",
                            "Both equally",
                            "Neither"
                        ],
                        "answer": "Ovum"
                    },
                    {
                        "question": "Which of the following best explains why meiosis is important in sexual reproduction?",
                        "options": [
                            "It creates genetically identical cells",
                            "It ensures chromosome number is doubled",
                            "It halves the chromosome number to maintain genetic stability",
                            "It allows mitosis to occur in gametes"
                        ],
                        "answer": "It halves the chromosome number to maintain genetic stability"
                    },
                    {
                        "question": "What term refers to the production of sperm cells?",
                        "options": [
                            "Oogenesis",
                            "Fertilization",
                            "Spermatogenesis",
                            "Meiosis"
                        ],
                        "answer": "Spermatogenesis"
                    },
                    {
                        "question": "Why are polar bodies formed during oogenesis?",
                        "options": [
                            "To contribute to embryo development",
                            "To ensure equal division of cytoplasm",
                            "To discard excess genetic material while preserving cytoplasm for the ovum",
                            "To produce multiple viable eggs"
                        ],
                        "answer": "To discard excess genetic material while preserving cytoplasm for the ovum"
                    }
                ],
                "blurting": [html.Div([
                        html.P([
                            html.Strong("Spermatogenesis and Oogenesis:"),
                            " These are the processes by which male and female gametes are formed through meiosis.",
                            " Spermatogenesis begins with diploid spermatogonia and produces four haploid sperm.",
                            " Oogenesis begins with diploid oogonia and results in one haploid ovum and two or three non-functional polar bodies.",
                            " The key difference from mitosis is that meiosis reduces chromosome number by half, creating genetically unique haploid cells."
                            ])
                        ])],
                "feynman": [html.Div([
                                html.P([
                                    html.Strong("Feynman Summary:"),
                                    " Making sperm and eggs is like halving a recipe so the embryo doesn’t get double ingredients.",
                                    " Sperm are made all the time and each starting cell makes four tiny, identical haploid cells.",
                                    " Eggs start early, take breaks, and only finish dividing if fertilized—ending with one large haploid cell and a few discarded parts.",
                                    " Meiosis is different from mitosis because it halves the DNA—so the sperm and egg each give just one set of chromosomes to the baby."
                                ])
                ])]
            }, 
            "q2": {
                "question": html.P("Know the major steps involved in fertilization, the union of sperm and egg to produce a zygote.  Be prepared to discuss the details of the acrosome reaction and the process of sperm adhesion and fusion with the egg. What is the role of G actin in these processes?"),
                "overview": html.Div([
                                html.P([
                                    html.Strong("Fertilization Overview:"),
                                    " Fertilization is the union of a haploid sperm and egg to form a diploid zygote.",
                                    " It involves sperm activation, penetration of the egg's outer layers via the acrosomal reaction, adhesion and fusion of gamete membranes, and the prevention of polyspermy.",
                                    " G-actin plays a key role in sperm by polymerizing into f-actin during the acrosomal reaction, enabling sperm-egg contact and fusion."
                                ]),
                                html.P([html.Strong("The Acrosomal Reaction:")]),
                                html.Ul([
                                    html.Li("1. **Sperm Activation:** Sperm reach the egg and undergo changes to become capable of fertilization."),
                                    html.Li("2. **Acrosomal Reaction:** Triggered by contact with egg jelly (in external fertilizers like sea urchins). Calcium influx leads to G-actin polymerization into f-actin."),
                                    html.Li("3. **Extension of Acrosomal Process:** F-actin forms a long protrusion that helps the sperm penetrate the egg’s outer layers."),
                                    html.Li("4. **Enzyme Release:** The acrosome releases digestive enzymes to break through the egg’s extracellular matrix (e.g., vitelline layer or zona pellucida)."),
                                    html.Li("5. **Adhesion and Fusion:** The sperm membrane binds to and fuses with the egg membrane."),
                                    html.Li("6. **Egg Activation:** The egg responds with calcium release and polyspermy prevention mechanisms."),
                                    html.Li("7. **Polyspermy Block:** Fast block (membrane depolarization) and slow block (cortical granule release to modify outer egg layers) prevent additional sperm from fusing."),
                                    html.Li("8. **Formation of the Zygote:** Male and female pronuclei fuse to form a diploid nucleus.")
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Steps of Fertilization:"),
                                    " Fertilization is a multi-step process involving both sperm and egg responses. Key steps include:"
                                ]),
                                html.Ul([
                                    html.Li("1. **Sperm Activation:** Sperm reach the egg and undergo changes to become capable of fertilization."),
                                    html.Li("2. **Acrosomal Reaction:** Triggered by contact with egg jelly (in external fertilizers like sea urchins). Calcium influx leads to G-actin polymerization into f-actin."),
                                    html.Li("3. **Extension of Acrosomal Process:** F-actin forms a long protrusion that helps the sperm penetrate the egg’s outer layers."),
                                    html.Li("4. **Enzyme Release:** The acrosome releases digestive enzymes to break through the egg’s extracellular matrix (e.g., vitelline layer or zona pellucida)."),
                                    html.Li("5. **Adhesion and Fusion:** The sperm membrane binds to and fuses with the egg membrane."),
                                    html.Li("6. **Egg Activation:** The egg responds with calcium release and polyspermy prevention mechanisms."),
                                    html.Li("7. **Polyspermy Block:** Fast block (membrane depolarization) and slow block (cortical granule release to modify outer egg layers) prevent additional sperm from fusing."),
                                    html.Li("8. **Formation of the Zygote:** Male and female pronuclei fuse to form a diploid nucleus.")
                                ]),
                                html.P([
                                    html.Strong("Role of G-actin:"),
                                    " G-actin (globular actin) is a monomeric protein that polymerizes into filamentous actin (f-actin) during the acrosomal reaction.",
                                    " This polymerization forms an actin-based extension that drives the sperm forward and aids in membrane fusion."
                                ]),
                                html.P([
                                    html.Strong("Histogenesis:"),
                                    " After fertilization, the resulting zygote undergoes multiple rounds of cell division and differentiation—a process called histogenesis—to form specialized tissues and organs."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is the main outcome of fertilization?",
                        "options": [
                            "Creation of haploid gametes",
                            "Fusion of two diploid cells",
                            "Formation of a diploid zygote from haploid sperm and egg",
                            "Separation of chromosomes into gametes"
                        ],
                        "answer": "Formation of a diploid zygote from haploid sperm and egg"
                    },
                    {
                        "question": "Where does the acrosomal reaction occur?",
                        "options": [
                            "In the egg cytoplasm",
                            "On the surface of the sperm",
                            "Inside the zygote",
                            "In the uterus"
                        ],
                        "answer": "On the surface of the sperm"
                    },
                    {
                        "question": "What ion triggers the acrosomal reaction in sperm?",
                        "options": [
                            "Sodium",
                            "Potassium",
                            "Calcium",
                            "Chloride"
                        ],
                        "answer": "Calcium"
                    },
                    {
                        "question": "What is the role of G-actin during the acrosomal reaction?",
                        "options": [
                            "To digest egg membranes",
                            "To provide energy for the sperm",
                            "To polymerize into f-actin and form a protrusion",
                            "To block other sperm from fertilizing the egg"
                        ],
                        "answer": "To polymerize into f-actin and form a protrusion"
                    },
                    {
                        "question": "What structure helps the sperm penetrate the egg’s outer layers?",
                        "options": [
                            "Mitochondria",
                            "F-actin-based protrusion",
                            "Flagellum",
                            "Sperm tail"
                        ],
                        "answer": "F-actin-based protrusion"
                    },
                    {
                        "question": "Which of the following is released from the sperm’s acrosome?",
                        "options": [
                            "Calcium",
                            "Enzymes that digest egg layers",
                            "DNA",
                            "Actin"
                        ],
                        "answer": "Enzymes that digest egg layers"
                    },
                    {
                        "question": "What is the egg’s fast block to polyspermy?",
                        "options": [
                            "Enzyme digestion",
                            "Depolarization of the membrane",
                            "Fusion with another sperm",
                            "Release of G-actin"
                        ],
                        "answer": "Depolarization of the membrane"
                    },
                    {
                        "question": "What is the slow block to polyspermy?",
                        "options": [
                            "Fusion of sperm mitochondria",
                            "Release of cortical granules to modify egg membrane",
                            "DNA replication",
                            "Extension of acrosomal process"
                        ],
                        "answer": "Release of cortical granules to modify egg membrane"
                    },
                    {
                        "question": "Which term refers to tissue development after fertilization?",
                        "options": [
                            "Histogenesis",
                            "Gametogenesis",
                            "Polyspermy",
                            "Acrosome reaction"
                        ],
                        "answer": "Histogenesis"
                    },
                    {
                        "question": "In which organisms is polyspermy block especially studied?",
                        "options": [
                            "Humans and mice",
                            "Sea urchins and madako eggs",
                            "Birds and reptiles",
                            "Frogs and fish"
                        ],
                        "answer": "Sea urchins and madako eggs"
                    },
                    {
                        "question": "What is the length of a G-actin monomer?",
                        "options": [
                            "10 nm",
                            "25 nm",
                            "37 nm",
                            "100 nm"
                        ],
                        "answer": "37 nm"
                    },
                    {
                        "question": "What property of G-actin allows it to form polar filaments?",
                        "options": [
                            "Its charge",
                            "Its shape",
                            "It has a plus and minus end",
                            "It is nonpolar"
                        ],
                        "answer": "It has a plus and minus end"
                    },
                    {
                        "question": "What does the fusion of egg and sperm membranes result in?",
                        "options": [
                            "Formation of f-actin",
                            "Polyspermy",
                            "Activation of the egg",
                            "Release of calcium from sperm"
                        ],
                        "answer": "Activation of the egg"
                    },
                    {
                        "question": "What follows the adhesion of sperm to the egg surface?",
                        "options": [
                            "Egg divides immediately",
                            "Sperm DNA is released",
                            "Fusion of the plasma membranes",
                            "Fast block to polyspermy is activated first"
                        ],
                        "answer": "Fusion of the plasma membranes"
                    },
                    {
                        "question": "Which structure in the sperm helps it move toward the egg?",
                        "options": [
                            "Flagellum",
                            "Nucleus",
                            "Cortical granule",
                            "Acrosome"
                        ],
                        "answer": "Flagellum"
                    },
                    {
                        "question": "What process ensures that only one sperm fertilizes the egg?",
                        "options": [
                            "Zona digestion",
                            "Histogenesis",
                            "Polyspermy blocks",
                            "DNA recombination"
                        ],
                        "answer": "Polyspermy blocks"
                    },
                    {
                        "question": "What is the immediate result of sperm-egg membrane fusion?",
                        "options": [
                            "Egg polarity loss",
                            "Calcium release in the egg",
                            "Sperm breakdown",
                            "Histogenesis"
                        ],
                        "answer": "Calcium release in the egg"
                    },
                    {
                        "question": "What does the acrosome contain?",
                        "options": [
                            "Centrioles",
                            "Enzymes for penetrating the egg",
                            "Cortical granules",
                            "Mitochondria"
                        ],
                        "answer": "Enzymes for penetrating the egg"
                    },
                    {
                        "question": "What happens to the egg’s outer layers after fertilization?",
                        "options": [
                            "They harden and block other sperm",
                            "They are removed by enzymes",
                            "They attract more sperm",
                            "They turn into the zygote’s membrane"
                        ],
                        "answer": "They harden and block other sperm"
                    },
                    {
                        "question": "Why is actin polymerization critical during fertilization?",
                        "options": [
                            "It provides energy for sperm motility",
                            "It activates the sperm nucleus",
                            "It allows the sperm to reach and fuse with the egg",
                            "It triggers cortical granule release"
                        ],
                        "answer": "It allows the sperm to reach and fuse with the egg"
                    }
                ],
                "blurting": [html.Div([
                                html.P([
                                    html.Strong("Fertilization Overview:"),
                                    " Fertilization is the union of a haploid sperm and egg to form a diploid zygote.",
                                    " It involves sperm activation, penetration of the egg's outer layers via the acrosomal reaction, adhesion and fusion of gamete membranes, and the prevention of polyspermy.",
                                    " G-actin plays a key role in sperm by polymerizing into f-actin during the acrosomal reaction, enabling sperm-egg contact and fusion."
                                ]),
                                html.P([html.Strong("The Acrosomal Reaction:")]),
                                html.Ul([
                                    html.Li("1. **Sperm Activation:** Sperm reach the egg and undergo changes to become capable of fertilization."),
                                    html.Li("2. **Acrosomal Reaction:** Triggered by contact with egg jelly (in external fertilizers like sea urchins). Calcium influx leads to G-actin polymerization into f-actin."),
                                    html.Li("3. **Extension of Acrosomal Process:** F-actin forms a long protrusion that helps the sperm penetrate the egg’s outer layers."),
                                    html.Li("4. **Enzyme Release:** The acrosome releases digestive enzymes to break through the egg’s extracellular matrix (e.g., vitelline layer or zona pellucida)."),
                                    html.Li("5. **Adhesion and Fusion:** The sperm membrane binds to and fuses with the egg membrane."),
                                    html.Li("6. **Egg Activation:** The egg responds with calcium release and polyspermy prevention mechanisms."),
                                    html.Li("7. **Polyspermy Block:** Fast block (membrane depolarization) and slow block (cortical granule release to modify outer egg layers) prevent additional sperm from fusing."),
                                    html.Li("8. **Formation of the Zygote:** Male and female pronuclei fuse to form a diploid nucleus.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    html.Strong("Feynman Summary:"),
                                    " Fertilization is like a sperm knocking on the egg’s door, using a special battering ram made of actin.",
                                    " When the sperm touches the egg, calcium tells its G-actin to build a rod (f-actin) that pushes forward and helps the sperm stick and fuse with the egg.",
                                    " The egg then shuts the door behind the first sperm to keep others out (polyspermy block), and together, they become a zygote ready to grow into an organism."
                                ])
                            ])]
            },
            "q3": {
                "question": html.P("Understand the mechanisms involved in the blocks to polyspermy.  Be familiar with the difference between the slow and the fast blocks. Know the role that Ernest Everett played in improving our understanding of fertilization."),
                "overview": html.Div([
                                html.P([
                                    html.Strong("Blocks to Polyspermy:"),
                                    " Polyspermy is the fusion of more than one sperm with an egg, which can be lethal to the embryo.",
                                    " Fertilized eggs prevent this using two major mechanisms: the fast block and the slow block.",
                                    " The fast block involves rapid depolarization of the egg membrane due to sodium influx.",
                                    " The slow block involves calcium-triggered cortical granule release that modifies the egg's outer layer to prevent sperm entry."
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Fast Block to Polyspermy:"),
                                    " Discovered by Lora Rothschild and Rindy Jaffe, this block occurs within 10 seconds of sperm fusion.",
                                    " Sperm binding activates sodium channels in the egg membrane, causing Na⁺ influx and depolarization from -70 mV to +10 mV.",
                                    " This depolarization prevents additional sperm from fusing.",
                                    " Experiments showed that if Na⁺ is removed from seawater, depolarization doesn’t occur and polyspermy happens, confirming Na⁺'s critical role."
                                ]),
                                html.P([
                                    html.Strong("Slow Block to Polyspermy:"),
                                    " Described by Ernest Everett Just in 1902, the slow block is initiated by a Ca²⁺ wave that triggers cortical granule exocytosis.",
                                    " Cortical granules release enzymes and solutes that:"
                                ]),
                                html.Ul([
                                    html.Li("Detach the vitelline layer from the plasma membrane."),
                                    html.Li("Alter the vitelline layer so it forms a hardened fertilization envelope."),
                                    html.Li("Release solutes into the perivitelline space, lowering water potential."),
                                    html.Li("Water enters the space, expanding it and physically pushing away extra sperm.")
                                ]),
                                html.P([
                                    "This structural change takes about 1 minute and permanently prevents further sperm fusion."
                                ]),
                                html.P([
                                    html.Strong("Role of Ca²⁺:"),
                                    " In all studied species, sperm-egg fusion triggers a rapid Ca²⁺ increase inside the egg.",
                                    " Artificially raising cytosolic Ca²⁺ can initiate fertilization-like events and even lead to embryonic development without sperm."
                                ]),
                                html.P([
                                    html.Strong("Historical Insight:"),
                                    " Ernest Everett Just's research at the Marine Biological Laboratory provided foundational insights into the slow block and egg surface changes during fertilization."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What is polyspermy?",
                        "options": [
                            "Fusion of one sperm with an egg",
                            "Failure of egg activation",
                            "Fusion of more than one sperm with an egg",
                            "The release of cortical granules"
                        ],
                        "answer": "Fusion of more than one sperm with an egg"
                    },
                    {
                        "question": "Which block to polyspermy happens first?",
                        "options": [
                            "Slow block",
                            "Zygote block",
                            "Calcium block",
                            "Fast block"
                        ],
                        "answer": "Fast block"
                    },
                    {
                        "question": "What ion is involved in the fast block to polyspermy?",
                        "options": [
                            "Potassium (K⁺)",
                            "Chloride (Cl⁻)",
                            "Sodium (Na⁺)",
                            "Calcium (Ca²⁺)"
                        ],
                        "answer": "Sodium (Na⁺)"
                    },
                    {
                        "question": "How quickly does the fast block to polyspermy occur?",
                        "options": [
                            "Within 1 minute",
                            "Within 10 seconds",
                            "After fertilization is complete",
                            "Only after egg activation"
                        ],
                        "answer": "Within 10 seconds"
                    },
                    {
                        "question": "What electrical change happens during the fast block?",
                        "options": [
                            "Membrane potential goes from +10 mV to -70 mV",
                            "Membrane depolarizes from -70 mV to +10 mV",
                            "Membrane becomes more negative",
                            "The membrane repolarizes"
                        ],
                        "answer": "Membrane depolarizes from -70 mV to +10 mV"
                    },
                    {
                        "question": "What prevents the fast block from occurring if removed from sea water?",
                        "options": [
                            "Calcium",
                            "Potassium",
                            "Sodium",
                            "Oxygen"
                        ],
                        "answer": "Sodium"
                    },
                    {
                        "question": "Who was the scientist who discovered the fast block to polyspermy?",
                        "options": [
                            "Ernest Everett Just",
                            "Lora Rothschild",
                            "Charles Darwin",
                            "Rindy Just"
                        ],
                        "answer": "Lora Rothschild"
                    },
                    {
                        "question": "Which Purdue alumnus aided in discovering the fast block?",
                        "options": [
                            "Ernest Just",
                            "Rindy Jaffe",
                            "Rosalind Franklin",
                            "Craig Venter"
                        ],
                        "answer": "Rindy Jaffe"
                    },
                    {
                        "question": "What triggers the slow block to polyspermy?",
                        "options": [
                            "Sodium influx",
                            "Oxygen release",
                            "Calcium wave",
                            "Sperm tail penetration"
                        ],
                        "answer": "Calcium wave"
                    },
                    {
                        "question": "What cellular structures release contents during the slow block?",
                        "options": [
                            "Nucleus",
                            "Cortical granules",
                            "Mitochondria",
                            "Ribosomes"
                        ],
                        "answer": "Cortical granules"
                    },
                    {
                        "question": "What happens to the vitelline layer during the slow block?",
                        "options": [
                            "It fuses with the sperm membrane",
                            "It dissolves entirely",
                            "It detaches and hardens to form a protective barrier",
                            "It turns into the zygote membrane"
                        ],
                        "answer": "It detaches and hardens to form a protective barrier"
                    },
                    {
                        "question": "How long does the slow block to polyspermy take to complete?",
                        "options": [
                            "About 1 second",
                            "About 10 seconds",
                            "About 1 minute",
                            "About 10 minutes"
                        ],
                        "answer": "About 1 minute"
                    },
                    {
                        "question": "What causes water to rush into the perivitelline space during the slow block?",
                        "options": [
                            "A rise in temperature",
                            "Sperm membrane fusion",
                            "Increased solute concentration from cortical granules",
                            "Actin polymerization"
                        ],
                        "answer": "Increased solute concentration from cortical granules"
                    },
                    {
                        "question": "What is the perivitelline space?",
                        "options": [
                            "The interior of the sperm",
                            "The outer shell of the zygote",
                            "The space created between the plasma membrane and vitelline layer",
                            "The area between two sperm nuclei"
                        ],
                        "answer": "The space created between the plasma membrane and vitelline layer"
                    },
                    {
                        "question": "What is the role of enzymes released from cortical granules?",
                        "options": [
                            "To depolarize the membrane",
                            "To polymerize G-actin",
                            "To modify the vitelline layer and prevent sperm binding",
                            "To attract more sperm"
                        ],
                        "answer": "To modify the vitelline layer and prevent sperm binding"
                    },
                    {
                        "question": "Who discovered the mechanisms of the slow block to polyspermy?",
                        "options": [
                            "Lora Rothschild",
                            "Rindy Jaffe",
                            "Ernest Everett Just",
                            "Gregor Mendel"
                        ],
                        "answer": "Ernest Everett Just"
                    },
                    {
                        "question": "Where did Ernest Everett Just conduct his fertilization research?",
                        "options": [
                            "Harvard University",
                            "Marine Biological Laboratory at Woods Hole, MA",
                            "Purdue University",
                            "Cold Spring Harbor Laboratory"
                        ],
                        "answer": "Marine Biological Laboratory at Woods Hole, MA"
                    },
                    {
                        "question": "What happens if cytosolic Ca²⁺ is artificially increased in an egg?",
                        "options": [
                            "Fertilization is blocked",
                            "Only polyspermy occurs",
                            "Fertilization-like events begin and embryos may form",
                            "The egg membrane repolarizes"
                        ],
                        "answer": "Fertilization-like events begin and embryos may form"
                    },
                    {
                        "question": "What kind of experiments confirmed that Na⁺ is necessary for the fast block?",
                        "options": [
                            "Depolarization by potassium injection",
                            "Removal of Na⁺ from seawater and observing polyspermy",
                            "Blocking Ca²⁺ channels",
                            "Adding glucose to the egg medium"
                        ],
                        "answer": "Removal of Na⁺ from seawater and observing polyspermy"
                    },
                    {
                        "question": "What key cellular change occurs in the egg during the fast block?",
                        "options": [
                            "Vesicle formation",
                            "Na⁺ leaves the cell",
                            "Membrane becomes positively charged",
                            "Calcium release stops"
                        ],
                        "answer": "Membrane becomes positively charged"
                    }
                ],
                "blurting": [html.Div([
                                html.P([html.Strong("Fast Block to Polyspermy (within ~10 seconds):")]),
                                html.Ul([
                                    html.Li("1. Sperm fuses with the egg’s plasma membrane."),
                                    html.Li("2. Sperm fusion triggers the opening of sodium (Na⁺) channels in the egg membrane."),
                                    html.Li("3. Sodium ions rush into the egg, depolarizing the membrane from approximately -70 mV to +10 mV."),
                                    html.Li("4. This change in membrane potential prevents additional sperm from binding to or fusing with the egg."),
                                    html.Li("5. If Na⁺ is removed from the environment, this block fails and polyspermy can occur."),
                                    html.Li("6. This fast electrical block is temporary but essential for immediate protection.")
                                ]),
                                html.Br(),
                                html.P([html.Strong("Slow Block to Polyspermy (completes in ~1 minute):")]),
                                html.Ul([
                                    html.Li("1. Sperm fusion also triggers a wave of calcium (Ca²⁺) release in the egg’s cytoplasm."),
                                    html.Li("2. Elevated Ca²⁺ causes cortical granules (vesicles just under the egg membrane) to fuse with the plasma membrane."),
                                    html.Li("3. Cortical granules release enzymes and solutes into the space between the egg membrane and the vitelline layer (now the perivitelline space)."),
                                    html.Li("4. Enzymes modify the vitelline layer, making it resistant to sperm binding and penetration."),
                                    html.Li("5. Solutes increase the osmolarity of the perivitelline space, drawing water in by osmosis."),
                                    html.Li("6. Water entry expands the space, physically lifting and hardening the vitelline layer into a fertilization envelope."),
                                    html.Li("7. This long-lasting mechanical and chemical barrier ensures only one sperm fertilizes the egg.")
                                ])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    html.Strong("Feynman Summary:"),
                                    " When a sperm fuses with an egg, the egg quickly zaps its membrane (depolarization) to stop more sperm—this is the fast block.",
                                    " Then it slowly builds a protective shield using stored enzymes (the slow block), kind of like sealing a door after locking it.",
                                    " Calcium makes this shield form by triggering a wave of reactions that lift and harden the egg’s outer layer.",
                                    " Ernest Everett Just figured out the egg’s secret sauce for sealing itself nearly a century ago."
                                ])
                ])]
            },
            "q4": {
                "question": html.P("Know the role Ernest Everett played in improving our understanding of fertilization."),
                "overview": html.Div([html.P([
                                        html.Strong("Ernest Everett Just and the Slow Block to Polyspermy:"),
                                        " Ernest Everett Just was a pioneering cell biologist who made key discoveries in the early 1900s about fertilization.",
                                        " He studied sea urchin eggs and found that substances released from cortical granules alter the egg’s surface to prevent polyspermy.",
                                        " His work at the Marine Biological Laboratory in Woods Hole, MA laid the foundation for our modern understanding of the slow block to polyspermy."
                                        ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Scientific Contributions of Ernest Everett Just:")
                                ]),
                                html.Ul([
                                    html.Li("In 1902, Just conducted fertilization experiments using marine invertebrates, especially sea urchins."),
                                    html.Li("He observed that after a single sperm entered the egg, granules just beneath the plasma membrane (called cortical granules) released their contents."),
                                    html.Li("This release caused visible and structural changes to the egg’s outer surface, forming a barrier to additional sperm."),
                                    html.Li("He identified this process as the basis of what we now call the 'slow block to polyspermy'."),
                                    html.Li("His work demonstrated that the egg plays an active role in regulating fertilization and preventing errors in early development."),
                                    html.Li("These discoveries were made at the Marine Biological Laboratory in Woods Hole, Massachusetts—a major hub for marine biology research.")
                                ]),
                                html.P([
                                    "Ernest Everett Just was also a champion of experimental rigor and emphasized the importance of studying cells in natural conditions, not just under artificial lab settings.",
                                    " His careful observation and innovative methods advanced both embryology and cell biology."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                     {
                        "question": "Who was Ernest Everett Just?",
                        "options": [
                            "A geneticist who discovered DNA structure",
                            "A neuroscientist who studied action potentials",
                            "A cell biologist who studied fertilization and egg biology",
                            "An ecologist who discovered coral reproduction"
                        ],
                        "answer": "A cell biologist who studied fertilization and egg biology"
                    },
                    {
                        "question": "Where did Ernest Everett Just conduct his key research on fertilization?",
                        "options": [
                            "Harvard University",
                            "Purdue University",
                            "Cold Spring Harbor Laboratory",
                            "Marine Biological Laboratory in Woods Hole, MA"
                        ],
                        "answer": "Marine Biological Laboratory in Woods Hole, MA"
                    },
                    {
                        "question": "In what year did Ernest Everett Just perform his key fertilization experiments?",
                        "options": [
                            "1865",
                            "1902",
                            "1953",
                            "1990"
                        ],
                        "answer": "1902"
                    },
                    {
                        "question": "Which structure did Ernest Everett Just discover was responsible for surface changes in the egg?",
                        "options": [
                            "Zona pellucida",
                            "Polar bodies",
                            "Cortical granules",
                            "Sperm tail"
                        ],
                        "answer": "Cortical granules"
                    },
                    {
                        "question": "What do cortical granules do during the slow block to polyspermy?",
                        "options": [
                            "Increase sperm motility",
                            "Release enzymes and solutes that alter the egg’s surface",
                            "Create new chromosomes",
                            "Prevent calcium signaling"
                        ],
                        "answer": "Release enzymes and solutes that alter the egg’s surface"
                    },
                    {
                        "question": "Why is the slow block important in fertilization?",
                        "options": [
                            "It speeds up zygote formation",
                            "It ensures only one sperm fertilizes the egg",
                            "It prevents the egg from dividing",
                            "It neutralizes calcium ions"
                        ],
                        "answer": "It ensures only one sperm fertilizes the egg"
                    },
                    {
                        "question": "Which organism did Just primarily use in his fertilization experiments?",
                        "options": [
                            "Frogs",
                            "Sea urchins",
                            "Chickens",
                            "Mice"
                        ],
                        "answer": "Sea urchins"
                    },
                    {
                        "question": "What forms between the egg’s plasma membrane and vitelline layer during the slow block?",
                        "options": [
                            "Zona reaction",
                            "Perivitelline space",
                            "Amniotic cavity",
                            "Cytosol"
                        ],
                        "answer": "Perivitelline space"
                    },
                    {
                        "question": "Which event initiates cortical granule release?",
                        "options": [
                            "Sperm flagella contact",
                            "Mitochondrial activation",
                            "Rise in intracellular calcium (Ca²⁺)",
                            "Drop in membrane potential"
                        ],
                        "answer": "Rise in intracellular calcium (Ca²⁺)"
                    },
                    {
                        "question": "What was one of Ernest Everett Just’s major contributions to science besides his discoveries?",
                        "options": [
                            "Creating artificial embryos",
                            "Emphasizing natural conditions in experimental design",
                            "Inventing calcium-sensitive dyes",
                            "Using genetic engineering"
                        ],
                        "answer": "Emphasizing natural conditions in experimental design"
                    },
                    {
                        "question": "What happens to the egg’s surface as a result of cortical granule release?",
                        "options": [
                            "It becomes softer",
                            "It fuses with the sperm tail",
                            "It hardens and prevents additional sperm entry",
                            "It dissolves entirely"
                        ],
                        "answer": "It hardens and prevents additional sperm entry"
                    },
                    {
                        "question": "Which block to polyspermy did Just’s research help explain?",
                        "options": [
                            "Fast block",
                            "Slow block",
                            "Mechanical block",
                            "Electrical block"
                        ],
                        "answer": "Slow block"
                    },
                    {
                        "question": "What types of molecules are released from cortical granules?",
                        "options": [
                            "Hormones",
                            "DNA fragments",
                            "Enzymes and solutes",
                            "Nutrients"
                        ],
                        "answer": "Enzymes and solutes"
                    },
                    {
                        "question": "What is the ultimate result of cortical granule exocytosis?",
                        "options": [
                            "Membrane depolarization",
                            "Cilia formation",
                            "Fertilization envelope formation",
                            "Release of polar bodies"
                        ],
                        "answer": "Fertilization envelope formation"
                    },
                    {
                        "question": "Why is Ernest Everett Just considered a pioneer in developmental biology?",
                        "options": [
                            "He cloned a frog",
                            "He sequenced the human genome",
                            "He discovered sperm competition",
                            "He identified critical egg surface responses to sperm entry"
                        ],
                        "answer": "He identified critical egg surface responses to sperm entry"
                    },
                    {
                        "question": "Which layer of the egg is modified to block more sperm after cortical granule release?",
                        "options": [
                            "Zona pellucida",
                            "Plasma membrane",
                            "Vitelline layer",
                            "Cytoskeleton"
                        ],
                        "answer": "Vitelline layer"
                    },
                    {
                        "question": "What happens to water potential in the perivitelline space during the slow block?",
                        "options": [
                            "It increases",
                            "It decreases, drawing in water",
                            "It stays constant",
                            "It pushes water out"
                        ],
                        "answer": "It decreases, drawing in water"
                    },
                    {
                        "question": "What physical change helps push remaining sperm away during the slow block?",
                        "options": [
                            "Muscle contraction",
                            "Membrane depolarization",
                            "Influx of water into the perivitelline space",
                            "Actin polymerization"
                        ],
                        "answer": "Influx of water into the perivitelline space"
                    },
                    {
                        "question": "Why was Just’s work particularly innovative for his time?",
                        "options": [
                            "He used microscopes for the first time",
                            "He proposed cells acted independently of environmental cues",
                            "He focused on egg cell responses instead of sperm-driven fertilization",
                            "He believed in spontaneous generation"
                        ],
                        "answer": "He focused on egg cell responses instead of sperm-driven fertilization"
                    },
                    {
                        "question": "What long-term scientific principle did Just help establish?",
                        "options": [
                            "That eggs are passive in fertilization",
                            "That the environment doesn't affect cell behavior",
                            "That the egg actively controls entry and development after fertilization",
                            "That sperm alone determine offspring traits"
                        ],
                        "answer": "That the egg actively controls entry and development after fertilization"
                    }
                ],
                "blurting": [html.Div([html.P([
                                        html.Strong("Ernest Everett Just and the Slow Block to Polyspermy:"),
                                        " Ernest Everett Just was a pioneering cell biologist who made key discoveries in the early 1900s about fertilization.",
                                        " He studied sea urchin eggs and found that substances released from cortical granules alter the egg’s surface to prevent polyspermy.",
                                        " His work at the Marine Biological Laboratory in Woods Hole, MA laid the foundation for our modern understanding of the slow block to polyspermy."
                                        ])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    html.Strong("Feynman Summary:"),
                                    " Ernest Everett Just watched sea urchin eggs under a microscope and noticed that when a sperm entered, the egg fought off more sperm by changing its surface.",
                                    " He figured out this was caused by little bags inside the egg—cortical granules—that burst and built a shield around the egg.",
                                    " Thanks to him, we understand how eggs defend themselves after one sperm gets in, so no extras mess things up."
                                ])
                ])]
            },
            "q5": {
                "question": html.P("Be able to explain the contributions of Ca+ and of cortical granules to the process of fertilization."),
                "overview": html.Div([
                                html.P([
                                    html.Strong("Role of Ca²⁺ and Cortical Granules in Fertilization:"),
                                    " Following sperm-egg membrane fusion, there is a rapid increase in cytosolic calcium (Ca²⁺) inside the egg.",
                                    " This calcium surge triggers the release of cortical granules, which cause the vitelline membrane to separate from the egg’s plasma membrane, forming the perivitelline space.",
                                    " This process is essential to prevent polyspermy, acting as the slow block to fertilization."
                                ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    html.Strong("Calcium (Ca²⁺) Surge at Fertilization:"),
                                    " Upon sperm fusion with the egg membrane, Ca²⁺ levels inside the egg cytosol rise sharply.",
                                    " This universal signal activates downstream events necessary for egg activation and embryonic development."
                                ]),
                                html.P([
                                    html.Strong("Cortical Granule Exocytosis:"),
                                    " The increase in cytosolic Ca²⁺ causes cortical granules—small vesicles located just beneath the egg plasma membrane—to fuse with the membrane and release their contents into the perivitelline space."
                                ]),
                                html.P([
                                    html.Strong("Formation of the Perivitelline Space and Slow Block:"),
                                    " The enzymes and solutes released from cortical granules modify the vitelline membrane, causing it to lift off the plasma membrane, thereby creating the perivitelline space.",
                                    " This new space, along with the hardened vitelline layer, forms a physical and chemical barrier that prevents additional sperm from penetrating the egg, effectively preventing polyspermy."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What triggers the rapid increase in cytosolic Ca²⁺ in the egg during fertilization?",
                        "options": [
                            "Sperm membrane fusion with the egg membrane",
                            "Egg membrane depolarization",
                            "Release of cortical granules",
                            "DNA replication"
                        ],
                        "answer": "Sperm membrane fusion with the egg membrane"
                    },
                    {
                        "question": "What is the role of the increased Ca²⁺ inside the egg after fertilization?",
                        "options": [
                            "To break down sperm DNA",
                            "To activate cortical granule exocytosis",
                            "To depolarize the sperm membrane",
                            "To initiate egg membrane fusion"
                        ],
                        "answer": "To activate cortical granule exocytosis"
                    },
                    {
                        "question": "Where are cortical granules located in the egg?",
                        "options": [
                            "Inside the nucleus",
                            "Just beneath the plasma membrane",
                            "In the cytoplasm near the mitochondria",
                            "In the vitelline membrane"
                        ],
                        "answer": "Just beneath the plasma membrane"
                    },
                    {
                        "question": "What happens when cortical granules release their contents?",
                        "options": [
                            "The vitelline membrane detaches from the egg membrane",
                            "The sperm membrane depolarizes",
                            "The egg starts DNA replication",
                            "The sperm fuses with the egg"
                        ],
                        "answer": "The vitelline membrane detaches from the egg membrane"
                    },
                    {
                        "question": "What is the perivitelline space?",
                        "options": [
                            "The space between the sperm and egg membranes",
                            "The space created by separation of the vitelline membrane from the egg membrane",
                            "The interior of the sperm",
                            "The space inside the egg nucleus"
                        ],
                        "answer": "The space created by separation of the vitelline membrane from the egg membrane"
                    },
                    {
                        "question": "What is the function of the perivitelline space in fertilization?",
                        "options": [
                            "To allow sperm entry",
                            "To provide nutrients to the sperm",
                            "To prevent polyspermy by creating a physical barrier",
                            "To help the sperm swim faster"
                        ],
                        "answer": "To prevent polyspermy by creating a physical barrier"
                    },
                    {
                        "question": "Which process is known as the slow block to polyspermy?",
                        "options": [
                            "Membrane depolarization",
                            "Cortical granule exocytosis and vitelline membrane modification",
                            "Sperm motility increase",
                            "Sperm DNA degradation"
                        ],
                        "answer": "Cortical granule exocytosis and vitelline membrane modification"
                    },
                    {
                        "question": "What type of molecules are released from cortical granules?",
                        "options": [
                            "Enzymes and solutes",
                            "DNA and RNA",
                            "Calcium ions",
                            "Sodium ions"
                        ],
                        "answer": "Enzymes and solutes"
                    },
                    {
                        "question": "How does the rise in Ca²⁺ inside the egg relate to embryo development?",
                        "options": [
                            "It initiates developmental signaling pathways",
                            "It causes sperm to multiply",
                            "It depolarizes the egg membrane permanently",
                            "It breaks down the egg membrane"
                        ],
                        "answer": "It initiates developmental signaling pathways"
                    },
                    {
                        "question": "What would happen if the Ca²⁺ increase did not occur after sperm fusion?",
                        "options": [
                            "Cortical granules would not release their contents",
                            "Polyspermy would be prevented",
                            "The egg would immediately divide",
                            "Sperm would fail to fuse"
                        ],
                        "answer": "Cortical granules would not release their contents"
                    },
                    {
                        "question": "Why is preventing polyspermy important?",
                        "options": [
                            "Multiple sperm increase genetic diversity",
                            "Multiple sperm cause lethal chromosomal abnormalities",
                            "It speeds up fertilization",
                            "It prevents egg activation"
                        ],
                        "answer": "Multiple sperm cause lethal chromosomal abnormalities"
                    },
                    {
                        "question": "Which ion’s rapid increase is universal in all eggs at fertilization?",
                        "options": [
                            "Sodium (Na⁺)",
                            "Potassium (K⁺)",
                            "Calcium (Ca²⁺)",
                            "Chloride (Cl⁻)"
                        ],
                        "answer": "Calcium (Ca²⁺)"
                    },
                    {
                        "question": "What is the immediate cause of cortical granule fusion with the plasma membrane?",
                        "options": [
                            "Sperm DNA entering the egg",
                            "Calcium ion increase in the cytosol",
                            "Sodium influx",
                            "Egg membrane repolarization"
                        ],
                        "answer": "Calcium ion increase in the cytosol"
                    },
                    {
                        "question": "Which fertilization event physically pushes extra sperm away from the egg?",
                        "options": [
                            "Membrane depolarization",
                            "Water influx into the perivitelline space",
                            "Sperm flagella movement",
                            "DNA synthesis"
                        ],
                        "answer": "Water influx into the perivitelline space"
                    },
                    {
                        "question": "What causes water to flow into the perivitelline space?",
                        "options": [
                            "Increase in solute concentration from cortical granules",
                            "Decrease in calcium concentration",
                            "Sperm membrane depolarization",
                            "Decrease in osmotic pressure"
                        ],
                        "answer": "Increase in solute concentration from cortical granules"
                    },
                    {
                        "question": "How fast does the slow block to polyspermy take to develop?",
                        "options": [
                            "Seconds",
                            "Approximately 1 minute",
                            "Several hours",
                            "Immediately"
                        ],
                        "answer": "Approximately 1 minute"
                    },
                    {
                        "question": "Which structure in the egg modifies to form a hardened barrier after cortical granule release?",
                        "options": [
                            "Plasma membrane",
                            "Vitelline membrane",
                            "Nuclear envelope",
                            "Sperm tail"
                        ],
                        "answer": "Vitelline membrane"
                    },
                    {
                        "question": "What is the effect of cortical granule enzymes on the vitelline membrane?",
                        "options": [
                            "They dissolve it",
                            "They harden and lift it away from the egg membrane",
                            "They make it more permeable",
                            "They cause it to fuse with sperm"
                        ],
                        "answer": "They harden and lift it away from the egg membrane"
                    },
                    {
                        "question": "What triggers the rise of cytosolic Ca²⁺ in the egg at fertilization?",
                        "options": [
                            "Sperm binding and fusion",
                            "Egg membrane repolarization",
                            "Enzyme release",
                            "DNA replication"
                        ],
                        "answer": "Sperm binding and fusion"
                    },
                    {
                        "question": "What role does Ca²⁺ play in fertilization beyond cortical granule release?",
                        "options": [
                            "It has no other role",
                            "It activates egg metabolism and embryonic development",
                            "It inhibits fertilization",
                            "It depolarizes sperm membrane"
                        ],
                        "answer": "It activates egg metabolism and embryonic development"
                    }
                ],
                "blurting": [html.Div([
                    html.P([
                                    html.Strong("Role of Ca²⁺ and Cortical Granules in Fertilization:"),
                                    " Following sperm-egg membrane fusion, there is a rapid increase in cytosolic calcium (Ca²⁺) inside the egg.",
                                    " This calcium surge triggers the release of cortical granules, which cause the vitelline membrane to separate from the egg’s plasma membrane, forming the perivitelline space.",
                                    " This process is essential to prevent polyspermy, acting as the slow block to fertilization."
                                ])
                ])],
                "feynman": [html.Div([
                            html.P([
                                html.Strong("Feynman Summary:"),
                                " When the sperm meets the egg, calcium inside the egg shoots up like a signal flare.",
                                " This calcium tells little bags called cortical granules to open up and spill their contents.",
                                " The spill makes the egg’s outer shell lift and harden, creating a barrier that stops any other sperm from getting in."
                            ])
                ])]
            }, 
            "q6": {
                "question": html.P("Be able to define the term Homunculus.  Be able to describe the difference between the theories of “Preformation” and “Epigenesis”."),
                "overview": html.Div([
                    html.P(["A ", html.Strong("homunculus "), "is an imagined miniature human once through to be visible inside of a sperm cell. This encapsulates the outdated theory of ", html.Strong("preformation.")]),
                    html.Br(), 
                    html.P([html.Strong("Preformation versus Epigenesis")]),
                    html.Ul([
                        html.Li([html.Strong("Preformation: "), "suggested that organisms develop from fully formed, miniature versions of themselves"]),
                        html.Li([html.Strong("Epigenesis: ")]), "is the modern understanding that organisms gradually develop from a relatively unstructured egg, whose later structuring is guided by internal molecular cues and asymmetries"
                    ])
                ]), 
                "deep_dive": html.Div([
                                html.P([
                                    "The concept of the ", html.Strong("homunculus"), " was part of the theory of ",
                                    html.Strong("preformation"), ", which claimed that development involved the growth of a tiny, fully formed human inside the sperm or egg. ",
                                    "Early microscopists believed they saw such structures, reinforcing the belief that all traits and body parts were already pre-made."
                                ]),
                                html.P([
                                    "This contrasts sharply with the modern theory of ", html.Strong("epigenesis"),
                                    ", which states that organisms develop through a step-by-step process where structures and organs form progressively. ",
                                    "Development starts from a relatively unpatterned egg, which already contains ", html.Strong("asymmetries"),
                                    " in its structure. These asymmetries can be differences in pigment, proteins, or mRNA distribution between poles of the egg, ",
                                    "and they help set up the body plan — for example, the ", html.Strong("animal pole"), " typically becomes the head region of the embryo."
                                ])
                ]), 
                "image": html.Div([
                    html.H2("Visual Summary", className = "text-center"), 
                    html.Img(
                        src = "/assets/studyguide1question1.jpg",
                        style={"width": "100%", "maxWidth": "80%", "display": "block", "margin": "0 auto"})
                ]), 
                "practice_questions": [
                    {
                        "question": "What did early microscopists believe they saw inside human sperm cells?",
                        "options": ["Zygotes", "Egg cells", "Chromosomes", "Homunculi", "Embryos"],
                        "answer": "Homunculi"
                    },
                    {
                        "question": "Which theory suggested that development is a gradual process from a simple egg?",
                        "options": ["Preformation", "Epigenesis", "Cell theory", "Germ theory", "Vitalism"],
                        "answer": "Epigenesis"
                    },
                    {
                        "question": "Which term describes the belief that all traits were pre-packaged in a tiny human within the sperm or egg?",
                        "options": ["Epigenesis", "Symmetry", "Differentiation", "Preformation", "Totipotency"],
                        "answer": "Preformation"
                    },
                    {
                        "question": "What evidence within the egg supports the theory of epigenesis?",
                        "options": ["Presence of DNA", "Asymmetry in pigment and mRNA", "Preformed limbs", "Tiny human structure", "All cells being identical"],
                        "answer": "Asymmetry in pigment and mRNA"
                    },
                    {
                        "question": "What typically becomes the head region of an embryo?",
                        "options": ["Vegetal pole", "Animal pole", "Germinal center", "Blastopore", "Neural tube"],
                        "answer": "Animal pole"
                    },
                    {
                        "question": "Who believed in the concept of the homunculus?",
                        "options": ["Modern developmental biologists", "Preformationists", "Geneticists", "Embryologists", "Anatomists"],
                        "answer": "Preformationists"
                    },
                    {
                        "question": "Which of the following best describes epigenesis?",
                        "options": [
                            "A human is fully formed at conception",
                            "The egg and sperm are identical",
                            "Development arises gradually through organized changes",
                            "All cells start as neurons",
                            "The embryo does not change after fertilization"
                        ],
                        "answer": "Development arises gradually through organized changes"
                    },
                    {
                        "question": "Which structure in the egg often has more pigment and becomes the head end?",
                        "options": ["Vegetal pole", "Animal pole", "Zygote", "Morula", "Cleavage furrow"],
                        "answer": "Animal pole"
                    },
                    {
                        "question": "Which molecular difference in the egg helps determine body axis formation?",
                        "options": [
                            "Equal chromatin distribution",
                            "Symmetrical protein patterns",
                            "Asymmetrical mRNA and protein gradients",
                            "Presence of mitochondria",
                            "Nuclear size differences"
                        ],
                        "answer": "Asymmetrical mRNA and protein gradients"
                    },
                    {
                        "question": "Why is the theory of preformation considered incorrect today?",
                        "options": [
                            "It doesn’t explain fertilization",
                            "It was based on blurry images",
                            "It lacks evidence of gradual development",
                            "It ignored DNA",
                            "It was religious in origin"
                        ],
                        "answer": "It lacks evidence of gradual development"
                    },
                    {
                        "question": "Which pole of the egg typically contains more cytoplasm and yolk?",
                        "options": ["Animal pole", "Vegetal pole", "Neural pole", "Blastopore", "Cleavage pole"],
                        "answer": "Vegetal pole"
                    },
                    {
                        "question": "What does the term 'epigenesis' literally mean?",
                        "options": ["Pre-made life", "Outside origin", "Layered growth", "Inner change", "Miniature form"],
                        "answer": "Layered growth"
                    },
                    {
                        "question": "What structure forms after fertilization and represents a one-cell stage?",
                        "options": ["Morula", "Zygote", "Blastula", "Neural tube", "Gastrula"],
                        "answer": "Zygote"
                    },
                    {
                        "question": "Which scientific tool led early researchers to believe in homunculi?",
                        "options": ["Stethoscope", "Ultrasound", "Light microscope", "Electron microscope", "MRI"],
                        "answer": "Light microscope"
                    },
                    {
                        "question": "What type of biological evidence contradicts preformation?",
                        "options": ["Stem cell potency", "Genetic recombination", "Stepwise embryonic stages", "Muscle fiber contraction", "Neural crest migration"],
                        "answer": "Stepwise embryonic stages"
                    },
                    {
                        "question": "What do differences between the animal and vegetal poles indicate?",
                        "options": ["Cell death", "Preformation", "Polarity in early development", "Symmetrical division", "Zygote failure"],
                        "answer": "Polarity in early development"
                    },
                    {
                        "question": "Which concept most closely aligns with modern developmental biology?",
                        "options": ["Preformation", "Spontaneous generation", "Epigenesis", "Biogenesis", "Evolution"],
                        "answer": "Epigenesis"
                    },
                    {
                        "question": "The homunculus theory incorrectly assumed that:",
                        "options": [
                            "Development occurs after birth",
                            "The egg was unnecessary",
                            "An entire organism was pre-formed in sperm",
                            "Genes could be turned on or off",
                            "Embryos are identical to adults"
                        ],
                        "answer": "An entire organism was pre-formed in sperm"
                    },
                    {
                        "question": "What stage follows the zygote in early development?",
                        "options": ["Gastrula", "Neurula", "Morula", "Organogenesis", "Blastocyst"],
                        "answer": "Morula"
                    },
                    {
                        "question": "Which term refers to the emergence of new structures during development?",
                        "options": ["Regression", "Epigenesis", "Preformation", "Involution", "Cleavage"],
                        "answer": "Epigenesis"
                    }
                ],
                "blurting": [html.Div([
                    html.P(["A ", html.Strong("homunculus "), "is an imagined miniature human once through to be visible inside of a sperm cell. This encapsulates the outdated theory of ", html.Strong("preformation.")]),
                    html.Br(), 
                    html.P([html.Strong("Preformation versus Epigenesis")]),
                    html.Ul([
                        html.Li([html.Strong("Preformation: "), "suggested that organisms develop from fully formed, miniature versions of themselves"]),
                        html.Li([html.Strong("Epigenesis: ")]), "is the modern understanding that organisms gradually develop from a relatively unstructured egg, whose later structuring is guided by internal molecular cues and asymmetries"
                    ])
                ])],
                "feynman": [html.Div([
                                html.P([
                                    "People used to think sperm had tiny people inside called ", html.Strong("homunculi"), " — like Russian dolls. ",
                                    "That idea, called ", html.Strong("preformation"), ", said everything was already pre-made. ",
                                    "But we now know development works through ", html.Strong("epigenesis"),
                                    ", where the form slowly builds up from a simple egg. The egg isn't blank; one side is different from the other, ",
                                    "and that helps the embryo grow in the right way."
                                ])
                ])]
            },
        }
    }
}


