# notes

Exe options: use 32, deactivated
vis options: turn of fshow data path and control path
- working on RISC architecture - small iinstruction set, single cycle executrion, load/store architecture

- pileinging (instuction execution) - optimisation techniwuee that helps perfomance, taking adv of parrelilsm  where emultiple instructions are overlapped in execurion
- it helps the num of instrunctions executed per unit time

- so what parts of computation can be compartmentalised
- stages of instruction exectuito i sfecth decode execte cyvle and store(writing resulst)
- in the pipeline we break it down such that some part of each instruction make some progress, ie when one instruction is decoded others can be fecyched as they are non blovkin/overlapping where they use diff regiesters

- how does the system change when performing branching instructions ?

- function + opcode : what to do
 - where to do given by rs1, rs2.. refering to registers
  - 32bit - each regitser has 4 bytes
  - instructio formats tell you teh yuoe if instryction: ie branch or store ...
  - immediate vals (constant vals)
  pc increases by 4 bytes after every instruction aas we are in 32 bit sys, therefore we point to next instruction

  - pc is normally sequesntial therefore can just increment 4 bytes to prev val else if jump perfomed need to start from where the jump "landed"