import gym
import numpy as np
from matplotlib import pyplot as plt
import itertools
from lib.env.threedmountain_car import ThreeDMountainCarEnv

env = ThreeDMountainCarEnv()

state = env.reset()

for t in itertools.count():
	# action = env.action_space.sample()
	next_state, reward, done, info = env.step(2)
	env.render()

	if done:
		break

	state = next_state

	# if t == 100:
	# 	env.close_gui()
	# 	break

