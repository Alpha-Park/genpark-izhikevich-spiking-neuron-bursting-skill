class IzhikevichNeuron:
    """Izhikevich 2D dynamical spiking neuron model."""
    def __init__(self, a: float = 0.02, b: float = 0.2, c: float = -65.0, d: float = 8.0):
        # Parameters for regular spiking (RS)
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.v = -65.0
        self.u = b * self.v

    def step(self, current_injection: float, dt: float = 0.5) -> tuple[int, float]:
        # Euler integration step
        v_next = self.v + dt * (0.04 * self.v ** 2 + 5.0 * self.v + 140.0 - self.u + current_injection)
        self.u += dt * (self.a * (self.b * self.v - self.u))

        if v_next >= 30.0:
            self.v = self.c
            self.u += self.d
            return 1, 30.0 # Spike peak
        else:
            self.v = v_next
            return 0, self.v

    def simulate(self, steps: int = 200, current: float = 10.0) -> dict:
        spikes = []
        voltage_trace = []
        for _ in range(steps):
            spk, v = self.step(current)
            spikes.append(spk)
            voltage_trace.append(round(v, 2))
        return {
            "steps": steps,
            "current_input": current,
            "spikes_emitted": sum(spikes),
            "trace_sample": voltage_trace[:10]
        }
