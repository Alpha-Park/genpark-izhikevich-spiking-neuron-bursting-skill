from client import IzhikevichNeuron

def main():
    print("=== Izhikevich Phenomenological Spiking Neuron ===")
    neuron = IzhikevichNeuron()
    res = neuron.simulate(steps=150, current=10.0)
    print("Simulation:", res["steps"], "steps, fired", res["spikes_emitted"], "spikes.")
    assert res["spikes_emitted"] >= 2
    print("Izhikevich Spiking Neuron verified successfully!")

if __name__ == "__main__":
    main()
