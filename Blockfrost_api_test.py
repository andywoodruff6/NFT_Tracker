from blockfrost import BlockFrostApi, ApiError, ApiUrls
from blockfrost.utils import Api
import pandas as pd
import json

api = BlockFrostApi(project_id='z6y93S2GgrHBwooKwhOVCU1DZ4c8HRG4')
# Type api. to see all of the commands that are available to be called

try:
    # version = api
    # print(version) # Prints blockfrost.api.BlockFrostApi object at 0x000002478F7911C8

    health = api.health()
    print(health.is_healthy) # Either True or False

    # meterics = api.metrics()
    # print(meterics) # Time (of first call) and number of calls made in the last 30 days

    # meteric_end = api.metrics_endpoints()
    # print(meteric_end)

    # account_rewards = api.account_rewards(
    # stake_address='stake1ux3g2c9dx2nhhehyrezyxpkstartcqmu9hk63qgfkccw5rqttygt7',
    # count=20,
    # )
    # print(account_rewards[0].epoch) 
    # print(len(account_rewards))
    # address = api.address_total(
    #     'addr1q8nd8k5apx3336xry309gss2pt8x0pufxayx9vf0za83pdha8kjn5mw6ka0uaqk8wwtf39tzhrxedgkwr9wv8axy7has5za7xf'
    # )
    # print(address)
    # a = api.policy_assets(
    #   policy_id='d5e6bf0500378d4f0da4e8dde6becec7621cd8cbf5cbb9b87013d4cc')
    # print(a) # This doesnt work
    b = api.asset_transactions(
        asset='d5e6bf0500378d4f0da4e8dde6becec7621cd8cbf5cbb9b87013d4cc537061636542756439363431')
    # print(b)

except ApiError as e:
    print(e)

data = json.loads(b)
print(data)
# df = pd.read_json(b)
# print(df.head())