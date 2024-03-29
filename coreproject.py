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
