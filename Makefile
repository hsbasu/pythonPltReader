# build an executable named from a .py
#
# # *****************************************************
# # Parameters to control Makefile operation
MAINCODE = main

PYTHON=@python
PY3=@python3
PYFLAGS=-m pydoc -w 
# 
# #special phony target, ".PHONY" contain all "targets"
.PHONY: all clean
# 
# # phony target "all" can have "any number" of targets
all: run
# 
run:
	${PY3} ${PYFLAGS} ${MAINCODE}
clean:
	@echo "Cleaning up..."
	rm -Rf __pycache__ *.html log
