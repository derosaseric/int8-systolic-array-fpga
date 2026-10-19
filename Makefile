WAVES ?= 1
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
VERILOG_SOURCES += $(PWD)/rtl/mac.v
TOPLEVEL = mac
MODULE = test_mac
COCOTB_TOPLEVEL = mac
COCOTB_TEST_MODULES = test_mac
export PYTHONPATH := $(PWD)/tb:$(PYTHONPATH)
include $(shell cocotb-config --makefiles)/Makefile.sim
