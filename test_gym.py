import gym
#import panda_gym

env = gym.make('FetchReach-v1')

obs = env.reset()
done = False
while not done:
    action = env.action_space.sample()  # random action
    obs, reward, done, info = env.step(action)
    print(obs, reward, done, info)
env.close()
