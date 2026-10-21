import random
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge

def to_signed(val, bits=32):
    return val - (1 << bits) if val >= (1 << (bits - 1)) else val

async def reset(dut):
    dut.rst.value = 1
    dut.en.value = 0
    dut.a.value = 0
    dut.b.value = 0
    await FallingEdge(dut.clk)
    await FallingEdge(dut.clk)
    dut.rst.value = 0

@cocotb.test()
async def mac_random(dut):
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())
    await reset(dut)

    expected = 0
    for _ in range(1000):
        a = random.randint(-128, 127)
        b = random.randint(-128, 127)
        dut.a.value = a & 0xFF
        dut.b.value = b & 0xFF
        dut.en.value = 1
        await FallingEdge(dut.clk)
        expected += a * b
        got = to_signed(int(dut.acc.value))
        assert got == expected, f"a={a} b={b} expected={expected} got={got}"

@cocotb.test()
async def mac_enable_hold(dut):
    cocotb.start_soon(Clock(dut.clk, 10, "ns").start())
    await reset(dut)

    # accumulate once: 3 * 4 = 12
    dut.a.value = 3
    dut.b.value = 4
    dut.en.value = 1
    await FallingEdge(dut.clk)
    assert to_signed(int(dut.acc.value)) == 12

    # disable and change inputs: acc must hold
    dut.en.value = 0
    dut.a.value = 100
    dut.b.value = 100
    for _ in range(5):
        await FallingEdge(dut.clk)
        assert to_signed(int(dut.acc.value)) == 12
