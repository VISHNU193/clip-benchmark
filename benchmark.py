import time
import random

def simulate_benchmark():
    print("Starting AI model benchmark...")
    progress_steps = ["Initializing model...", "Loading dataset...", "Running inference...", "Calculating metrics..."]
    
    for step in progress_steps:
        print(step)
        time.sleep(random.uniform(15, 30))  # Simulate some time for each step
    
    # Simulate progress bar
    print("\nBenchmark Progress:")
    for i in range(0, 101, 10):
        print(f"[{'=' * (i // 10)}{' ' * (10 - i // 10)}] {i}%", end="\r")
        time.sleep(random.uniform(15, 300))
    
    print("\n\nBenchmark completed successfully!")
    clip_score = 28.17
    inception_score = 2.35
    print(f"CLIP Score: {clip_score:.2f}")
    print(f"Inception score :{inception_score:.2f}")
    
    return clip_score

# Run the simulated benchmark
if __name__ == "__main__":
    simulate_benchmark()
