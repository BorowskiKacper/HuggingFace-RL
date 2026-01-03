import gymnasium as gym
from gymnasium.utils.play import play

# Global variables to track stats
death_count = 0
current_score = 0

def stats_callback(obs_t, obs_tp1, action, rew, terminated, truncated, info):
    global death_count, current_score
    
    # Increment score for every frame you survive
    current_score += 1

    if terminated or truncated:
        death_count += 1
        print(f"💀 Died! Score: {current_score} | Total Deaths: {death_count}")
        
        # Reset score for the next run
        current_score = 0

# Setup the environment
mapping = {"a": 0, "d": 1}
env = gym.make("CartPole-v1", render_mode="rgb_array")

print("Controls: 'a' (Left), 'd' (Right). Check console for stats!")

# Pass the callback function to play
play(env, keys_to_action=mapping, fps=15, callback=stats_callback)