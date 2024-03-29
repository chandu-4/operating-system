import pandas as pd
import numpy as np
import random
import datetime

def simulate_memory_usage_data(node_count=10, days=7):
    """
    Simulates memory usage data for a cluster.
    
    :param node_count: Number of nodes in the cluster.
    :param days: Number of days to simulate data for.
    :return: DataFrame with simulated memory data.
    """
    timestamps = pd.date_range(end=datetime.datetime.now(), periods=24*days, freq='H')
    data = {
        'timestamp': np.tile(timestamps, node_count),
        'node_id': np.repeat(range(node_count), len(timestamps)),
        'memory_used_gb': [random.uniform(50, 200) for _ in range(node_count * len(timestamps))],
        'memory_total_gb': 256  # Assuming each node has 256 GB of total memory for simplicity.
    }
    return pd.DataFrame(data)

# Simulate memory usage data
memory_data = simulate_memory_usage_data()
print(memory_data.head())
def analyze_memory_constraints(memory_data):
    """
    Analyzes memory constraints based on usage data.
    
    :param memory_data: DataFrame with memory usage data.
    """
    # Calculate average and peak memory usage
    average_usage = memory_data.groupby('node_id')['memory_used_gb'].mean()
    peak_usage = memory_data.groupby('node_id')['memory_used_gb'].max()
    
    # Identify nodes with high average or peak memory usage
    high_avg_usage_nodes = average_usage[average_usage > (0.8 * 256)].index.tolist()  # 80% of total memory
    high_peak_usage_nodes = peak_usage[peak_usage > (0.9 * 256)].index.tolist()  # 90% of total memory
    
    print(f"Nodes with high average memory usage: {high_avg_usage_nodes}")
    print(f"Nodes with high peak memory usage: {high_peak_usage_nodes}")
    
    # Visualization (optional)
    average_usage.plot(kind='bar', title='Average Memory Usage per Node')
    peak_usage.plot(kind='bar', color='red', title='Peak Memory Usage per Node')

# Analyze the simulated data
analyze_memory_constraints(memory_data)

