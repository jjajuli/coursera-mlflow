from mlflow import log_metric
from random import choice

import mlflow
experiment_name = 'produce-metrics'
mlflow.set_experiment(experiment_name)

metric_names = ["cpu", "ram", "disk"]

percentages = [i for i in range(0,100)]

# for i in range(40):
#     log_metric(choice(metric_names), choice(percentages))
log_metric("cpu", choice(percentages))
log_metric("ram", choice(percentages))
log_metric("disk", choice(percentages))