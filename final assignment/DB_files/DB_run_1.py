from ema_workbench.em_framework.parameters import Constant
from ema_workbench.em_framework.optimization import ArchiveLogger, EpsilonProgress
from ema_workbench import (
    Model,
    Policy,
    ema_logging,
    SequentialEvaluator,
    perform_experiments,
    MPIEvaluator
)
from problem_formulation import get_model_for_problem_formulation
import pickle
import optimization_tuned

if __name__ == '__main__':
    # Records the events when running ema_workbench functions
    ema_logging.log_to_stderr(level=ema_logging.INFO, pass_root_logger_level=True)
    # Load reference scenarios
    with open("../data/ScenariosOpenExplo", 'rb') as file2:
        Scenarios = pickle.load(file2)
    # Remove a third reference scenario which is a duplicate of the first
    Scenarios.pop(2)
    # Create an instance of the model which is workable with the ema workbench
    dike_model2, planning_steps2 = get_model_for_problem_formulation(6)
    # Alter policy levers to the correct ones
    dele = []
    for x in dike_model2.levers:
        if x.name not in ["3_RfR 2", "3_RfR 1",
                          "3_RfR 0", "2_RfR 0",
                          "2_RfR 1", "2_RfR 2",
                          "A.5_DikeIncrease 0",
                          "A.5_DikeIncrease 1",
                          "A.3_DikeIncrease 0",
                          "EWS_DaysToThreat"]:
            dele.append(x.name)
    for i in dele:
        dike_model2.levers.__delitem__(i)
        dike_model2.constants.extend(Constant(i, 0))

    # Define the evaluator used to run the experiments
    with MPIEvaluator(dike_model2) as evaluator:
        # Saves the data for the convergence metrics
        convergence_metrics = [
            ArchiveLogger(
                r".",
                decision_varnames=[l.name for l in dike_model2.levers],
                outcome_varnames=[o.name for o in dike_model2.outcomes],
                base_filename=f"Seed-{0}Scen-{0}.tar.gz",
            ),

            EpsilonProgress(),
        ]
        # Run the optimizer
        result, convergence = evaluator.optimize(
            nfe=50000,
            searchover="levers",
            epsilons=[0.1, 0.1, 10000, 0.1, 10000, 0.1],
            convergence=convergence_metrics,
            reference=Scenarios[0]
        )
        # Save the results as pickle file
        with open(f'Seed-{0}Scen-{0}.pkl', 'wb') as file:
            pickle.dump([result, convergence], file)
        print("pos save")
