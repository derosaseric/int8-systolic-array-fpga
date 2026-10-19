# INT8 Systolic Array on FPGA

A parameterized INT8 matrix-multiply accelerator in Verilog,
verified with cocotb against a NumPy reference model.

## Status
- [x] 8-bit MAC + cocotb test
- [ ] Processing element and 1D chain
- [ ] 4x4 systolic array
- [ ] AXI-Stream wrapper, tiling, requantization
- [ ] FPGA synthesis and results

## Run the tests
    python3 -m venv venv && source venv/bin/activate
    pip install cocotb
    make


