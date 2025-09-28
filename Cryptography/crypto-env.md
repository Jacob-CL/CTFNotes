# crypto-env
```
python3 -m venv crypto-env
```
```
source crypto-env/bin/activate
```
```
cat > requirements.txt << EOF
pycryptodome
cryptography
gmpy2
sympy
z3-solver
pwntools
ecdsa
jupyter
rsa
requests
numpy
matplotlib
EOF
```
Install everything:
```
pip install -r requirements.txt
```

