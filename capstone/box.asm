// Draw box when key pressed
// Row = 79
// Height = 20
// Width = 64 pixels

(KBDCHECK)
@24576
D=M

@DRAW
D;JNE

@CLEAR
0;JMP

(DRAW)

@16384
D=A

@2528
D=D+A

@addr
M=D

@20
D=A
@rows
M=D

(LOOPDRAW)

@addr
A=M

M=-1
A=A+1
M=-1
A=A+1
M=-1
A=A+1
M=-1

@addr
D=M

@32
D=D+A

@addr
M=D

@rows
MD=M-1

@LOOPDRAW
D;JGT

@KBDCHECK
0;JMP

(CLEAR)

@16384
D=A

@2528
D=D+A

@addr
M=D

@20
D=A
@rows
M=D

(LOOPCLEAR)

@addr
A=M

M=0
A=A+1
M=0
A=A+1
M=0
A=A+1
M=0

@addr
D=M

@32
D=D+A

@addr
M=D

@rows
MD=M-1

@LOOPCLEAR
D;JGT

@KBDCHECK
0;JMP