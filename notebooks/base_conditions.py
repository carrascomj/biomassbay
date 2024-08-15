"""Base conditions for all simulations."""

import json
from pathlib import Path

import cobra


def apply_base_conditions(model: cobra.Model, exchange_groups_path: Path):
    """Apply base conditions in-place."""
    with open(exchange_groups_path) as file:
        reac_groups = json.load(file)
    for ex in reac_groups["influx"]:
        if model.reactions.get_by_id(ex).lower_bound < 0:
            model.reactions.get_by_id(ex).upper_bound = 0
        else:
            model.reactions.get_by_id(ex).bounds = 0, 0
    for ex in reac_groups["outflux"]:
        if model.reactions.get_by_id(ex).upper_bound > 0:
            model.reactions.get_by_id(ex).lower_bound = 0
        else:
            model.reactions.get_by_id(ex).bounds = 0, 0
    for reac in reac_groups["nadph_producing"]:
        if model.reactions.get_by_id(reac).lower_bound > 0:
            model.reactions.get_by_id(reac).upper_bound = 0
        else:
            model.reactions.get_by_id(reac).bounds = 0, 0
    for reac in reac_groups["kos"]:
        model.reactions.get_by_id(reac).bounds = 0, 0
    for ex in list(reac_groups["substrates"]) + list(reac_groups["aminoacids"]):
        model.reactions.get_by_id(ex).lower_bound = 0
    model.reactions.get_by_id("rxn10114_c0").bounds = (
        0,
        0,
    )  #   TCA,## zero formate ubiquinone reaction
    # Allow Rnf complex to be reversible
    model.reactions.get_by_id(
        "leq000002_c0"
    ).lower_bound = -1000  
    # Fix L-Glutamate:NADP+ oxidoreductase reaction, irreversible towards
    # glutamine. The reaction uses NADPH to form glutamate from glutamine +
    # 2-oxoglutamrate
    model.reactions.rxn00085_c0.upper_bound = 0  
    # Allow Rnf complex to be reversible
    model.reactions.get_by_id(
        "M002"
    ).lower_bound = -1000  
    # Set sodium-proline symport for import only, use proline exporter for export
    model.reactions.get_by_id(
        "rxn05221_c0"
    ).lower_bound = (
        0  
    )
    # Irreversible acetaldehyde oxidoreductase towards production of acetaldehyde (NADH)
    model.reactions.rxn00171_c0.lower_bound = 0

    # model.reactions.get_by_id("cpd00047_ext_b").bounds = (0, 0)     #  Block formate from leaving the cell

    # rxn 964 block formate dehydrogenase (ferredoxin added)
    model.reactions.rxn00103_c0.bounds = 0, 0        
    model.reactions.rxn00234_c0.lower_bound = 0  # Stop glutamate degredation pathway from being reversible
