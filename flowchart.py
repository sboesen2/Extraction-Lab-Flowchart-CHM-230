from graphviz import Digraph
from IPython.display import display

# Create a new directed graph
flowchart = Digraph("Extraction and Isolation Experiment", node_attr={'shape': 'box', 'style': 'filled', 'color': 'lightblue'})

# Start: Preparation and Setup
flowchart.node("Start", "Preparation & Setup: Weigh ~150 mg analgesic, dissolve in 4 mL diethyl ether")
flowchart.node("Weigh", "Weigh ~150 mg of unknown analgesic\n(Observation: 0.15 g)")
flowchart.node("Shake", "Add to conical tube with 4 mL diethyl ether\n(Observation: Shaking the mixture)")

# Phase 1: Extraction
flowchart.node("AcidWash1", "Step 1: Add 2 mL of 3M HCl (Acid Wash)\nVENT the mixture\n(Observation: Mixture yellow, strong odor)")
flowchart.node("SepLayers1", "Step 2: Separate bottom aqueous layer into Solution A")
flowchart.node("CheckVol1", "Did you extract correct volume of HCl?")

# Decision 1: Correct HCl Volume
flowchart.node("Yes1", "Yes: Continue", shape="diamond", style="filled", color="lightgreen")
flowchart.node("No1", "No: Adjust extraction\n(Observation: Adjusted to correct HCl volume)", shape="diamond", style="filled", color="lightcoral")

# Second Acid Wash
flowchart.node("AcidWash2", "Step 3: Add 2 mL HCl again to remaining organic layer\nSeparate bottom layer into Solution A\nCombine both washes")
flowchart.node("AcidDone", "End of Acid Extraction: Solution A prepared")

# Phase 1: Basic Wash
flowchart.node("BasicWash1", "Step 4: Add 2 mL NaOH to organic layer\nSeparate bottom aqueous layer into Solution B")
flowchart.node("BasicWash2", "Step 5: Repeat NaOH wash and combine into Solution B")
flowchart.node("BasicDone", "End of Basic Extraction: Solution B prepared\n(Organic layer is Solution C)")

# Phase 2: Isolation - Solution A
flowchart.node("NeutralizeA", "Step 6: Slowly add 6M NaOH to Solution A\nReach pH 10 (blue litmus)\n(Observation: pH 10 reached)")
flowchart.node("VacFilterA", "Step 7: Vacuum filtration to collect crystals from Solution A\n(Observation: Low yield of crystals)")

# Decision 2: Enough Crystals?
flowchart.node("EnoughA", "Are there enough crystals for a melting point?", shape="diamond", style="filled", color="yellow")
flowchart.node("YesA", "Yes: Proceed to melting point test", shape="diamond", style="filled", color="lightgreen")
flowchart.node("NoA", "No: Redo extraction\n(Observation: Redid extraction for Solution A)", shape="diamond", style="filled", color="lightcoral")

# Final Step for Solution A
flowchart.node("MeltingA", "Step 8: Perform melting point test\n(Observation: Melting point 89-93°C)")

# Solution B Isolation
flowchart.node("NeutralizeB", "Step 9: Add 6M HCl to Solution B to reach pH 2\nVacuum filter to collect crystals\n(No melting point recorded)")

# Connections
flowchart.edges([("Start", "Weigh"), ("Weigh", "Shake"), ("Shake", "AcidWash1"), 
                 ("AcidWash1", "SepLayers1"), ("SepLayers1", "CheckVol1"),
                 ("CheckVol1", "Yes1"), ("CheckVol1", "No1"), 
                 ("Yes1", "AcidWash2"), ("No1", "AcidWash2"),
                 ("AcidWash2", "AcidDone"), 
                 ("AcidDone", "BasicWash1"), ("BasicWash1", "BasicWash2"), 
                 ("BasicWash2", "BasicDone"), 
                 ("BasicDone", "NeutralizeA"), 
                 ("NeutralizeA", "VacFilterA"), 
                 ("VacFilterA", "EnoughA"), 
                 ("EnoughA", "YesA"), ("EnoughA", "NoA"), 
                 ("YesA", "MeltingA"), ("NoA", "NeutralizeA"),
                 ("BasicDone", "NeutralizeB")])

# Display the flowchart directly in the notebook
display(flowchart)
