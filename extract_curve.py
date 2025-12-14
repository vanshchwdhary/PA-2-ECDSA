
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec

with open("certificate.pem", "rb") as f:
    cert_data = f.read()

cert = x509.load_pem_x509_certificate(cert_data, default_backend())
public_key = cert.public_key()

if isinstance(public_key, ec.EllipticCurvePublicKey):
    curve = public_key.curve
    print("Elliptic Curve Name:", curve.name)

    if curve.name == "secp256r1":
        print("Curve Equation: y^2 = x^3 + ax + b (mod p)")
        print("Field Characteristic (p): 2^256 − 2^224 + 2^192 + 2^96 − 1")
else:
    print("Certificate does not use ECDSA")
