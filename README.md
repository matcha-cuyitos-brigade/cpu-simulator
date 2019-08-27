# cpu-simulator
***
# What is this?
🎛 A simple CPU simulation that reads its configurations from a bios.yml and interprets assembly-like code files.
***
## Folder structure
```bash
.
└── frontend_cpu
    ├── Dockerfile
    ├── nginx
    │   ├── mime.types
    │   └── nginx.conf
    └── templates
        ├── ALU_cuyo.jpg
        ├── CLOCK_cuyo.jpg
        ├── RAM_CUYO.jpg
        ├── REGIST_cuyo.jpg
        ├── addr_register.png
        ├── background.jpg
        ├── clock.png
        ├── controlunit.png
        ├── index.html
        ├── input1.png
        ├── input2.png
        ├── output.png
        ├── ram.png
        └── register.png
```
## Components
### CU
A Control Unit is responsible of fetching the instruction set, controlling the data flow across the whole CPU,  controls the timing of each operation and the interaction with peripheral devices. 

### ALU
Arithmetic Logic Unit, is a digital electronic circuit responsible for (depending on the processor) doing all the arithmetic operations such as (but not limited to): 
* Add
* Subtraction
* Subtract with borrow
* One’s complement
* Two’s complement
* AND
* OR
* Bit shift operations

### REGISTERS
An important piece of memory that the CU and the ALU can store temporarily the data, one important register is the program counter which keeps track  of where the CPU is reading from the instruction set.

* Instruction Register (Current instruction loaded)
* Instruction Address Register (program counter)

### RAM
Random Access Memory

### Clock
In charge of control the fetch-decode-execute cycle.










