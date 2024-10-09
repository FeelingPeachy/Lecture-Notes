# risc & cisc
retitred instruct - properly completer instruct
- risc achitecture requires alot of compiutiational infra to be able to execute instruct in parallel, as need alu, devode, fech , memory write


to resolve data hazard 
- can either stall pipelione for as many cyces as necessary
hardware forwardiong tecgnique
-critical path is the lognest path that the program can take in its execution


branch is where we hit a condition. forom that point, any of its succsesso iss unsure as it relies on the fullfilment of prior instructions

static predictoy
- we already take a defualt assumption, and we always assumne if this branch we assume this branch is taken so correct 50% tuine
- dynamic will look at program history

- cannot fill a delay slot with a branch because can create a loop