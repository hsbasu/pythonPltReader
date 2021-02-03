# build an executable named from a .py
#
# *****************************************************

# Parameters to control Makefile operation
# MAINCODE = pyPLTreader
MAINCODE = main

PYTHON = @python
PY3 = @python3
PYFLAGS = -m pydoc -w

# phony target "all" can have "any number" of targets
all: run pyPLTreader-help

pyPLTreader-help:
	${PY3} ${PYFLAGS} pyPLTreader

run:
	${PY3} ${PYFLAGS} ${MAINCODE}
clean:
	@echo "Cleaning up..."
	rm -Rf __pycache__ *.pyc main.html log
