def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

#input values accordingly
    p = 2249403991
    q = 9836262662
    n = p * q
    e = 65537
    ct = 10000000000

    # Compute phi(n)
    phi = (p-1) * (q-1)

    # Compute modular inverse of e
    gcd, a, b = egcd(e, phi)
    d = a

    print( "d: " + str(d) );

    # Decrypt ciphertext
    
    pt = pow(ct, d, n)
    print( "pt: " + str(pt) )

if __name__ == "__main__":
    main()
