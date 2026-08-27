#!/data/data/com.termux/files/usr/bin/bash
# Configures OpenSSH in Termux for remote debugging from a PC

echo "[+] Installing and configuring OpenSSH..."
pkg install openssh -y

# Generate host keys if they don't exist
sshd

echo "[+] SSH Server started on port 8022."
echo "[+] Your username is: $(whoami)"
echo "[+] Set your password below:"
passwd
