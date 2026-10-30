# INT8 Systolic Array on FPGA

Work in progress: an INT8 matrix-multiply accelerator in Verilog, verified
with cocotb against Python reference models. Goal: a parameterized systolic 
array on a real FPGA, with measured latency, Fmax, and resource use.

## Status
- [x] 8-bit signed MAC with cocotb tests
- [ ] Processing element and 1D chain
- [ ] 4x4 systolic array
- [ ] AXI-Stream wrapper, tiling, requantization
- [ ] FPGA synthesis and results

## Verification approach
- Random test: 1000 random input pairs checked against a Python golden model
- Directed tests: enable-hold, reset-during-accumulation, signed corner cases
- Fault injection: tests were validated by deliberately breaking the design
  (removing `signed`, ignoring `en`, swapping reset priority) and confirming
  that they fail

## Requirements
- Icarus Verilog (`sudo apt install iverilog`)
- Python 3 and cocotb

## Run the tests
```bash
python3 -m venv venv
source venv/bin/activate
pip install cocotb
make
```

Waveform: `gtkwave sim_build/mac.fst`
