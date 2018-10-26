def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def main():

    p = 2249403991
    q = 9836262662
    n = p * q
    e = 65537
    ct = 3175522185288915756817736101377329731290656722019219018506850142825373811446557752133046783277141611328625068933636450001328160798980650578666695816499016850032082960297783061099251252606669408058718046291551594511731292679847228808709384039236002399590292208249498879936372720524430812843988225098379189

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
