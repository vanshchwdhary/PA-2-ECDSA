
# PA-2: Elliptic Curve Digital Signature Algorithm (ECDSA)

## Objective
Extract elliptic curve equation and finite field characteristic from an ECDSA-based SSL/TLS certificate.

## Steps
1. Export SSL certificate from a website using OpenSSL.
2. Save it as certificate.pem in this folder.
3. Run the Python script to extract curve details.

## How to Export Certificate
openssl s_client -connect example.com:443 -showcerts

## How to Run
pip install cryptography
python extract_curve.py

## Output
Displays elliptic curve name and finite field characteristic.
# PA-2-ECDSA
