#!/usr/bin/env python3
"""
Boot l'ISO stinux-dawin-bash dans QEMU (sur un runner GitHub Actions, avec un
vrai acces reseau) et verifie que `apt install xfce4 xfce4-goodies` reussit
reellement (pas en simulation).
"""
import pexpect
import sys

CMD = (
    "qemu-system-x86_64 -m 4096 -smp 2 -accel tcg "
    "-cdrom stinux-dawin-bash.iso "
    "-netdev user,id=net0 -device virtio-net-pci,netdev=net0 "
    "-display none -serial mon:stdio -no-reboot"
)

PROMPT = r"user@stinuxos:[^\$]*\$\s*$"

def run():
    child = pexpect.spawn(CMD, timeout=300, encoding="utf-8", logfile=sys.stdout)

    print("### attente du login automatique ###")
    child.expect(PROMPT, timeout=240)

    print("### apt update (reseau reel) ###")
    child.sendline("sudo apt update")
    child.expect(PROMPT, timeout=180)

    print("### apt install -y xfce4 xfce4-goodies (reseau reel) ###")
    child.sendline("sudo apt install -y xfce4 xfce4-goodies")
    child.expect(PROMPT, timeout=1800)

    print("### verification dpkg ###")
    child.sendline("echo RESULT:$(dpkg -l | grep -c '^ii  xfce4-session')")
    child.expect(PROMPT, timeout=30)
    result_output = child.before

    child.sendline("sudo poweroff")
    try:
        child.expect(pexpect.EOF, timeout=60)
    except Exception:
        child.close(force=True)

    if "RESULT:1" in result_output:
        print("\n=== SUCCES : xfce4-session installe avec un reseau reel ===")
        return 0

    print("\n=== ECHEC : xfce4-session non installe ===")
    print("Sortie de verification :", result_output)
    return 1

if __name__ == "__main__":
    sys.exit(run())
