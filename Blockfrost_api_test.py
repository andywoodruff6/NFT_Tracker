from blockfrost import BlockFrostApi, ApiError, ApiUrls
import pandas as pd

api = BlockFrostApi(project_id='z6y93S2GgrHBwooKwhOVCU1DZ4c8HRG4')

try:
    health = api.health()
    print(health.is_healthy)

    account_rewards = api.account_rewards(
    stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
    count=20,
    )
    print(account_rewards[0].epoch) 
    print(len(account_rewards))
except ApiError as e:
    print(e)