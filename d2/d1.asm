BITS 16

;; Anthony Di Falco
;; 1/18/18

start:
        cli             ; turn off interrupts for the prelude
			; if interrupts are on, a hardware device
			; could alter a register and prevent the
			; computer from booting any further

        mov ax, 07C0h   ; This line loads the size of the this code section into a register.
        mov ds, ax      ; This line moves this size to another register in order to track the 
			; size after modifying the original.

        add ax, 0020h   ; This line determines where the code section is -- assuming that hex number is the offset in memory.
			; 
        mov ss, ax      ; This line loads the location register vals into a permanent register
        mov sp, 1000h   ; This line loads the size of the following code section.

        sti             ; turn the interrupts back on
	mov ah, 0Eh	;
	mov al, 43h	;
	mov bh, 0h	;
	int 10h		;
	mov al, 44h	;
	int 10h		;
	mov si, thestring
	call print	;



	jmp $

	print:
		ret
	thestring db 'mcduck', 0	;DATA

	; the lines below are nasm directives, NOT x86 instructions
	; they tell nasm to fill the rest of the space from our
	; current location to 510 bytes with zeros
	; then set the last two bytes (dw = define word) to AA55
	; this is by convention, since the firmware validates the bootloader
	; by reading the last two bytes and confirming that they are AA55
	; the firmware will not execute the bootloader without it
	times 510-($-$$) db 0
	dw 0xAA55	; BIOS looks for AA55 at the end of the sector

