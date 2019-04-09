from gym.envs.registration import register

register(
    id='Deterministic-4x4-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': False})

register(
    id='Deterministic-8x8-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '8x8',
            'is_slippery': False})

register(
    id='Stochastic-4x4-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '4x4',
            'is_slippery': True})

register(
    id='Stochastic-8x8-FrozenLake-v0',
    entry_point='gym.envs.toy_text.frozen_lake:FrozenLakeEnv',
    kwargs={'map_name': '8x8',
            'is_slippery': True})


register(
    id='Deterministic-4x4-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '4x4',
            'is_slippery': False})

register(
    id='Stochastic-4x4-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '4x4',
            'is_slippery': True})

register(
    id='Deterministic-8x8-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '8x8',
            'is_slippery': False})

register(
    id='Stochastic-8x8-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '8x8',
            'is_slippery': True})
  
register(
    id='Deterministic-16x16-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '16x16',
            'is_slippery': False})

register(
    id='Stochastic-16x16-neg-reward-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:NegRewardFrozenLake',
    kwargs={'map_name': '16x16',
            'is_slippery': True})


register(
    id='Deterministic-4x4-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '4x4',
            'is_slippery': False})

register(
    id='Stochastic-4x4-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '4x4',
            'is_slippery': True})

register(
    id='Deterministic-8x8-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '8x8',
            'is_slippery': False})

register(
    id='Stochastic-8x8-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '8x8',
            'is_slippery': True})
  
register(
    id='Deterministic-16x16-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '16x16',
            'is_slippery': False})

register(
    id='Stochastic-16x16-Windy-FrozenLake-v0',
    entry_point='gym_lake_custom.envs:WindyFrozenLake',
    kwargs={'map_name': '16x16',
            'is_slippery': True})