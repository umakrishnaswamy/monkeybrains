import wandb 

wandb.init(project='monkeybrains')

for i in range(10):
    wandb.log(i)

wandb.finish()